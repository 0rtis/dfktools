FAIL_ON_NOT_FOUND = False

types = {
    1: "attemptBased",
    #2: "timeBased",
    #3: "well",
}


def parse_type(id):
    value = types.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Quest type not found")
    return value


def human_readable_quest(raw_quest):
    if raw_quest is None:
        return None

    quest = {}
    i = 0

    if len(raw_quest) == 10:  # v2
        quest['id'] = raw_quest[i]
        i = i + 1
        quest['address'] = raw_quest[i]
        i = i + 1
        quest['level'] = raw_quest[i]
        i = i + 1
        quest['heroes'] = raw_quest[i]
        i = i + 1
        quest['player'] = raw_quest[i]
        i = i + 1
        quest['startBlock'] = raw_quest[i]
        i = i + 1
        quest['startTime'] = raw_quest[i]
        i = i + 1
        quest['completeAtTime'] = raw_quest[i]
        i = i + 1
        quest['attempts'] = raw_quest[i]
        i = i + 1
        quest['type'] = parse_type(raw_quest[i])
    else:  # TODO:// v1 - remove once old quests have been migrated
        quest['id'] = raw_quest[i]
        i = i + 1
        quest['address'] = raw_quest[i]
        i = i + 1
        quest['heroes'] = raw_quest[i]
        i = i + 1
        quest['player'] = raw_quest[i]
        i = i + 1
        quest['startTime'] = raw_quest[i]
        i = i + 1
        quest['startBlock'] = raw_quest[i]
        i = i + 1
        quest['completeAtTime'] = raw_quest[i]
        i = i + 1
        quest['attempts'] = raw_quest[i]
        i = i + 1
        quest['type'] = parse_type(raw_quest[i])

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