import web3.contract
from web3 import Web3

SERENDALE_CONTRACT_ADDRESS = '0x573e407Be90a50EAbA28748cbb62Ff9d6038A3e9'
SERENDALE_CHAIN_ID = 1666600000
CRYSTALVALE_CONTRACT_ADDRESS = '0x739B1666c2956f601f095298132773074c3E184b'
CRYSTALVALE_CHAIN_ID = 53935
SERENDALE2_CONTRACT_ADDRESS = '0xEE258eF5F4338B37E9BA9dE6a56382AdB32056E2'
SERENDALE2_CHAIN_ID = 8217

ABI = '''
    [
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"stateMutability":"payable","type":"fallback"},
        {"inputs":[],"name":"admin","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"newAdmin","type":"address"}],"name":"changeAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"implementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"newImplementation","type":"address"}],"name":"upgradeTo","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"newImplementation","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"arrivalChainId","type":"uint256"}],"name":"HeroArrived","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"arrivalChainId","type":"uint256"}],"name":"HeroSent","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_srcChainId","type":"uint256"},{"indexed":false,"internalType":"bytes32","name":"_srcAddress","type":"bytes32"}],"name":"SetTrustedRemote","type":"event"},
        {"inputs":[],"name":"assistingAuction","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"_srcAddress","type":"bytes32"},{"internalType":"uint256","name":"_srcChainId","type":"uint256"},{"internalType":"bytes","name":"_message","type":"bytes"},{"internalType":"address","name":"_executor","type":"address"}],"name":"executeMessage","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_chainId","type":"uint256"}],"name":"getTrustedRemote","outputs":[{"internalType":"bytes32","name":"trustedRemote","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"heroes","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_messageBus","type":"address"},{"internalType":"address","name":"_heroes","type":"address"},{"internalType":"address","name":"_assistingAuction","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"messageBus","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"msgGasLimit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"},{"internalType":"uint256","name":"_dstChainId","type":"uint256"}],"name":"sendHero","outputs":[],"stateMutability":"payable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_assistingAuction","type":"address"}],"name":"setAssistingAuctionAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_messageBus","type":"address"}],"name":"setMessageBus","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_msgGasLimit","type":"uint256"}],"name":"setMsgGasLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_srcChainId","type":"uint256"},{"internalType":"bytes32","name":"_srcAddress","type":"bytes32"}],"name":"setTrustedRemote","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"initialLogic","type":"address"},{"internalType":"address","name":"initialAdmin","type":"address"},{"internalType":"bytes","name":"_data","type":"bytes"}],"stateMutability":"payable","type":"constructor"}
    ]
    '''


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


def assisting_auction(realm_contract, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract = Web3.toChecksumAddress(realm_contract)
    contract = w3.eth.contract(contract, abi=ABI)
    result = contract.functions.assistingAuction().call()

    return result


def heroes(realm_contract, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract = Web3.toChecksumAddress(realm_contract)
    contract = w3.eth.contract(contract, abi=ABI)
    result = contract.functions.heroes().call()

    return result


def send_hero(origin_realm_contract_address, hero_id, destination_chain_id, bridge_fee_in_wei, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):

    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    origin_realm_contract_address = Web3.toChecksumAddress(origin_realm_contract_address)
    contract = w3.eth.contract(origin_realm_contract_address, abi=ABI)

    tx = contract.functions.sendHero(hero_id, destination_chain_id)

    if isinstance(gas_price_gwei, dict):   # dynamic fee
        tx = tx.buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'),
             'value': bridge_fee_in_wei, 'nonce': nonce})
    else:   # legacy
        tx = tx.buildTransaction({'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'value': bridge_fee_in_wei, 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info(
        "Waiting for transaction " + block_explorer_link(origin_realm_contract_address, signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt