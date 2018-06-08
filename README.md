call_spdk
=========
The call_spdk project is an example about how the upper application calls these modified methods of the  SPDK(/scripts/rpc/nvmf.py) [0]. It directly bypasses the /scripts/rpc.py and imports the /scripts/rpc/*.py modules from SPDK.

Executive Command
-----------------
#sudo python test_spdk.py

Running Results
---------------
[
    {
      "nqn": "nqn.2014-08.org.nvmexpress.discovery",
      "subtype": "Discovery"
      "listen_addresses": [],
      "hosts": [],
      "allow_any_host": true
    }
]

This result is consistent with the result of running the command (sudo ./rpc.py -s /var/tmp/spdk.sock -p 5260 get_nvmf_subsystems) directly.

Reference links
---------------
[0]https://review.gerrithub.io/c/spdk/spdk/+/414296
