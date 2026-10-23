# The Neighbours

**Scope:** the tools that live next door to
OpenWebRX — one fork, two fellow web
receivers, and the desktop programs — and
how to choose between them. All described
from their own documentation; this guide's
lab installed none of them.

## OpenWebRX+

A community fork of OpenWebRX (by Marat
Fayzullin, maintained in recent years with
a wider set of bundled decoders and
receivers, themes, and extra modes and
conveniences layered on top). It aims to be
a drop-in expansion: same concepts, same
device-and-profile model, more built in.
The trade is the usual fork trade — more
features per install against a smaller
team and a faster-moving target. Owners who
outgrow the stock decoder list usually
look here first.

## WebSDR

The elder of web radio: PA3FWM's WebSDR has
run public receivers, many on university
and club stations, since long before SDR
dongles were cheap. Its page is plainer and
its model stricter (the host's hardware is
often bespoke), and the software is
available to established stations rather
than as a general download. If you've
listened to a famous HF receiver in a
browser, odds are it was a WebSDR or a
KiwiSDR.

## KiwiSDR

A hardware-and-software bundle: a dedicated
receiver board (with its own GPS for
timing) covering 0–30 MHz, famous for HF
and for networked tricks several KiwiSDRs
can do together, like direction finding.
You buy the board; the web receiver comes
with it. For HF specifically it is often
the better tool; it doesn't do VHF/UHF
dongle work at all, which is OpenWebRX's
home turf.

## The desktop programs

SDR++, GQRX, SDR# and friends put the radio
on *your* desk instead of in a browser:
one listener, every control local, no
sharing rules. They are the right answer
for exploring solo, for transmit-capable
rigs' control, and for weak-signal work
where you want the DSP close to the
antenna. The companion RTL-SDR guide's
toolkit (`rtl_fm`, `dump1090`, `rtl_433`)
is the command-line expression of the same
idea — and several of those tools feed an
OpenWebRX receiver nicely via recipe 1.

## Choosing, in one breath

A receiver the household or the world
should be able to hear from a browser:
OpenWebRX (or its + fork for the extra
decoders). HF only, with money for
dedicated hardware: KiwiSDR. Just you, at
the desk, exploring: a desktop program or
the command-line tools.
