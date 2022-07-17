import logging
import sys
from web3 import Web3
import consumable.consumable as consumable

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-consumable")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    stamina_vial_address = '0x959ba19508827d1ed2333B1b503Bd5ab006C710e'

    w3 = Web3(Web3.HTTPProvider(rpc_server))
    private_key = None  # set private key
    account_address = w3.eth.account.privateKeyToAccount(private_key).address
    gas_price_gwei = 40
    tx_timeout_seconds = 30

    hero_id = 1
    consumable.consume_item(stamina_vial_address, hero_id, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, tx_timeout_seconds, rpc_server, logger)