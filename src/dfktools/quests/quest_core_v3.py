import copy
from web3 import Web3
from defikingdoms.lib.src.dfktools.hero.utils import utils as hero_utils

SERENDALE_CONTRACT_ADDRESS = None
CRYSTALVALE_CONTRACT_ADDRESS = None
SERENDALE2_CONTRACT_ADDRESS = None


ABI = """
    [	
        {"inputs":[{"internalType":"uint256","name":"_questInstanceId","type":"uint256"}],"name":"clearActiveQuests","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"clearActiveQuestsAndHeroes","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_offset","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"clearActiveQuestsAndHeroesWithOffset","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"questInstanceId","type":"uint256"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enumQuestStatus","name":"status","type":"uint8"},{"internalType":"uint8","name":"questType","type":"uint8"}],"indexed":false,"internalType":"structQuest","name":"quest","type":"tuple"}],"name":"QuestCanceled","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"questInstanceId","type":"uint256"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enumQuestStatus","name":"status","type":"uint8"},{"internalType":"uint8","name":"questType","type":"uint8"}],"indexed":false,"internalType":"structQuest","name":"quest","type":"tuple"}],"name":"QuestCompleted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"address","name":"rewardItem","type":"address"},{"indexed":false,"internalType":"uint256","name":"itemQuantity","type":"uint256"}],"name":"QuestReward","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"profession","type":"uint8"},{"indexed":false,"internalType":"uint16","name":"skillUp","type":"uint16"}],"name":"QuestSkillUp","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"staminaSpent","type":"uint256"}],"name":"QuestStaminaSpent","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"questInstanceId","type":"uint256"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enumQuestStatus","name":"status","type":"uint8"},{"internalType":"uint8","name":"questType","type":"uint8"}],"indexed":false,"internalType":"structQuest","name":"quest","type":"tuple"},{"indexed":false,"internalType":"uint256","name":"startAtTime","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"completeAtTime","type":"uint256"}],"name":"QuestStarted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint64","name":"xpEarned","type":"uint64"}],"name":"QuestXP","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"xpBefore","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"xpAfter","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"percentage","type":"uint256"}],"name":"QuickStudy","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":true,"internalType":"address","name":"reward","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"data","type":"uint256"}],"name":"RewardMinted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokenBonusAwarded","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"success","type":"bool"},{"indexed":false,"internalType":"uint256","name":"attempt","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"TrainingAttemptDone","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"winCount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"attempts","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"TrainingSuccessRatio","type":"event"},
        {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"cancelQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"completeQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_account","type":"address"}],"name":"getAccountActiveQuests","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"questInstanceId","type":"uint256"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enumQuestStatus","name":"status","type":"uint8"},{"internalType":"uint8","name":"questType","type":"uint8"}],"internalType":"structQuest[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"getCurrentStamina","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"getHeroQuest","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"questInstanceId","type":"uint256"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enumQuestStatus","name":"status","type":"uint8"},{"internalType":"uint8","name":"questType","type":"uint8"}],"internalType":"structQuest","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"getQuestInstanceIds","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"heroToQuest","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"}],"name":"multiCompleteQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256[][]","name":"_heroIds","type":"uint256[][]"},{"internalType":"uint256[]","name":"_questInstanceId","type":"uint256[]"},{"internalType":"uint8[]","name":"_attempts","type":"uint8[]"},{"internalType":"uint8[]","name":"_level","type":"uint8[]"},{"internalType":"uint8[]","name":"_type","type":"uint8[]"}],"name":"multiStartQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"questCounter","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"quests","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"questInstanceId","type":"uint256"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enumQuestStatus","name":"status","type":"uint8"},{"internalType":"uint8","name":"questType","type":"uint8"}],"internalType":"structQuest","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"},{"internalType":"uint256","name":"_questInstanceId","type":"uint256"},{"internalType":"uint8","name":"_attempts","type":"uint8"},{"internalType":"uint8","name":"_level","type":"uint8"},{"internalType":"uint8","name":"_type","type":"uint8"}],"name":"startQuest","outputs":[],"stateMutability":"nonpayable","type":"function"}
    ]
    """

QUEST_TYPE_FISHING = 1
QUEST_TYPE_FORAGING = 2
QUEST_TYPE_GOLD_MINING = 3
QUEST_TYPE_TOKEN_MINING = 4
QUEST_TYPE_GARDENING = 5
QUEST_TYPE_TRAINING = 6

