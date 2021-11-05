import logging
import sys
import summoning.summoning as summoning


if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-summoning")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    crystals = summoning.get_user_crystal_ids('0x2E7669F61eA77F02445A015FBdcFe2DE47083E02', rpc_server)

    logger.info("Crystal ids: " + str(crystals))

