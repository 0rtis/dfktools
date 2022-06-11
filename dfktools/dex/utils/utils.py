
def swap_expected_amount1(reserve0, reserve1, amount0_wei=1):
    p = reserve0 / reserve1
    amount1_wei = amount0_wei / p
    p2 = (reserve0 + amount0_wei) / (reserve1 - amount1_wei)
    return (amount1_wei + amount0_wei / p2) / 2


def human_readable_pool_info(pool_info):
    if pool_info is None:
        return None

    human_readable = {}
    human_readable['address'] = pool_info[0]
    human_readable['allocPoint'] = pool_info[1]
    human_readable['lastRewardBlock'] = pool_info[2]
    human_readable['accGovTokenPerShare'] = pool_info[3]

    return human_readable


def human_readable_user_info(user_info):
    if user_info is None:
        return None

    human_readable = {}
    human_readable['amount'] = user_info[0]
    human_readable['rewardDebt'] = user_info[1]
    human_readable['rewardDebtAtBlock'] = user_info[2]
    human_readable['lastWithdrawBlock'] = user_info[3]
    human_readable['firstDepositBlock'] = user_info[4]
    human_readable['blockdelta'] = user_info[5]
    human_readable['lastDepositBlock'] = user_info[6]

    return human_readable
