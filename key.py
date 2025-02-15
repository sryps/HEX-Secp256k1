import sys
from ecdsa import SigningKey, SECP256k1
import base64
import hashlib
import json
import binascii

priv_key_hex = sys.argv[1]

priv_key_bytes = bytes.fromhex(priv_key_hex)

sk = SigningKey.from_string(priv_key_bytes, curve=SECP256k1)

pub_key = sk.verifying_key.to_string("compressed")

binary_data = binascii.unhexlify(pub_key.hex())
base64_encoded = base64.b64encode(binary_data).decode()
pub_key_bytes = base64.b64decode(base64_encoded)

sha256_hash = hashlib.sha256(pub_key_bytes).digest()

ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
address_bytes = ripemd160_hash

address_hex = address_bytes.hex()

bd = binascii.unhexlify(priv_key_hex)
bd64enc = base64.b64encode(bd).decode()

datajson = {
  "address": address_hex.upper(),
  "pub_key": {
    "type": "tendermint/PubKeySecp256k1",
    "value": base64_encoded
  },
  "priv_key": {
    "type": "tendermint/PrivKeySecp256k1",
    "value": bd64enc
  }
}

print(json.dumps(datajson, indent=2))
