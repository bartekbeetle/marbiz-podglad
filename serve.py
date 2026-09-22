#!/usr/bin/env python3
"""Lekki serwer statyczny dla strony Marbiz — localhost:3007.

Zwykły `python3 -m http.server` nie potrafi serwować własnej strony 404.html
ze statusem HTTP 404 (oddaje generyczną stronę biblioteki). Ten skrypt
nadpisuje send_error tak, żeby brakująca ścieżka zwracała treść 404.html
z realnym kodem 404 — wymóg checklisty startowej (SPA fallback ≠ prawdziwe 404).
"""

import http.server
import os
import socketserver

PORT = 3007
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class MarbizHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            path_404 = os.path.join(DIRECTORY, "404.html")
            try:
                with open(path_404, "rb") as f:
                    content = f.read()
            except OSError:
                return super().send_error(code, message, explain)

            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(content)
            return

        return super().send_error(code, message, explain)

    def log_message(self, fmt, *args):
        # Log skrótowy zamiast domyślnego (mniej szumu w terminalu).
        print(f"[marbiz-www] {self.address_string()} - {fmt % args}")


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


if __name__ == "__main__":
    with ReusableTCPServer(("", PORT), MarbizHandler) as httpd:
        print(f"Marbiz — serwuję {DIRECTORY} pod http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nZatrzymano.")
