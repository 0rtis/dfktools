import logging
import sys
import time
from web3 import Web3
import dex.erc20 as erc20
import stone_carver.stone_carver as stone_carver

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-stone-carver")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    lesser_chaos_stone = erc20.symbol2item('DFKLCHSST', 'serendale')
    lesser_chaos_stone_address = erc20.symbol2address('DFKLCHSST', 'serendale')

    # Request recipe for one Stone
    stone = stone_carver.get_recipe(lesser_chaos_stone_address, stone_carver.SERENDALE_CONTRACT_ADDRESS, rpc_server)
    logger.info(f"{lesser_chaos_stone[2]}: {stone}")

    # Request Stone Carver availability
    availability = stone_carver.get_availability(stone_carver.SERENDALE_CONTRACT_ADDRESS, rpc_server)
    logger.info(f"Working until: {availability[0]} / Reopens at: {availability[1]}")

    # Displays Working until Timestamp / whether SC is currently working
    working = stone_carver.working_until(stone_carver.SERENDALE_CONTRACT_ADDRESS, rpc_server)
    logger.info(f"Working until: {working} / Currently Working: {True if time.time() < working else False}")

    # Crafting Lesser Chaos Stone
    w3 = Web3(Web3.HTTPProvider(rpc_server))
    private_key = None  # set private key
    account_address = w3.eth.account.privateKeyToAccount(private_key).address
    gas_price_gwei = 100
    tx_timeout_seconds = 30
    stone_carver.carve_stone(stone_carver.SERENDALE_CONTRACT_ADDRESS, lesser_chaos_stone_address, 1, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, tx_timeout_seconds, rpc_server, logger)