QUEST_PARAM_TRAINING_STRENGTH = 0
QUEST_PARAM_TRAINING_INTELLIGENCE = 1
QUEST_PARAM_TRAINING_WISDOM = 2
QUEST_PARAM_TRAINING_LUCK = 3
QUEST_PARAM_TRAINING_AGILITY = 4
QUEST_PARAM_TRAINING_VITALITY = 5
QUEST_PARAM_TRAINING_ENDURANCE = 6
QUEST_PARAM_TRAINING_DEXTERITY = 7


def block_explorer_link(contract_address: str, txid: str):
    if hasattr(contract_address, 'address'):
        contract_address = str(contract_address.address)
    contract_address = str(contract_address).upper()
    if contract_address == SERENDALE_CONTRACT_ADDRESS.upper():
        return 'https://explorer.harmony.one/tx/' + str(txid)
    elif contract_address == CRYSTALVALE_CONTRACT_ADDRESS.upper():
        return 'https://subnets.avax.network/defi-kingdoms/dfk-chain/explorer/tx/' + str(txid)
    elif contract_address == SERENDALE2_CONTRACT_ADDRESS.upper():
        return 'https://scope.klaytn.com/tx/' + str(txid)
    else:
        return str(txid)


def start_quest(quest_core_contract_address: str, hero_ids: list, quest_type: int, attempts: int, level: int, quest_param: int, private_key: str, nonce: int, gas_price_gwei, tx_timeout_seconds: int, rpc_address: str, logger):
    """

    :param quest_core_contract_address:
    :param hero_ids:
    :param quest_type:
    :param attempts:
    :param level:
    :param quest_param:  for quests that have additional varieties, a type input will determine which quest the Hero ultimately is sent to.
            - For Gardening, type will follow the poolId of the Garden
            - For Training Quests, type will follow the stat order used on the HeroCore contract, which is not the same order as the mapping used for
    :param private_key:
    :param nonce:
    :param gas_price_gwei:
    :param tx_timeout_seconds:
    :param rpc_address:
    :param logger:
    :return:
    """
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.from_key(private_key)
    w3.eth.default_account = account.address

    quest_core_contract_address = Web3.to_checksum_address(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)

    tx = contract.functions.startQuest(hero_ids, quest_type, attempts, level, quest_param)

    if isinstance(gas_price_gwei, dict):   # dynamic fee
        tx = tx.build_transaction(
            {'maxFeePerGas': w3.to_wei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.to_wei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:   # legacy
        tx = tx.build_transaction({'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info(
        "Waiting for transaction " + block_explorer_link(quest_core_contract_address, signed_tx.hash.hex()) + " to be mined")

    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def multi_start_quest(quest_core_contract_address, hero_idss: list, quest_types: list, attempts: list, levels: list, quest_params: list, private_key: str, nonce: int, gas_price_gwei, tx_timeout_seconds: int, rpc_address:str, logger):
    """

    :param quest_core_contract_address:
    :param hero_idss:
    :param quest_types:
    :param attempts:
    :param levels:
    :param quest_params: for quests that have additional varieties, a type input will determine which quest the Hero ultimately is sent to.
            - For Gardening, type will follow the poolId of the Garden
            - For Training Quests, type will follow the stat order used on the HeroCore contract, which is not the same order as the mapping used for
    :param private_key:
    :param nonce:
    :param gas_price_gwei:
    :param tx_timeout_seconds:
    :param rpc_address:
    :param logger:
    :return:
    """
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.from_key(private_key)
    w3.eth.default_account = account.address

    quest_core_contract_address = Web3.to_checksum_address(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)

    tx = contract.functions.multiStartQuest(hero_idss, quest_types, attempts, levels, quest_params)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.build_transaction(
            {'maxFeePerGas': w3.to_wei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.to_wei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.build_transaction({'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info(
        "Waiting for transaction " + block_explorer_link(quest_core_contract_address, signed_tx.hash.hex()) + " to be mined")

    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def complete_quest(quest_core_contract_address: str, hero_id: int, private_key: str, nonce: int, gas_price_gwei, tx_timeout_seconds: int, rpc_address: str, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.from_key(private_key)
    w3.eth.default_account = account.address

    quest_core_contract_address = Web3.to_checksum_address(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)

    tx = contract.functions.completeQuest(hero_id)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.build_transaction(
            {'maxFeePerGas': w3.to_wei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.to_wei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.build_transaction(
            {'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info(
        "Waiting for transaction " + block_explorer_link(quest_core_contract_address, signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt

def multi_complete_quest(quest_core_contract_address: str, hero_ids: list, private_key: str, nonce: int, gas_price_gwei, tx_timeout_seconds: int, rpc_address: str, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.from_key(private_key)
    w3.eth.default_account = account.address

    quest_core_contract_address = Web3.to_checksum_address(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)

    tx = contract.functions.multiCompleteQuest(hero_ids)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.build_transaction(
            {'maxFeePerGas': w3.to_wei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.to_wei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.build_transaction({'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info(
        "Waiting for transaction " + block_explorer_link(quest_core_contract_address, signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def parse_complete_quest_receipt(quest_core_contract_address: str, tx_receipt, rpc_address: str):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    quest_core_contract_address = Web3.to_checksum_address(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)

    quest_result = {}

    quest_reward = contract.events.RewardMinted().process_receipt(tx_receipt)
    quest_result['reward'] = quest_reward

    quest_xp = contract.events.QuestXP().process_receipt(tx_receipt)
    quest_result['xp'] = quest_xp

    quest_skill_up = contract.events.QuestSkillUp().process_receipt(tx_receipt)
    quest_result['skillUp'] = quest_skill_up

    return quest_result


def cancel_quest(quest_core_contract_address: str, hero_id: int, private_key: str, nonce: int, gas_price_gwei, tx_timeout_seconds: int, rpc_address: str, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.from_key(private_key)
    w3.eth.default_account = account.address

    quest_core_contract_address = Web3.to_checksum_address(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)

    tx = contract.functions.cancelQuest(hero_id)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.build_transaction(
            {'maxFeePerGas': w3.to_wei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.to_wei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.build_transaction({'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info(
        "Waiting for transaction " + block_explorer_link(quest_core_contract_address, signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def multi_cancel_quests(quest_core_contract_address: str, hero_ids: list, private_key: str, nonce: int, gas_price_gwei, tx_timeout_seconds:int, rpc_address: str, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.from_key(private_key)
    w3.eth.default_account = account.address

    quest_core_contract_address = Web3.to_checksum_address(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)

    tx = contract.functions.multiCancelQuest(hero_ids)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.build_transaction(
            {'maxFeePerGas': w3.to_wei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.to_wei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.build_transaction({'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info(
        "Waiting for transaction " + block_explorer_link(quest_core_contract_address, signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def clear_active_quest_and_heroes(quest_core_contract_address: str, private_key: str, nonce: int, gas_price_gwei, tx_timeout_seconds: int, rpc_address: str, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.from_key(private_key)
    w3.eth.default_account = account.address

    quest_core_contract_address = Web3.to_checksum_address(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)

    tx = contract.functions.clearActiveQuestsAndHeroes()

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.build_transaction(
            {'maxFeePerGas': w3.to_wei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.to_wei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.build_transaction({'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info(
        "Waiting for transaction " + block_explorer_link(quest_core_contract_address, signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def hero_to_quest_id(quest_core_contract_address: str, hero_id: int, rpc_address: str):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    quest_core_contract_address = Web3.to_checksum_address(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)
    result = contract.functions.heroToQuest(hero_id).call()

    return result


def get_active_quest(quest_core_contract_address: str, address: str, rpc_address: str):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    quest_core_contract_address = Web3.to_checksum_address(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)
    result = contract.functions.getAccountActiveQuests(address).call()

    return result


def get_hero_quest(contract_address: str, hero_id: int, rpc_address: str):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.getHeroQuest(hero_id).call()

    if result[0] <= 0:
        return None

    return result


def get_current_stamina(quest_core_contract_address: str, hero_id: int, rpc_address: str):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    quest_core_contract_address = Web3.to_checksum_address(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)
    result = contract.functions.getCurrentStamina(hero_id).call()

    return result

def get_quest_types(quest_core_contract_address: str, rpc_address: str):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    quest_core_contract_address = Web3.to_checksum_address(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)
    result = contract.functions.getQuestInstanceIds().call()

    return result

def get_quest_counter(quest_core_contract_address: str, rpc_address: str):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    quest_core_contract_address = Web3.to_checksum_address(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)
    result = contract.functions.questCounter().call()

    return result

