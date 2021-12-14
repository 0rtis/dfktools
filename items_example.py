import item.items as items
import logging
import sys


if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-items")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    balance = items.balance('0x2E7669F61eA77F02445A015FBdcFe2DE47083E02', items.JEWEL, rpc_server)
    balance = items.gwei2eth(balance)
    logger.info(str(balance) + " JEWEL")

