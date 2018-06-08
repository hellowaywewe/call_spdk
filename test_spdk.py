from rpc.client import print_dict, JSONRPCException, JSONRPCClient
import rpc


class SPDKTgt(object):
    def __init__(
            self,
            server="/var/tmp/spdk.sock",
            port=5260,
            verbose=False,
            timeout=60.0):
        super(SPDKTgt, self).__init__()
        self.server_addr = server
        self.port = port
        self.verbose = verbose
        self.timeout = timeout

    # Get the client after connecting to the SPDK_based target
    def get_client(self):
        try:
            return JSONRPCClient(self.server_addr, self.port, self.verbose, self.timeout)
        except JSONRPCException as ex:
            print(ex.message)
            exit(1)


if __name__ == "__main__":
    spdk_tgt = SPDKTgt()
    client = spdk_tgt.get_client()
    try:
        subsystems = rpc.nvmf.get_nvmf_subsystems(client)
        print_dict(subsystems)
    except JSONRPCException as ex:
        print(ex.message)
        exit(1)

