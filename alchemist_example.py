import logging
import sys
from web3 import Web3
import dex.erc20 as erc20
import alchemist.alchemist as alchemist


if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-alchemist")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    stamina_vial_address = erc20.symbol2address('DFKSTMNPTN')

    # request recipe for one potion
    potion = alchemist.get_potion(stamina_vial_address, rpc_server)
    potion_id = alchemist.address_to_potion_id('0x24Bb3844552AcdeE1f11f2E267CBd43929D6a17D', rpc_server)
    logger.info("Potion id " + str(potion_id) + ": " +str(potion))

    # request recipe for all potions
    potions = alchemist.get_potions(rpc_server)
    all_potions_log = "All potions:\n"
    for potion in potions:
        all_potions_log += "\t" + str(potion) + "\n"
    logger.info(all_potions_log)

    # potion id to address and batch size
    potion_addr_batch = alchemist.potion_id_to_address_amount(1, rpc_server)
    logger.info("Potion id to address & batch size: " + str(potion_addr_batch))

    # crafting Stamina Vial
    w3 = Web3(Web3.HTTPProvider(rpc_server))
    private_key = None  # set private key
    account_address = w3.eth.account.privateKeyToAccount(private_key).address
    gas_price_gwei = 40
    tx_timeout_seconds = 30
    alchemist.create_potion(stamina_vial_address, 1, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, tx_timeout_seconds, rpc_server, logger)