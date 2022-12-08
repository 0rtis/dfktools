SERENDALE_QUEST_CONTRACT_ADDRESS_V1 = '0xe4154B6E5D240507F9699C730a496790A722DF19'
CRYSTALVALE_QUEST_CONTRACT_ADDRESSES_V2 = [
    (0, 'wJEWEL-xJEWEL', '0xd3d8ff8e42C2eD51FabE4BA34080C6ac79395f24'),
    (1, 'CRYSTAL-AVAX', '0x8eDA0ceA7a90E794B33708Cc0768727A1A612f3d'),
    (2, 'CRYSTAL-wJEWEL', '0xC4839Fb9A5466878168EaE3fD58c647B71475b61'),
    (3, 'CRYSTAL-USDC', '0x6FEF23498877bC4c3940ebE121dd7D138BdA4e11'),
    (4, 'ETH-USDC', '0xdeF7cBeE7d0B62037616ee26BCAc1C8364f53476'),
    (5, 'wJEWEL-USDC', '0xaac3933Faa3B668304C9276d10CA88853463BD42'),
    (6, 'CRYSTAL-ETH', '0x810e1fF51fDd58c474c66A31013713D1A17BF458'),
    (7, 'CRYSTAL-BTC.b', '0x706916dbC3b66d89632708CC193080ea05E0534A'),
    (8, 'CRYSTAL-KLAY', '0x1fCc67a01525fd715A67bCcbF73665Fb3dBE76c7'),
    (9, 'JEWEL-KLAY', '0x2A70aA48f9dBF859239ae5E7f98fe95aE27A6CD4'),
    (10, 'JEWEL-AVAX', '0xA0d17554F09047d65E0ae0e76CD8923A9525183c'),
    (11, 'JEWEL-BTC.b', '0x3391B9384AC66C7Aa3BF4A75A4f441942B1dCf30'),
    (12, 'JEWEL-ETH', '0xbaEc39Dd81b964B57bc5fa5f5421Cd82185409E6'),
    (13, 'BTC.b-USDC', '0x045838dBfb8026520E872c8298F4Ed542B81Eaca')
]

SERENDALE2_QUEST_CONTRACT_ADDRESSES = [
    (0, 'JADE-JEWEL', '0x3837612f3A14C92Da8E0186AB398A753fe169dc1'),
    (1, 'JADE-wKLAY', '0xc1C01a860B841F47f8191026D9Ca8eE2F1f37ab3'),
    (2, 'JADE-AVAX', '0x7643ADB5AaF129A424390CB055d6e23231fFd690'),
    (3, 'JADE-oUSDT', '0x177D9F3A92630CB8C46F169b1F99a12A7a326c45'),
    (4, 'JADE-oBTC', '0x05305c97e9A2FDC0F5Ea23824c1348DEeD9Aff04'),
    (5, 'JADE-oETH', '0xb911F5D6F9129365d1a415DD3CBa17F0240CFA70'),
    (6, 'JEWEL-wKLAY', '0x3198f51A1c8cFC5f1FeaD58feaa19E6dFc8e9737'),
    (7, 'JEWEL-AVAX', '0xDAd93871e42a11aD577E4DCa02c7C426800A47D5'),
    (8, 'EWEL-oUSDT', '0x0831f733870e847263907F32B3367De2f47CeAf0'),
    (9, 'JEWEL-oBTC', '0x85106b1aF8B0337CB39a9aacDa87849B882a3170'),
    (10, 'JEWEL-oETH', '0x7038F49cAA6e2f26677D237A2A40EC6354bA1eA5')
]

def get_contract_info(contract_address, address):
    address = str(address).upper()
    for addr in contract_address:
        if addr[2].upper() == address:
            return addr
    return None


def get_pool_id_contract_address(contract_address, pool_id):
    for addr in contract_address:
        if addr[0] == pool_id:
            return addr[2]
    return None


def get_liquidity_pair_contract_address(contract_address, liquidity_pair):
    for addr in contract_address:
        if addr[1] == liquidity_pair:
            return addr[2]
    return None

def get_crystalvale_contract_info(address):
   return get_contract_info(CRYSTALVALE_QUEST_CONTRACT_ADDRESSES_V2, address)

def get_crystalvale_pool_id_contract_address(pool_id):
    return get_pool_id_contract_address(CRYSTALVALE_QUEST_CONTRACT_ADDRESSES_V2, pool_id)

def get_crystalvale_liquidity_pair_contract_address(liquidity_pair):
   return get_liquidity_pair_contract_address(CRYSTALVALE_QUEST_CONTRACT_ADDRESSES_V2, liquidity_pair)

def get_serendale2_contract_info(address):
   return get_contract_info(SERENDALE2_QUEST_CONTRACT_ADDRESSES, address)

def get_serendale2_pool_id_contract_address(pool_id):
    return get_pool_id_contract_address(SERENDALE2_QUEST_CONTRACT_ADDRESSES, pool_id)

def get_serendale2_liquidity_pair_contract_address(liquidity_pair):
   return get_liquidity_pair_contract_address(SERENDALE2_QUEST_CONTRACT_ADDRESSES, liquidity_pair)
