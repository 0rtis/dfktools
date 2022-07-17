def human_readable_auction(auction):
    human_readable = {}
    human_readable['seller'] = auction[0]
    human_readable['tokenId'] = auction[1]
    human_readable['startingPrice'] = auction[2]
    human_readable['endingPrice'] = auction[3]
    human_readable['duration'] = auction[4]
    human_readable['startedAt'] = auction[5]
    human_readable['winner'] = auction[6]
    human_readable['open'] = auction[7]

    return human_readable