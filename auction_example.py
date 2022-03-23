import logging
import sys
import auctions.hero.sale_auctions as hero_sales
import auctions.hero.rent_auctions as hero_rental
from auctions.auction import Auction
import auctions.land as land_auction
import auctions.utils.utils as auction_utils

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-auctions")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    graphql = 'http://graph3.defikingdoms.com/subgraphs/name/defikingdoms/apiv5'

    auctions = hero_sales.get_open_auctions(graphql, 0, 10)
    logger.info("Hero sale auctions:")
    for auction in auctions:
        logger.info(str(auction))

    # sales.bid_hero(hero_id, ether2wei(100), prv_key, nonce, gas_price_gwei, 30, rpc_server, logger)

    logger.info("\n")
    logger.info("Hero rental auctions:")
    auctions = hero_rental.get_open_auctions(graphql, 0, 10)
    for auction in auctions:
        logger.info(str(auction))


    # land
    user = '0x2E7669F61eA77F02445A015FBdcFe2DE47083E02'

    land_auction = Auction(land_auction.AUCTION_CONTRACT_ADDRESS, rpc_server, logger)
    logger.info("Total land auctions: " + str(land_auction.total_auctions()))
    logger.info("Auctions of " + user + ": " + str(land_auction.get_user_auctions(user)))

    for i in range(0, min(10, land_auction.total_auctions())):
        auction = auction_utils.human_readable_auction(land_auction.auctions(i))
        logger.info("Auction index " + str(i) + ": " + str(auction))

    auction = land_auction.get_auction(48)
    auction = auction_utils.human_readable_auction(auction)
    logger.info(str(auction))
    logger.info(str(land_auction.is_on_auction(33)))



