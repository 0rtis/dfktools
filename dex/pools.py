def id2pair(pool_id):
    pairs = {
        0: 'JEWEL-ONE',
        1: 'JEWEL-BUSD',
        2: 'JEWEL-bscBNB',
        3: '1ETH-JEWEL',
        4: 'WONE-BUSD',
        5: 'JEWEL-XYA',
        6: 'JEWEL-1USDC',
        7: '1BTC-JEWEL',
        8: 'UST-JEWEL',
        9: '1ETH-WONE',
        10: '1USDC-WONE',
        11: '1BTC-1ETH',
        12: '1SUPERBID-JEWEL',
        13: '1SUPERBID-WONE',
        14: 'JEWEL-MIS',
        15: 'JEWEL-AVAX',
        16: 'JEWEL-FTM',
        17: 'JEWEL-LUNA',
        18: 'JEWEL-WMATIC'
    }

    return pairs.get(pool_id, None)
