import logging
import sys
from web3 import Web3
import pets.pet_core as pet_core
import pets.hatchery as hatchery
import pets.exchange as exchange
import pets.utils.utils as pet_utils

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-pet")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc'
    logger.info("Using RPC server " + rpc_server)

    user = '0x2E7669F61eA77F02445A015FBdcFe2DE47083E02'

    # pet NFT
    logger.info("Total existing pet: {}".format(str(pet_core.next_pet_id(pet_core.CRYSTALVALE_CONTRACT_ADDRESS, rpc_server))))
    user_balance = pet_core.balance_of(pet_core.CRYSTALVALE_CONTRACT_ADDRESS, user, rpc_server)
    logger.info("Player {} is owner of {} pets".format(user, user_balance))

    user_pets = pet_core.get_user_pets(pet_core.CRYSTALVALE_CONTRACT_ADDRESS, user, rpc_server)
    for pet in user_pets:
        logger.info(str(pet_utils.human_readable_pet(pet)))

    # exchange
    logger.info("Total pet exchange: {}".format(exchange.total_exchanges(exchange.CRYSTALVALE_CONTRACT_ADDRESS, rpc_server)))
    logger.info("Player {} has {} pet exchange pending".format(user, len(
        exchange.get_user_pet_exchanges(exchange.CRYSTALVALE_CONTRACT_ADDRESS, user, rpc_server))))

    # hatching
    incubating_eggs = hatchery.get_user_eggs(hatchery.CRYSTALVALE_CONTRACT_ADDRESS, user, rpc_server)
    logger.info("Player {} is incubating {} eggs".format(user, len(incubating_eggs)))

    blue_egg_cost = hatchery.egg_type_costs(hatchery.CRYSTALVALE_CONTRACT_ADDRESS, 0, rpc_server)
    grey_egg_cost = hatchery.egg_type_costs(hatchery.CRYSTALVALE_CONTRACT_ADDRESS, 1, rpc_server)
    logger.info("Incubating cost of blue egg: {}".format(str(blue_egg_cost)))
    logger.info("Incubating cost of grey egg: {}".format(str(grey_egg_cost)))

    private_key = None  # set private key
    gas_price_gwei = 115
    tx_timeout = 30
    w3 = Web3(Web3.HTTPProvider(rpc_server))
    account_address = w3.eth.account.privateKeyToAccount(private_key).address

    hatchery.incubate_egg(hatchery.CRYSTALVALE_CONTRACT_ADDRESS,0, 2, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, tx_timeout, rpc_server, logger)
    hatchery.crack(hatchery.CRYSTALVALE_CONTRACT_ADDRESS, 404, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, tx_timeout,
                  rpc_server, logger)