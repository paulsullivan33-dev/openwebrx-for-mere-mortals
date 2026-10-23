# Installing OpenWebRX

**Scope:** the three supported ways to get
a receiver running — Docker, the Raspberry
Pi image, and Linux packages — with the
ports, volumes, and device access each one
needs. The Docker route is the project's
recommended path and the one this guide
follows in detail.

> A note on evidence: this guide's lab ran
> the server from the official image's own
> filesystem because the lab machine has no
> container runtime. The commands below are
> the project's documented route, checked
> against the image's own startup scripts;
> `criteria.md` keeps the ledger.

## What you need

- A machine that stays on: a Raspberry Pi
  4 or later, a small home server, or a
  spare laptop. The work is light — one
  device at 2.4 MS/s is comfortably served
  by a Pi-class machine; CPU grows with
  sample rate and listeners.
- A receiver the project supports: an
  RTL-SDR dongle is the usual first device.
  The hardware itself — dongles, antennas —
  is the companion guide's subject (*RTL-SDR
  for Mere Mortals*).
- For Docker: Docker with the Compose
  plugin, on Linux. (This series' Docker
  guides cover that install.)

## Route 1: Docker (recommended)

The official image is `jketterl/openwebrx`.
A Compose file is the tidy way to run it —
`examples/docker-compose.yml` in this repo
is a complete starting point:

```yaml
services:
  openwebrx:
    image: jketterl/openwebrx:stable
    container_name: openwebrx
    restart: unless-stopped
    ports:
      - "8073:8073"
    environment:
      OPENWEBRX_ADMIN_USER: "rowan"
      OPENWEBRX_ADMIN_PASSWORD: "choose-a-real-one"
    volumes:
      - openwebrx-settings:/var/lib/openwebrx
      - openwebrx-config:/etc/openwebrx
      - openwebrx-tmp:/tmp/openwebrx
    devices:
      - /dev/bus/usb:/dev/bus/usb
```

The moving pieces, one at a time:

- **The admin environment variables** are
  read once at startup: if the named user
  doesn't exist yet, it is created with
  that password. This is the painless way
  to bootstrap the first account. (Chapter 4
  shows the command-line route, which is
  what you use afterwards.)
- **The volumes are the receiver.** All
  state lives in `/var/lib/openwebrx` and
  `/etc/openwebrx` (chapter 2's table), so
  those two mounts *are* your backup
  boundary. `/tmp/openwebrx` is scratch.
- **The device passthrough** hands the USB
  bus to the container so the connector can
  open the dongle. On the host, the usual
  RTL-SDR housekeeping applies — the
  kernel's DVB-T driver must not grab the
  dongle first (the blacklist step from the
  RTL-SDR guide).

```text
$ docker compose up -d
$ curl -s localhost:8073/status.json
{... "version": "v1.2.2" ...}
```

**Check:** the status JSON answers and the
page at `http://<host>:8073/` shows the
receiver. If the waterfall never starts,
the dongle is the first suspect — chapter
14.

Tag discipline: `:stable` tracks releases.
Pinning an exact version tag (for example
`1.2.2`) makes upgrades a decision instead
of a surprise; chapter 10 covers upgrading
deliberately.

## Route 2: the Raspberry Pi image

The project publishes a ready-made SD card
image with OpenWebRX and the common drivers
already installed — the fastest route if
the receiver will live on a Pi by the
antenna. You write the image, boot, and the
receiver answers on port 8073; the admin
account is created with the command-line
route in chapter 4. Settings, profiles and
files all live in the same places as every
other route, so the rest of this guide
applies unchanged. (Documented route — the
lab did not run a Pi.)

## Route 3: packages

For Debian and Ubuntu, the project runs its
own package repository; installing the
`openwebrx` package pulls in the connectors
and decoders as dependencies and runs the
server as a system service. This suits a
machine that already hosts other services
and dislikes containers. Same files, same
port, same admin command. (Documented
route.)

## Which route, honestly

Docker if you already run containers or
want the receiver to be one tidy folder of
volumes. The Pi image if the Pi *is* the
project. Packages if the machine is a
traditional Linux server and you'd rather
have one less runtime. All three run the
same program; nothing in the chapters that
follow depends on the choice.
