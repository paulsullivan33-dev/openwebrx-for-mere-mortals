# Devices and Profiles

**Scope:** the two ideas all configuration
hangs off. A **device** is a tuner.
A **profile** is one window that tuner can
be pointed at, with everything a listener
needs pre-decided. Getting these right is
most of administering a receiver.

## Devices: one entry per tuner

Settings → **SDR devices and profiles** →
**Add new device**. The form asks for a name
and a type — and the type list is short on
purpose: it only offers types the feature
report (chapter 2) calls available. A type
missing from the list means a missing
driver or connector on the server, not a
form to argue with (chapter 14).

The lab created its device this way —
invented name, type `rtl_tcp`, because the
lab's "radio" was a test-signal server on
the same machine (transcript t04):

| Field | Lab value | Meaning |
| --- | --- | --- |
| Name | Bench Test Receiver | Shown to listeners |
| Type | rtl_tcp | Which connector drives it |
| Remote | 127.0.0.1:1234 | Where the rtl_tcp source listens |

A USB dongle's form differs in the obvious
way: no remote address, instead device
selection and gain options that make sense
for hardware in the machine. Two fields
appear on most device forms:

- **Enabled** — a disabled device is hidden
  from listeners but kept in the config.
- **Always on / services** — whether the
  device may run for background decoding
  when nobody is listening (chapter 9).

Saving writes the device into
`settings.json` immediately; there is no
separate "apply" step anywhere in
OpenWebRX settings.

## Profiles: windows, pre-decided

Under each device, **Add new profile**.
A profile is a complete answer to "what
should a listener get when they choose
this?":

| Field | Lab value | Meaning |
| --- | --- | --- |
| Name | Lab Test Band | What listeners pick from the list |
| Center frequency | 145 MHz | The middle of the window |
| Sample rate | 2.4 MS/s | The width of the window |
| Start frequency | 145.25 MHz | Where a new listener starts tuned |
| Start modulation | NFM | The mode they start in |
| RF gain | auto (AGC) | Or a fixed gain, per profile |

The form takes frequencies as a number plus
a unit (145 with "MHz"), because spectrum
numbers get long: the file underneath
stores plain hertz — 145000000 — which is
what the transcripts show.

**Check:** the profile is real when the
public status endpoint lists it:

```text
$ curl localhost:8073/status.json
... "name": "Lab Test Band",
    "center_freq": 145000000,
    "sample_rate": 2400000 ...
```

## The defaults you inherit

A fresh install is not empty. Built into
the program are sample devices — the lab's
untouched configuration held an "RTL-SDR USB
Stick" with two profiles (2 m at 145 MHz,
70 cm repeaters at 438.8 MHz), plus sample
Airspy HF+ and SDRPlay devices. Treat them
as scaffolding: rename, edit or delete them
to match the hardware you actually own, and
don't be surprised when the log notes that
a sample device whose hardware you don't
have is "not available" — the receiver runs
perfectly well on the devices that exist.

## Designing profiles people enjoy

Craft notes, from how receivers get used:

- **One profile per purpose**, named for
  the listener, not the hardware: "2 m
  repeaters", "Airband", "FM broadcast"
  beat "Profile 3".
- **Start frequency on something alive.**
  A new listener's first seconds decide
  whether they stay; start on the busiest
  channel in the window, in the right mode.
- **Sample rate is a trade.** Wider windows
  show more band and cost CPU, network, and
  (on RTL-SDR hardware) dynamic range.
  2.4 MS/s is the well-worn default for a
  reason.
- **Gain belongs to the profile** because
  bands differ: the setting that hears a
  weak repeater will overload on broadcast
  FM. Auto (AGC) is a sane start; fixed
  gains are for windows you know well.
