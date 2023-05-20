FAIL_ON_NOT_FOUND = False

v2_quest_types = {
    1: "attemptBased",
    #2: "timeBased",
    #3: "well",
}


v3_quest_types = {
  1: "Fishing",
  2: "Foraging",
  3: "Gold Mining",
  4: "Token Mining",
  5: "Gardening",
  6: "Training"
}

v3_training_quest_param = {
  0: "Strength",
  1: "Intelligence",
  2: "Wisdom",
  3: "Luck",
  4: "Agility",
  5: "Vitality",
  6: "Endurance",
  7: "Dexterity"
}

v3_quest_statuses = {
    0: None,
    1: 'STARTED',
    2: 'COMPLETED',
    3: 'CANCELED',
}

def parse_v3_quest_type(_id):
    value = v3_quest_types.get(_id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Quest type not found")
    return value

def parse_v3_quest_type_label(quest_type_label: str):
    for k in v3_quest_types.keys():
        if v3_quest_types[k] == quest_type_label:
            return k
    return None

def parse_v3_training_quest_param(_id: int):
    value = v3_training_quest_param.get(_id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Quest training param not found")

def parse_v3_training_quest_param_label(training_type_label: str):
    for k in v3_training_quest_param.keys():
        if v3_training_quest_param[k] == training_type_label:
            return k
    return None

def parse_v3_quest_status(_id: int):
    value = v3_quest_statuses.get(_id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Quest status not found")

def parse_v3_quest_status_label(quest_status_label: str):
    for k in v3_quest_statuses.keys():
        if v3_quest_statuses[k] == quest_status_label:
            return k
    return None

def parse_v2_quest_type(_id):
    value = v2_quest_types.get(_id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Quest type not found")
    return value


def human_readable_quest(raw_quest):
    if raw_quest is None:
        return None

    quest = {}

    if len(raw_quest) == 11: #v3
        quest['id'] = raw_quest[0]
        quest['type'] = parse_v3_quest_type(raw_quest[1])
        quest['level'] = raw_quest[2]
        quest['heroes'] = raw_quest[3]
        quest['player'] = raw_quest[4]
        quest['startBlock'] = raw_quest[5]
        quest['startTime'] = raw_quest[6]
        quest['completeAtTime'] = raw_quest[7]
        quest['attempts'] = raw_quest[8]
        quest['status'] = parse_v3_quest_status(raw_quest[9])
        quest['param'] = parse_v3_training_quest_param_label(raw_quest[10]) if quest['type'] == 'Training' else raw_quest[10]
    if len(raw_quest) == 10:  # v2
        quest['id'] = raw_quest[0]
        quest['address'] = raw_quest[1]
        quest['level'] = raw_quest[2]
        quest['heroes'] = raw_quest[3]
        quest['player'] = raw_quest[4]
        quest['startBlock'] = raw_quest[5]
        quest['startTime'] = raw_quest[6]
        quest['completeAtTime'] = raw_quest[7]
        quest['attempts'] = raw_quest[8]
        quest['type'] = parse_v2_quest_type(raw_quest[9])
    else:  # TODO:// v1 - remove once old quests have been migrated
        quest['id'] = raw_quest[0]
        quest['address'] = raw_quest[1]
        quest['heroes'] = raw_quest[2]
        quest['player'] = raw_quest[3]
        quest['startTime'] = raw_quest[4]
        quest['startBlock'] = raw_quest[5]
        quest['completeAtTime'] = raw_quest[6]
        quest['attempts'] = raw_quest[7]
        quest['type'] = parse_v2_quest_type(raw_quest[8])

    return quest


def human_readable_quest_results(quest_results, very_human=False):
    quest_rewards = {}
    rewards = quest_results['reward']
    xps = quest_results['xp']
    skill_ups = quest_results['skillUp']

    for rew in rewards:
        hero_id = rew['args']['heroId']
        item = rew['args']['rewardItem'] if 'rewardItem' in rew['args'] else rew['args']['reward']
        qty = rew['args']['itemQuantity'] if 'itemQuantity' in rew['args'] else rew['args']['amount']

        if very_human:
            if item.upper() == '0x72Cb10C6bfA5624dD07Ef608027E366bd690048F'.upper()\
                    or item.upper() == '0x4f60a160D8C2DDdaAfe16FCC57566dB84D674BD6'.upper():
                item = "JEWEL"
                qty = qty / 1e18
            elif item.upper() == '0x3a4EDcf3312f44EF027acfd8c21382a5259936e7'.upper()\
                    or item.upper() == '0x576C260513204392F0eC0bc865450872025CB1cA'.upper():
                item = "DFKGOLD"
                qty = qty / 1e3

        if hero_id not in quest_rewards:
            quest_rewards[hero_id] = {
                "rewards": {},
                "xpEarned": 0.0,
                "skillUp": 0.0
            }

        if item not in quest_rewards[hero_id]["rewards"]:
            quest_rewards[hero_id]["rewards"][item] = 0

        quest_rewards[hero_id]["rewards"][item] += qty

    for xp in xps:
        hero_id = xp['args']['heroId']
        xp_earned = xp['args']['xpEarned']

        if hero_id not in quest_rewards:
            quest_rewards[hero_id] = {
                "rewards": {},
                "xpEarned": 0.0,
                "skillUp": 0.0
            }

        quest_rewards[hero_id]["xpEarned"] += xp_earned

    for su in skill_ups:
        hero_id = su['args']['heroId']
        su_earned = su['args']['skillUp']

        if hero_id not in quest_rewards:
            quest_rewards[hero_id] = {
                "rewards": {},
                "xpEarned": 0.0,
                "skillUp": 0.0
            }

        quest_rewards[hero_id]["skillUp"] += su_earned

    return quest_rewards