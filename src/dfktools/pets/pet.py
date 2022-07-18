from web3 import Web3

SERENDALE_CONTRACT_ADDRESS = '0xAC9AFb5900C8A27B766bCad3A37423DC0F4C22d3'

ABI = '''
    [
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"petId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"}],"indexed":false,"internalType":"struct Pet","name":"pet","type":"tuple"}],"name":"PetHatched","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"petId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"}],"indexed":false,"internalType":"struct Pet","name":"pet","type":"tuple"}],"name":"PetUpdated","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
        {"inputs":[],"name":"BRIDGE_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"MINTER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"PET_MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"address","name":"_to","type":"address"}],"name":"bridgeMint","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getPet","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"}],"internalType":"struct Pet","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"getUserPets","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"}],"internalType":"struct Pet[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"components":[{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"}],"internalType":"struct PetOptions","name":"_petOptions","type":"tuple"},{"internalType":"address","name":"owner","type":"address"}],"name":"hatchPet","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"nextPetId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"}],"internalType":"struct Pet","name":"_pet","type":"tuple"}],"name":"updatePet","outputs":[],"stateMutability":"nonpayable","type":"function"}
    ]
    '''


def block_explorer_link(txid):
    return 'https://explorer.harmony.one/tx/' + str(txid)


def balance_of(account, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.balanceOf(Web3.toChecksumAddress(account)).call()


def get_pet(pet_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getPet(pet_id).call()


def get_user_pets(account, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getUserPets(account).call()


def owner_of(pet_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.ownerOf(pet_id).call()


def next_pet_id(rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.nextPetId().call()


def safe_transfer_from(_from, to, egg_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):

    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address
    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.safeTransferFrom(_from, to, egg_id)

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


def transfer_from(_from, to, egg_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):

    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address
    contract_address = Web3.toChecksumAddress(SERENDALE_CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.transferFrom(_from, to, egg_id)

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