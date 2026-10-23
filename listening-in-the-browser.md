# Listening in the Browser

**Scope:** the receiver page itself — what
a listener sees, how tuning works, and what
the sharing rule from chapter 1 feels like
from the listener's chair.

## The page

Open `http://<host>:8073/`. The screen is
mostly **waterfall**: frequency runs left
to right across the profile's window, time
scrolls downward, and brightness is signal
strength — live carriers stand out as
bright threads, and the band's character
(noise floor, busy hours, dead hours) is
visible at a glance. A frequency scale and
band labels sit above it, drawn from the
band plan. The lab's waterfall, measured
rather than admired: 4096 points across a
2.4 MHz window, a noise floor at −64 dB,
and the three test signals exactly where
they had been placed (transcript t07).

Down the side and across the bottom live
the controls: volume, mode, bandwidth,
squelch, and the tuning readout. Nothing
here needs an account.

## Tuning

- **Click** on the waterfall to tune there.
- **Drag** to fine-tune in small steps.
- The **mouse wheel** over the frequency
  readout steps by the tuning precision;
  typing a frequency directly is the fast
  route across the window.
- The passband marker on the frequency
  scale shows exactly which slice of
  spectrum your demodulator is drinking
  from; its width is the bandwidth control.

Modes offered follow the window: **NFM**
for repeaters and most voice, **WFM** for
broadcast FM (with stereo and RDS where
the signal carries them), **AM** for
airband and medium wave, **LSB/USB** for
the HF voice bands, **CW**, and — where the
feature report says the decoders exist —
digital modes from packet and POCSAG to
FT8 and digital voice. Choosing a mode also
chooses sensible default bandwidth and
step; both remain adjustable.

**Squelch** mutes the audio until a signal
crosses the level you set — the difference
between listening to a repeater and
listening to its silence. The S-meter
readout beside it is the same measurement
the server sends listeners several times a
second.

## Switching profiles

The profile list is the receiver's front
door: pick "Airband" and the window moves —
for you, and, per chapter 1, for everyone.
OpenWebRX handles the social reality of
that plainly: profiles are the unit of
sharing, the current profile is visible to
all, and changing it is a public act. On a
household receiver this is a shrug; on a
busy public one it's why owners keep the
profile list short and purposeful
(chapter 5).

## Many listeners, one receiver

Listeners are independent in everything
except the window: each tunes, picks a
mode, and sets volume and squelch alone.
The server caps concurrent clients (20 by
default, a general setting) and shows the
count in its status. When the last listener
leaves, the device is released — the lab
watched the connector disconnect the moment
its scripted listener closed (t06).

What a listener's browser actually
receives, for the curious: a websocket
carrying small JSON messages (profile
changes, S-meter, configuration) and two
binary streams — waterfall frames and
demodulated audio. The page's first act on
connecting is a small ceremony worth
knowing if you ever script against it: it
greets the server with the text
`SERVER DE CLIENT ... type=receiver`, and
nothing is answered before that greeting
arrives.
