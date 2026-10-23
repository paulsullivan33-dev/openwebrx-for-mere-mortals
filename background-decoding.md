# Background Decoding

**Scope:** the receiver's second job —
decoding digital traffic on a schedule,
while nobody is listening — and an honest
note about how far this guide's lab got
with it.

## The idea

Plenty of radio traffic is machines talking
to machines in standard encodings: aircraft
and ships aside, there are APRS position
packets, FT8 and WSPR signals that cross
continents on milliwatts, pagers, weather
satellites' slower cousins. A listener
rarely sits through these; a computer is
happy to. Background decoding lets
OpenWebRX park a profile on a digital
mode's dial frequency and decode whatever
passes, unattended.

Two switches make it happen:

- On the **profile**, the *services* option
  marks it as available for background work
  and chooses which decoding service runs
  there.
- In Settings → **Background decoding**,
  scheduling decides *when*: continuously,
  or in time windows (a receiver can follow
  the sun across bands, in effect, by
  scheduling different profiles at
  different hours on devices that support
  it).

While services run, the device is busy —
a listener who connects gets the profile
the schedule chose. Services also need the
device to be allowed to run when
unattended, which is the device-level
setting met in chapter 5.

## What can be decoded

Depends entirely on which decoders the
install can find — ask the feature report
(chapter 2). The lab's report said
available:

- **WSJT-X modes** (FT8, FT4, WSPR, JT65…)
  via the wsjt-x tools
- **Packet / APRS** via the packet decoder
- **POCSAG** paging
- **JS8Call**
- **FreeDV** and **M17** digital voice

And unavailable in the lab: DMR/D-Star via
digiham (wants the codec server running,
chapter 2) and DRM broadcasts (wants a
decoder this image doesn't carry). Your
install's list will differ with your
choices; the report, not this page, is the
authority.

Decoded results surface in the UI (the map
view plots APRS and similar position
traffic) and can be forwarded: Settings →
**Spotting and reporting** connects the
receiver to the hobby's reporting networks
(PSK Reporter for the WSJT modes, APRS-IS
for packets), which is how a receiver in a
quiet location ends up contributing
propagation data the whole hobby reads.
Reporting is off until you configure it —
check what a network expects of reporters
before switching it on.

## Honesty box

This chapter is the guide's most
documented-only. The lab verified that the
decoders *report available* in 1.2.2's
feature report, and read the scheduling and
services machinery in the settings; it did
not decode real traffic, having no real
signals to decode (criteria.md). The
mechanism is as described in the project's
documentation; your first real FT8 spots
on the map are the true check, and on a
real antenna with the dial frequencies the
program already knows, they typically
arrive within minutes.
