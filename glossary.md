# Glossary

**ADPCM** — the compression applied to the
waterfall and audio streams by default:
small, slightly lossy, and the reason a
browser tab costs so little bandwidth.

**AGC (automatic gain control)** — letting
the receiver set its own gain moment to
moment, instead of a fixed value in a
profile.

**Background decoding** — scheduled
decoding of digital traffic (FT8, APRS,
pagers) while nobody is listening.

**Band plan** — the agreed map of who uses
which frequencies; OpenWebRX keeps one in
`bands.json` to label the waterfall.

**Bookmark** — a named frequency plus a
mode, shared by the whole receiver, that
tunes a listener in one click.

**Centre frequency** — the middle of a
profile's window; the tuner is parked here.

**Codec server** — the separate program
that decodes AMBE-wrapped digital voice
(DMR, D-Star) for OpenWebRX.

**Connector** — the small program that owns
one kind of device for OpenWebRX, takes its
tuning commands, and streams its samples.

**csdr / pycsdr** — the DSP library, and
its Python bindings, that turn raw samples
into waterfalls and audio.

**Device** — one tuner, as far as
OpenWebRX configuration is concerned.

**Dial frequency** — the agreed reference
frequency for a digital mode (the FT8
watering holes), shown as a marker.

**DSP (digital signal processing)** — the
maths between raw samples and things humans
recognise: filters, demodulators, FFTs.

**FFT** — the calculation that turns a slice
of samples into a spectrum picture; one row
of the waterfall.

**Feature report** — OpenWebRX's runtime
inventory of which drivers and decoders it
can actually use, at `/features`.

**I/Q samples** — the raw output of an SDR:
pairs of numbers describing the signal's
wave, millions per second, from which all
else is computed.

**Mode / modulation** — the encoding a
signal uses: NFM, WFM, AM, SSB, CW, and the
digital family. Choosing wrong sounds like
noise.

**Profile** — a pre-decided window: centre,
sample rate, start frequency and mode, and
gain, under one friendly name. The unit
listeners choose, and share.

**rtl_tcp** — a simple protocol for serving
a dongle's samples over a network; also an
OpenWebRX device type that consumes such a
stream.

**Sample rate** — samples per second, and
therefore the width of the window a profile
can see.

**S-meter** — the signal-strength readout;
in OpenWebRX, a live level sent to every
listener's page.

**Squelch** — a gate that mutes audio until
a signal crosses a set level.

**Waterfall** — the scrolling spectrum
picture: frequency across, time down,
brightness for strength.
