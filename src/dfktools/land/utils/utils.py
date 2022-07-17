def human_readable_land(land):
    human_readable = {}
    human_readable['id'] = land[0]
    human_readable['name'] = land[1]
    human_readable['owner'] = land[2]
    human_readable['region'] = land[3]
    human_readable['level'] = land[4]
    human_readable['steward'] = land[5]
    human_readable['score'] = land[6]

    return human_readable
