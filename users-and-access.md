# Users and Access

**Scope:** what an OpenWebRX user account
is for — and what it is not for — plus the
full account toolbox, which lives on the
command line, and the honest options for
restricting who can listen.

## What accounts gate, and what they don't

Set this down plainly, because nearly every
new owner gets it wrong: **listening does
not require an account.** Anyone who can
load the page can listen, tune, and switch
profiles. An account unlocks:

- the settings (all seven sections of
  chapter 4) — this is the big one;
- changing your own password (`/pwchange`
  while signed in);
- being the named admin the receiver's
  identity page points at.

If your plan was "a password so only the
family can listen", the account system is
not that tool. The section below gives the
tools that are.

## Managing accounts

There is no user page in the web settings
in 1.2.2. Accounts are managed where the
first one was born — the admin command
(chapter 4), run inside the install:

| Task | Command |
| --- | --- |
| Create | `openwebrx admin adduser <name>` |
| List enabled | `openwebrx admin listusers` |
| Exists? | `openwebrx admin hasuser <name>` |
| Reset password | `openwebrx admin resetpassword <name>` |
| Disable | `openwebrx admin disableuser <name>` |
| Re-enable | `openwebrx admin enableuser <name>` |
| Delete | `openwebrx admin removeuser <name>` |

Accounts live in `/var/lib/openwebrx/
users.json` as a list with the password
stored as a salted hash (the lab's file
shows a `pbkdf2_sha256` entry — transcript
t03), the enabled flag, and a
must-change-password flag. Keep the number
of accounts small: each one is a settings
key to your receiver, so each should be a
person you'd hand the antenna coax to.

**Check:** after creating a second admin
for a household member, `listusers` shows
both names, and a login with the new
account reaches the settings index.

## Actually restricting listening

In rough order of how people really do it:

1. **Don't publish it.** On a home network,
   the receiver is reachable by the house
   and guests on the house Wi-Fi. For many
   owners that *is* the requirement, met.
2. **Put it behind a VPN or a tailnet.**
   Expose port 8073 only inside WireGuard,
   Tailscale, or an SSH tunnel. The receiver
   stays unmodified; the network does the
   gating. This is the pattern this series
   recommends for home services generally.
3. **A reverse proxy with authentication.**
   If it must be on the public internet
   with a gate, let a proxy (with its own
   user database and HTTPS) stand in front,
   and treat OpenWebRX's own login as the
   second lock, for settings only.
4. **Publish it properly.** Many owners run
   public receivers on purpose and list
   them in the project's receiver directory.
   That's a fine choice made with open
   eyes: anyone may listen, bandwidth is
   yours to pay for, and chapter 13's legal
   notes apply.

Whichever you choose, HTTPS matters the
moment credentials or listening cross the
open internet; the proxy in option 3 is
also where certificates belong.
