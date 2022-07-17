FAIL_ON_NOT_FOUND = False

egg_types = {
    0: "blue",
    1: "grey"
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


def human_readable_pet(raw_pet):
    if raw_pet is None:
        return None

    pet = {}
    i = 0

    pet['id'] = raw_pet[i]
    i = i + 1
    pet['originId'] = raw_pet[i]
    i = i + 1
    pet['name'] = raw_pet[i]
    i = i + 1
    pet['season'] = raw_pet[i]
    i = i + 1
    pet['eggType'] = parse_egg_type(raw_pet[i])
    i = i + 1
    pet['rarity'] = parse_egg_rarity(raw_pet[i])
    i = i + 1
    pet['element'] = parse_egg_element(raw_pet[i])
    i = i + 1
    pet['bonusCount'] = raw_pet[i]
    i = i + 1
    pet['profBonus'] = raw_pet[i]
    i = i + 1
    pet['profBonusScalar'] = raw_pet[i]
    i = i + 1
    pet['craftBonus'] = raw_pet[i]
    i = i + 1
    pet['combatBonusScalar'] = raw_pet[i]
    i = i + 1
    pet['appearance'] = raw_pet[i]
    i = i + 1
    pet['background'] = raw_pet[i]
    i = i + 1
    pet['shiny'] = raw_pet[i]
    i = i + 1
    pet['hungryAt'] = raw_pet[i]
    i = i + 1
    pet['equippableAt   '] = raw_pet[i]
    i = i + 1
    pet['equippedTo'] = raw_pet[i]
    i = i + 1




    return pet