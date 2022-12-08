# stone_carver.py

from web3 import Web3

SERENDALE_CONTRACT_ADDRESS = '0xfFB8a55676edA75954AB45a6Ce16F88b119dC511'
CRYSTALVALE_CONTRACT_ADDRESS = '0xc32A0e963e50AAAED273A75425fC39902b0d0b3b'

ABI = '''
	[
		{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"stoneAddress","type":"address"},{"indexed":false,"internalType":"address[]","name":"requiredResources","type":"address[]"},{"indexed":false,"internalType":"uint32[]","name":"requiredQuantities","type":"uint32[]"},{"indexed":false,"internalType":"bool","name":"active","type":"bool"}],"name":"RecipeSet","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"workingUntil","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"awayUntil","type":"uint256"}],"name":"ShopSetUp","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"address","name":"stoneAddress","type":"address"},{"indexed":false,"internalType":"uint256","name":"quantity","type":"uint256"}],"name":"StoneCarved","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
		{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"adminSetupShop","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[],"name":"awayUntil","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"address","name":"_stoneAddress","type":"address"},{"internalType":"uint256","name":"_quantity","type":"uint256"}],"name":"carveStone","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[],"name":"getAvailability","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"address","name":"stoneAddress","type":"address"}],"name":"getRecipe","outputs":[{"components":[{"internalType":"address[]","name":"requiredResources","type":"address[]"},{"internalType":"uint32[]","name":"requiredQuantities","type":"uint32[]"},{"internalType":"bool","name":"active","type":"bool"}],"internalType":"struct StoneCarver.Recipe","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[],"name":"minClosedTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"minOpenTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"recipes","outputs":[{"internalType":"bool","name":"active","type":"bool"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"address","name":"_stoneAddress","type":"address"},{"internalType":"address[]","name":"_requiredResources","type":"address[]"},{"internalType":"uint32[]","name":"_requiredQuantities","type":"uint32[]"},{"internalType":"bool","name":"_active","type":"bool"}],"name":"setRecipe","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"uint256","name":"_minOpenTime","type":"uint256"},{"internalType":"uint256","name":"_varOpenTime","type":"uint256"},{"internalType":"uint256","name":"_minClosedTime","type":"uint256"},{"internalType":"uint256","name":"_varClosedTime","type":"uint256"}],"name":"setTimes","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[],"name":"setUpShop","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[],"name":"varClosedTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"varOpenTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"workingUntil","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}
	]
'''


def block_explorer_link(contract_address, txid):
	if hasattr(contract_address, 'address'):
		contract_address = str(contract_address.address)
	contract_address = str(contract_address).upper()
	if contract_address == SERENDALE_CONTRACT_ADDRESS.upper():
		return 'https://explorer.harmony.one/tx/' + str(txid)
	elif contract_address == CRYSTALVALE_CONTRACT_ADDRESS.upper():
		return 'https://subnets.avax.network/defi-kingdoms/dfk-chain/explorer/tx/' + str(txid)
	else:
		return str(txid)


def away_until(contract_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))
	contract = w3.eth.contract(Web3.toChecksumAddress(contract_address), abi=ABI)
	return contract.functions.awayUntil().call()


def carve_stone(contract_address, item_address, quantity, private_key, nonce, gas_price_gwei, tx_timeout_seconds,
				rpc_address, logger):
	w3 = Web3(Web3.HTTPProvider(rpc_address))
	account = w3.eth.account.privateKeyToAccount(private_key)
	w3.eth.default_account = account.address

	contract_address = Web3.toChecksumAddress(contract_address)
	contract = w3.eth.contract(contract_address, abi=ABI)

	if isinstance(gas_price_gwei, dict):  # dynamic fee
		tx = contract.functions.carveStone(item_address, quantity).buildTransaction(
			{'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
			 'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
	else:  # legacy
		tx = contract.functions.carveStone(item_address, quantity).buildTransaction(
			{'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

	logger.debug("Signing transaction")
	signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
	logger.debug("Sending transaction " + str(tx))
	ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
	logger.debug("Transaction successfully sent !")
	logger.info(
		"Waiting for transaction " + block_explorer_link(contract_address, signed_tx.hash.hex()) + " to be mined")
	tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
													 poll_latency=2)
	logger.info("Transaction mined !")
	return tx_receipt


def get_availability(contract_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))
	contract = w3.eth.contract(Web3.toChecksumAddress(contract_address), abi=ABI)
	return contract.functions.getAvailability().call()


def get_recipe(contract_address, item_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))
	contract = w3.eth.contract(Web3.toChecksumAddress(contract_address), abi=ABI)
	return contract.functions.getRecipe(item_address).call()


def min_closed_time(contract_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))
	contract = w3.eth.contract(Web3.toChecksumAddress(contract_address), abi=ABI)
	return contract.functions.minClosedTime().call()


def min_open_time(contract_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))
	contract = w3.eth.contract(Web3.toChecksumAddress(contract_address), abi=ABI)
	return contract.functions.minOpenTime().call()


def recipes(item_address, contract_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))
	contract = w3.eth.contract(Web3.toChecksumAddress(contract_address), abi=ABI)
	return contract.functions.recipes(item_address).call()


def set_up_shop(contract_address, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
	w3 = Web3(Web3.HTTPProvider(rpc_address))
	account = w3.eth.account.privateKeyToAccount(private_key)
	w3.eth.default_account = account.address

	contract_address = Web3.toChecksumAddress(contract_address)
	contract = w3.eth.contract(contract_address, abi=ABI)

	if isinstance(gas_price_gwei, dict):  # dynamic fee
		tx = contract.functions.setUpShop().buildTransaction(
			{'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
			 'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
	else:  # legacy
		tx = contract.functions.setUpShop().buildTransaction(
			{'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

	logger.debug("Signing transaction")
	signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
	logger.debug("Sending transaction " + str(tx))
	ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
	logger.debug("Transaction successfully sent !")
	logger.info(
		"Waiting for transaction " + block_explorer_link(contract_address, signed_tx.hash.hex()) + " to be mined")
	tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
													 poll_latency=2)
	logger.info("Transaction mined !")
	return tx_receipt


def var_closed_time(contract_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))
	contract = w3.eth.contract(Web3.toChecksumAddress(contract_address), abi=ABI)
	return contract.functions.varClosedTime().call()


def var_open_time(contract_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))
	contract = w3.eth.contract(Web3.toChecksumAddress(contract_address), abi=ABI)
	return contract.functions.varOpenTime().call()


def working_until(contract_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))
	contract = w3.eth.contract(Web3.toChecksumAddress(contract_address), abi=ABI)
	return contract.functions.workingUntil().call()
