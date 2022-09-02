import logging
import sys
from web3 import Web3
import dex.erc20 as erc20
import airdrop.airdrop as airdrop

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-airdrop")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    # View Player Airdrops (Serendale)
    player_address = "0xf543311360d1072873D627B06ffe85587e8fc41a"  # insert target player address
    airdrops = airdrop.view_airdrops(airdrop.SERENDALE_CONTRACT_ADDRESS, player_address, rpc_server)
    for airdrop in airdrops:
        airdrop["tokenName"] = erc20.address2item(airdrop["tokenAddress"], 'serendale')[2]
    logger.info(airdrops)

    # Claim Airdrop
    w3 = Web3(Web3.HTTPProvider(rpc_server))
    private_key = None  # set private key
    account_address = w3.eth.account.privateKeyToAccount(private_key).address
    gas_price_gwei = 100
    tx_timeout_seconds = 30
    airdrop_id = 0  # Use index from view_airdrops list
    airdrop.claim_airdrop(airdrop.SERENDALE_CONTRACT_ADDRESS, airdrop_id, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, tx_timeout_seconds, rpc_server, logger)
