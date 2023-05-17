import logging
import json
import sys
import profile.profile_v2 as profiles

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-profile")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc' # Profiles are not synced across chains. A profile only exists in the contract & chain it was first created
    logger.info("Using RPC server " + rpc_server)
    realm_contract_address = profiles.CRYSTALVALE_CONTRACT_ADDRESS

    profile = profiles.get_profile(realm_contract_address, '0xEd446a4385fc2a680Db2cf590A5f6C4CC2f98FbF', rpc_server)

    logger.info(json.dumps(profile, indent=4, sort_keys=False))

