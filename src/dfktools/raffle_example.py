import logging
import sys
import raffle.raffle_master as raffle_master
import raffle.utils.utils as raffle_utils
from web3 import Web3

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-raffle")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    w3 = Web3(Web3.HTTPProvider(rpc_server))
    private_key = ""  # set private key
    account_address = "0x"  # w3.eth.account.privateKeyToAccount(private_key).address
    gas_price_gwei = 115
    tx_timeout_seconds = 30

    # Get current raffles
    current_raffle = raffle_master.get_current_raffle_data(rpc_server)

    raffle_log = "Current raffle:"
    for r in current_raffle[0]:
        raffle_log = raffle_log + "\n\t" + str(raffle_utils.human_readable_raffle(r))
    logger.info(raffle_log)

    raffle_type_log = "Current raffle type:"
    for r in current_raffle[1]:
        raffle_type_log = raffle_type_log + "\n\t" + str(raffle_utils.human_readable_raffle_type(r))
    logger.info(raffle_type_log)

    # Get raffle by id
    raffle_by_id = raffle_master.get_raffle_list([1, 2], rpc_server)
    raffle_by_id_log = "Getting raffle by ids:"
    for r in raffle_by_id:
        raffle_by_id_log = raffle_by_id_log + "\n\t" + str(raffle_utils.human_readable_raffle(r))
    logger.info(raffle_by_id_log)

    # Get raffle allowed maximum entries
    raffle_id = [current_raffle[0][0][0]]
    raffle_max_entries = raffle_master.get_raffle_tickets_allowance_list(raffle_id, rpc_server)
    logger.info("Maximum allowed entries for raffle {} : {}".format(raffle_id[0],  raffle_max_entries[0]))

    # Enter raffle
    raffle_master.enter_raffle(3555, 1,
                               private_key, w3.eth.getTransactionCount(account_address),
                               gas_price_gwei, tx_timeout_seconds, rpc_server, logger)
