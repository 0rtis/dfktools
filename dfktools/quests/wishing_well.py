from web3 import Web3


CONTRACT_ADDRESS = '0xf5ff69f4ac4a851730668b93fc408bc1c49ef4ce'

ABI = """
        [
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"QuestCanceled","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"QuestCompleted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"address","name":"rewardItem","type":"address"},{"indexed":false,"internalType":"uint256","name":"itemQuantity","type":"uint256"}],"name":"QuestReward","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"profession","type":"uint8"},{"indexed":false,"internalType":"uint64","name":"skillUp","type":"uint64"}],"name":"QuestSkillUp","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"indexed":false,"internalType":"uint16","name":"staminaSpent","type":"uint16"}],"name":"QuestStaminaSpent","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"QuestStarted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint64","name":"xpEarned","type":"uint64"}],"name":"QuestXP","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
            {"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"cancelQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"completeQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"randomNumber","type":"uint256"},{"internalType":"uint256","name":"digits","type":"uint256"},{"internalType":"uint256","name":"offset","type":"uint256"}],"name":"extractNumber","outputs":[{"internalType":"uint256","name":"result","type":"uint256"}],"stateMutability":"pure","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"getCurrentStamina","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"heroToQuest","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"_heroCoreAddress","type":"address"},{"internalType":"address","name":"_statScienceAddress","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"lastRewardIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"questLevel","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"rewardItems","outputs":[{"internalType":"contract IInventoryItem","name":"item","type":"address"},{"internalType":"int64","name":"expBonus","type":"int64"},{"internalType":"int64","name":"skillUpChance","type":"int64"},{"internalType":"int64","name":"smallSkillUpMod","type":"int64"},{"internalType":"int64","name":"mediumSkillUpMod","type":"int64"},{"internalType":"int64","name":"largeSkillUpMod","type":"int64"},{"internalType":"int64","name":"baseChance","type":"int64"},{"internalType":"int64","name":"skillMod","type":"int64"},{"internalType":"int64","name":"statMod","type":"int64"},{"internalType":"int64","name":"luckMod","type":"int64"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"runeRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"components":[{"internalType":"contract IInventoryItem","name":"item","type":"address"},{"internalType":"int64","name":"expBonus","type":"int64"},{"internalType":"int64","name":"skillUpChance","type":"int64"},{"internalType":"int64","name":"smallSkillUpMod","type":"int64"},{"internalType":"int64","name":"mediumSkillUpMod","type":"int64"},{"internalType":"int64","name":"largeSkillUpMod","type":"int64"},{"internalType":"int64","name":"baseChance","type":"int64"},{"internalType":"int64","name":"skillMod","type":"int64"},{"internalType":"int64","name":"statMod","type":"int64"},{"internalType":"int64","name":"luckMod","type":"int64"}],"internalType":"struct ProfessionQuest.RewardItem","name":"_item","type":"tuple"}],"name":"setRewardItem","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_rate","type":"uint256"}],"name":"setTearRate","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_timePerStamina","type":"uint256"}],"name":"setTimePerStamina","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"},{"internalType":"uint8","name":"_attempts","type":"uint8"}],"name":"startQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"tearRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"timePerStamina","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"vrf","outputs":[{"internalType":"bytes32","name":"result","type":"bytes32"}],"stateMutability":"view","type":"function"}
        ]
        """


def block_explorer_link(txid):
    return 'https://explorer.harmony.one/tx/' + str(txid)


def start_quest(hero_id, attempts, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    logger.info("Starting quest with hero id " + str(hero_id))
    tx = contract.functions.startQuest(hero_id, attempts).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info(
        "Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")

    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")
    logger.info(str(tx_receipt))


def complete_quest(hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    logger.debug("Completing quest with hero id " + str(hero_id))
    tx = contract.functions.completeQuest(hero_id).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info(
        "Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")
    logger.info(str(tx_receipt))

    return tx_receipt


def parse_complete_quest_receipt(tx_receipt, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    quest_result = {}

    quest_reward = contract.events.QuestReward().processReceipt(tx_receipt)
    quest_result['tear'] = sum([result.args.itemQuantity for result in quest_reward])

    quest_xp = contract.events.QuestXP().processReceipt(tx_receipt)
    quest_result['xp'] = sum([result.args.xpEarned for result in quest_xp])

    return quest_result


def quest_level(rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.questLevel().call()

    return result


def rewards(quest_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.rewardItems(quest_id).call()

    return result


def last_reward_index(rpc_address):

    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.lastRewardIndex().call()

    return result


def hero_to_quest(hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.heroToQuest(hero_id).call()

    return result


def get_current_stamina(hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.getCurrentStamina(hero_id).call()

    return result
