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

    rpc_server = 'https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc'
    logger.info("Using RPC server " + rpc_server)

    realm_contract_address = stone_carver.CRYSTALVALE_CONTRACT_ADDRESS
    lesser_chaos_stone = erc20.symbol2item('DFKLCHSST', 'cv')
    lesser_chaos_stone_address = erc20.symbol2address('DFKLCHSST', 'cv')

    # Request recipe for one Stone
    stone = stone_carver.get_recipe(realm_contract_address, lesser_chaos_stone_address, rpc_server)
    logger.info(f"{lesser_chaos_stone[2]}: {stone}")

    # Request Stone Carver availability
    availability = stone_carver.get_availability(realm_contract_address, rpc_server)
    logger.info(f"Working until: {availability[0]} / Reopens at: {availability[1]}")

    # Displays Working until Timestamp / whether SC is currently working
    working = stone_carver.working_until(realm_contract_address, rpc_server)
    logger.info(f"Working until: {working} / Currently Working: {True if time.time() < working else False}")

    # Crafting Lesser Chaos Stone
    w3 = Web3(Web3.HTTPProvider(rpc_server))
    private_key = None  # set private key
    account_address = w3.eth.account.from_key(private_key).address
    gas_price_gwei = 100
    tx_timeout_seconds = 30
    stone_carver.carve_stone(realm_contract_address, lesser_chaos_stone_address, 1, private_key, w3.eth.get_transaction_count(account_address), gas_price_gwei, tx_timeout_seconds, rpc_server, logger)
