from web3 import Web3

CONTRACT_ADDRESS = '0x6a56222A67df18FC282CD58dCDF12e61Be812f97'

ABI = """
    [{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"raffleId","type":"uint256"}],"name":"RaffleClosed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"raffleId","type":"uint256"},{"indexed":true,"internalType":"address","name":"winner","type":"address"}],"name":"RaffleDrawn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"raffleId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tickets","type":"uint256"}],"name":"RaffleEntered","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"raffleId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address[]","name":"rewards","type":"address[]"},{"internalType":"uint256[]","name":"rewardAmounts","type":"uint256[]"},{"internalType":"uint256","name":"maxWinners","type":"uint256"},{"internalType":"uint64","name":"duration","type":"uint64"}],"indexed":false,"internalType":"struct RaffleMaster.RaffleType","name":"raffleType","type":"tuple"}],"name":"RaffleStarted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"raffleTypeId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"bucket","type":"uint256"}],"name":"RaffleTypeActivated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address[]","name":"rewards","type":"address[]"},{"internalType":"uint256[]","name":"rewardAmounts","type":"uint256[]"},{"internalType":"uint256","name":"maxWinners","type":"uint256"},{"internalType":"uint64","name":"duration","type":"uint64"}],"indexed":false,"internalType":"struct RaffleMaster.RaffleType","name":"raffleType","type":"tuple"}],"name":"RaffleTypeAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"raffleTypeId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"bucket","type":"uint256"}],"name":"RaffleTypeDeactivated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"activeRaffleTypes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"uint256","name":"_bucket","type":"uint256"}],"name":"addActiveRaffleType","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_rewards","type":"address[]"},{"internalType":"uint256[]","name":"_rewardAmounts","type":"uint256[]"},{"internalType":"uint256","name":"_maxWinners","type":"uint256"},{"internalType":"uint64","name":"_duration","type":"uint64"},{"internalType":"uint256[]","name":"_buckets","type":"uint256[]"}],"name":"addAndActivateRaffleType","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_rewards","type":"address[]"},{"internalType":"uint256[]","name":"_rewardAmounts","type":"uint256[]"},{"internalType":"uint256","name":"_maxWinners","type":"uint256"},{"internalType":"uint64","name":"_duration","type":"uint64"}],"name":"addRaffleType","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"closeRaffles","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_raffleTypeId","type":"uint256"},{"internalType":"uint256","name":"_bucket","type":"uint256"}],"name":"createRaffle","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"currentRaffleBuckets","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"drawWinners","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_raffleId","type":"uint256"},{"internalType":"uint256","name":"_tickets","type":"uint256"}],"name":"enterRaffle","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"entries","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentRaffleBuckets","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentRaffleData","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"raffleType","type":"uint256"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"totalEntries","type":"uint256"},{"internalType":"uint256","name":"endTime","type":"uint256"},{"internalType":"uint256","name":"closedBlock","type":"uint256"},{"internalType":"address[]","name":"winners","type":"address[]"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct RaffleMaster.Raffle[]","name":"","type":"tuple[]"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address[]","name":"rewards","type":"address[]"},{"internalType":"uint256[]","name":"rewardAmounts","type":"uint256[]"},{"internalType":"uint256","name":"maxWinners","type":"uint256"},{"internalType":"uint64","name":"duration","type":"uint64"}],"internalType":"struct RaffleMaster.RaffleType[]","name":"","type":"tuple[]"},{"internalType":"uint256[]","name":"","type":"uint256[]"},{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLastRaffleBuckets","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPreviousRaffleData","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"raffleType","type":"uint256"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"totalEntries","type":"uint256"},{"internalType":"uint256","name":"endTime","type":"uint256"},{"internalType":"uint256","name":"closedBlock","type":"uint256"},{"internalType":"address[]","name":"winners","type":"address[]"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct RaffleMaster.Raffle[]","name":"","type":"tuple[]"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address[]","name":"rewards","type":"address[]"},{"internalType":"uint256[]","name":"rewardAmounts","type":"uint256[]"},{"internalType":"uint256","name":"maxWinners","type":"uint256"},{"internalType":"uint64","name":"duration","type":"uint64"}],"internalType":"struct RaffleMaster.RaffleType[]","name":"","type":"tuple[]"},{"internalType":"uint256[]","name":"","type":"uint256[]"},{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_raffleBuckets","type":"uint256[]"}],"name":"getRaffleList","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"raffleType","type":"uint256"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"totalEntries","type":"uint256"},{"internalType":"uint256","name":"endTime","type":"uint256"},{"internalType":"uint256","name":"closedBlock","type":"uint256"},{"internalType":"address[]","name":"winners","type":"address[]"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct RaffleMaster.Raffle[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_raffleBuckets","type":"uint256[]"}],"name":"getRaffleTicketsAllowanceList","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_raffleBuckets","type":"uint256[]"}],"name":"getRaffleTicketsList","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_raffleBuckets","type":"uint256[]"}],"name":"getRaffleTypesList","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address[]","name":"rewards","type":"address[]"},{"internalType":"uint256[]","name":"rewardAmounts","type":"uint256[]"},{"internalType":"uint256","name":"maxWinners","type":"uint256"},{"internalType":"uint64","name":"duration","type":"uint64"}],"internalType":"struct RaffleMaster.RaffleType[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"uint256","name":"_raffleId","type":"uint256"}],"name":"getTicketAllowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_buckets","type":"uint256"}],"name":"initRaffleBuckets","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_raffleTickets","type":"address"},{"internalType":"address","name":"_airdropClaim","type":"address"},{"internalType":"address","name":"_itemMinter","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"lastRaffleBuckets","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"name":"playerEntries","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"raffleTypes","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"maxWinners","type":"uint256"},{"internalType":"uint64","name":"duration","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"raffles","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"raffleType","type":"uint256"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"totalEntries","type":"uint256"},{"internalType":"uint256","name":"endTime","type":"uint256"},{"internalType":"uint256","name":"closedBlock","type":"uint256"},{"internalType":"uint8","name":"status","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_index","type":"uint256"},{"internalType":"uint256","name":"_bucket","type":"uint256"}],"name":"removeActiveRaffleType","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_raffleTypeId","type":"uint256"},{"internalType":"address[]","name":"_rewards","type":"address[]"},{"internalType":"uint256[]","name":"_rewardAmounts","type":"uint256[]"},{"internalType":"uint256","name":"_maxWinners","type":"uint256"},{"internalType":"uint64","name":"_duration","type":"uint64"}],"name":"setRaffleType","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_bucket","type":"uint256"}],"name":"startRandomRaffle","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_buckets","type":"uint256[]"}],"name":"startRandomRaffles","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"timePerTicket","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalRaffleTypes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalRaffles","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"}]
    """


def block_explorer_link(txid):
    return 'https://explorer.harmony.one/tx/' + str(txid)

    
def get_current_raffle_buckets(rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getCurrentRaffleBuckets().call()


def get_current_raffle_data(rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getCurrentRaffleData().call()


def get_last_raffle_buckets(rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getLastRaffleBuckets().call()


def get_previous_raffle_data(rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getPreviousRaffleData().call()


def get_total_raffles(rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.totalRaffles().call()


def get_ticket_allowance(address, raffle_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getTicketAllowance(Web3.toChecksumAddress(address),raffle_id).call()


def get_total_raffle_types(rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.totalRaffleTypes().call()


def get_raffle_list(raffle_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getRaffleList(raffle_id).call()


def get_raffle_tickets_allowance_list(raffle_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getRaffleTicketsAllowanceList(raffle_id).call()


def get_raffle_tickets_list(raffle_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getRaffleTicketsList(raffle_id).call()


def get_raffle_types_list(raffle_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getRaffleTypesList(raffle_id).call()


def enter_raffle(raffle_id, tickets, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.enterRaffle(raffle_id, tickets)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.buildTransaction({'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt
