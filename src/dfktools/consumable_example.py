import logging
import sys
from web3 import Web3
import dex.erc20 as erc20
import consumable.consumable as consumable

if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-consumable")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://klaytn.rpc.defikingdoms.com/'
    logger.info("Using RPC server " + rpc_server)

    stamina_vial_address = erc20.symbol2address('DFKSTMNPTN', 'sd2')
    realm_consumable_contract_address = consumable.SERENDALE2_CONTRACT_ADDRESS

    w3 = Web3(Web3.HTTPProvider(rpc_server))
    private_key = None  # set private key
    account_address = w3.eth.account.from_key(private_key).address
    gas_price_gwei = 40
    tx_timeout_seconds = 30

    hero_id = 1
    consumable.consume_item(realm_consumable_contract_address, stamina_vial_address, hero_id, private_key, w3.eth.get_transaction_count(account_address), gas_price_gwei, tx_timeout_seconds, rpc_server, logger)