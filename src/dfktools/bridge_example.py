import logging
import sys
from web3 import Web3
import bridge.hero_bridge as hero_bridge
import bridge.dfktears_bridge as dfktears_bridge

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-bridge")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    serendale_rpc_server = 'https://api.harmony.one'
    crystalvale_rpc_server = 'https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc'
    logger.info("Using RPC servers " + serendale_rpc_server + ", " + crystalvale_rpc_server)

    private_key = None  # set private key
    tx_timeout = 30
    hero_id = 404

    # Serendale to Crystalvale
    gas_price_gwei = 115
    w3 = Web3(Web3.HTTPProvider(serendale_rpc_server))
    account_address = w3.eth.account.privateKeyToAccount(private_key).address
    hero_bridge.send_hero(hero_bridge.SERENDALE_CONTRACT_ADDRESS, hero_id, hero_bridge.CRYSTALVALE_CHAIN_ID,
                          w3.toWei(0.004, "ether"), private_key, w3.eth.getTransactionCount(account_address),
                          gas_price_gwei, tx_timeout, serendale_rpc_server, logger)

    # Crystalvale to Serendale
    gas_price_gwei = {'maxFeePerGas': 2, 'maxPriorityFeePerGas': 2}  # EIP-1559
    w3 = Web3(Web3.HTTPProvider(crystalvale_rpc_server))
    account_address = w3.eth.account.privateKeyToAccount(private_key).address
    hero_bridge.send_hero(hero_bridge.CRYSTALVALE_CONTRACT_ADDRESS, hero_id, hero_bridge.SERENDALE_CHAIN_ID,
                          w3.toWei(0.05, "ether"), private_key,
                          Web3(Web3.HTTPProvider(crystalvale_rpc_server)).eth.getTransactionCount(account_address),
                          gas_price_gwei, tx_timeout, crystalvale_rpc_server, logger)