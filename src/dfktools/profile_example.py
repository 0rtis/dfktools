import logging
import json
import sys
import profile.profile_v2 as profiles

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-profile")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://klaytn.rpc.defikingdoms.com/'
    logger.info("Using RPC server " + rpc_server)
    realm_contract_address = profiles.SERENDALE2_CONTRACT_ADDRESS

    profile = profiles.get_profile(realm_contract_address, '0x2E7669F61eA77F02445A015FBdcFe2DE47083E02', rpc_server)

    logger.info(json.dumps(profile, indent=4, sort_keys=False))

