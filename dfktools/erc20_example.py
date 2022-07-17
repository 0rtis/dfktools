import dex.erc20 as tokens
import logging
import sys
from web3 import Web3


if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-erc20")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    w3 = Web3(Web3.HTTPProvider(rpc_server))

    realm = 'serendale'
    serendale_items = tokens.get_realm_item_list(realm)
    logger.info('{} items in {}'.format(len(serendale_items), realm))
    token_address = tokens.symbol2address('JEWEL', realm)
    name = tokens.name(token_address, rpc_server)
    symbol = tokens.symbol(token_address, rpc_server)
    decimal = tokens.decimals(token_address, rpc_server)
    balance = tokens.balance_of('0x2E7669F61eA77F02445A015FBdcFe2DE47083E02', token_address, rpc_server)
    balance = tokens.wei2eth(w3, balance)
    logger.info(name + " -> " + str(balance) + " " + symbol)

