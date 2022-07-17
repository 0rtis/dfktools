import logging
import sys
import quests.wishing_well as wishing_well

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-wishing well quest")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    level = wishing_well.quest_level(rpc_server)
    logger.info("Quest level "+str(level))

    hero_id = 1  # <your hero id here>
    stamina = wishing_well.get_current_stamina(hero_id, rpc_server)
    logger.info("Current stamina on hero " + str(hero_id) + ": " + str(stamina))

    #w3 = Web3(Web3.HTTPProvider(rpc_server))
    #gas_price_gwei = 10
    #private_key = # set private key
    #account_address = w3.eth.account.privateKeyToAccount(private_key).address
    #wishing_well.start_quest(hero_id, 5, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, 30, rpc_server, logger)
    #time.sleep(60)
    #tx_receipt = wishing_well.complete_quest(hero_id, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, 30, rpc_server, logger)

    #quest_result = wishing_well.parse_complete_quest_receipt(tx_receipt, rpc_server)
    #logger.info("Quest earned " + str(quest_result['tear']) + " tears and " + str(quest_result['xp']) + " xp")



