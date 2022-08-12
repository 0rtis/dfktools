import logging
import sys
import time
from dfktools.summoning import summoning
from web3 import Web3

SD = 'serendale'
CV = 'crystalvale'

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-summoning")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    realm = 'serendale'

    if realm == SD:
        rpc_server = 'https://api.harmony.one'
        gas_price_gwei = 115 
        tx_timeout = 30
        contract_address = summoning.SERENDALE_CONTRACT_ADDRESS
    else:
        rpc_server = 'https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc'
        gas_price_gwei = {'maxFeePerGas': 2, 'maxPriorityFeePerGas': 2} 
        tx_timeout = 30
        contract_address = summoning.CRYSTALVALE_CONTRACT_ADDRESS


    logger.info("Using RPC server " + rpc_server)

    # All these will need to be customized for your address
    address = '0x<YOUR_ADDRESS_HERE>'
    private_key = '<YOUR_KEY_HERE>'
    hero_id_1 = 12345
    hero_id_2 = 67890

    w3 = Web3(Web3.HTTPProvider(rpc_server))
    nonce = w3.eth.getTransactionCount( address)

    hero_1_tears = 10 # Should be 10 more for every 5 levels attained
    hero_2_tears = 10 

    summoning.summon_crystal(contract_address, hero_id_1, hero_id_2, hero_1_tears, hero_2_tears, private_key, nonce, gas_price_gwei, tx_timeout, rpc_server, logger)

    crystals = summoning.get_user_crystal_ids(contract_address, address, rpc_server)
    if crystals:
        logger.info(f"Waiting 20 seconds before opening crystal {crystals[0]}")
        time.sleep(20)
        tx_receipt = summoning.open_crystal(contract_address, crystals[0], private_key, nonce, gas_price_gwei, tx_timeout, rpc_server, logger)
        hero_id = summoning.parse_opened_crystal(contract_address, tx_receipt, rpc_server)
        logger.info("Summoned hero: "+ str(hero_id))
    


