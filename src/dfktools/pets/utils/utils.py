FAIL_ON_NOT_FOUND = False

CRYSTALEVALE_PET_OFFSET = 1_000_000_000_000
SERENDALE2_PET_OFFSET = 2_000_000_000_000

egg_types = {
    0: "blue",
    1: "grey",
    2: "green",
    3: "yellow",
    4: "golden",
}

egg_rarity = {
    0: "common",
    1: "uncommon",
    2: "rare",
    3: "legendary",
    4: "mythic",
}


egg_elements = {
    0: 'fire',
    1: 'water',
    2: 'earth',
    3: 'wind',
    4: 'lightning',
    5: 'ice',
    6: 'light',
    7: 'dark',
}

food_types = {
    -1: None,
    0: 'regular',
    1: 'premium',
    2: 'regular-powered-up',
    3: 'premium-powered-up',
}

backgrounds = {
    0: "Stillwood Meadow",
    1: "Forest Trail",
    2: "Swamp of Eoxis",
    3: "Vithraven Outskirts",
    4: "Path of Fire",
    5: "Reyalin Mountain Pass",
    6: "Adelyn Side Street",
    7: "Bloater Falls",
    8: "Haywood Farmstead",
    9: "Inner Grove",
    10: "Vuhlmira Ruins"
}

blue_pet_bonuses = {
    1: "Unrevealed",
    80: "Unrevealed",
    160: "Unrevealed",
    2: "Efficient Angler",
    81: "Efficient Angler",
    161: "Efficient Angler",
    3: "Bountiful Catch",
    82: "Bountiful Catch",
    162: "Bountiful Catch",
    4: "Keen Eye",
    83: "Keen Eye",
    163: "Keen Eye",
    5: "Fortune Seeker",
    84: "Fortune Seeker",
    164: "Fortune Seeker",
    6: "Clutch Collector",
    85: "Clutch Collector",
    165: "Clutch Collector",
    7: "Runic Discoveries",
    86: "Runic Discoveries",
    166: "Runic Discoveries",
    8: "Skilled Angler",
    87: "Skilled Angler",
    167: "Skilled Angler",
    9: "Astute Angler",
    88: "Astute Angler",
    168: "Astute Angler",
    10: "Bonus Bounty",
    89: "Bonus Bounty",
    169: "Bonus Bounty",
    11: "Gaia's Chosen",
    90: "Gaia's Chosen",
    170: "Gaia's Chosen",
    171: "Innate Angler"
}

grey_pet_bonuses = {
    1: "Unrevealed",
    80: "Unrevealed",
    160: "Unrevealed",
    2: "Efficient Scavenger",
    81: "Efficient Scavenger",
    161: "Efficient Scavenger",
    3: "Bountiful Haul",
    82: "Bountiful Haul",
    162: "Bountiful Haul",
    4: "Keen Eye",
    83: "Keen Eye",
    163: "Keen Eye",
    5: "Fortune Seeker",
    84: "Fortune Seeker",
    164: "Fortune Seeker",
    6: "Clutch Collector",
    85: "Clutch Collector",
    165: "Clutch Collector",
    7: "Runic Discoveries",
    86: "Runic Discoveries",
    166: "Runic Discoveries",
    8: "Skilled Scavenger",
    87: "Skilled Scavenger",
    167: "Skilled Scavenger",
    9: "Astute Scavenger",
    88: "Astute Scavenger",
    168: "Astute Scavenger",
    10: "Bonus Bounty",
    89: "Bonus Bounty",
    169: "Bonus Bounty",
    11: "Gaia's Chosen",
    90: "Gaia's Chosen",
    170: "Gaia's Chosen",
    171: "Innate Scavenger"
}

green_pet_bonuses = {
    1: "Unrevealed",
    80: "Unrevealed",
    160: "Unrevealed",
    2: "Efficient Greenskeeper",
    81: "Efficient Greenskeeper",
    161: "Efficient Greenskeeper",
    3: "Bountiful Harvest",
    82: "Bountiful Harvest",
    162: "Bountiful Harvest",
    4: "Second Chance",
    83: "Second Chance",
    163: "Second Chance",
    5: "Clutch Collector",
    84: "Clutch Collector",
    164: "Clutch Collector",
    6: "Runic Discoveries",
    85: "Runic Discoveries",
    165: "Runic Discoveries",
    7: "Skilled Greenskeeper",
    86: "Skilled Greenskeeper",
    166: "Skilled Greenskeeper",
    8: "Astute Greenskeeper",
    87: "Astute Greenskeeper",
    167: "Astute Greenskeeper",
    9: "Bonus Bounty",
    88: "Bonus Bounty",
    168: "Bonus Bounty",
    10: "Gaia's Chosen",
    89: "Gaia's Chosen",
    169: "Gaia's Chosen",
    90: "Power Surge",
    170: "Power Surge",
    171: "Innate Greenskeeper"
}



def cv2norm_pet_id(cv_pet_id):
    return cv_pet_id - CRYSTALEVALE_PET_OFFSET


def norm2cv_pet_id(norm_pet_id):
    return norm_pet_id + CRYSTALEVALE_PET_OFFSET

def sd2norm_pet_id(sd2_pet_id):
    return sd2_pet_id - SERENDALE2_PET_OFFSET


def norm2sd_pet_id(norm_pet_id):
    return norm_pet_id + SERENDALE2_PET_OFFSET

def parse_egg_type(egg_type):
    value = egg_types.get(egg_type, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Egg type not found")
    return value


def parse_egg_rarity(rarity):
    value = egg_rarity.get(rarity, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Egg rarity not found")
    return value


def parse_egg_element(element):
    value = egg_elements.get(element, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Egg element not found")
    return value

def parse_food_type(food_type):
    value = food_types.get(food_type, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Food type not found")
    return value

def parse_background(background):
    value = backgrounds.get(background, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Background type not found")
    return value

def parse_bonus_rarity(bonus):
    if bonus < 80:
        return 'common'
    elif bonus < 160:
        return 'rare'
    else:
        return 'mythic'

def parse_bonus_type(egg_type, bonus):
    if type(egg_type) == int:
        egg_type = parse_egg_type(egg_type)

    value = None
    if egg_type == 'blue':
        value = blue_pet_bonuses.get(bonus, None)
    elif egg_type == 'grey':
        value = grey_pet_bonuses.get(bonus, None)
    elif egg_type == 'green':
        value = green_pet_bonuses.get(bonus, None)
    elif egg_type == 'yellow':
        value = None
    elif egg_type == 'golden':
        value = None

    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Egg bonus type not found")
    return value