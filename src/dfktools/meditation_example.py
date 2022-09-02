import logging
from web3 import Web3
import sys
import time
import meditation.meditation as meditation

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-meditation")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    # NOTE: make sure you use the realm where your hero currently is
    realm = 'crystalvale'
    if realm == 'serendale':
        rpc_server = 'https://api.harmony.one'
        contract_address = meditation.SERENDALE_CONTRACT_ADDRESS
        gas_price_gwei = 115
        tx_timeout_seconds = 30        
    elif realm == 'crystalvale':
        rpc_server = 'https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc'
        contract_address = meditation.CRYSTALVALE_CONTRACT_ADDRESS
        gas_price_gwei = {'maxFeePerGas': 2, 'maxPriorityFeePerGas': 2}
        tx_timeout_seconds = 30

    logger.info("Using RPC server " + rpc_server)

    # Customize your hero info, stats, & credentials here
    hero_id = 1
    level = 1    
    private_key = None  # set private key
    account_address = '0x...'
    # Stats to update should be full words, lowercase. 
    # See meditation.stat2id() for examples
    stat1 = 'strength'
    stat2 = 'endurance'
    stat3 = 'luck'
    attunement_crystal_address = meditation.ZERO_ADDRESS

    w3 = Web3(Web3.HTTPProvider(rpc_server))
    # NOTE that you will have to have approved Shvas runes & the meditation contract 
    # before calling these functions, and that account address has all the needed
    # runes
    active_meditations = meditation.get_active_meditations(contract_address, account_address, rpc_server)
    logger.info("Pending meditation on address " + str(account_address) + ": "+str(active_meditations))

    
    required_runes = meditation.get_required_runes(contract_address, level, rpc_server)
    meditation.start_meditation(contract_address, hero_id, stat1, stat2, stat3,
                                attunement_crystal_address, private_key, w3.eth.getTransactionCount(account_address),
                                gas_price_gwei, tx_timeout_seconds, rpc_server, logger)
    hero_meditation = meditation.get_hero_meditation(contract_address, hero_id, rpc_server)
    logger.info("Pending meditation "+str(hero_meditation))
    logger.info("Waiting 20 seconds to complete meditation")
    time.sleep(20)
    tx_receipt = meditation.complete_meditation(contract_address, hero_id, private_key, w3.eth.getTransactionCount(account_address),
                                   gas_price_gwei, tx_timeout_seconds, rpc_server, logger)

    level_up = meditation.parse_meditation_results(contract_address, tx_receipt, rpc_server)
                
    meditation_results_msg = ""
    for hero_id in level_up:
        inc = level_up[hero_id]
        meditation_results_msg += f"""
            ```
            Hero: {hero_id}
                Level: {inc['new level']}  STAM: +{inc.get("STAMINA", {}).get("increase", 0)}  HP: +{inc.get("HP",{}).get("increase", 0)}
                STR: +{inc.get("STR", {}).get("increase", 0)}  DEX: +{inc.get("DEX", {}).get("increase", 0)}
                AGI: +{inc.get("AGI", {}).get("increase", 0)}  VIT: +{inc.get("VIT", {}).get("increase", 0)}
                END: +{inc.get("END", {}).get("increase", 0)}  INT: +{inc.get("INT", {}).get("increase", 0)}
                WIS: +{inc.get("WIS", {}).get("increase", 0)}  LCK: +{inc.get("LCK", {}).get("increase", 0)}
            ```"""

    msg = f"Completed level up: {meditation_results_msg}"
    logger.info(msg)

