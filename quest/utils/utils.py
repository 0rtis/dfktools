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
    quest['id'] = raw_quest[0]
    quest['address'] = raw_quest[1]
    quest['heroes'] = raw_quest[2]
    quest['player'] = raw_quest[3]
    quest['startTime'] = raw_quest[4]
    quest['startBlock'] = raw_quest[5]
    quest['completeAtTime'] = raw_quest[6]
    quest['attempts'] = raw_quest[7]
    quest['type'] = parse_type(raw_quest[8])

    return quest