# What OpenWebRX Is

**Scope:** the idea of the thing — a radio
receiver that lives on a server and is heard
through a web page — and the three facts
about it that explain everything else in
this guide.

## A receiver with a web page for a face

A software-defined radio (SDR) dongle does
very little by itself: it tunes to a
frequency, digitises a slice of the spectrum
a few megahertz wide, and hands the raw
samples — called I/Q — to the computer.
Everything a listener recognises as "a
radio" — picking a station out of that
slice, demodulating it into audio — is
software. The companion guide in this
series, *RTL-SDR for Mere Mortals*, covers
that hardware and the command-line tools
that drive it, one listener at a time.

OpenWebRX takes the same dongle and puts a
server in the middle:

- The dongle plugs into a machine that runs
  all the time — a Raspberry Pi by the
  antenna, a small home server.
- OpenWebRX reads the samples, draws the
  **waterfall** (a scrolling picture of the
  slice, frequency across, time down,
  brightness for strength), and demodulates
  whatever each listener tunes to inside
  the slice.
- Listeners open a web page. No install, no
  account needed just to listen: the page
  shows the waterfall and plays the audio.

It began as a university project in
Hungary (the server still greets its
clients with a ham-radio flourish, and its
author's callsign is in the protocol) and
is now maintained by Jakob Ketterl; the
project is open source, and 1.2.2 is the
release this guide was built against.

## Fact one: one tuner, one window

The dongle can only be tuned to one place
at a time, and its slice is a few megahertz
wide. Every listener therefore looks at the
*same* window onto the spectrum. Within the
window you have complete freedom — tune
where you like, choose your mode, set your
squelch — but you cannot wander off to a
different band, because the hardware isn't
there. When somebody changes the window
(the **profile**, chapter 5), it changes
for everyone connected.

This single fact explains most of
OpenWebRX's shape: profiles exist to make
window-changing deliberate; the receiver's
owner curates a small set of windows worth
sharing; and a busy moment on a public
receiver is a small negotiation, not a
queue.

## Fact two: the server does the work

Demodulation, the waterfall maths, and the
digital decoders all run on the server, in
a pipeline built from the `csdr` tools. A
listener's laptop or phone does almost
nothing — which is why a ten-year-old
tablet makes a perfectly good receiver
face, and why the server's CPU, not the
listeners', is the budget to watch
(chapter 13).

The streams are cooked to order: the
waterfall is compressed before it travels,
and the audio is sent as a small compressed
stream (ADPCM by default) rather than raw
samples. A browser tab ends up costing on
the order of a low-quality voice call in
bandwidth — the guide quotes no exact
figure because it depends on the settings
you choose in chapter 7.

## Fact three: listening is public, settings are not

Out of the box, anyone who can reach the
page can listen. Changing anything — the
receiver's name, its devices, its profiles —
needs an admin account and lives behind a
login. User accounts exist, but their job
is narrower than newcomers expect: they
gate the settings and a few optional
extras, not the act of listening itself
(chapter 8 covers what accounts do and
don't do, and how to really restrict a
receiver if you need to).

## What it is not

- **Not a scanner.** It sits in one window
  until a human moves it.
- **Not a transmitter.** Receive only;
  there is no transmit path to configure
  away.
- **Not one radio per listener.** Twenty
  listeners, one window — chapter 6 shows
  how that feels in practice.
- **Not a recording archive.** It decodes
  some digital modes in the background
  (chapter 9) but it is a live receiver,
  not a DVR for the spectrum.
