import logging
import sys
import quest.wishing_well as wishing_well


if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-wishing well quest")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    level = wishing_well.quest_level(rpc_server)
    logger.info("Quest level "+str(level))

    hero_id = 1
    stamina = wishing_well.get_current_stamina(hero_id, rpc_server)
    logger.info("Current stamina on hero " + str(hero_id) + ": " + str(stamina))

    # wishing_well.start_quest(hero_id, 5, private_key, nonce, gas_price_gwei, rpc_server, logger)
    # quest_id = hero_to_quest(hero_id, rpc_server)
    # nonce = nonce + 1
    # time.sleep(30)
    # complete_quest(hero_id, prv, nonce, gas_price_gwei, rpc_server, logger)



