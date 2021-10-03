import copy
from web3 import Web3
import json
import logging
import sys

PROFILE_CONTRACT_ADDRESS = '0xabD4741948374b1f5DD5Dd7599AC1f85A34cAcDD'


def get_profile(address, rpc_address, profile_contract_abi):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    profile_contract_address = Web3.toChecksumAddress(PROFILE_CONTRACT_ADDRESS)
    profile_contract = w3.eth.contract(profile_contract_address, abi=profile_contract_abi)
    profile_contract_entry = profile_contract.functions.getProfileByAddress(Web3.toChecksumAddress(address)).call()

    profile = {}
    profile['id'] = profile_contract_entry[0]
    profile['address'] = str(profile_contract_entry[1])
    profile['name'] = profile_contract_entry[2]
    profile['creation_time'] = profile_contract_entry[3]
    profile['pic_id'] = profile_contract_entry[4]
    profile['hero_id'] = profile_contract_entry[5]

    return profile


if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK profile")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'

    logger.info("Using RPC server " + rpc_server)

    with open('profile.abi', 'r') as f:
        profile_abi_json = f.read()
    logger.info("Profile contract ABI loaded")

    profile = get_profile('0x2E7669F61eA77F02445A015FBdcFe2DE47083E02', rpc_server, profile_abi_json)

    logger.info(json.dumps(profile, indent=4, sort_keys=False))

