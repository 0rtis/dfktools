import logging
import sys
import time
from web3 import Web3
from quest import foraging
from quest import fishing
from quest.quest import Quest
from quest.utils import utils as quest_utils

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-quest")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    private_key = None  # set private key
    gas_price_gwei = 15
    tx_timeout = 30
    w3 = Web3(Web3.HTTPProvider(rpc_server))
    account_address = w3.eth.account.privateKeyToAccount(private_key).address

    quest_contract = fishing.CONTRACT_ADDRESS  # foraging.CONTRACT_ADDRESS
    quest = Quest(quest_contract, rpc_server, logger)

    my_heroes_id = [1, 2, 3, 4]
    quest.start_quest(my_heroes_id, 3, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, tx_timeout)
    quest_info = quest_utils.parse_quest(quest.get_hero_quest(my_heroes_id[0]))

    logger.info(
        "Waiting " + str(quest_info['completeAtTime'] - time.time()) + " secs to complete quest " + str(quest_info))
    while time.time() < quest_info['completeAtTime']:
        time.sleep(2)

    tx_receipt = quest.complete_quest(my_heroes_id[0], private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, tx_timeout)
    quest_result = quest.parse_complete_quest_receipt(tx_receipt)
    logger.info("Rewards: " + str(quest_result))
