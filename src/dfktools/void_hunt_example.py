import logging
import sys
import void_hunt.hunts_diamond as hunts
import time
from web3 import Web3
from datetime import datetime

if __name__ == "__main__":
    log_format = "%(asctime)s|%(name)s|%(levelname)s: %(message)s"

    logger = logging.getLogger("DFK-hunts")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = "https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc"
    logger.info("Using RPC server " + rpc_server)

    # View Hero Hunt Ready Time (Crystalvale)
    hunt_id = 1  # Boar hunt
    hero_ids = [1000000139507, 700]
    heroes_timers = hunts.getHeroHuntAvailableAtTimestamps(
        hunts.CRYSTALVALE_CONTRACT_ADDRESS, hunt_id, hero_ids, rpc_server
    )

    sorted_heroes_timers = sorted(heroes_timers, key=lambda x: x["ready"])

    logger.info("Heroes boar hunt ready:")

    for hero in sorted_heroes_timers:
        ready = (
            "Now"
            if hero["ready"] < time.time()
            else datetime.fromtimestamp(hero["ready"])
        )
        logger.info(f"{hero['heroId']} -- {ready}")
