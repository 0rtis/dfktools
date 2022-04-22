import logging
import json
import sys
import dfk_lib.hero.utils.utils as hero_utils
import dfk_lib.hero.hero as heroes
from pathlib import Path

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-hero")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    hero_dir = Path(__file__).parent.parent / 'hero'
    females_path = hero_dir / 'femaleFirstName.json'
    males_path = hero_dir / 'maleFirstName.json'
    last_names_path = hero_dir / 'lastName.json'

    female_first_names = hero_utils.parse_names(females_path.read_text())
    logger.info("Female hero first name loaded")
    male_first_names = hero_utils.parse_names(males_path.read_text())
    logger.info("Male hero first name loaded")
    last_names = hero_utils.parse_names(last_names_path.read_text())
    logger.info("Hero last name loaded")

    # transfer(1, 'private key of the owner', 'next nonce of owner account', 'receiver address', 200, rpc_server, hero_abi_json, logger)

    for i in range(1, 100):
        logger.info("Processing hero #"+str(i))
        owner = heroes.get_owner(i, rpc_server)
        hero = heroes.get_hero(i, rpc_server)
        readable_hero = heroes.human_readable_hero(hero, male_first_names, female_first_names, last_names)
        logger.info(json.dumps(readable_hero, indent=4, sort_keys=False) + "\n Owned by " + owner)
