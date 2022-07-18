import requests
from web3 import Web3

ABI = """
    [
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"auctionId","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"AuctionCancelled","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"auctionId","type":"uint256"},{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"startingPrice","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"endingPrice","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"duration","type":"uint256"},{"indexed":false,"internalType":"address","name":"winner","type":"address"}],"name":"AuctionCreated","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"auctionId","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalPrice","type":"uint256"},{"indexed":false,"internalType":"address","name":"winner","type":"address"}],"name":"AuctionSuccessful","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
        {"inputs":[],"name":"BIDDER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"ERC721","outputs":[{"internalType":"contract IERC721Upgradeable","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"auctionIdOffset","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"auctions","outputs":[{"internalType":"address","name":"seller","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint128","name":"startingPrice","type":"uint128"},{"internalType":"uint128","name":"endingPrice","type":"uint128"},{"internalType":"uint64","name":"duration","type":"uint64"},{"internalType":"uint64","name":"startedAt","type":"uint64"},{"internalType":"address","name":"winner","type":"address"},{"internalType":"bool","name":"open","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_bidAmount","type":"uint256"}],"name":"bid","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_bidder","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_bidAmount","type":"uint256"}],"name":"bidFor","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"cancelAuction","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"cancelAuctionWhenPaused","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint128","name":"_startingPrice","type":"uint128"},{"internalType":"uint128","name":"_endingPrice","type":"uint128"},{"internalType":"uint64","name":"_duration","type":"uint64"},{"internalType":"address","name":"_winner","type":"address"}],"name":"createAuction","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getAuction","outputs":[{"components":[{"internalType":"address","name":"seller","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint128","name":"startingPrice","type":"uint128"},{"internalType":"uint128","name":"endingPrice","type":"uint128"},{"internalType":"uint64","name":"duration","type":"uint64"},{"internalType":"uint64","name":"startedAt","type":"uint64"},{"internalType":"address","name":"winner","type":"address"},{"internalType":"bool","name":"open","type":"bool"}],"internalType":"struct ERC721AuctionBase.Auction","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"}],"name":"getAuctions","outputs":[{"components":[{"internalType":"address","name":"seller","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint128","name":"startingPrice","type":"uint128"},{"internalType":"uint128","name":"endingPrice","type":"uint128"},{"internalType":"uint64","name":"duration","type":"uint64"},{"internalType":"uint64","name":"startedAt","type":"uint64"},{"internalType":"address","name":"winner","type":"address"},{"internalType":"bool","name":"open","type":"bool"}],"internalType":"struct ERC721AuctionBase.Auction[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getCurrentPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"getUserAuctions","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_landCoreAddress","type":"address"},{"internalType":"address","name":"_jewelTokenAddress","type":"address"},{"internalType":"uint256","name":"_cut","type":"uint256"},{"internalType":"uint256","name":"_auctionIdOffset","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"isOnAuction","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"jewelToken","outputs":[{"internalType":"contract IJewelToken","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"maxPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"minPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"pure","type":"function"},
        {"inputs":[],"name":"ownerCut","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address[]","name":"_feeAddresses","type":"address[]"},{"internalType":"uint256[]","name":"_feePercents","type":"uint256[]"}],"name":"setFees","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_min","type":"uint256"},{"internalType":"uint256","name":"_max","type":"uint256"}],"name":"setLimits","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"totalAuctions","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"userAuctions","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}
    ]
    """


def block_explorer_link(txid):
    return 'https://explorer.harmony.one/tx/' + str(txid) + ' or https://subnets.avax.network/defi-kingdoms/dfk-chain/explorer/tx/' + str(txid)


def bid(auction_contract_address, token_id, bid_amount_wei, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    auction_contract_address = Web3.toChecksumAddress(auction_contract_address)
    contract = w3.eth.contract(auction_contract_address, abi=ABI)

    tx = contract.functions.bid(token_id, bid_amount_wei)

    if isinstance(gas_price_gwei, dict):   # dynamic fee
        tx = tx.buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:   # legacy
        tx = tx.buildTransaction({'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.info("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.info("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.info("Transaction successfully sent !")
    logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")
    logger.info(str(tx_receipt))


def create_auction(auction_address, token_id, starting_price_wei, ending_price_wei, duration, winner, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    auction_contract_address = Web3.toChecksumAddress(auction_address)
    auction_contract = w3.eth.contract(auction_contract_address, abi=ABI)

    tx = auction_contract.functions.createAuction(token_id, starting_price_wei, ending_price_wei, duration, winner).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.info("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.info("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.info("Transaction successfully sent !")
    logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")
    logger.info(str(tx_receipt))


def cancel_auction(auction_address, token_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    auction_contract_address = Web3.toChecksumAddress(auction_address)
    auction_contract = w3.eth.contract(auction_contract_address, abi=ABI)

    tx = auction_contract.functions.cancelAuction(token_id).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.info("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.info("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.info("Transaction successfully sent !")
    logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")
    logger.info(str(tx_receipt))


def is_on_auction(auction_address, token_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    auction_contract_address = Web3.toChecksumAddress(auction_address)
    auction_contract = w3.eth.contract(auction_contract_address, abi=ABI)
    return auction_contract.functions.isOnAuction(token_id).call()


def get_auction(auction_address, token_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    auction_contract_address = Web3.toChecksumAddress(auction_address)
    auction_contract = w3.eth.contract(auction_contract_address, abi=ABI)
    return auction_contract.functions.getAuction(token_id).call()


def get_auctions(auction_address, token_ids, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    auction_contract_address = Web3.toChecksumAddress(auction_address)
    auction_contract = w3.eth.contract(auction_contract_address, abi=ABI)
    return auction_contract.functions.getAuctions(token_ids).call()


def total_auctions(auction_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    auction_contract_address = Web3.toChecksumAddress(auction_address)
    auction_contract = w3.eth.contract(auction_contract_address, abi=ABI)
    return auction_contract.functions.totalAuctions().call()


def get_user_auctions(auction_address, user, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    auction_contract_address = Web3.toChecksumAddress(auction_address)
    auction_contract = w3.eth.contract(auction_contract_address, abi=ABI)
    return auction_contract.functions.getUserAuctions(Web3.toChecksumAddress(user)).call()


def auctions(auction_address, index, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    auction_contract_address = Web3.toChecksumAddress(auction_address)
    auction_contract = w3.eth.contract(auction_contract_address, abi=ABI)
    return auction_contract.functions.auctions(index).call()

