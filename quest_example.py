import logging
import sys
import time
from web3 import Web3
from quests.professions import gardening
from quests.training import dancing
import quests.quest_v2 as quest_v2
import quests.quest_v1 as quest_v1
from quests.utils import utils as quest_utils
import dex.master_gardener


ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'

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

    '''
    All quest but gardening & mining should be started with V2
    '''

    questV2 = quest_v2.Quest(rpc_server, logger)
    quest_contract = dancing.QUEST_CONTRACT_ADDRESS
    my_heroes_id = [1, 2, 3, 4]
    attempts = 3
    level = 1
    questV2.start_quest(quest_contract, my_heroes_id, 3, attempts, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, tx_timeout)
    quest_info = quest_utils.human_readable_quest(questV2.get_hero_quest(my_heroes_id[0]))

    logger.info(
        "Waiting " + str(quest_info['completeAtTime'] - time.time()) + " secs to complete quest " + str(quest_info))
    while time.time() < quest_info['completeAtTime']:
        time.sleep(2)

    tx_receipt = questV2.complete_quest(my_heroes_id[0], private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, tx_timeout)
    quest_result = questV2.parse_complete_quest_receipt(tx_receipt)
    logger.info("Rewards: " + str(quest_result))

    # gardening quest
    pool_id = 0  # See gardens.master_gardener
    questV1 = quest_v1.Quest(rpc_server, logger)
    quest_data = (pool_id, 0, 0, 0, 0, 0, '', '', ZERO_ADDRESS, ZERO_ADDRESS, ZERO_ADDRESS, ZERO_ADDRESS)
    my_gardener_heroes_id = [5]
    attempts = 1
    questV1.start_quest_with_data(gardening.QUEST_CONTRACT_ADDRESS, quest_data, my_gardener_heroes_id, attempts, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, tx_timeout)
    quest_info = quest_utils.human_readable_quest(questV1.get_hero_quest(my_heroes_id[0]))

    logger.info(
        "Waiting " + str(quest_info['completeAtTime'] - time.time()) + " secs to complete gardening quest " + str(quest_info))
    while time.time() < quest_info['completeAtTime']:
        time.sleep(2)

    questV1.complete_quest(my_gardener_heroes_id[0], private_key, w3.eth.getTransactionCount(account_address),
                                      gas_price_gwei, tx_timeout)