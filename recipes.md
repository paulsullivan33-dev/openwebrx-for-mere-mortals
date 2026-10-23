# Recipes

**Scope:** four jobs owners actually ask
for, each a short path through machinery
the earlier chapters built. Hardware
details stay in the companion guide,
*RTL-SDR for Mere Mortals*.

## 1. The dongle by the antenna, the server in the house

Antennas live in awkward places; servers
prefer cupboards. `rtl_tcp` splits the
difference: a small machine at the antenna
runs the dongle and serves its samples over
the network, and OpenWebRX treats the
stream as a device.

On the antenna machine (from the RTL-SDR
guide's toolkit):

```text
$ rtl_tcp -a 192.168.1.50 -p 1234
```

On the OpenWebRX server: add a device of
type **rtl_tcp** (chapter 5), set its
*remote* to `192.168.1.50:1234`, and give it
profiles as usual. The server starts the
stream when the first listener arrives and
lets go when the last leaves — the lab
verified this exact conversation against a
test source, watching the connector issue
the profile's centre frequency and sample
rate before a single sample flowed
(transcript t06).

Worth knowing: rtl_tcp carries the raw
stream, so on Wi-Fi the 2.4 MS/s default
(about 38 Mbit/s of samples) is a real
load. Wired, or a lower sample rate in the
profile, keeps it civil.

## 2. Three profiles every receiver gets asked for

- **FM broadcast** — centre inside the
  88–108 MHz band, sample rate 2.4 MS/s,
  start on a strong local station, mode
  **WFM**. Gain modest: broadcast signals
  are loud, and overload sounds worse than
  weakness.
- **2 m repeaters** — centre 146 MHz,
  start on your busiest repeater's output,
  mode **NFM**. The built-in sample profile
  (chapter 5) is a fine template.
- **Airband** — centre in 118–137 MHz,
  start on a tower or ATIS frequency, mode
  **AM**. Transmissions are short and
  sparse; squelch earns its keep here.

Each is a five-minute job in chapter 5's
form once the device exists.

## 3. A receiver with no radio (the test rig)

For trying OpenWebRX before any hardware
arrives — or for checking a server rebuild —
the lab's synthetic source serves again:
`examples/fake-rtltcp.py` streams a known
little band (three signals on a noise
floor) to any `rtl_tcp` device pointed at
it. If the waterfall shows peaks at
−170 kHz, +250 kHz and +600 kHz from centre
and the FM signal at +250 kHz plays a
steady 1 kHz tone, the server, connector,
DSP and page are all healthy, and only the
real dongle remains unproven. It is also
the safest way to learn the settings pages:
nothing you break here is on the air.

## 4. Two dongles, two windows

The sharing rule is per device, so a second
dongle is the honest way to offer two bands
at once: add it as a second device with its
own profiles. Listeners pick a device and
profile together, each window keeps its own
audience, and the server's CPU bill grows
by roughly one receiver's worth. (Nothing
exotic is involved — but watch the USB
power and the feature report if a device
type needs its driver installed.)
