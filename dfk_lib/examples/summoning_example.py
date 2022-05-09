import logging
import sys
import dfk_lib.summoning.summoning as summoning


if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-summoning")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    # summoning.summon_crystal(summoning.SERENDALE_CONTRACT_ADDRESS, hero_id_1, hero_id_2, hero1_tears, hero2_tears, private_key, nonce, gas_price_gwei, 30, rpc_address, logger)

    crystals = summoning.get_user_crystal_ids(summoning.SERENDALE_CONTRACT_ADDRESS, '0x2E7669F61eA77F02445A015FBdcFe2DE47083E02', rpc_server)
    logger.info("Crystal ids: " + str(crystals))

    # summoning.open_crystal(summoning.SERENDALE_CONTRACT_ADDRESS, crystals[0], private_key, nonce, gas_price_gwei, 30, rpc_address, logger)


