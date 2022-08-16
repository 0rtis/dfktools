from web3 import Web3

SERENDALE_CONTRACT_ADDRESS = '0xAa9a289ce0565E4D6548e63a441e7C084E6B52F6'
CRYSTALVALE_CONTRACT_ADDRESS = '0xE9AbfBC143d7cef74b5b793ec5907fa62ca53154'

ABI = """
        [
           	{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct Quest","name":"quest","type":"tuple"}],"name":"QuestCanceled","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct Quest","name":"quest","type":"tuple"}],"name":"QuestCompleted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"address","name":"rewardItem","type":"address"},{"indexed":false,"internalType":"uint256","name":"itemQuantity","type":"uint256"}],"name":"QuestReward","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"profession","type":"uint8"},{"indexed":false,"internalType":"uint16","name":"skillUp","type":"uint16"}],"name":"QuestSkillUp","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"staminaSpent","type":"uint256"}],"name":"QuestStaminaSpent","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct Quest","name":"quest","type":"tuple"}],"name":"QuestStarted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint64","name":"xpEarned","type":"uint64"}],"name":"QuestXP","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":true,"internalType":"address","name":"reward","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"data","type":"uint256"}],"name":"RewardMinted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"success","type":"bool"},{"indexed":false,"internalType":"uint256","name":"attempt","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"TrainingAttemptDone","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"winCount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"attempts","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"TrainingSuccessRatio","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
            {"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"_questAddress","type":"address"}],"name":"activateQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"activeAccountQuests","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"cancelQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"completeQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"_questAddress","type":"address"},{"internalType":"uint256","name":"_questIndex","type":"uint256"}],"name":"deactivateQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"address","name":"_account","type":"address"}],"name":"getAccountActiveQuests","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"internalType":"struct Quest[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"_role","type":"bytes32"}],"name":"getAccountsWithRole","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"getCurrentStamina","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"getHeroQuest","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"internalType":"struct Quest","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"getQuestContracts","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"heroToQuest","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"_heroCoreAddress","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isQuest","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"internalType":"struct Quest","name":"_quest","type":"tuple"},{"internalType":"uint256","name":"_heroId","type":"uint256"},{"internalType":"uint8","name":"_profession","type":"uint8"},{"internalType":"uint16","name":"_skillUp","type":"uint16"}],"name":"logSkillUp","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"internalType":"struct Quest","name":"_quest","type":"tuple"},{"internalType":"uint256","name":"_heroId","type":"uint256"},{"internalType":"uint64","name":"_xpEarned","type":"uint64"}],"name":"logXp","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"}],"name":"multiCancelQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address[]","name":"_questAddress","type":"address[]"},{"internalType":"uint256[][]","name":"_heroIds","type":"uint256[][]"},{"internalType":"uint8[]","name":"_attempts","type":"uint8[]"},{"internalType":"uint8[]","name":"_level","type":"uint8[]"}],"name":"multiStartQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"questCounter","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"questRewarder","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"quests","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"_questRewarder","type":"address"}],"name":"setQuestRewarder","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_timePerStamina","type":"uint256"}],"name":"setTimePerStamina","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"},{"internalType":"address","name":"_questAddress","type":"address"},{"internalType":"uint8","name":"_attempts","type":"uint8"},{"internalType":"uint8","name":"_level","type":"uint8"}],"name":"startQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"timePerStamina","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"},{"internalType":"address","name":"_questAddress","type":"address"},{"internalType":"uint8","name":"_attempts","type":"uint8"},{"components":[{"internalType":"uint256","name":"uint1","type":"uint256"},{"internalType":"uint256","name":"uint2","type":"uint256"},{"internalType":"uint256","name":"uint3","type":"uint256"},{"internalType":"uint256","name":"uint4","type":"uint256"},{"internalType":"int256","name":"int1","type":"int256"},{"internalType":"int256","name":"int2","type":"int256"},{"internalType":"string","name":"string1","type":"string"},{"internalType":"string","name":"string2","type":"string"},{"internalType":"address","name":"address1","type":"address"},{"internalType":"address","name":"address2","type":"address"},{"internalType":"address","name":"address3","type":"address"},{"internalType":"address","name":"address4","type":"address"}],"internalType":"struct IQuestTypes.QuestData","name":"_questData","type":"tuple"}],"name":"startQuestWithData","outputs":[],"stateMutability":"nonpayable","type":"function"}
        ]
        """


