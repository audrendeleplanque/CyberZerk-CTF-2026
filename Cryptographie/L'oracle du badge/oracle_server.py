#!/usr/bin/env python3
"""Oracle ECB HTTP — Opération CyberZerk. GET /?data=<hex> -> chiffré hex.
Chiffre AES-128-ECB( PREFIXE || data || SECRET ). Clé+préfixe aléatoires au démarrage."""
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
from Crypto.Cipher import AES

_KEY    = os.urandom(16)
_PREFIX = os.urandom(13)
_SECRET = os.environ.get("BADGE_FLAG", "CyberZerk{ceci_est_un_exemple}").encode()

def _pad(b):
    n = 16 - (len(b) % 16); return b + bytes([n]) * n

def _encrypt(data: bytes) -> bytes:
    return AES.new(_KEY, AES.MODE_ECB).encrypt(_pad(_PREFIX + data + _SECRET))

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        q = parse_qs(urlparse(self.path).query)
        if "data" not in q:
            body = (b"Lecteur de badge Tricatel.\n"
                    b"Usage: GET /?data=<hex>  ->  AES-ECB(PREFIXE||data||SECRET) en hex\n")
            self.send_response(200); self.send_header("Content-Type","text/plain")
            self.end_headers(); self.wfile.write(body); return
        try:
            data = bytes.fromhex(q["data"][0])
        except ValueError:
            self.send_response(400); self.end_headers(); self.wfile.write(b"hex invalide"); return
        out = _encrypt(data).hex().encode()
        self.send_response(200); self.send_header("Content-Type","text/plain")
        self.end_headers(); self.wfile.write(out + b"\n")

if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8000), H).serve_forever()
