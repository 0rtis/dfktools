import logging
from web3 import Web3
import sys
import time
import dfk_lib.meditation.meditation as meditation


if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-meditation")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    private_key = None  # set private key
    account_address = '0x2E7669F61eA77F02445A015FBdcFe2DE47083E02'
    gas_price_gwei = 10
    tx_timeout_seconds = 30
    w3 = Web3(Web3.HTTPProvider(rpc_server))

    active_meditations = meditation.get_active_meditations(account_address, rpc_server)
    logger.info("Pending meditation on address " + str(account_address) + ": "+str(active_meditations))

    level = 1
    hero_id = 1
    required_runes = meditation.get_required_runes(level, rpc_server)
    meditation.start_meditation(1, meditation.stat2id('strength'), meditation.stat2id('endurance'), meditation.stat2id('luck'),
                               meditation.ZERO_ADDRESS, private_key, w3.eth.getTransactionCount(account_address),
                               gas_price_gwei, tx_timeout_seconds, rpc_server, logger)
    hero_meditation = meditation.get_hero_meditation(hero_id, rpc_server)
    logger.info("Pending meditation "+str(hero_meditation))
    time.sleep(5)
    meditation.complete_meditation(hero_id, private_key, w3.eth.getTransactionCount(account_address),
                                  gas_price_gwei, tx_timeout_seconds, rpc_server, logger)