def block_explorer_link(contract_address, txid):
    if hasattr(contract_address, 'address'):
        contract_address = str(contract_address.address)
    contract_address = str(contract_address).upper()
    if contract_address == SERENDALE_CONTRACT_ADDRESS.upper():
        return 'https://explorer.harmony.one/tx/' + str(txid)
    elif contract_address == CRYSTALVALE_CONTRACT_ADDRESS.upper():
        return 'https://subnets.avax.network/defi-kingdoms/dfk-chain/explorer/tx/' + str(txid)
    else:
        return str(txid)


def start_quest(quest_core_contract_address, quest_address, hero_ids, attempts, level, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    quest_core_contract_address = Web3.toChecksumAddress(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)

    if isinstance(gas_price_gwei, dict):   # dynamic fee
        tx = contract.functions.startQuest(hero_ids, quest_address, attempts, level).buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:   # legacy
        tx = contract.functions.startQuest(hero_ids, quest_address, attempts, level).buildTransaction(
            {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

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


def start_quests(quest_core_contract_address, quest_addresses, hero_idss, attempts, levels, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    quest_core_contract_address = Web3.toChecksumAddress(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = contract.functions.multiStartQuest(quest_addresses, hero_idss, attempts, levels).buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = contract.functions.multiStartQuest(quest_addresses, hero_idss, attempts, levels).buildTransaction(
            {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

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


def complete_quest(quest_core_contract_address, hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    quest_core_contract_address = Web3.toChecksumAddress(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = contract.functions.completeQuest(hero_id).buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = contract.functions.completeQuest(hero_id).buildTransaction(
            {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

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


def parse_complete_quest_receipt(quest_core_contract_address, tx_receipt, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    quest_core_contract_address = Web3.toChecksumAddress(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)

    quest_result = {}

    quest_reward = contract.events.RewardMinted().processReceipt(tx_receipt)
    quest_result['reward'] = quest_reward

    quest_xp = contract.events.QuestXP().processReceipt(tx_receipt)
    quest_result['xp'] = quest_xp

    quest_skill_up = contract.events.QuestSkillUp().processReceipt(tx_receipt)
    quest_result['skillUp'] = quest_skill_up

    return quest_result


def cancel_quest(quest_core_contract_address, hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    quest_core_contract_address = Web3.toChecksumAddress(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = contract.functions.cancelQuest(hero_id).buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = contract.functions.cancelQuest(hero_id).buildTransaction(
            {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

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


def cancel_quests(quest_core_contract_address, hero_ids, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    quest_core_contract_address = Web3.toChecksumAddress(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = contract.functions.multiCancelQuest(hero_ids).buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = contract.functions.multiCancelQuest(hero_ids).buildTransaction(
            {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

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


def hero_to_quest_id(quest_core_contract_address, hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    quest_core_contract_address = Web3.toChecksumAddress(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)
    result = contract.functions.heroToQuest(hero_id).call()

    return result


def get_active_quest(quest_core_contract_address, address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    quest_core_contract_address = Web3.toChecksumAddress(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)
    result = contract.functions.getAccountActiveQuests(address).call()

    return result


def get_hero_quest(contract_address, hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.getHeroQuest(hero_id).call()

    if result[0] <= 0:
        return None

    return result


def get_quests(quest_core_contract_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    quest_core_contract_address = Web3.toChecksumAddress(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)
    result = contract.functions.getQuestContracts().call()

    return result


def get_quest(quest_core_contract_address, quest_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    quest_core_contract_address = Web3.toChecksumAddress(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)
    result = contract.functions.getQuest(quest_id).call()

    if result[0] <= 0:
        return None

    return result


def is_quest(quest_core_contract_address, address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    quest_core_contract_address = Web3.toChecksumAddress(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)
    result = contract.functions.isQuest(address).call()

    return result


def get_quest_data(quest_core_contract_address, quest_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    quest_core_contract_address = Web3.toChecksumAddress(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)
    result = contract.functions.getQuestData(quest_id).call()

    return result


def quest_address_to_type(quest_core_contract_address, quest_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    quest_core_contract_address = Web3.toChecksumAddress(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)
    result = contract.functions.questAddressToType(quest_address).call()

    return result


def get_current_stamina(quest_core_contract_address, hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    quest_core_contract_address = Web3.toChecksumAddress(quest_core_contract_address)
    contract = w3.eth.contract(quest_core_contract_address, abi=ABI)
    result = contract.functions.getCurrentStamina(hero_id).call()

    return result


