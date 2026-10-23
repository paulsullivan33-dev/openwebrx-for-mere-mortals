# Limits

**Scope:** what OpenWebRX cannot do, costs
that surprise people, and the one page of
legal common sense every receiver owner
should read once.

## The structural limits

- **One window per device.** Everyone on a
  device shares its centre frequency and
  sample rate (chapter 1). A second window
  means a second tuner (recipe 4). No
  setting changes this; it is physics, not
  policy.
- **Profiles move for everyone.** A profile
  switch is instant and public. Busy
  receivers manage this socially, not
  technically.
- **Receive only.** There is no transmitter
  support to enable or secure; the software
  cannot transmit.
- **Your hardware's limits are inherited.**
  An 8-bit dongle's dynamic range, its
  frequency drift, its spurs: OpenWebRX
  displays them faithfully. The companion
  guide covers what the hardware can and
  can't hear.

## The running costs

- **CPU is per sample-rate and per
  listener.** The waterfall FFT is computed
  once per device and shared; each
  listener's demodulator is their own. A
  Pi serves a dongle and a household easily;
  wide sample rates to many listeners is
  where small machines run out.
- **Bandwidth is per listener.** With the
  default ADPCM compression, each listener
  costs a modest, steady stream; turn
  compression off (chapter 7) or raise FFT
  size and rate and that stream grows for
  everybody at once.
- **Decoders are external programs.** If a
  mode's decoder isn't installed, the mode
  quietly isn't offered — the feature
  report is the ledger, and it only knows
  what it can find at runtime.

## Software limits worth knowing

- **Accounts don't gate listening**
  (chapter 8). If that surprises you, it
  surprises you once, here, rather than
  after you've shared the link.
- **Users are managed on the command
  line.** No web user administration in
  1.2.2.
- **Settings save whole.** The general
  settings form rejects partial posts
  (chapter 7); devices and profiles save
  per form.
- **Bookmarks are one global list.** No
  per-profile or per-user sets.

## Listening, legally

Rules vary by country, and this guide is
not a lawyer — but the common shape, stated
plainly: receiving broadcast, amateur,
airband, and other transmissions intended
for general reception is broadly lawful in
many places; some jurisdictions restrict
receiving or *disclosing* other traffic
(encrypted services, private
communications, anything scrambled is off
limits in practice as well as law), and
re-streaming what you hear to the public
can change the legal picture entirely,
quite apart from the bandwidth bill. Know
your local rules before a receiver leaves
your own network, and never rebroadcast
content you wouldn't read aloud to the
people transmitting it.
