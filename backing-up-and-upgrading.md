# Backing Up and Upgrading

**Scope:** the shortest important chapter
in the guide. An OpenWebRX receiver's whole
identity is a handful of files; backing it
up is copying them, and restoring is
putting them back.

## What to copy

From chapter 2's table, the state is:

| Copy this | Because it holds |
| --- | --- |
| `/var/lib/openwebrx/settings.json` | Devices, profiles, general settings |
| `/var/lib/openwebrx/users.json` | Every account and its hashed password |
| `/var/lib/openwebrx/bookmarks.json` | The bookmark list |
| `/etc/openwebrx/openwebrx.conf` (+ `.conf.d/`) | Core settings, port, paths |
| `/etc/openwebrx/bands.json` | Your band plan edits, if any |

In the Docker route those are exactly the
two volumes from chapter 3 — back up the
volumes, or the folder behind them, with
whatever already backs up the rest of your
server. Skip `/tmp/openwebrx`: it is
scratch, recreated at start.

**Check:** a backup you haven't restored is
a hope, not a backup. The drill takes five
minutes on a spare machine or a second
container: install fresh, stop the server,
drop the five files in, start, and sign in
with your usual account to find your
devices, profiles and bookmarks waiting.
The lab's whole configuration — one device,
one profile, one bookmark, one user — fits
in a few kilobytes; yours will too.

## Upgrading

An upgrade replaces the program, not the
state. The files above persist across it
(the Docker volumes; the package manager
doesn't touch `/var/lib` or your `/etc`
edits), and at start the new version
migrates configuration if its format has
moved — the lab's first start logged
exactly such a migration line, once, and
then never again.

Working habits:

- **Pin, then choose your moment.** If you
  followed chapter 3's advice and pinned a
  version tag, upgrading is editing the
  tag, pulling, and restarting — done when
  you're there to watch the first listener
  connect, not by an unattended timer.
- **Read the release notes for config
  changes** before, not after; they are
  short and specific.
- **Back up first anyway.** The five files
  take seconds; they are the difference
  between "upgrade went oddly" and "put
  the old files and the old tag back".

Downgrading is the reverse with one
caution: a config already migrated forward
may not be readable by the old version,
which is the second reason the pre-upgrade
copy matters.
