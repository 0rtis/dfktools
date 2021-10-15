from web3 import Web3
import logging
import sys

SUMMONING_CONTRACT_ADDRESS = '0xa2D001C829328aa06a2DB2740c05ceE1bFA3c6bb'


def get_user_crystal_ids(user_address, rpc_address, summoning_contract_abi):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    summoning_contract_address = Web3.toChecksumAddress(SUMMONING_CONTRACT_ADDRESS)
    summoning_contract = w3.eth.contract(summoning_contract_address, abi=summoning_contract_abi)

    return summoning_contract.functions.getUserCrystals(Web3.toChecksumAddress(user_address)).call()


def open_crystal(crystal_id, rpc_address, summoning_contract_abi):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    summoning_contract_address = Web3.toChecksumAddress(SUMMONING_CONTRACT_ADDRESS)
    summoning_contract = w3.eth.contract(summoning_contract_address, abi=summoning_contract_abi)

    return summoning_contract.functions.open(crystal_id).call()


if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-summoning")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'

    logger.info("Using RPC server " + rpc_server)

    with open('summoning.abi', 'r') as f:
        summoning_abi_json = f.read()

    crystals = get_user_crystal_ids('user address', rpc_server, summoning_abi_json)









