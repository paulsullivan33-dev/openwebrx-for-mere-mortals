#!/usr/bin/env python3
"""A synthetic rtl_tcp server: plays a test engineer, not a radio.

Speaks just enough of the rtl_tcp protocol to satisfy rtl_tcp_connector:
12-byte dongle header, then an endless loop of precomputed 8-bit I/Q.
The "band" (2.4 MS/s around whatever centre the client asks for) contains:
  -170 kHz : an AM carrier, 700 Hz tone, 60% depth
     0 Hz   : a weak steady carrier (the "centre spur")
  +250 kHz : an FM carrier, 1 kHz tone, +/-4 kHz deviation
  +600 kHz : a strong steady carrier
plus a gentle noise floor. Commands from the client (set frequency,
set sample rate, gain, ...) are logged line by line as evidence.
Buffer is 1 s long; the two tones divide 1 s evenly, so the loop is
seamless. Noise is regenerated per pass so the floor is not a loop.
"""
import socket, struct, sys, threading
import numpy as np

SR = 2_400_000
N = SR  # one second
rng = np.random.default_rng(20261022)

t = np.arange(N) / SR

def tone_fm(offset, tone_hz, dev_hz, amp):
    phase = 2 * np.pi * offset * t + (dev_hz / tone_hz) * np.sin(2 * np.pi * tone_hz * t)
    return amp * np.exp(1j * phase)

def tone_am(offset, tone_hz, depth, amp):
    env = 1.0 + depth * np.sin(2 * np.pi * tone_hz * t)
    return amp * env * np.exp(1j * 2 * np.pi * offset * t)

def carrier(offset, amp):
    return amp * np.exp(1j * 2 * np.pi * offset * t)

# deterministic part of the band, computed once
signal = (tone_am(-170_000, 700, 0.6, 0.35)
          + carrier(0, 0.10)
          + tone_fm(+250_000, 1000, 4000, 0.55)
          + carrier(+600_000, 0.8))

def iq_bytes():
    noise = (rng.normal(0, 0.045, N) + 1j * rng.normal(0, 0.045, N))
    x = signal + noise
    i = np.clip(np.round(127.5 + 127 * x.real), 0, 255).astype(np.uint8)
    q = np.clip(np.round(127.5 + 127 * x.imag), 0, 255).astype(np.uint8)
    out = np.empty(2 * N, dtype=np.uint8)
    out[0::2] = i
    out[1::2] = q
    return out.tobytes()

CMDS = {0x01: "set center frequency", 0x02: "set sample rate",
        0x03: "set gain mode", 0x04: "set gain", 0x05: "set ppm",
        0x06: "set gain by index", 0x08: "set agc mode",
        0x0d: "set direct sampling", 0x0e: "set bias tee"}

def handle(conn, addr):
    print(f"client connected from {addr}", flush=True)
    # dongle info: magic, tuner type 5 (R820T), 29 gain steps
    conn.sendall(b"RTL0" + struct.pack(">II", 5, 29))
    stop = threading.Event()

    def reader():
        buf = b""
        while not stop.is_set():
            try:
                data = conn.recv(4096)
            except OSError:
                return
            if not data:
                return
            buf += data
            while len(buf) >= 5:
                cmd, param = buf[0], struct.unpack(">I", buf[1:5])[0]
                buf = buf[5:]
                print(f"command 0x{cmd:02x}: {CMDS.get(cmd, 'unknown')} = {param}",
                      flush=True)
    threading.Thread(target=reader, daemon=True).start()
    try:
        while True:
            conn.sendall(iq_bytes())  # 1 s of I/Q per pass
    except (BrokenPipeError, ConnectionResetError, OSError):
        print("client disconnected", flush=True)
    finally:
        stop.set()
        conn.close()

def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 1234
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", port))
    srv.listen(1)
    print(f"fake rtl_tcp server listening on 127.0.0.1:{port}", flush=True)
    while True:
        conn, addr = srv.accept()
        handle(conn, addr)

if __name__ == "__main__":
    main()
