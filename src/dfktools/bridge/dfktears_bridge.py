from web3 import Web3

SERENDALE_CONTRACT_ADDRESS = '0x27B7C0C87B9ecA92E5101852709e63685bF9d299'
CRYSTALVALE_CONTRACT_ADDRESS = '0x6a00Dc976a7291a1E9F5380FE6F96fE006dCdD3c'

ABI = '''
    [
        {"inputs":[{"internalType":"address","name":"_messageBus","type":"address"},{"internalType":"address","name":"_gaiaTear","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"dstUser","type":"address"},{"indexed":false,"internalType":"uint256","name":"arrivalChainId","type":"uint256"}],"name":"GaiaArrived","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"dstUser","type":"address"},{"indexed":false,"internalType":"uint256","name":"arrivalChainId","type":"uint256"}],"name":"GaiaSent","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_srcChainId","type":"uint256"},{"indexed":false,"internalType":"bytes32","name":"_srcAddress","type":"bytes32"}],"name":"SetTrustedRemote","type":"event"},
        {"inputs":[{"internalType":"bytes32","name":"_srcAddress","type":"bytes32"},{"internalType":"uint256","name":"_srcChainId","type":"uint256"},{"internalType":"bytes","name":"_message","type":"bytes"},{"internalType":"address","name":"_executor","type":"address"}],"name":"executeMessage","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"gaiaTears","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_chainId","type":"uint256"}],"name":"getTrustedRemote","outputs":[{"internalType":"bytes32","name":"trustedRemote","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"messageBus","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"msgGasLimit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_tearsAmount","type":"uint256"},{"internalType":"uint256","name":"_dstChainId","type":"uint256"}],"name":"sendTear","outputs":[],"stateMutability":"payable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_messageBus","type":"address"}],"name":"setMessageBus","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_msgGasLimit","type":"uint256"}],"name":"setMsgGasLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_srcChainId","type":"uint256"},{"internalType":"bytes32","name":"_srcAddress","type":"bytes32"}],"name":"setTrustedRemote","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}
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


def gaia_tears(realm_contract, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract = Web3.toChecksumAddress(realm_contract)
    contract = w3.eth.contract(contract, abi=ABI)
    result = contract.functions.gaiaTears().call()

    return result


def send_tear(origin_realm_contract, amount, destination_chain_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    origin_realm_contract = Web3.toChecksumAddress(origin_realm_contract)
    origin_realm_contract = w3.eth.contract(origin_realm_contract, abi=ABI)

    tx = origin_realm_contract.functions.sendTear(amount, destination_chain_id)

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
    logger.info(
        "Waiting for transaction " + block_explorer_link(origin_realm_contract, signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt