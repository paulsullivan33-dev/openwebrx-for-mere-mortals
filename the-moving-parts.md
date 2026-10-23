# The Moving Parts

**Scope:** what is actually running when an
OpenWebRX receiver runs — five pieces of
software, three places state lives, and
what breaks when each piece stops.

## The server

The centre is a Python program,
`openwebrx.py`, serving HTTP and websockets
on port **8073** by default. It serves the
web page, takes each listener's tuning
requests over a websocket, and owns all the
configuration. One process, no database
server, no separate web tier — when people
say "the receiver is down", this process is
what they mean.

**Check:** the status endpoint answers even
with nobody listening:

```text
$ curl http://localhost:8073/status.json
{ "receiver": {...}, "max_clients": 20,
  "version": "v1.2.2", "sdrs": [...] }
```

## The DSP chain

Raw I/Q samples are useless until maths
happens: filtering to one signal, shifting
it to centre, demodulating it. That work is
done by the **csdr** library and its Python
bindings **pycsdr**, assembled per listener
into a small pipeline: a shared FFT feeds
everybody's waterfall, and each listener
gets their own demodulator branch. This is
where the CPU goes, and its size scales
with the sample rate and the listener
count.

## The connectors

OpenWebRX does not talk to most hardware
directly. For each device type there is a
small connector program — from the
**owrx_connector** package — that owns the
device, takes tuning commands ("centre
145 MHz, 2.4 MS/s, gain auto") and streams
samples back. Different connectors suit
different hardware: `rtl_connector` for
RTL-SDR dongles, a SoapySDR connector for
the wide Soapy family, an `rtl_tcp`
connector for a receiver that lives on
another machine (recipe 1).

The lab watched one work: when the first
listener arrived, `rtl_tcp_connector`
connected to the test source and issued
exactly the commands the profile specified
(`openwebrx-lab/transcripts/t06`). When the
listener left, it disconnected. Devices are
started on demand, not held open.

## The codec server

Some digital voice modes (DMR, D-Star, and
friends) are wrapped in a patent-era voice
codec, AMBE. Decoding those is delegated to
a separate program, **codecserver**, which
OpenWebRX talks to when a listener picks a
digital voice mode. If it isn't running,
analogue modes are unaffected and the
feature report (below) marks digital voice
unavailable. The lab did not start it —
see `criteria.md`.

## The feature report

Because drivers and decoders are optional,
OpenWebRX inventories itself at runtime:
which device types it can drive, which
decoders it can find. The result is at
`/features` in a browser and `/api/features`
as JSON.

**Check:** before blaming a device, ask the
receiver what it thinks it has:

```text
$ curl localhost:8073/api/features
{ "core": ..., "rtl_sdr": {"available":
  true, ...}, "sdrplay": {"available":
  false, ...}, ... }
```

The settings pages obey the same list —
the new-device form only offers types the
report calls available, which is why a
missing driver shows up as a missing menu
entry rather than an error (chapter 14).

## Where the state lives

Three places, all plain files:

| Path | Holds |
| --- | --- |
| `/etc/openwebrx/openwebrx.conf` | Core settings: data directory, port |
| `/etc/openwebrx/bands.json` | The band plan the UI draws and labels |
| `/var/lib/openwebrx/settings.json` | Devices, profiles, general settings — written the first time an admin saves anything |
| `/var/lib/openwebrx/users.json` | User accounts, passwords hashed |
| `/var/lib/openwebrx/bookmarks.json` | The shared bookmark list |
| `/tmp/openwebrx` | Temporary files: waterfall and stream scratch |

Two consequences worth remembering. First,
a fresh install has **no** `settings.json`:
the program runs on built-in defaults (a
sample RTL-SDR device with 2 m and 70 cm
profiles among them) until an admin changes
something, at which point the current
configuration is written out whole.
Second, backup is a solved problem the
moment you know this table — chapter 10 is
short because this table is short.
