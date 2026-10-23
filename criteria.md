# Writing Criteria

Every guide in this repo is written to the same
standard. If you're adding or editing a guide —
human or AI — hold it to these.

1. **Plain words, real ideas.** Simple language,
   never dumbed-down concepts. Explain jargon on
   first use; collect terms in the glossary.
2. **No hype.** No marketing adjectives, no
   "revolutionary," no promises about what
   something will do for the reader.
3. **Honest about limits.** Say what the thing
   *can't* do. State uncertainty instead of
   smoothing it over. Validation notes include
   what remains unverified.
4. **No invented numbers.** Benchmarks, defaults,
   and specs are either measured or qualified with
   "depends on your setup." If it wasn't tested,
   say so.
5. **Checkable.** Commands are meant to be run,
   with "Check:" blocks showing what success looks
   like. Sources are linked, not asserted.
6. **Respect the reader's setup.** Call out
   Windows/Mac/Linux differences. Don't assume a
   GPU, a budget, or prior experience.
7. **Safety isn't skipped.** Real risks get
   stated plainly, not buried.
8. **Scoped.** Each guide says what it covers and
   points elsewhere for the rest. No guide
   pretends to be the whole subject.
9. **Structure over prose.** Tables, before/after
   examples, symptom → fix. Scannable beats essay.

## Verification notes for this guide

Built and verified 2026-10-22 against
**OpenWebRX 1.2.2**, the current release on
build day, taken from the project's official
Docker image (`jketterl/openwebrx:stable`,
registry digest verified after download).

The lab had no container runtime and no radio
hardware, so two substitutions were made, both
declared wherever they matter:

- The image's filesystem was unpacked and
  executed directly (its own loader, Python and
  libraries), with `/etc/openwebrx` seeded the
  way the image's own startup script seeds it.
  Same code, same versions, no container around
  it. The Docker commands in chapter 3 are the
  documented route, not the route the lab ran.
- A synthetic `rtl_tcp` server (in `examples/`)
  played the part of the radio: precomputed I/Q
  samples carrying three known signals. That
  proves the whole receive chain except the
  last metre — an actual tuner hearing actual
  radio waves.

### Verified live

Transcripts in `openwebrx-lab/transcripts/`.

- Image pulled from Docker Hub; all 11 layer
  digests verified; version 1.2.2 read from the
  image itself (t00).
- Server starts; web UI serves on port 8073
  with the expected page; `/status.json`
  reports version, limits and the built-in
  sample devices (t01).
- Feature report read from `/api/features`:
  rtl_sdr, rtl_tcp, perseus, hpsdr and runds
  sources available, wsjt-x, packet, pocsag,
  js8call, FreeDV and M17 decoders available;
  the list of what was *not* available in the
  sandbox is in t02 and is environmental, not
  a defect list.
- Admin user created with the admin command
  (non-interactive route), confirmed with
  `hasuser` and `listusers`; `users.json`
  inspected — passwords stored hashed (t03).
- Login through the real web form (303 to the
  settings index); settings refuse anonymous
  visitors (t04).
- A receiver device (type rtl_tcp) and a
  profile (145 MHz centre, 2.4 MS/s, NFM)
  created through the web settings forms and
  found persisted in `settings.json` (t04).
- General settings saved through the form —
  receiver name, location, admin contact, and
  both compression settings — and reflected in
  `/status.json` (t05). A partial form post is
  rejected; the whole form must be submitted.
- The real `rtl_tcp_connector` (0.6.2) connected
  to the synthetic source and issued the
  correct tuning commands — centre frequency
  and sample rate matching the profile (t06).
- Full listening session over the websocket
  protocol, scripted to mirror the web page:
  handshake, config and profile messages,
  39 waterfall frames and 49 audio frames in
  15 s. The waterfall's peaks sit at the three
  offsets the synthetic signals were placed at
  (−170 kHz, +250 kHz, +600 kHz), and the
  demodulated audio's dominant tone measures
  1004 Hz against the 1000 Hz tone the FM
  signal was built with (t07).
- A bookmark created through the settings
  route and persisted in `bookmarks.json`
  (t08).

### Documented only — not run in the lab

- **The Docker install itself.** No container
  runtime exists in this sandbox (mounts are
  blocked), so chapter 3 follows the project's
  documentation and the image's own scripts,
  which the lab read line by line. The server
  it describes is bit-for-bit the server the
  lab ran.
- **Real radio reception.** No SDR hardware.
  The synthetic source proves everything from
  the connector onwards; antenna, tuner and
  real signals are the companion RTL-SDR
  guide's territory.
- **USB device handling** — permissions, udev
  rules, dongle enumeration. Follows the
  project documentation; nothing to plug in.
- **Background decoding of real traffic.** The
  decoders report available in the feature
  report, but no real APRS, FT8 or pager
  traffic was decoded; chapter 9 describes
  the mechanism and says so.
- **Digital voice (DMR, D-Star).** Needs the
  codecserver and its AMBE codec; the lab did
  not start it, and the feature report marks
  digiham unavailable.
- **The Raspberry Pi image and the Debian
  packages.** Documented routes, read from
  the project site, not installed.
- **Many simultaneous listeners.** One lab
  client at a time; the 20-client default
  limit is the program's, quoted as such.
- **OpenWebRX+** and the other neighbours in
  chapter 12 are described from their own
  documentation, not installed.

Fixtures: every name in this guide is invented
for the purpose — the admin user "rowan", the
"Bench Test Receiver", the "Lab Test Band".
No real person, station, or organisation is
modelled. Lab passwords and hashes are not
reproduced.
