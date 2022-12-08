from web3 import Web3

SERENDALE_CONTRACT_ADDRESS = '0xf4d3aE202c9Ae516f7eb1DB5afF19Bf699A5E355'
CRYSTALVALE_CONTRACT_ADDRESS = '0xBc36D18662Bb97F9e74B1EAA1B752aA7A44595A7'
SERENDALE2_CONTRACT_ADDRESS = '0xb086584f476Ad21B40aF0672f385a67334A0b294'

ABI = """
    [
        {"name": "CrystalOpen", "type": "event", "inputs": [{"name": "owner", "type": "address", "internalType": "address", "indexed": true}, {"name": "crystalId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "heroId", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
        {"name": "CrystalSummoned", "type": "event", "inputs": [{"name": "crystalId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "owner", "type": "address", "internalType": "address", "indexed": true}, {"name": "summonerId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "assistantId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "generation", "type": "uint16", "internalType": "uint16", "indexed": false}, {"name": "createdBlock", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "summonerTears", "type": "uint8", "internalType": "uint8", "indexed": false}, {"name": "assistantTears", "type": "uint8", "internalType": "uint8", "indexed": false}, {"name": "enhancementStone", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
        {"name": "EnhancementStoneAdded", "type": "event", "inputs": [{"name": "atunementItemAddress", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
        {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "internalType": "uint8", "indexed": false}], "anonymous": false},
        {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
        {"name": "RoleAdminChanged", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "previousAdminRole", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "newAdminRole", "type": "bytes32", "internalType": "bytes32", "indexed": true}], "anonymous": false},
        {"name": "RoleGranted", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "account", "type": "address", "internalType": "address", "indexed": true}, {"name": "sender", "type": "address", "internalType": "address", "indexed": true}], "anonymous": false},
        {"name": "RoleRevoked", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "account", "type": "address", "internalType": "address", "indexed": true}, {"name": "sender", "type": "address", "internalType": "address", "indexed": true}], "anonymous": false},
        {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
        {"name": "DEFAULT_ADMIN_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
        {"name": "MODERATOR_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
        {"name": "activeEnhancementStones", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
        {"name": "addEnhancementStone", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "approveAuctionSpending", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "baseCooldown", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
        {"name": "baseSummonFee", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
        {"name": "calculateSummoningCost", "type": "function", "inputs": [{"name": "_hero", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "summoningInfo", "type": "tuple", "components": [{"name": "summonedTime", "type": "uint256", "internalType": "uint256"}, {"name": "nextSummonTime", "type": "uint256", "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "summons", "type": "uint32", "internalType": "uint32"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}], "internalType": "struct IHeroTypes.SummoningInfo"}, {"name": "info", "type": "tuple", "components": [{"name": "statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "rarity", "type": "uint8", "internalType": "enum IHeroTypes.Rarity"}, {"name": "shiny", "type": "bool", "internalType": "bool"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}, {"name": "class", "type": "uint8", "internalType": "uint8"}, {"name": "subClass", "type": "uint8", "internalType": "uint8"}], "internalType": "struct IHeroTypes.HeroInfo"}, {"name": "state", "type": "tuple", "components": [{"name": "staminaFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "hpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "mpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint16", "internalType": "uint16"}, {"name": "xp", "type": "uint64", "internalType": "uint64"}, {"name": "currentQuest", "type": "address", "internalType": "address"}, {"name": "sp", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum IHeroTypes.HeroStatus"}], "internalType": "struct IHeroTypes.HeroState"}, {"name": "stats", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hp", "type": "uint16", "internalType": "uint16"}, {"name": "mp", "type": "uint16", "internalType": "uint16"}, {"name": "stamina", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroStats"}, {"name": "primaryStatGrowth", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroStatGrowth"}, {"name": "secondaryStatGrowth", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroStatGrowth"}, {"name": "professions", "type": "tuple", "components": [{"name": "mining", "type": "uint16", "internalType": "uint16"}, {"name": "gardening", "type": "uint16", "internalType": "uint16"}, {"name": "foraging", "type": "uint16", "internalType": "uint16"}, {"name": "fishing", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroProfessions"}], "internalType": "struct IHeroTypes.Hero"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
        {"name": "cooldownPerGen", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
        {"name": "createCrystal", "type": "function", "inputs": [{"name": "_owner", "type": "address", "internalType": "address"}, {"name": "_summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "_assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "_generation", "type": "uint16", "internalType": "uint16"}, {"name": "_summonerBonusTears", "type": "uint8", "internalType": "uint8"}, {"name": "_assistantBonusTears", "type": "uint8", "internalType": "uint8"}, {"name": "_enhancementStone", "type": "address", "internalType": "address"}, {"name": "_maxSummons", "type": "uint32", "internalType": "uint32"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "crystalIdOffset", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
        {"name": "crystals", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "createdBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "summonerTears", "type": "uint8", "internalType": "uint8"}, {"name": "assistantTears", "type": "uint8", "internalType": "uint8"}, {"name": "enhancementStone", "type": "address", "internalType": "address"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
        {"name": "determineRarity", "type": "function", "inputs": [{"name": "_rarityRoll", "type": "uint256", "internalType": "uint256"}, {"name": "_rarityMod", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint8", "internalType": "enum IHeroTypes.Rarity"}], "stateMutability": "pure"},
        {"name": "enabled", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
        {"name": "getCrystal", "type": "function", "inputs": [{"name": "_crystalId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "createdBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "summonerTears", "type": "uint8", "internalType": "uint8"}, {"name": "assistantTears", "type": "uint8", "internalType": "uint8"}, {"name": "enhancementStone", "type": "address", "internalType": "address"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}], "internalType": "struct ICrystalTypes.HeroCrystal"}], "stateMutability": "view"},
        {"name": "getRoleAdmin", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
        {"name": "getUserCrystals", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
        {"name": "grantRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "hasRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
        {"name": "increasePerGen", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
        {"name": "increasePerSummon", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
        {"name": "initialize", "type": "function", "inputs": [{"name": "_heroCoreAddress", "type": "address", "internalType": "address"}, {"name": "_geneScienceAddress", "type": "address", "internalType": "address"}, {"name": "_jewelTokenAddress", "type": "address", "internalType": "address"}, {"name": "_gaiaTearsAddress", "type": "address", "internalType": "address"}, {"name": "_statScienceAddress", "type": "address", "internalType": "address"}, {"name": "_crystalIdOffset", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "jewelToken", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IJewelToken"}], "stateMutability": "view"},
        {"name": "newSummonCooldown", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
        {"name": "open", "type": "function", "inputs": [{"name": "_crystalId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
        {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
        {"name": "removeEnhancementStone", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "renounceRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "revokeRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "setFees", "type": "function", "inputs": [{"name": "_feeAddresses", "type": "address[]", "internalType": "address[]"}, {"name": "_feePercents", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "setGeneScienceAddress", "type": "function", "inputs": [{"name": "_geneScienceAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "setStatScienceAddress", "type": "function", "inputs": [{"name": "_statScienceAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "setSummonCooldowns", "type": "function", "inputs": [{"name": "_newSummonCooldown", "type": "uint256", "internalType": "uint256"}, {"name": "_baseCooldown", "type": "uint256", "internalType": "uint256"}, {"name": "_cooldownPerGen", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "setSummonFees", "type": "function", "inputs": [{"name": "_baseSummonFee", "type": "uint256", "internalType": "uint256"}, {"name": "_increasePerSummon", "type": "uint256", "internalType": "uint256"}, {"name": "_increasePerGen", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "statScience", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IStatScience"}], "stateMutability": "view"},
        {"name": "summonCrystal", "type": "function", "inputs": [{"name": "_summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "_assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "_summonerTears", "type": "uint16", "internalType": "uint16"}, {"name": "_assistantTears", "type": "uint16", "internalType": "uint16"}, {"name": "_enhancementStone", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "summonCrystalWithAuction", "type": "function", "inputs": [{"name": "_summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "_assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "_summonerTears", "type": "uint16", "internalType": "uint16"}, {"name": "_assistantTears", "type": "uint16", "internalType": "uint16"}, {"name": "_enhancementStone", "type": "address", "internalType": "address"}, {"name": "_assistingAuctionAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "summonCrystalWithAuctionOld", "type": "function", "inputs": [{"name": "_summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "_assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "_summonerTears", "type": "uint16", "internalType": "uint16"}, {"name": "_assistantTears", "type": "uint16", "internalType": "uint16"}, {"name": "_enhancementStone", "type": "address", "internalType": "address"}, {"name": "_assistingAuctionAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "supportsInterface", "type": "function", "inputs": [{"name": "interfaceId", "type": "bytes4", "internalType": "bytes4"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
        {"name": "toggleEnabled", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "totalCrystals", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
        {"name": "userCrystals", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"}
    ]
        """


