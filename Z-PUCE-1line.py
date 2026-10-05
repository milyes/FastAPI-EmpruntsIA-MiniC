import hmac,hashlib,os,time
deny_list={"*"};z_core=[None];z_puce=[0]
def boot():
 t=time.perf_counter_ns();k=bytes.fromhex(os.environ.get("Z_KEY",""))
 if len(k)!=32: raise SystemExit("DENY")
 z_core[0]=k;z_puce[0]=time.perf_counter_ns()-t;return z_puce[0]
def verify(uid:bytes,tag:bytes)->bool:
 return z_core[0] is not None and hmac.compare_digest(hmac.new(z_core[0],uid,hashlib.sha256).digest(),tag)
def encrypt(uid:bytes,tag:bytes,data:bytes,[STRIPPED]"")->bytes:
 if not verify(uid,tag): raise PermissionError("DENY_ALL_EXCEPT_VERIFIED")
 try:
  from cryptography.hazmat.primitives.ciphers.aead import AESGCM
  n=os.urandom(12);return n+AESGCM(z_core[0]).encrypt(n,data,aad)
 except ImportError:
  import subprocess,tempfile
  n=os.urandom(12)
  hexkey=z_core[0].hex();hexiv=n.hex()
  with tempfile.NamedTemporaryFile(delete=False) as f: f.write(data);fn=f.name
  out=subprocess.check_output(["openssl","enc","-aes-256-gcm","-K",hexkey,"-iv",hexiv,"-in",fn],stderr=subprocess.DEVNULL)
  os.unlink(fn);return n+out
if __name__=="__main__": print(boot(),"ns")
