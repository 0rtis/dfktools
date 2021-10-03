import copy
from web3 import Web3
import json
import logging
import sys


def transfer(hero_id, owner_private_key, owner_nonce, receiver_address, gas_price_gwei, rpc_address, hero_contract_abi, logger):
    """Tranfer a hero from the owner to the receiver. USE AT YOUR OWN RISK !"""
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(owner_private_key)
    w3.eth.default_account = account.address

    hero_contract_address = Web3.toChecksumAddress('0x5f753dcdf9b1ad9aabc1346614d1f4746fd6ce5c')
    hero_contract = w3.eth.contract(hero_contract_address, abi=hero_contract_abi)

    owner = hero_contract.functions.ownerOf(hero_id).call()
    logger.info("Hero's owner " + str(owner))

    if owner != account.address:
        raise Exception("Owner mismatch")

    tx = hero_contract.functions.transferFrom(owner, receiver_address, hero_id).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': owner_nonce})
    logger.info("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=owner_private_key)
    logger.info("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.info("Transaction successfully sent !")
    logger.info(
        "Waiting for transaction https://explorer.harmony.one/tx/" + str(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=24 * 3600,
                                                     poll_latency=3)
    logger.info("Transaction mined !")
    logger.info(str(tx_receipt))


def read_from_contract(hero_id, rpc_address, hero_contract_abi):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    hero_contract_address = Web3.toChecksumAddress('0x5f753dcdf9b1ad9aabc1346614d1f4746fd6ce5c')
    hero_contract = w3.eth.contract(hero_contract_address, abi=hero_contract_abi)
    hero_contract_entry = hero_contract.functions.getHero(hero_id).call()

    hero = {}
    tuple_index = 0

    hero['id'] = hero_contract_entry[tuple_index]
    tuple_index = tuple_index + 1

    # SummoningInfo
    summoning_info = {}
    summoning_info['summonedTime'] = hero_contract_entry[tuple_index][0]
    summoning_info['nextSummonTime'] = hero_contract_entry[tuple_index][1]
    summoning_info['assistantId']= hero_contract_entry[tuple_index][2]
    summoning_info['summons']= hero_contract_entry[tuple_index][3]
    summoning_info['maxSummons']= hero_contract_entry[tuple_index][4]

    hero['summoningInfo'] = summoning_info
    tuple_index = tuple_index + 1

    # HeroInfo
    hero_info = {}
    hero_info['statGenes'] = hero_contract_entry[tuple_index][0]
    hero_info['visualGenes'] = hero_contract_entry[tuple_index][1]
    hero_info['rarity'] = hero_contract_entry[tuple_index][2]
    hero_info['shiny'] = hero_contract_entry[tuple_index][3]
    hero_info['generation'] = hero_contract_entry[tuple_index][4]
    hero_info['firstName'] = hero_contract_entry[tuple_index][5]
    hero_info['lastName'] = hero_contract_entry[tuple_index][6]
    hero_info['shinyStyle'] = hero_contract_entry[tuple_index][7]
    hero_info['class'] = hero_contract_entry[tuple_index][8]
    hero_info['subClass'] = hero_contract_entry[tuple_index][9]

    hero['info'] = hero_info
    tuple_index = tuple_index + 1

    # HeroState
    hero_state = {}
    hero_state['staminaFullAt'] = hero_contract_entry[tuple_index][0]
    hero_state['hpFullAt'] = hero_contract_entry[tuple_index][1]
    hero_state['mpFullAt'] = hero_contract_entry[tuple_index][2]
    hero_state['level'] = hero_contract_entry[tuple_index][3]
    hero_state['xp'] = hero_contract_entry[tuple_index][4]
    hero_state['currentQuest'] = hero_contract_entry[tuple_index][5]
    hero_state['sp'] = hero_contract_entry[tuple_index][6]
    hero_state['status'] = hero_contract_entry[tuple_index][6]

    hero['state'] = hero_state
    tuple_index = tuple_index + 1

    # HeroStats
    hero_stats = {}
    hero_stats['strength'] = hero_contract_entry[tuple_index][0]
    hero_stats['intelligence'] = hero_contract_entry[tuple_index][1]
    hero_stats['wisdom'] = hero_contract_entry[tuple_index][2]
    hero_stats['luck'] = hero_contract_entry[tuple_index][3]
    hero_stats['agility'] = hero_contract_entry[tuple_index][4]
    hero_stats['vitality'] = hero_contract_entry[tuple_index][5]
    hero_stats['endurance'] = hero_contract_entry[tuple_index][6]
    hero_stats['dexterity'] = hero_contract_entry[tuple_index][7]
    hero_stats['hp'] = hero_contract_entry[tuple_index][8]
    hero_stats['mp'] = hero_contract_entry[tuple_index][9]
    hero_stats['stamina'] = hero_contract_entry[tuple_index][10]

    hero['stats'] = hero_stats
    tuple_index = tuple_index + 1

    # primary HeroStatGrowth
    hero_primary_stat_growth = {}
    hero_primary_stat_growth['strength'] = hero_contract_entry[tuple_index][0]
    hero_primary_stat_growth['intelligence'] = hero_contract_entry[tuple_index][1]
    hero_primary_stat_growth['wisdom'] = hero_contract_entry[tuple_index][2]
    hero_primary_stat_growth['luck'] = hero_contract_entry[tuple_index][3]
    hero_primary_stat_growth['agility'] = hero_contract_entry[tuple_index][4]
    hero_primary_stat_growth['vitality'] = hero_contract_entry[tuple_index][5]
    hero_primary_stat_growth['endurance'] = hero_contract_entry[tuple_index][6]
    hero_primary_stat_growth['dexterity'] = hero_contract_entry[tuple_index][7]
    hero_primary_stat_growth['hpSm'] = hero_contract_entry[tuple_index][8]
    hero_primary_stat_growth['hpRg'] = hero_contract_entry[tuple_index][9]
    hero_primary_stat_growth['hpLg'] = hero_contract_entry[tuple_index][10]
    hero_primary_stat_growth['mpSm'] = hero_contract_entry[tuple_index][11]
    hero_primary_stat_growth['mpRg'] = hero_contract_entry[tuple_index][12]
    hero_primary_stat_growth['mpLg'] = hero_contract_entry[tuple_index][13]

    hero['primaryStatGrowth'] = hero_primary_stat_growth
    tuple_index = tuple_index + 1

    # secondary HeroStatGrowth
    hero_secondary_stat_growth = {}
    hero_secondary_stat_growth['strength'] = hero_contract_entry[tuple_index][0]
    hero_secondary_stat_growth['intelligence'] = hero_contract_entry[tuple_index][1]
    hero_secondary_stat_growth['wisdom'] = hero_contract_entry[tuple_index][2]
    hero_secondary_stat_growth['luck'] = hero_contract_entry[tuple_index][3]
    hero_secondary_stat_growth['agility'] = hero_contract_entry[tuple_index][4]
    hero_secondary_stat_growth['vitality'] = hero_contract_entry[tuple_index][5]
    hero_secondary_stat_growth['endurance'] = hero_contract_entry[tuple_index][6]
    hero_secondary_stat_growth['dexterity'] = hero_contract_entry[tuple_index][7]
    hero_secondary_stat_growth['hpSm'] = hero_contract_entry[tuple_index][8]
    hero_secondary_stat_growth['hpRg'] = hero_contract_entry[tuple_index][9]
    hero_secondary_stat_growth['hpLg'] = hero_contract_entry[tuple_index][10]
    hero_secondary_stat_growth['mpSm'] = hero_contract_entry[tuple_index][11]
    hero_secondary_stat_growth['mpRg'] = hero_contract_entry[tuple_index][12]
    hero_secondary_stat_growth['mpLg'] = hero_contract_entry[tuple_index][13]

    hero['secondaryStatGrowth'] = hero_secondary_stat_growth
    tuple_index = tuple_index + 1

    # HeroProfessions
    hero_professions = {}
    hero_professions['mining'] = hero_contract_entry[tuple_index][0]
    hero_professions['gardening'] = hero_contract_entry[tuple_index][0]
    hero_professions['foraging'] = hero_contract_entry[tuple_index][0]
    hero_professions['fishing'] = hero_contract_entry[tuple_index][0]

    hero['professions'] = hero_professions

    return hero


def human_readable_hero(raw_hero, hero_male_first_names, hero_female_first_names, hero_last_names):
    rarity = {
        0: "Common",
        1: "Uncommon",
        2: "Rare",
        3: "Legendary",
        4: "Mythic",
    }
    _class = {
        0: "Warrior",
        1: "Knight",
        2: "Thief",
        3: "Archer",
        4: "Priest",
        5: "Wizard",
        6: "Monk",
        7: "Pirate",
    }

    readable_hero = copy.deepcopy(raw_hero)

    readable_hero['info']['rarity'] = rarity.get(readable_hero['info']['rarity'], None)
    readable_hero['info']['class'] = _class.get(readable_hero['info']['class'], None)
    readable_hero['info']['subClass'] = _class.get(readable_hero['info']['subClass'], None)

    if not readable_hero['info']['rarity']:
        raise Exception("Rarity not found")

    if not readable_hero['info']['class']:
        raise Exception("Class not found")

    if not readable_hero['info']['subClass']:
        raise Exception("Subclass not found")

    # visualGenes
    visual_genes = {}
    visual_genes['raw'] = readable_hero['info']['visualGenes']

    ALPHABET = '123456789abcdefghijkmnopqrstuvwx'

    def genesToKai(genes):
        BASE = len(ALPHABET)

        buf = ''
        while genes >= BASE:
            mod = int(genes % BASE)
            buf = ALPHABET[int(mod)] + buf
            genes = (genes - mod) // BASE

        # Add the last 4 (finally).
        buf = ALPHABET[int(genes)] + buf

        # Pad with leading 0s.
        buf = buf.rjust(48, '1')

        return ' '.join(buf[i:i + 4] for i in range(0, len(buf), 4))

    def kai2dec(kai):
        return ALPHABET.index(kai)

    raw_kai = "".join(genesToKai(visual_genes['raw']).split(' '))
    traits = {
        0: 'gender',
        1: 'headAppendage',
        2: 'backAppendage',
        3: 'background',
        4: 'hairStyle',
        5: 'hairColor',
        6: 'visualUnknown1',
        7: 'eyeColor',
        8: 'skinColor',
        9: 'appendageColor',
        10: 'backAppendageColor',
        11: 'visualUnknown2'
    }
    for ki in range(0, len(raw_kai)):
        trait = traits.get(int(ki / 4), None)
        kai = raw_kai[ki]
        value_num = kai2dec(kai)

        visual_genes[trait] = value_num

    visual_genes['gender'] = 'Male' if visual_genes['gender'] == 1 else 'Female'
    readable_hero['info']['visualGenes'] = visual_genes

    # names
    readable_hero['info']['firstName'] = hero_male_first_names[readable_hero['info']['firstName']] if readable_hero['info']['visualGenes']['gender'] == 'Male' else hero_female_first_names[readable_hero['info']['firstName']]
    readable_hero['info']['lastName'] = hero_last_names[readable_hero['info']['lastName']]

    return readable_hero


if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK hero")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'

    logger.info("Using RPC server " + rpc_server)

    with open('hero.abi', 'r') as f:
        hero_abi_json = f.read()
    logger.info("Hero contract ABI loaded")

    with open('femaleFirstName.json', 'r') as f:
        female_first_names = json.load(f)
    logger.info("Female hero first name loaded")

    with open('maleFirstName.json', 'r') as f:
        male_first_names = json.load(f)
    logger.info("Male hero first name loaded")

    with open('lastName.json', 'r') as f:
        last_names = json.load(f)
    logger.info("Hero last name loaded")

    # transfer(1, 'private key of the owner', 'next nonce of owner account', 'receiver address', 200, rpc_server, hero_abi_json, logger)

    for i in range(1, 2074):
        logger.info("Processing hero #"+str(i))
        hero = read_from_contract(i, rpc_server, hero_abi_json)
        readable_hero = human_readable_hero(hero, male_first_names, female_first_names, last_names)
        logger.info(json.dumps(readable_hero, indent=4, sort_keys=False))
