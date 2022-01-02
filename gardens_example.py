import logging
import sys
import gardens.master_gardener as master_gardener
from gardens.pool import Garden
import gardens.utils.utils as utils
import erc20.erc20 as tokens
from web3 import Web3


if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-gardens")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    w3 = Web3(Web3.HTTPProvider(rpc_server))

    user_address = '0x2E7669F61eA77F02445A015FBdcFe2DE47083E02'

    for pool_id in range(0, master_gardener.pool_length(rpc_server)):
        pool_info = utils.human_readable_pool_info(master_gardener.pool_info(pool_id, rpc_server))
        logger.info(str(pool_info))
        garden = Garden(pool_info['address'], rpc_server, logger)
        logger.info("Id:\t" + str(garden.id()))
        logger.info("Symbol:\t" + garden.symbol())
        logger.info("Pair:\t" + tokens.symbol(garden.token_0(), rpc_server) + "-" + tokens.symbol(garden.token_1(), rpc_server))
        logger.info("Total Supply:\t" + str(w3.fromWei(garden.total_supply(), 'ether')))
        user = utils.human_readable_user_info(garden.user_info(user_address))
        logger.info("LP balance:\t" + str(w3.fromWei(Garden.user_info_lp_balance(user), 'ether')))
        logger.info("Pool share :\t" + str(round(100 * Garden.user_info_lp_balance(user)/garden.total_supply(), 2)) + "%")





