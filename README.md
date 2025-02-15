# EVM hex private key to Cometbft signing key

Tested on Debian12 with apt package `python-ecdsa`

`apt install python-ecdsa`

Example:

```bash
python3 key.py 8a2fd0a985d5bd9cb94ce78df65ba0b8017f4a111a6760d5985f5c7ea399459

{
  "address": "C00190A76D4611AB3FE52567E0851A12B45E68F4",
  "pub_key": {
    "type": "tendermint/PubKeySecp256k1",
    "value": "Ayl0UeAVrPiC+daKzS9vQpwY9/8gBzoW6oK/53CTNPzs"
  },
  "priv_key": {
    "type": "tendermint/PrivKeySecp256k1",
    "value": "aKL9CphdW9nLlM5432W6C4AX9KERpnYNWYX1x+o5lFk="
  }
}
```

**USE AT YOUR OWN DISCRETION - NOT FOR PRODUCTION**