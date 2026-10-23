# Bookmarks and Settings

**Scope:** the finishing touches an owner
applies once the receiver works — the
bookmark list listeners navigate by, the
receiver's public identity, and the two
compression settings that decide how the
streams are cooked.

## Bookmarks

A bookmark is a named frequency with a
mode attached: "Harbour control — 156.8 MHz
— NFM". Bookmarks appear on the receiver
page as markers; clicking one tunes there
and switches mode in one motion.

They are managed in Settings → **Bookmark
editor**, and they are **one global list**
for the whole receiver — not per device,
not per profile. A bookmark only makes
sense inside a window that contains its
frequency, so a tidy bookmark list and a
tidy profile list grow together.

Underneath, the list is a small JSON file,
`/var/lib/openwebrx/bookmarks.json`:

```json
[
  {
    "name": "Lab FM Test Signal",
    "frequency": 145250000,
    "modulation": "nfm"
  }
]
```

(The lab's one bookmark, created through
the settings page — transcript t08.) The
file is a fair emergency editor: stop the
server, edit carefully, keep the JSON
valid, restart.

There are also **dial frequencies**: for
the digital modes, OpenWebRX knows the
agreed watering-hole frequencies (the FT8
and WSPR dials and friends) and can show
them as markers. Those come from the
program, not from your bookmark file, and
arrive with the configuration when a
listener connects.

## The receiver's identity

Settings → **General settings** holds the
public face: receiver **name**, **location**
text, the admin **contact**, map
coordinates and elevation, and a photo and
description for the receiver's listing
page. On a fresh install these are the
project's placeholders — a receiver still
calling itself "[Callsign]" in "Budapest,
Hungary" is announcing that nobody has
visited this page yet. The lab set its
fixture identity here (transcript t05) and
watched it appear in `/status.json` at
once: these fields are what receiver
directories and curious visitors read, so
write them for strangers.

Two behaviours of this form caught the lab
out and are worth knowing:

- **It saves whole or not at all.** Every
  field is validated together; submit a
  partial or invalid form and you get the
  form back with nothing stored.
- There is no draft state. A successful
  save is live for the next listener who
  connects.

## Compression: the stream settings

Also on the general page, two settings
decide how the two binary streams are
encoded:

| Setting | Default | Alternatives |
| --- | --- | --- |
| Audio compression | ADPCM | None |
| FFT (waterfall) compression | ADPCM | None |

ADPCM shrinks both streams a long way at a
small quality cost, which is the right
default for anything beyond a LAN. "None"
sends raw samples — more bandwidth, and
the choice the lab made deliberately so
its test client could read the waterfall
numbers and demodulated audio directly
(transcripts t05, t07). Leave both on
ADPCM unless you have a reason as specific
as that one.

Nearby settings worth a look while you're
on the page: **max clients** (20 by
default), the **waterfall levels** (auto
by default; manual levels suit a band whose
noise floor you know), and **FFT size and
rate** — bigger and faster is prettier and
costs CPU on the server and bandwidth to
every listener at once.
