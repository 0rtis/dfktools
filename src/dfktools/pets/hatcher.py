from web3 import Web3

SERENDALE_CONTRACT_ADDRESS = '0x576C260513204392F0eC0bc865450872025CB1cA'

ABI = '''
    [
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"eggId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"petId","type":"uint256"}],"name":"EggCracked","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"eggId","type":"uint256"},{"indexed":true,"internalType":"uint8","name":"eggType","type":"uint8"},{"indexed":true,"internalType":"uint8","name":"tier","type":"uint8"}],"name":"EggIncubated","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
        {"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"HATCHING_MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_eggId","type":"uint256"}],"name":"crack","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"eggTypeCosts","outputs":[{"internalType":"address","name":"eggAddress","type":"address"},{"internalType":"address","name":"itemAddress1","type":"address"},{"internalType":"uint16","name":"itemAmount1","type":"uint16"},{"internalType":"address","name":"itemAddress2","type":"address"},{"internalType":"uint16","name":"itemAmount2","type":"uint16"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_eggId","type":"uint256"}],"name":"getEgg","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"petId","type":"uint256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint256","name":"seedblock","type":"uint256"},{"internalType":"uint256","name":"finishTime","type":"uint256"},{"internalType":"uint8","name":"tier","type":"uint8"}],"internalType":"struct UnhatchedEgg","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"getUserEggs","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint8","name":"_eggType","type":"uint8"},{"internalType":"uint8","name":"_tier","type":"uint8"}],"name":"incubateEgg","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_petCoreAddress","type":"address"},{"internalType":"address","name":"_jewelTokenAddress","type":"address"},{"internalType":"address","name":"_goldAddress","type":"address"},{"internalType":"address","name":"_gaiaTearsAddress","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"jewelToken","outputs":[{"internalType":"contract IJewelToken","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"originId","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"priceTiers","outputs":[{"internalType":"uint8","name":"jewelCost","type":"uint8"},{"internalType":"uint16","name":"goldCost","type":"uint16"},{"internalType":"uint8","name":"tearCost","type":"uint8"},{"internalType":"uint32","name":"incubationTime","type":"uint32"},{"internalType":"uint16","name":"shinyChance","type":"uint16"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"season","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint8","name":"_eggType","type":"uint8"},{"internalType":"uint8","name":"_rarity","type":"uint8"},{"internalType":"uint8","name":"_isSpecial","type":"uint8"},{"internalType":"uint256","name":"_startIndex","type":"uint256"},{"internalType":"uint256","name":"_endIndex","type":"uint256"}],"name":"setAppearanceChoices","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint8","name":"_eggType","type":"uint8"},{"components":[{"internalType":"address","name":"eggAddress","type":"address"},{"internalType":"address","name":"itemAddress1","type":"address"},{"internalType":"uint16","name":"itemAmount1","type":"uint16"},{"internalType":"address","name":"itemAddress2","type":"address"},{"internalType":"uint16","name":"itemAmount2","type":"uint16"}],"internalType":"struct EggTypeCost","name":"_eggTypeCost","type":"tuple"}],"name":"setEggTypeCosts","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address[]","name":"_feeAddresses","type":"address[]"},{"internalType":"uint256[]","name":"_feePercents","type":"uint256[]"}],"name":"setFees","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_petCoreAddress","type":"address"}],"name":"setPetCore","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint8","name":"_priceTierIndex","type":"uint8"},{"components":[{"internalType":"uint8","name":"jewelCost","type":"uint8"},{"internalType":"uint16","name":"goldCost","type":"uint16"},{"internalType":"uint8","name":"tearCost","type":"uint8"},{"internalType":"uint32","name":"incubationTime","type":"uint32"},{"internalType":"uint16","name":"shinyChance","type":"uint16"}],"internalType":"struct PriceTier","name":"_priceTier","type":"tuple"}],"name":"setPriceTiers","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"totalEggs","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"}
    ]
    '''


def block_explorer_link(txid):
    return 'https://explorer.harmony.one/tx/' + str(txid)


def get_user_eggs(account, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getUserEggs(Web3.toChecksumAddress(account)).call()


def egg_type_costs(egg_type, rpc_address):
    '''
    :param egg_type: color of the egg as int (0: )
    :param rpc_address:
    :return:
    '''
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.eggTypeCosts(egg_type).call()


def get_egg(egg_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getEgg(egg_id).call()


def season(rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.season().call()


def total_eggs(rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.totalEggs().call()


def incubate_egg(egg_type, tier, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    '''
    :param egg_type: color of the egg
    :param tier: 0, 1 or 2
    :param private_key:
    :param nonce:
    :param gas_price_gwei:
    :param tx_timeout_seconds:
    :param rpc_address:
    :param logger:
    :return:
    '''
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address
    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.incubateEgg(egg_type, tier)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.buildTransaction({'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")

    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def crack(egg_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address
    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.crack(egg_id)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.buildTransaction({'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")

    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt
