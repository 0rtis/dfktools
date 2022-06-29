type = {
    'solo': 1,
    'squad': 3,
    'war': 9
}

background = {
    'desert': 0,
    'forest': 2,
    'plains': 4,
    'island': 6,
    'swamp': 8,
    'mountains': 10,
    'city': 12,
    'arctic': 14
}

stat = {
    'strength': 0,
    'agility': 2,
    'intelligence': 4,
    'wisdom': 6,
    'luck': 8,
    'vitality': 10,
    'endurance': 12,
    'dexterity': 14
}


def string2id(attr, label):
    if attr == "type":
        return type.get(label, None)
    elif attr == 'background':
        return background.get(label, None)
    elif attr == 'stat':
        return stat.get(label, None)

    return None
