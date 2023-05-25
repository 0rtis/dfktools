import logging
import sys
import time
from web3 import Web3
import quests.professions.fishing as fishing
import quests.professions.gardening as gardening
import quests.quest_v3 as quest_v3, quests.quest_core_v3 as quest_core_v3, quests.quest_v2 as quest_v2, quests.quest_core_v2 as quest_core_v2, quests.quest_v1 as quest_v1
import quests.utils.utils as quest_utils

ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-quest")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    serendale2_rpc_server = 'https://klaytn.rpc.defikingdoms.com/'
    crystalvale_rpc_server = 'https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc'
    logger.info("Using RPC servers " + serendale2_rpc_server + ", " + crystalvale_rpc_server)

    w3_serendale2 = Web3(Web3.HTTPProvider(serendale2_rpc_server))
    w3_crystalvale = Web3(Web3.HTTPProvider(crystalvale_rpc_server))

    # Parse completeQuest transaction receipt V2
    tx_receipt = w3_serendale2.eth.get_transaction_receipt('0x7096f3742c27dedb5c9020d895f453524ec583b99a007238095e2cddce8e67aa')
    quest_result = quest_v2.Quest(quest_core_v2.SERENDALE2_CONTRACT_ADDRESS, serendale2_rpc_server, logger).parse_complete_quest_receipt(tx_receipt)
    quest_rewards = quest_utils.human_readable_quest_results(quest_result, very_human=True)
    logger.info("Rewards V2: {}".format(str(quest_rewards)))

    # Full quest flow
    private_key = None  # set private key
    gas_price_gwei_serendale = {'maxFeePerGas': 55, 'maxPriorityFeePerGas': 25}  # EIP-1559
    gas_price_gwei_crystalvale = {'maxFeePerGas': 2, 'maxPriorityFeePerGas': 2}  # EIP-1559
    tx_timeout = 30

    account_address = w3_serendale2.eth.account.from_key(private_key).address

    # Fishing in Crystalvale
    questV3 = quest_v3.Quest(quest_core_v3.CRYSTALVALE_CONTRACT_ADDRESS, crystalvale_rpc_server, logger)
    my_heroes_id = [1, 2, 3, 4]
    attempts = 3
    level = 1
    questV3.start_quest(my_heroes_id, quest_core_v3.QUEST_TYPE_FISHING, attempts, level, 0, private_key, w3_crystalvale.eth.get_transaction_count(account_address), gas_price_gwei_crystalvale, tx_timeout)
    quest_info = quest_utils.human_readable_quest(questV3.get_hero_quest(my_heroes_id[0]))

    logger.info(
        "Waiting " + str(quest_info['completeAtTime'] - time.time()) + " secs to complete quest " + str(quest_info))
    while time.time() < quest_info['completeAtTime']:
        time.sleep(2)

    tx_receipt = questV3.complete_quest(my_heroes_id[0], private_key, w3_crystalvale.eth.get_transaction_count(account_address), gas_price_gwei_crystalvale, tx_timeout)
    quest_result = questV3.parse_complete_quest_receipt(tx_receipt)
    quest_rewards = quest_utils.human_readable_quest_results(quest_result, very_human=True)
    logger.info("Rewards: {}".format(str(quest_rewards)))

    # Gardening in Serendale
    questV3 = quest_v3.Quest(quest_core_v3.SERENDALE2_CONTRACT_ADDRESS, serendale2_rpc_server, logger)
    pool_id = 0 # 'wJEWEL-xJEWEL' (see gardens.master_gardener)
    quest_data = (pool_id, 0, 0, 0, 0, 0, '', '', ZERO_ADDRESS, ZERO_ADDRESS, ZERO_ADDRESS, ZERO_ADDRESS)
    my_gardener_heroes_id = [5]
    attempts = 1
    level = 0
    questV3.start_quest(my_gardener_heroes_id, quest_core_v3.QUEST_TYPE_GARDENING, attempts, level, pool_id, private_key,
                        w3_serendale2.eth.get_transaction_count(account_address), gas_price_gwei_crystalvale, tx_timeout)
    quest_info = quest_utils.human_readable_quest(questV3.get_hero_quest(my_heroes_id[0]))

    logger.info(
        "Waiting " + str(quest_info['completeAtTime'] - time.time()) + " secs to complete quest " + str(quest_info))
    while time.time() < quest_info['completeAtTime']:
        time.sleep(2)

    tx_receipt = questV3.complete_quest(my_heroes_id[0], private_key,
                                        w3_serendale2.eth.get_transaction_count(account_address),
                                        gas_price_gwei_crystalvale, tx_timeout)
    quest_result = questV3.parse_complete_quest_receipt(tx_receipt)
    quest_rewards = quest_utils.human_readable_quest_results(quest_result, very_human=True)
    logger.info("Rewards: {}".format(str(quest_rewards)))

    # Gardening in Crystalvale
    questV3 = quest_v3.Quest(quest_core_v3.CRYSTALVALE_CONTRACT_ADDRESS, crystalvale_rpc_server, logger)
    pool_id = 0 # 'wJEWEL-xJEWEL'
    my_heroes_id = [1, 2]
    attempts = 1
    level = 0
    questV3.start_quest(my_heroes_id, quest_core_v3.QUEST_TYPE_GARDENING, attempts, level, pool_id, private_key, w3_crystalvale.eth.get_transaction_count(account_address), gas_price_gwei_crystalvale, tx_timeout)
    quest_info = quest_utils.human_readable_quest(questV3.get_hero_quest(my_heroes_id[0]))

    logger.info(
        "Waiting " + str(quest_info['completeAtTime'] - time.time()) + " secs to complete quest " + str(quest_info))
    while time.time() < quest_info['completeAtTime']:
        time.sleep(2)

    tx_receipt = questV3.complete_quest(my_heroes_id[0], private_key, w3_crystalvale.eth.get_transaction_count(account_address), gas_price_gwei_crystalvale, tx_timeout)
    quest_result = questV3.parse_complete_quest_receipt(tx_receipt)
    quest_rewards = quest_utils.human_readable_quest_results(quest_result, very_human=True)
    logger.info("Rewards: {}".format(str(quest_rewards)))