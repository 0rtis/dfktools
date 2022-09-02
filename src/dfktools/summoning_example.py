import logging
import sys
import time
import summoning.summoning as summoning
from web3 import Web3

SD = 'serendale'
CV = 'crystalvale'

def tears_for_hero(hero_level:int, hero_rank:str='basic', add_extra_tears=True) -> int:
    '''
    Tears are common, so it's best to maximize tears spent. 
    Tears are calculated as: 
    - basic class => 10, advanced => 40, Elite => 70, Transcendant => 100 
    - plus an optional 10 tears for every 5 levels completed
    '''   
    tears_for_rank = {
        'basic': 10,
        'advanced': 40,
        'elite': 70,
        'exalted': 100,
    }
    base_tears = tears_for_rank.get(hero_rank.lower(), 10)

    extra_tears = 10 * (hero_level // 5)
    if add_extra_tears:
        base_tears += extra_tears
    return base_tears


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

    # Customize with the level and rank of your heroes. Incorrect values will
    # raise 'not enough tears' or 'too many tears' errors from the blockchain
    hero_level_1 = 1
    hero_rank_1 = 'basic'
    hero_level_2 = 1
    hero_rank_2 = 'basic'

    hero_1_tears = tears_for_hero(hero_level_1, hero_rank_1, add_extra_tears=True)
    hero_2_tears = tears_for_hero(hero_level_2, hero_rank_2, add_extra_tears=True)

    w3 = Web3(Web3.HTTPProvider(rpc_server))

    summoning.summon_crystal(contract_address, hero_id_1, hero_id_2, hero_1_tears, hero_2_tears, private_key, w3.eth.getTransactionCount(address), gas_price_gwei, tx_timeout, rpc_server, logger)

    crystals = summoning.get_user_crystal_ids(contract_address, address, rpc_server)
    if crystals:
        logger.info(f"Waiting 20 seconds before opening crystal {crystals[0]}")
        time.sleep(20)
        tx_receipt = summoning.open_crystal(contract_address, crystals[0], private_key, w3.eth.getTransactionCount(address), gas_price_gwei, tx_timeout, rpc_server, logger)
        hero_id = summoning.parse_opened_crystal(contract_address, tx_receipt, rpc_server)
        logger.info("Summoned hero: " + str(hero_id))
