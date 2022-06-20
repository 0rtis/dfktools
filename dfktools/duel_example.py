import logging
import json
import sys
import duel.duel as duels

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-duel")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    result = duels.get_duel(1,rpc_server)
    
    # result = duels.getDuelTurns(1,rpc_server) # get duels details based on Duel ID
    # result = duels.get_total_open_duel_entries(3, rpc_server) # 1-Solo,3-Squad,9-War

    logger.info(json.dumps(result, indent=4, sort_keys=False))
