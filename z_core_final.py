import json, time, os
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

V = {"version":"v1_9 UNIFIED OPUS45","hash":"89b6df2e-v24","port":8001,"status":"NON DEPENDANCE VALIDEE","logics":22,"security":"ZeroTrust","size":"5.4K","stack":"Python3.11 0 dep Termux"}

class H(BaseHTTPRequestHandler):
 def do_GET(self):
  if self.path == '/api/status':
   self.send_response(200); self.send_header('Content-type','application/json'); self.send_header('Access-Control-Allow-Origin','*'); self.end_headers()
   V['uptime'] = time.time()
   self.wfile.write(json.dumps(V, indent=2).encode())
  elif self.path.startswith('/SAHBI'):
   self.send_response(200); self.send_header('Content-type','text/html'); self.end_headers()
   self.wfile.write(Path('SAHBI-SA-BIN.HTML').read_bytes() if Path('SAHBI-SA-BIN.HTML').exists() else b'BIN manquant')
  else:
   self.send_response(200); self.send_header('Content-type','text/html'); self.end_headers()
   html = f"""
   <body style='background:#000;color:#0f0;font-family:monospace;padding:20px'>
   <h1>Z-CORE {V['hash']} LIVE</h1>
   <p>NON DEPENDANCE VALIDEE | 22 logics | ZeroTrust | Port 8001</p>
   <pre>{json.dumps(V, indent=2)}</pre>
   <a href='/api/status' style='color:#0f0'>/api/status</a> | <a href='/SAHBI-SA-BIN.HTML' style='color:#0f0'>SAHBI-SA-BIN.HTML</a>
   <p>Uptime: {time.ctime()}</p>
   </body>
   """
   self.wfile.write(html.encode())
 def log_message(self, *a): pass

print(f"Z-CORE {V['hash']} — IMMORTEL sur :8001 — PID {os.getpid()}")
HTTPServer(('0.0.0.0',8001), H).serve_forever()
