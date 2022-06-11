import logging
import sys
import land.utils.utils as land_utils
import land.land as land

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-hero")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    user = '0x2E7669F61eA77F02445A015FBdcFe2DE47083E02'

    logger.info("Total land count " + str(land.total_supply(rpc_server)))

    land1 = land_utils.human_readable_land(land.get_land(1, rpc_server))
    logger.info("Land id 1:" + str(land1))
    logger.info("Owner of land id 1: " + land.owner_of(1, rpc_server))

    logger.info("Land own by " + user + ": " + str(land.get_account_lands(user, rpc_server)))

    region_log = "Land in region 0:"
    for l in land.get_lands_by_region(0, rpc_server):
        l = land_utils.human_readable_land(l)
        region_log = region_log + "\n\t" + str(l)

    logger.info(region_log)
