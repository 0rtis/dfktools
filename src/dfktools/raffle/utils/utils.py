def human_readable_raffle(raffle):
    human_readable = {}
    human_readable['id'] = raffle[0]
    human_readable['raffleType'] = raffle[1]
    human_readable['startTime'] = raffle[2]
    human_readable['totalEntries'] = raffle[3]
    human_readable['endTime'] = raffle[4]
    human_readable['closedBlock'] = raffle[5]
    human_readable['winners'] = raffle[6]
    human_readable['status'] = raffle[7]

    return human_readable


def human_readable_raffle_type(raffle):
    human_readable = {}
    human_readable['id'] = raffle[0]
    human_readable['rewards'] = raffle[1]
    human_readable['rewardAmounts'] = raffle[2]
    human_readable['maxWinners'] = raffle[3]
    human_readable['duration'] = raffle[4]

    return human_readable
