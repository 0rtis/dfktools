from web3 import Web3

SERENDALE_CONTRACT_ADDRESS = "0x87cba8f998f902f2fff990effa1e261f35932e57"
CRYSTALVALE_CONTRACT_ADDRESS = "0x2542e1Ce063FED3b5Aa81936c5a8f6Eeccaa6B4A"

ABI = '''
	[
		{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"potionAddress","type":"address"},{"indexed":false,"internalType":"address[]","name":"requiredResources","type":"address[]"},{"indexed":false,"internalType":"uint32[]","name":"requiredQuantities","type":"uint32[]"}],"name":"PotionAdded","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"address","name":"potionAddress","type":"address"},{"indexed":false,"internalType":"uint256","name":"quantity","type":"uint256"},{"indexed":false,"internalType":"address[]","name":"requiredResources","type":"address[]"},{"indexed":false,"internalType":"uint32[]","name":"requiredQuantities","type":"uint32[]"}],"name":"PotionCreated","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"potionAddress","type":"address"},{"indexed":false,"internalType":"address[]","name":"requiredResources","type":"address[]"},{"indexed":false,"internalType":"uint32[]","name":"requiredQuantities","type":"uint32[]"},{"indexed":false,"internalType":"uint8","name":"status","type":"uint8"}],"name":"PotionUpdated","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
		{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"address","name":"_potionAddress","type":"address"},{"internalType":"address[]","name":"_requiredResources","type":"address[]"},{"internalType":"uint32[]","name":"_requiredQuantities","type":"uint32[]"}],"name":"addPotion","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"addressToPotionId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"address","name":"_potionAddress","type":"address"},{"internalType":"uint256","name":"_quantity","type":"uint256"}],"name":"createPotion","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"address","name":"_potionAddress","type":"address"}],"name":"getPotion","outputs":[{"components":[{"internalType":"address","name":"potionAddress","type":"address"},{"internalType":"address[]","name":"requiredResources","type":"address[]"},{"internalType":"uint32[]","name":"requiredQuantities","type":"uint32[]"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct Alchemist.Potion","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"getPotions","outputs":[{"components":[{"internalType":"address","name":"potionAddress","type":"address"},{"internalType":"address[]","name":"requiredResources","type":"address[]"},{"internalType":"uint32[]","name":"requiredQuantities","type":"uint32[]"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct Alchemist.Potion[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"address","name":"_dfkGoldAddress","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"potions","outputs":[{"internalType":"address","name":"potionAddress","type":"address"},{"internalType":"uint8","name":"status","type":"uint8"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"togglePause","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"address","name":"_potionAddress","type":"address"},{"internalType":"address[]","name":"_requiredResources","type":"address[]"},{"internalType":"uint32[]","name":"_requiredQuantities","type":"uint32[]"},{"internalType":"uint8","name":"_status","type":"uint8"}],"name":"updatePotion","outputs":[],"stateMutability":"nonpayable","type":"function"}
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


def create_potion(contract_address, potion_address, quantity, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
	w3 = Web3(Web3.HTTPProvider(rpc_address))
	account = w3.eth.account.privateKeyToAccount(private_key)
	w3.eth.default_account = account.address

	contract_address = Web3.toChecksumAddress(contract_address)
	contract = w3.eth.contract(contract_address, abi=ABI)

	if isinstance(gas_price_gwei, dict):  # dynamic fee
		tx = contract.functions.createPotion(potion_address, quantity).buildTransaction(
			{'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
			 'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
	else:  # legacy
		tx = contract.functions.createPotion(potion_address, quantity).buildTransaction(
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


def address_to_potion_id(contract_address, potion_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))

	contract_address = Web3.toChecksumAddress(contract_address)
	contract = w3.eth.contract(contract_address, abi=ABI)

	return contract.functions.addressToPotionId(potion_address).call()


def potion_id_to_address_amount(contract_address, uint256, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))

	contract_address = Web3.toChecksumAddress(contract_address)
	contract = w3.eth.contract(contract_address, abi=ABI)

	raw = contract.functions.potions(uint256).call()
	return {'address': raw[0], 'batchSize': raw[1]}


def get_potion(contract_address, potion_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))

	contract_address = Web3.toChecksumAddress(contract_address)
	contract = w3.eth.contract(contract_address, abi=ABI)

	raw = contract.functions.getPotion(potion_address).call()
	return {'address': raw[0], 'ingredientAddresses': raw[1], 'ingredientQuantities': raw[2], 'batchSize': raw[3]}


def get_potions(contract_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))

	contract_address = Web3.toChecksumAddress(contract_address)
	contract = w3.eth.contract(contract_address, abi=ABI)

	raw = contract.functions.getPotions().call()
	potions = []
	for r in raw:
		potions.append({'address': r[0], 'ingredientAddresses': r[1], 'ingredientQuantities': r[2], 'batchSize': r[3]})

	return potions
