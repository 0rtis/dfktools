from web3 import Web3

SERENDALE_CONTRACT_ADDRESS = '0xeaF833A0Ae97897f6F69a728C9c17916296cecCA'

ABI = '''
    [
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"eggId1","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"eggId2","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"eggTypeRecieved","type":"uint8"}],"name":"PetExchangeCompleted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"eggId1","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"eggId2","type":"uint256"}],"name":"PetExchangeStarted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
        {"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
         {"inputs":[{"internalType":"uint256","name":"_exchangeId","type":"uint256"}],"name":"completeExchange","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"eggs","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_exchangeId","type":"uint256"}],"name":"getPetExchange","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"petId1","type":"uint256"},{"internalType":"uint256","name":"petId2","type":"uint256"},{"internalType":"uint256","name":"seedblock","type":"uint256"},{"internalType":"uint256","name":"finishTime","type":"uint256"},{"internalType":"enum PetExchangeStatus","name":"status","type":"uint8"}],"internalType":"struct PetExchangeData","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"getUserPetExchanges","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"petId1","type":"uint256"},{"internalType":"uint256","name":"petId2","type":"uint256"},{"internalType":"uint256","name":"seedblock","type":"uint256"},{"internalType":"uint256","name":"finishTime","type":"uint256"},{"internalType":"enum PetExchangeStatus","name":"status","type":"uint8"}],"internalType":"struct PetExchangeData[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"idToPetExchange","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"petId1","type":"uint256"},{"internalType":"uint256","name":"petId2","type":"uint256"},{"internalType":"uint256","name":"seedblock","type":"uint256"},{"internalType":"uint256","name":"finishTime","type":"uint256"},{"internalType":"enum PetExchangeStatus","name":"status","type":"uint8"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_petCoreAddress","type":"address"},{"internalType":"address","name":"_pastureAddress","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"profileExchangedPets","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"petId1","type":"uint256"},{"internalType":"uint256","name":"petId2","type":"uint256"},{"internalType":"uint256","name":"seedblock","type":"uint256"},{"internalType":"uint256","name":"finishTime","type":"uint256"},{"internalType":"enum PetExchangeStatus","name":"status","type":"uint8"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint8","name":"_index","type":"uint8"},{"internalType":"address","name":"_eggAddress","type":"address"}],"name":"setEgg","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_pastureAddress","type":"address"}],"name":"setPasture","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_petCoreAddress","type":"address"}],"name":"setPetCore","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_petId1","type":"uint256"},{"internalType":"uint256","name":"_petId2","type":"uint256"}],"name":"startExchange","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"totalExchanges","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"}
    ]
    '''


def block_explorer_link(txid):
    return 'https://explorer.harmony.one/tx/' + str(txid)


def get_pet_exchange(exchange_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getPetExchange(exchange_id).call()


def get_user_pet_exchanges(account, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getUserPetExchanges(account).call()


def total_exchanges(rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.totalExchanges().call()


def start_exchange(pet_id_1, pet_id_2, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):

    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address
    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.startExchange(pet_id_1, pet_id_2)

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


def complete_exchange(exchange_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):

    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address
    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.completeExchange(exchange_id)

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