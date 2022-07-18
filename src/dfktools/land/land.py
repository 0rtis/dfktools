from web3 import Web3

CONTRACT_ADDRESS = "0xD5f5bE1037e457727e011ADE9Ca54d21c21a3F8A"

ABI = '''
	[
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"landId","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"region","type":"uint256"}],"name":"LandClaimed","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"landId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"oldRegion","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newRegion","type":"uint256"}],"name":"LandMoved","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},
		{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
		{"inputs":[],"name":"CLAIMER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"MINTER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"claimLand","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"address","name":"_account","type":"address"}],"name":"getAccountLands","outputs":[{"components":[{"internalType":"uint256","name":"landId","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"region","type":"uint256"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256","name":"steward","type":"uint256"},{"internalType":"uint64","name":"score","type":"uint64"}],"internalType":"struct LandCore.LandMeta[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"getAllLands","outputs":[{"components":[{"internalType":"uint256","name":"landId","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"region","type":"uint256"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256","name":"steward","type":"uint256"},{"internalType":"uint64","name":"score","type":"uint64"}],"internalType":"struct LandCore.LandMeta[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"uint256","name":"_landId","type":"uint256"}],"name":"getLand","outputs":[{"components":[{"internalType":"uint256","name":"landId","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"region","type":"uint256"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256","name":"steward","type":"uint256"},{"internalType":"uint64","name":"score","type":"uint64"}],"internalType":"struct LandCore.LandMeta","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"uint32","name":"_region","type":"uint32"}],"name":"getLandsByRegion","outputs":[{"components":[{"internalType":"uint256","name":"landId","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"region","type":"uint256"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256","name":"steward","type":"uint256"},{"internalType":"uint64","name":"score","type":"uint64"}],"internalType":"struct LandCore.LandMeta[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"landIdToMeta","outputs":[{"internalType":"uint256","name":"landId","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"region","type":"uint256"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256","name":"steward","type":"uint256"},{"internalType":"uint64","name":"score","type":"uint64"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"pure","type":"function"},
		{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"regionToLandCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"regionToLands","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"uint256","name":"_landId","type":"uint256"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"uint32","name":"_region","type":"uint32"}],"name":"safeMint","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
		{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
		{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},
		{"inputs":[{"internalType":"uint256","name":"_landId","type":"uint256"},{"internalType":"uint256","name":"_region","type":"uint256"},{"internalType":"uint256","name":"_oldLandIndex","type":"uint256"}],"name":"updateLandRegion","outputs":[],"stateMutability":"nonpayable","type":"function"}
	]
'''


def block_explorer_link(txid):
	return 'https://explorer.harmony.one/tx/' + str(txid)


def get_account_lands(account, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))

	contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
	contract = w3.eth.contract(contract_address, abi=ABI)

	return contract.functions.getAccountLands(Web3.toChecksumAddress(account)).call()


def get_land(land_id, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))

	contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
	contract = w3.eth.contract(contract_address, abi=ABI)

	return contract.functions.getLand(land_id).call()


def get_lands_by_region(region_id, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))

	contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
	contract = w3.eth.contract(contract_address, abi=ABI)

	return contract.functions.getLandsByRegion(region_id).call()


def get_all_lands(rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))

	contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
	contract = w3.eth.contract(contract_address, abi=ABI)

	return contract.functions.getAllLands().call()


def owner_of(land_id, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))

	contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
	contract = w3.eth.contract(contract_address, abi=ABI)

	return contract.functions.ownerOf(land_id).call()


def total_supply(rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))

	contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
	contract = w3.eth.contract(contract_address, abi=ABI)

	return contract.functions.totalSupply().call()


def claim(landId, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
	w3 = Web3(Web3.HTTPProvider(rpc_address))
	account = w3.eth.account.privateKeyToAccount(private_key)
	w3.eth.default_account = account.address

	contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
	contract = w3.eth.contract(contract_address, abi=ABI)

	tx = contract.functions.claimLand(account.address, landId)

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
	logger.info(str(tx_receipt))
