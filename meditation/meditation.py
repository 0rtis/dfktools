from web3 import Web3

CONTRACT_ADDRESS = '0x0594d86b2923076a2316eaea4e1ca286daa142c1'

ABI = """
    [
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"atunementItemAddress","type":"address"}],"name":"AttunementCrystalAdded","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"struct IHeroTypes.SummoningInfo","name":"summoningInfo","type":"tuple"},{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enum IHeroTypes.Rarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"struct IHeroTypes.HeroInfo","name":"info","type":"tuple"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enum IHeroTypes.HeroStatus","name":"status","type":"uint8"}],"internalType":"struct IHeroTypes.HeroState","name":"state","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStats","name":"stats","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStatGrowth","name":"primaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStatGrowth","name":"secondaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"}],"internalType":"struct IHeroTypes.HeroProfessions","name":"professions","type":"tuple"}],"indexed":false,"internalType":"struct IHeroTypes.Hero","name":"hero","type":"tuple"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"struct IHeroTypes.SummoningInfo","name":"summoningInfo","type":"tuple"},{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enum IHeroTypes.Rarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"struct IHeroTypes.HeroInfo","name":"info","type":"tuple"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enum IHeroTypes.HeroStatus","name":"status","type":"uint8"}],"internalType":"struct IHeroTypes.HeroState","name":"state","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStats","name":"stats","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStatGrowth","name":"primaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStatGrowth","name":"secondaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"}],"internalType":"struct IHeroTypes.HeroProfessions","name":"professions","type":"tuple"}],"indexed":false,"internalType":"struct IHeroTypes.Hero","name":"oldHero","type":"tuple"}],"name":"LevelUp","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"meditationId","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"primaryStat","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"secondaryStat","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"tertiaryStat","type":"uint8"},{"indexed":false,"internalType":"address","name":"attunementCrystal","type":"address"}],"name":"MeditationBegun","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"meditationId","type":"uint256"}],"name":"MeditationCompleted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"stat","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"increase","type":"uint8"},{"indexed":false,"internalType":"enum MeditationCircle.UpdateType","name":"updateType","type":"uint8"}],"name":"StatUp","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint16","name":"_level","type":"uint16"}],"name":"_getRequiredRunes","outputs":[{"internalType":"uint16[10]","name":"","type":"uint16[10]"}],"stateMutability":"pure","type":"function"},
        {"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"activeAttunementCrystals","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"addAttunementCrystal","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"completeMeditation","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"randomNumber","type":"uint256"},{"internalType":"uint256","name":"digits","type":"uint256"},{"internalType":"uint256","name":"offset","type":"uint256"}],"name":"extractNumber","outputs":[{"internalType":"uint256","name":"result","type":"uint256"}],"stateMutability":"pure","type":"function"},
        {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"getActiveMeditations","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"heroId","type":"uint256"},{"internalType":"uint8","name":"primaryStat","type":"uint8"},{"internalType":"uint8","name":"secondaryStat","type":"uint8"},{"internalType":"uint8","name":"tertiaryStat","type":"uint8"},{"internalType":"address","name":"attunementCrystal","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct MeditationCircle.Meditation[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"getHeroMeditation","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"heroId","type":"uint256"},{"internalType":"uint8","name":"primaryStat","type":"uint8"},{"internalType":"uint8","name":"secondaryStat","type":"uint8"},{"internalType":"uint8","name":"tertiaryStat","type":"uint8"},{"internalType":"address","name":"attunementCrystal","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct MeditationCircle.Meditation","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getMeditation","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"heroId","type":"uint256"},{"internalType":"uint8","name":"primaryStat","type":"uint8"},{"internalType":"uint8","name":"secondaryStat","type":"uint8"},{"internalType":"uint8","name":"tertiaryStat","type":"uint8"},{"internalType":"address","name":"attunementCrystal","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct MeditationCircle.Meditation","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"heroToMeditation","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_heroCoreAddress","type":"address"},{"internalType":"address","name":"_statScienceAddress","type":"address"},{"internalType":"address","name":"_jewelTokenAddress","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"jewelToken","outputs":[{"internalType":"contract IJewelToken","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"profileActiveMeditations","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"heroId","type":"uint256"},{"internalType":"uint8","name":"primaryStat","type":"uint8"},{"internalType":"uint8","name":"secondaryStat","type":"uint8"},{"internalType":"uint8","name":"tertiaryStat","type":"uint8"},{"internalType":"address","name":"attunementCrystal","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint8","name":"status","type":"uint8"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address[]","name":"_feeAddresses","type":"address[]"},{"internalType":"uint256[]","name":"_feePercents","type":"uint256[]"}],"name":"setFees","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint8","name":"_index","type":"uint8"},{"internalType":"address","name":"_address","type":"address"}],"name":"setRune","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"},{"internalType":"uint8","name":"_primaryStat","type":"uint8"},{"internalType":"uint8","name":"_secondaryStat","type":"uint8"},{"internalType":"uint8","name":"_tertiaryStat","type":"uint8"},{"internalType":"address","name":"_attunementCrystal","type":"address"}],"name":"startMeditation","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"vrf","outputs":[{"internalType":"bytes32","name":"result","type":"bytes32"}],"stateMutability":"view","type":"function"}
    ]
    """

ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'


def block_explorer_link(txid):
    return 'https://explorer.harmony.one/tx/' + str(txid)


def get_required_runes(level, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions._getRequiredRunes(level).call()


def active_attunement_crystals(address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.activeAttunementCrystals(address).call()


def add_attunement_crystal(address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.addAttunementCrystal(address).call()


def start_meditation(hero_id, stat1, stat2, stat3, attunement_crystal_address, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):

    if type(stat1) == str:
        stat1 = stat2id(stat1)

    if type(stat2) == str:
        stat2 = stat2id(stat2)

    if type(stat3) == str:
        stat3 = stat2id(stat3)

    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.startMeditation(hero_id, stat1, stat2, stat3, attunement_crystal_address).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

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


def complete_meditation(hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.completeMeditation(hero_id).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

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


def get_active_meditations(address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getActiveMeditations(address).call()


def get_hero_meditation(hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    result = contract.functions.getHeroMeditation(hero_id).call()
    if result[0] == 0:
        return None
    return result


def get_meditation(meditation_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    result = contract.functions.getMeditation(meditation_id).call()
    if result[0] == 0:
        return None
    return result


def hero_to_meditation_id(hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.heroToMeditation(hero_id).call()


def profile_active_meditations(address, id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.profileActiveMeditations(address, id).call()


def stat2id(label):
    stats = {
        'strength': 0,
        'agility': 1,
        'intelligence': 2,
        'wisdom': 3,
        'luck': 4,
        'vitality': 5,
        'endurance': 6,
        'dexterity': 7
    }
    return stats.get(label, None)


def xp_per_Level(level):
    next_level = level + 1
    if level < 6:
        return next_level * 1000
    elif level < 9:
        return 4000 + (next_level - 5) * 2000
    elif level < 16:
        return 12000 + (next_level - 9) * 4000
    elif level < 36:
        return 40000 + (next_level - 16) * 5000
    elif level < 56:
        return 140000 + (next_level - 36) * 7500
    else:
        return 290000 + (next_level - 56) * 10000
