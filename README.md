# OpenWebRX for Mere Mortals

A software-defined radio receiver normally
serves one person: whoever is sitting at the
computer the dongle is plugged into.
**OpenWebRX** moves the receiver onto a
server and the listening into a web page, so
one modest receiver and one antenna can be
heard from any browser on the network — the
waterfall, the tuning, and the audio all
arrive over the wire, and several people can
listen to the same receiver at once. This
guide explains how it is put together, how
to install it, how to set up your first
device and profile, and how to think about
the one rule that governs everything else
it does: everybody listening shares the
same slice of spectrum, because there is
only one tuner.

The lab behind this guide ran the real
thing: **OpenWebRX 1.2.2**, the project's
current release on build day, from the
official Docker image. It was exercised the
way a first week with it actually goes — an
admin account created, a receiver and a
listening profile configured through the web
settings, the receiver's identity set, a
bookmark saved, and then a full listening
session: waterfall frames and demodulated
audio pulled over the same websocket the
real web page uses. Two honest caveats
shape the lab, and both are declared rather
than hidden. The build machine offers no
container runtime, so the image's own
filesystem was run directly — same code,
no container around it — and there was no
radio hardware on the bench, so a small
synthetic server stood in for the dongle
and played three known test signals down
the wire. The peaks landed in the waterfall
exactly where the signals were put, and the
tone came back out of the demodulator at
the frequency it went in. What the lab
could not do — real antennas, real signals,
background decoders chewing real traffic —
is labelled documented-only in
`criteria.md`, which keeps the full ledger.

For the hardware half of this hobby — the
dongles themselves, antennas, gain, and
what the numbers on the dials mean — the
companion guide in this series, *RTL-SDR
for Mere Mortals*, is the place to start.
This guide assumes a receiver exists and
picks up where plugging it in leaves off.

## What this guide covers

- [**What OpenWebRX is**](what-openwebrx-is.md) —
  the mental model: one tuner, many
  listeners, a receiver that lives in a
  browser tab; what it is not (a scanner, a
  transmitter, a private radio per listener)
- [**The moving parts**](the-moving-parts.md) —
  the server, the DSP chain, the connectors
  that talk to hardware, the codec server,
  and the handful of files that hold all
  the state
- [**Installing OpenWebRX**](installing.md) —
  the official Docker route, the Raspberry
  Pi image, and the package install, with
  ports, volumes, and the two ways the
  first admin account comes to exist
- [**First login and the admin user**](first-login-and-admin.md) —
  creating the admin, signing in, and a tour
  of the settings index you land on
- [**Devices and profiles**](devices-and-profiles.md) —
  the two ideas everything else hangs off:
  a device is a tuner, a profile is a
  window onto the spectrum, and profiles
  are what listeners actually choose
- [**Listening in the browser**](listening-in-the-browser.md) —
  the waterfall, tuning, modes, squelch,
  and what twenty people sharing one
  receiver really experience
- [**Bookmarks and settings**](bookmarks-and-settings.md) —
  the global bookmark list, the receiver's
  public identity, and the settings that
  change how the streams are cooked
- [**Users and access**](users-and-access.md) —
  who a user account does and doesn't gate,
  managing accounts from the command line,
  and sensible ways to share a receiver
- [**Background decoding**](background-decoding.md) —
  receivers that work while nobody listens:
  scheduled profiles, digital decoders, and
  reporting what they hear
- [**Backing up and upgrading**](backing-up-and-upgrading.md) —
  the small set of files that *are* your
  receiver, a restore drill, and what an
  upgrade actually touches
- [**Recipes**](recipes.md) — a receiver by
  the antenna on another machine over
  rtl_tcp, profiles for the bands people
  ask for first, and a no-hardware test rig
- [**The neighbours**](the-neighbours.md) —
  the OpenWebRX+ fork, WebSDR, KiwiSDR, and
  the desktop SDR programs, and which one
  fits which job
- [**Limits**](limits.md) — one tuner, one
  window; the costs in CPU and bandwidth;
  no transmitting; and the legal common
  sense of listening
- [**Troubleshooting**](troubleshooting.md) —
  symptom → fix, starting with the errors
  this guide's own lab produced
- [**Glossary**](glossary.md) — every term
  used above, in plain words

## What it doesn't cover

- **The radio hardware itself.** Choosing a
  dongle, antennas, amplifiers, and gain
  staging live in *RTL-SDR for Mere Mortals*
  and the guides for the other receivers.
- **Radio theory.** What I/Q samples are and
  why sample rate is a window width get a
  working explanation here; the mathematics
  has its own shelf of books.
- **Transmitting.** OpenWebRX is receive
  only, full stop.
- **Running a public internet receiver as a
  service.** The guide covers sharing on
  your own network and says what changes
  before you open one to the world, but a
  public deployment deserves its own
  security pass.

## How to use this guide

Read chapters 1–2 for the model, then
install (chapter 3) and set up (chapters
4–5) in order; after that the chapters
stand alone. Commands are shown the way
you would run them, with **Check:** blocks
showing what success looks like. Anything
the lab verified says so, with the evidence
in `openwebrx-lab/transcripts/`; anything
it couldn't is labelled documented-only in
`criteria.md` and in the text where it
appears.
