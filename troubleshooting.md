# Troubleshooting

**Scope:** symptom → likely cause → fix,
in the order an owner actually meets them.
Several entries are this guide's own lab
notes, marked as such.

## The page loads, but no waterfall, no audio

**Likely:** the device never started —
nobody's at fault; devices start on the
first listener and this *is* the first
listener.

**Fix:** check the server log while you
connect. You want to see the connector
start and connect to the device. If the
log says the device type is "not
available", that's the next entry. If the
connector starts and fails to open the
hardware, suspect USB permissions or the
kernel DVB driver holding the dongle —
both covered in the companion RTL-SDR
guide.

## The log says an SDR device is "not available"

**Likely:** OpenWebRX can't find — or can't
use — that device type's driver/connector.
The lab met this twice: sample devices for
hardware it didn't have, and its RTL-SDR
type before the connector tools were on
the program's path.

**Fix:** open `/features` (or
`/api/features`). Everything the report
calls unavailable is unavailable everywhere
— including the new-device form, which
simply won't offer the type. Install the
missing driver/connector for your device,
restart, and re-check the report before
touching any profile.

## The new-device form doesn't list my receiver's type

Same cause, same fix as above: the form is
built from the feature report. A missing
menu entry is a missing driver, not a
missing setting.

## `admin adduser` hangs forever

**Likely (lab-verified):** you ran it
non-interactively — a script, a shell with
no terminal — without `--noninteractive`.
The prompt reads the terminal device
directly and waits for a typist who isn't
there. `OWRX_PASSWORD` doesn't rescue it;
the variable is only read in non-interactive
mode.

**Fix:** at a real keyboard, just run it
plainly and type at the prompt. In scripts:

```text
OWRX_PASSWORD='...' \
  openwebrx admin --noninteractive adduser name
```

## Login keeps bouncing back to the login page

**Likely:** the account is disabled, the
password is wrong, or the browser is
refusing the session cookie (a plain-HTTP
receiver reached by an unexpected name is a
classic cookie trap).

**Fix:** verify the account exists and is
enabled from the command line (`hasuser`,
`listusers` — chapter 8's table), reset the
password if unsure, and try the login from
the exact address listeners use.

## Settings won't save

**Likely:** on the General settings page,
one field failed validation and the whole
form was returned unsaved — this page is
all-or-nothing by design (chapter 7).

**Fix:** look for the field the form is
unhappy about (coordinates and numeric
fields are the usual suspects), fix it, and
submit the form complete. Devices and
profiles save independently, so a stuck
general form never blocks them.

## Audio plays but it's just noise

Work the chain in order. **Wrong window?**
The profile's centre and the signal must
coincide — check `/status.json` against
reality. **Wrong mode?** AM in NFM and
friends sound like expensive static; the
bookmark and profile start modes exist to
prevent exactly this. **Squelch shut?** A
squelch set for a strong local repeater
will mute a weak one entirely — open it and
listen to the hiss change. **Gain?** Too
little and nothing rises from the floor;
too much and the waterfall's floor rises
to meet everything — the companion guide's
gain chapter is the deep version.

## The waterfall is alive but frozen in the past / smeared

**Likely:** the machine is out of CPU
(wide sample rate, large FFT, many
listeners) or the stream settings outran
the network path — most visible when raw
(uncompressed) streams were switched on
for a test and left on.

**Fix:** put both compressions back to
ADPCM unless you need raw streams, reduce
FFT size/rate, and check the server's CPU
while a listener is connected before
blaming the network.

## Two profiles fight over one window

Not an error: the device has one window
and the last profile chosen wins, for
everyone. If this is a household, it's a
conversation. If it's a public receiver,
shorten the profile list to the windows
you're willing to have strangers select
(chapter 5), and let background decoding
schedules (chapter 9) own the hours nobody
should be steering.

## When you script against the websocket

An odd one the lab earned: a client that
connects to `/ws/` and sends well-formed
requests gets *silence* until it performs
the application handshake — the literal
text message `SERVER DE CLIENT
client=<name> type=receiver`. The server
logs "handshake is not complete" (politely,
as a warning) and answers nothing. Browsers
do this invisibly; your script must do it
on purpose. The reply to expect:
`CLIENT DE SERVER server=openwebrx
version=...` (transcript t07).
