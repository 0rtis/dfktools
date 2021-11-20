import logging
import sys
import auctions.sale.sale_auctions as sales
import auctions.rent.rent_auctions as rental


if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-auctions")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    graphql = 'http://graph3.defikingdoms.com/subgraphs/name/defikingdoms/apiv5'

    auctions = sales.get_recent_open_auctions(graphql, 10)
    logger.info("Recent sale auctions:")
    for auction in auctions:
        logger.info(str(auction))

    # sale.bid_hero(hero_id, ether2wei(100), prv_key, nonce, gas_price_gwei, rpc_server, logger)

    logger.info("\n")
    logger.info("Recent rental auctions:")
    auctions = rental.get_recent_open_auctions(graphql, 10)
    for auction in auctions:
        logger.info(str(auction))
