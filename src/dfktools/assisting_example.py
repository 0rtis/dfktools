import logging
import sys
import time
import summoning.assisting as assisting
from web3 import Web3

SD = 'serendale'
CV = 'crystalvale'

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-assisting")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc'
    hero_id = 420

    ret = assisting.is_on_rent(assisting.CRYSTALVALE_CONTRACT_ADDRESS, 404, rpc_server)
    logger.info("Hero "+str(hero_id) + (" is up for rent" if ret else " is not available to rent"))