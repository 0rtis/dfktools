import logging
import json
import sys
import hero.utils.utils as hero_utils
import hero.hero_core as hero_core
from hero.hero import Hero


if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-hero")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    with open('hero/femaleFirstName.json', 'r') as f:
        female_first_names = hero_utils.parse_names(f.read())
    logger.info("Female hero first name loaded")

    with open('hero/maleFirstName.json', 'r') as f:
        male_first_names = hero_utils.parse_names(f.read())
    logger.info("Male hero first name loaded")

    with open('hero/lastName.json', 'r') as f:
        last_names = hero_utils.parse_names(f.read())
    logger.info("Hero last name loaded")

    serendale_heroes = Hero(hero_core.SERENDALE_CONTRACT_ADDRESS, 'https://api.harmony.one', logger)


    #serendale_heroes.transfer(1, 'private key of the owner', 'next nonce of owner account', 'receiver address', 45, 30)

    for i in range(1, 10):
        logger.info("Processing serendale hero #"+str(i))
        owner = serendale_heroes.get_owner(i)
        hero = serendale_heroes.get_hero(i)
        readable_hero = serendale_heroes.human_readable_hero(hero, male_first_names, female_first_names, last_names)
        logger.info(json.dumps(readable_hero, indent=4, sort_keys=False) + "\n Owned by " + owner)

    crystalvale_heroes = Hero(hero_core.CRYSTALVALE_CONTRACT_ADDRESS,
                              'https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc', logger)

    for i in range(1, 10):
        logger.info("Processing crystalvale hero #" + str(i))
        cv_hero_id = hero_utils.sd2cv_cv_hero_id(i)
        owner = crystalvale_heroes.get_owner(cv_hero_id)
        hero = crystalvale_heroes.get_hero(cv_hero_id)
        readable_hero = crystalvale_heroes.human_readable_hero(hero, male_first_names, female_first_names, last_names)
        logger.info(json.dumps(readable_hero, indent=4, sort_keys=False) + "\n Owned by " + owner)
