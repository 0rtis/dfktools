import logging
import sys
import dfk_lib.auctions.hero.sale_auctions as hero_sales
import dfk_lib.auctions.hero.rent_auctions as hero_rental
import dfk_lib.hero.utils.utils as hero_utils
from dfk_lib.auctions.auction import Auction
import dfk_lib.auctions.land as land_auction
import dfk_lib.auctions.utils.utils as auction_utils

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


    logger.info("\n")
    logger.info("Hero rental auctions:")
    auctions = hero_rental.get_open_auctions(graphql, 0, 10)
    for auction in auctions:
        logger.info(str(auction))

    # serendale hero auction
    logger.info(hero_sales.get_auction(hero_sales.SERENDALE_CONTRACT_ADDRESS, 181373, 'https://api.harmony.one'))
    # hero_sales.bid_hero(hero_sales.SERENDALE_CONTRACT_ADDRESS, 181373, hero_sales.ether2wei(100), 'prv key', 'nonce', 50, 30)


    # crystalvale hero auction
    cv_hero_auctions = Auction(hero_sales.CRYSTLAVALE_CONTRACT_ADDRESS, 'https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc', logger)
    logger.info(auction_utils.human_readable_auction(cv_hero_auctions.get_auction(hero_utils.sd2cv_cv_hero_id(250))))
    # cv_hero_auctions.bid_hero(hero_utils.sd2cv_cv_hero_id(250), hero_sales.ether2wei(100), 'prv key', 'nonce', 50, 30)


    # land
    user = '0x2E7669F61eA77F02445A015FBdcFe2DE47083E02'

    land_auction = Auction(land_auction.AUCTION_CONTRACT_ADDRESS, rpc_server, logger)
    logger.info("Total land auctions: " + str(land_auction.total_auctions()))
    logger.info("Auctions of " + user + ": " + str(land_auction.get_user_auctions(user)))

    for i in range(0, min(10, land_auction.total_auctions())):
        auction = auction_utils.human_readable_auction(land_auction.auctions(i))
        logger.info("Auction index " + str(i) + ": " + str(auction))

    auction = land_auction.get_auction(17)  # must be an open auction
    auction = auction_utils.human_readable_auction(auction)
    logger.info(str(auction))
    logger.info(str(land_auction.is_on_auction(33)))