def block_explorer_link(contract_address, txid):
    if hasattr(contract_address, 'address'):
        contract_address = str(contract_address.address)
    contract_address = str(contract_address).upper()
    if contract_address == SERENDALE_CONTRACT_ADDRESS.upper():
        return 'https://explorer.harmony.one/tx/' + str(txid)
    elif contract_address == CRYSTALVALE_CONTRACT_ADDRESS.upper():
        return 'https://subnets.avax.network/defi-kingdoms/dfk-chain/explorer/tx/' + str(txid)
    elif contract_address == SERENDALE2_CONTRACT_ADDRESS.upper():
        return 'https://scope.klaytn.com/tx/' + str(txid)
    else:
        return str(txid)


def get_user_crystal_ids(contract_address, user_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getUserCrystals(Web3.toChecksumAddress(user_address)).call()


def summon_crystal(contract_address, summoner_id, assistant_id, summoner_tears, assistant_tears, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger=None):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    if logger is not None:
        logger.info("Summoning with " + str(summoner_id) + " & "+str(assistant_id))
    tx = contract.functions.summonCrystal(summoner_id, assistant_id, summoner_tears, assistant_tears, '0x0000000000000000000000000000000000000000')
    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.buildTransaction({'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})
    if logger is not None:
        logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    if logger is not None:
        logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    if logger is not None:
        logger.debug("Transaction successfully sent !")
        logger.info(
            "Waiting for transaction " + block_explorer_link(contract_address, signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    if logger is not None:
        logger.info("Transaction mined !")
        logger.info(str(tx_receipt))
    return tx_receipt


def open_crystal(contract_address, crystal_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger=None):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    if logger is not None:
        logger.info("Opening crystal "+str(crystal_id))
    tx = contract.functions.open(crystal_id)
    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.buildTransaction({'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})
    if logger is not None:
        logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    if logger is not None:
        logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    if logger is not None:
        logger.debug("Transaction successfully sent !")
        logger.info(
            "Waiting for transaction " + block_explorer_link(contract_address, signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    if logger is not None:
        logger.info("Transaction mined !")
        logger.info(str(tx_receipt))
    return tx_receipt


def parse_opened_crystal(contract_address, tx_receipt, rpc_address):
    # Given the receipt from opening a crystal, return the id of the new hero
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract = w3.eth.contract(contract_address, abi=ABI)
    opened_info = contract.events.CrystalOpen().processReceipt(tx_receipt)
    hero_id = opened_info[0].args.heroId
    return hero_id


