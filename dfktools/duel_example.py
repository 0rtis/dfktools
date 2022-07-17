import logging
import json
import sys
import duel.duel as duels
from web3 import Web3

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-duel")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    result = duels.get_duel(1, rpc_server)
    logger.info(json.dumps(result, indent=4, sort_keys=False))

    w3 = Web3(Web3.HTTPProvider(rpc_server))
    private_key = ""  # set private key
    account_address = "0x"  # w3.eth.account.privateKeyToAccount(private_key).address
    gas_price_gwei = 120
    tx_timeout_seconds = 30


    # start ranked duel
    '''
    Ranked match jewel fees
    Solo: 0.1, 0.5, 1
    Squad: 0.3, 1.5, 3
    War: 1, 5, 10
    '''
    duels.enter_duel_lobby('solo', [241730], 0.1, 'forest', 'dexterity',
                            private_key, w3.eth.getTransactionCount(account_address),
                            gas_price_gwei, tx_timeout_seconds, rpc_server, logger)

    # start private duel
    duels.start_private_duel('solo', [241730], '0x', 'forest', 'dexterity',
                            private_key, w3.eth.getTransactionCount(account_address),
                            gas_price_gwei, tx_timeout_seconds, rpc_server, logger)

    # complete duel
    duels.complete_duel(40331,
                        private_key, w3.eth.getTransactionCount(account_address),
                        gas_price_gwei, tx_timeout_seconds, rpc_server, logger)

    # result = duels.getDuelTurns(1,rpc_server) # get duels details based on Duel ID
    # result = duels.get_total_open_duel_entries(3, rpc_server) # 1-Solo,3-Squad,9-War
