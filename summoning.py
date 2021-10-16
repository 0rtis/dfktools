from web3 import Web3
import logging
import sys

SUMMONING_CONTRACT_ADDRESS = '0xa2D001C829328aa06a2DB2740c05ceE1bFA3c6bb'


def get_user_crystal_ids(user_address, rpc_address, summoning_contract_abi):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    summoning_contract_address = Web3.toChecksumAddress(SUMMONING_CONTRACT_ADDRESS)
    summoning_contract = w3.eth.contract(summoning_contract_address, abi=summoning_contract_abi)

    return summoning_contract.functions.getUserCrystals(Web3.toChecksumAddress(user_address)).call()


def open_crystal(crystal_id, owner_private_key, owner_nonce, gas_price_gwei, rpc_address, summoning_contract_abi, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(owner_private_key)

    summoning_contract_address = Web3.toChecksumAddress(SUMMONING_CONTRACT_ADDRESS)
    summoning_contract = w3.eth.contract(summoning_contract_address, abi=summoning_contract_abi)

    fast_open_crystal(crystal_id, account.address, owner_private_key, owner_nonce, gas_price_gwei, summoning_contract, w3, logger)


def fast_open_crystal(crystal_id, owner_address, owner_private_key, owner_nonce, gas_price_gwei, summoning_contract, w3, logger):
    w3.eth.default_account = owner_address
    tx = summoning_contract.functions.open(crystal_id).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': owner_nonce})
    logger.info("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=owner_private_key)
    logger.info("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.info("Transaction successfully sent !")
    logger.info(
        "Waiting for transaction https://explorer.harmony.one/tx/" + str(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=24 * 3600,
                                                     poll_latency=3)
    logger.info("Transaction mined !")
    logger.info(str(tx_receipt))


if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-summoning")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'

    logger.info("Using RPC server " + rpc_server)

    with open('summoning.abi', 'r') as f:
        summoning_abi = f.read()

    crystals = get_user_crystal_ids('0x2E7669F61eA77F02445A015FBdcFe2DE47083E02', rpc_server, summoning_abi)

    logger.info("Crystal ids: " + str(crystals))









