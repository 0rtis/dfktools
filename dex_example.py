import logging
import sys
from web3 import Web3
import dex.uniswap_v2_factory as market_place
import dex.master_gardener as gardens
import dex.pool as pool
import dex.garden
import dex.utils.utils as utils
import erc20.erc20 as erc20

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-DEX")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    w3 = Web3(Web3.HTTPProvider(rpc_server))

    user_address = '0x2E7669F61eA77F02445A015FBdcFe2DE47083E02'

    logger.info("Liquidity pool count:\t" + str(market_place.all_pairs_length(rpc_server)))
    liquidity_pool_id = 0
    liquidity_pool_address = market_place.all_pairs(liquidity_pool_id, rpc_server)
    liquidity_pool = pool.Pool(liquidity_pool_address, rpc_server, logger)
    liquidity_pool_symbol = liquidity_pool.symbol()
    liquidity_pool_token0 = erc20.symbol(liquidity_pool.token_0(), rpc_server)
    liquidity_pool_token1 = erc20.symbol(liquidity_pool.token_1(), rpc_server)
    amount_token1 = 1
    amount_token0 = erc20.wei2eth(w3, liquidity_pool.swap_expected_amount0(erc20.eth2wei(w3, amount_token1)))
    logger.info(liquidity_pool_symbol + " " + liquidity_pool_token0 + "-" + liquidity_pool_token1 + " @ " + str(amount_token0) + " " + liquidity_pool_token0 + " per " + liquidity_pool_token1)

    liquidity_pool_balance = liquidity_pool.balance_of(user_address)
    logger.info("User balance:\t" + str(erc20.wei2eth(w3, liquidity_pool_balance)))

    logger.info("Staking pool count:\t" + str(gardens.pool_length(rpc_server)))
    staking_pool_id = 0
    staking_pool_info = utils.human_readable_pool_info(gardens.pool_info(staking_pool_id, rpc_server))
    staking_pool = dex.garden.Garden(staking_pool_info['address'], rpc_server, logger)
    staking_pool_symbol = staking_pool.symbol()
    staking_pool_token0 = erc20.symbol(staking_pool.token_0(), rpc_server)
    staking_pool_token1 = erc20.symbol(staking_pool.token_1(), rpc_server)
    staking_pool_total_supply = staking_pool.total_supply()
    logger.info(staking_pool_symbol + " " + staking_pool_token0 + "-" + staking_pool_token1 + ", total supply="
                + str(staking_pool_total_supply))
    staking_pool_user = utils.human_readable_user_info(staking_pool.user_info(user_address))
    staking_pool_balance = dex.garden.Garden.user_info_lp_balance(staking_pool_user)
    staking_pool_share = staking_pool_balance/staking_pool_total_supply
    logger.info("User LP balance:\t" + str(erc20.wei2eth(w3, staking_pool_balance)) + " (pool share " + str(round(100 * staking_pool_share, 2)) + "%)")

REASDME acutoipm mehod name + new mehod
readme dex (remove garden)