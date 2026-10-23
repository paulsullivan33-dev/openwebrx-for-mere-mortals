# First Login and the Admin User

**Scope:** the first account — how it comes
to exist, how you sign in, and what the
settings index you land on actually
contains.

## The account has to be made before it can be used

OpenWebRX does not ship with a default
username and password printed in a manual.
An admin account is created in one of two
ways:

**At first start, by the environment**
(Docker route). Set `OPENWEBRX_ADMIN_USER`
and `OPENWEBRX_ADMIN_PASSWORD` before the
first run, as chapter 3 does, and the
image's startup script creates that user if
it doesn't already exist. If the user
exists, the variables are ignored — they
are a bootstrap, not a reset mechanism.

**From the command line**, on any route:

```text
$ openwebrx admin adduser rowan
```

run inside the install. A package install
puts an `openwebrx` command on the path;
with Docker the same command runs inside
the container against the program file:
`docker exec -it openwebrx python3
openwebrx.py admin adduser rowan`. At a
keyboard it prompts for the password twice
and hides what you type.

For scripts there is a non-interactive
form, which the lab used and verified:

```text
$ OWRX_PASSWORD='...' \
    openwebrx admin --noninteractive \
    adduser rowan
Creating user rowan...
```

**Check:** the account exists, two ways:

```text
$ openwebrx admin --silent hasuser rowan
$ echo $?
0
$ openwebrx admin listusers
rowan
```

One trap, recorded because the lab fell
into it: without `--noninteractive`, the
command asks for the password by reading
the terminal device directly. Run it
somewhere with no terminal attached — a
script, a remote shell without a tty — and
it waits forever, silently, even if
`OWRX_PASSWORD` is set. The variable is
only honoured in non-interactive mode.

## Signing in

Open the receiver page and choose **Login**
(or go straight to `/login`), and sign in
with the account. A good login answers with
a redirect to `/settings`, and the settings
pages now open instead of bouncing you back
to the login form.

**Check:** `curl` shows the shape of it —
a `303` and a session cookie are what
success looks like, and without the cookie
every settings URL redirects to login.

## The settings index

Signing in lands on an index with seven
destinations. The whole rest of the guide
is mostly these seven, so meet them now:

| Section | What lives there | Chapter |
| --- | --- | --- |
| General settings | Receiver name, location, admin contact, map position, stream compression | 7 |
| SDR devices and profiles | The tuners and their listening windows | 5 |
| Bookmark editor | The shared bookmark list | 7 |
| Demodulation and decoding | Per-mode decoder options | 6, 9 |
| Background decoding | Scheduled decoding while nobody listens | 9 |
| Spotting and reporting | Sending decoded spots to reporting networks | 9 |
| Feature report | What this install can actually drive and decode | 2 |

Two habits worth starting immediately.
First, after any change here, open the
receiver page in a second, signed-out
browser window: that's what your listeners
see, and it's the view that matters.
Second, remember that none of these pages
exist for listeners — if a guest reports
seeing a settings screen, they are not
describing this software.
