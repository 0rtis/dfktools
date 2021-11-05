
import json

FAIL_ON_NOT_FOUND = False

ALPHABET = '123456789abcdefghijkmnopqrstuvwx'

rarity = {
    0: "common",
    1: "uncommon",
    2: "rare",
    3: "legendary",
    4: "mythic",
}

_class = {
    0: "warrior",
    1: "knight",
    2: "thief",
    3: "archer",
    4: "priest",
    5: "wizard",
    6: "monk",
    7: "pirate",
    16: "paladin",
    17: "darkKnight",
    18: "summoner",
    19: "ninja",
    24: "dragoon",
    25: "sage",
    28: "dreadKnight"
}

visual_traits = {
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

stat_traits = {
    0: 'class',
    1: 'subClass',
    2: 'profession',
    3: 'passive1',
    4: 'passive2',
    5: 'active1',
    6: 'active2',
    7: 'statBoost1',
    8: 'statBoost2',
    9: 'statsUnknown1',
    10: 'element',
    11: 'statsUnknown2'
}

professions = {
    0: 'mining',
    2: 'gardening',
    4: 'fishing',
    6: 'foraging',
}

stats = {
    0: 'strength',
    2: 'agility',
    4: 'intelligence',
    6: 'wisdom',
    8: 'luck',
    10: 'vitality',
    12: 'endurance',
    14: 'dexterity'
}

elements = {
    0: 'fire',
    2: 'water',
    4: 'earth',
    6: 'wind',
    8: 'lightning',
    10: 'ice',
    12: 'light',
    14: 'dark',
}


def parse_rarity(id):
    value = rarity.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Rarity not found")
    return value


def parse_class(id):
    value = _class.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Class not found")
    return value


def parse_profession(id):
    value = professions.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Profession not found")
    return value


def parse_stat(id):
    value = stats.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Stat not found")
    return value


def parse_element(id):
    value = elements.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Element not found")
    return value


def parse_stat_genes(genes):
    stat_genes = {}
    stat_genes['raw'] = genes

    stat_raw_kai = "".join(__genesToKai(stat_genes['raw']).split(' '))

    for ki in range(0, len(stat_raw_kai)):
        stat_trait = stat_traits.get(int(ki / 4), None)
        kai = stat_raw_kai[ki]
        value_num = __kai2dec(kai)
        stat_genes[stat_trait] = value_num

    stat_genes['class'] = parse_class(stat_genes['class'])
    stat_genes['subClass'] = parse_class(stat_genes['subClass'])

    stat_genes['profession'] = parse_profession(stat_genes['profession'])

    stat_genes['statBoost1'] = parse_stat(stat_genes['statBoost1'])
    stat_genes['statBoost2'] = parse_stat(stat_genes['statBoost2'])
    stat_genes['statsUnknown1'] = stats.get(stat_genes['statsUnknown1'], None)  # parse_stat(stat_genes['statsUnknown1'])
    stat_genes['statsUnknown2'] = stats.get(stat_genes['statsUnknown2'], None)  # parse_stat(stat_genes['statsUnknown2'])

    stat_genes['element'] = parse_element(stat_genes['element'])

    return stat_genes


def parse_visual_genes(genes):
    visual_genes = {}
    visual_genes['raw'] = genes

    visual_raw_kai = "".join(__genesToKai(visual_genes['raw']).split(' '))

    for ki in range(0, len(visual_raw_kai)):
        stat_trait = visual_traits.get(int(ki / 4), None)
        kai = visual_raw_kai[ki]
        value_num = __kai2dec(kai)
        visual_genes[stat_trait] = value_num

    visual_genes['gender'] = 'male' if visual_genes['gender'] == 1 else 'female'
    return visual_genes


def __genesToKai(genes):
    BASE = len(ALPHABET)

    buf = ''
    while genes >= BASE:
        mod = int(genes % BASE)
        buf = ALPHABET[int(mod)] + buf
        genes = (genes - mod) // BASE

    # Add the last 4 (finally).
    buf = ALPHABET[int(genes)] + buf

    # Pad with leading 1s.
    buf = buf.rjust(48, '1')

    return ' '.join(buf[i:i + 4] for i in range(0, len(buf), 4))


def __kai2dec(kai):
    return ALPHABET.index(kai)


def parse_names(names_raw_string):
    names_raw_string = names_raw_string\
        .replace("\\xf3", "ó") \
        .replace("\\xf2", "ò") \
        .replace("\\xe9", "é") \
        .replace("\\xe1", "á") \
        .replace("\\xc9", "É") \
        .replace("\\xe9", "é") \
        .replace("\\xed", "í") \
        .replace("\\xfa", "ú") \
        .replace("\\xec", "ì")

    if "\\x" in names_raw_string:
        raise Exception("Unhandled unicode found")

    return json.loads(names_raw_string)
