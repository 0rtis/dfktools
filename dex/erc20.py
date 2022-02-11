from web3 import Web3


JEWEL = "0x72Cb10C6bfA5624dD07Ef608027E366bd690048F"
DFKTEAR = "0x24eA0D436d3c2602fbfEfBe6a16bBc304C963D04"
DFKAMBRTFY = "0x6e1bC01Cc52D165B357c42042cF608159A2B81c1"
DFKDRKWD = "0x68EA4640C5ce6cC0c9A1F17B7b882cB1cBEACcd7"
DFKGLDVN = "0x600541aD6Ce0a8b5dae68f086D46361534D20E80"
DFKRGWD = "0x043F9bd9Bb17dFc90dE3D416422695Dd8fa44486"
DFKRDLF = "0x094243DfABfBB3E6F71814618ace53f07362a84c"
DFKRCKRT = "0x6B10Ad6E3b99090De20bF9f95F960addC35eF3E2"
DFKSWFTHSL = "0xCdfFe898E687E941b124dfB7d24983266492eF1d"
DFKBLOATER = "0x78aED65A2Cc40C7D8B0dF1554Da60b38AD351432"
DFKIRONSCALE = "0xe4Cfee5bF05CeF3418DA74CFB89727D8E4fEE9FA"
DFKLANTERNEYE = "0x8Bf4A0888451C6b5412bCaD3D9dA3DCf5c6CA7BE"
DFKREDGILL = "0xc5891912718ccFFcC9732D1942cCD98d5934C2e1"
DFKSAILFISH = "0xb80A07e13240C31ec6dc0B5D72Af79d461dA3A70"
DFKSHIMMERSCALE = "0x372CaF681353758f985597A35266f7b330a2A44D"
DFKSILVERFIN = "0x2493cfDAcc0f9c07240B5B1C4BE08c62b8eEff69"
DFKSHVAS = "0x66F5BfD910cd83d3766c4B39d13730C911b2D286"
DFKBLUEEGG = "0x9678518e04Fe02FB30b55e2D0e554E26306d0892"
DFKGREGG = "0x95d02C1Dc58F05A015275eB49E107137D9Ee81Dc"
DFKGREENEGG = "0x6d605303e9Ac53C59A3Da1ecE36C9660c7A71da5"
PET_EGG_GOLDEN = "0x9edb3Da18be4B03857f3d39F83e5C6AAD67bc148"
PET_EGG_YELLOW = "0x3dB1fd0Ad479A46216919758144FD15A21C3e93c"
DFKBLUESTEM = "0xAC5c49Ff7E813dE1947DC74bbb1720c353079ac9"
DFKMILKWEED = "0xc0214b37FCD01511E6283Af5423CF24C96BB9808"
DFKSPIDRFRT = "0x19B9F05cdE7A61ab7aae5b0ed91aA62FF51CF881"
DFKGATONECR = "0x17f3B5240C4A71a3BBF379710f6fA66B9b51f224"  # Greater Atonement Crystal
DFKLATONECR = "0x1f3F655079b70190cb79cE5bc5AE5F19dAf2A6Cf"  # Lesser Atonement Crystal
DFKATONECR = "0x27dC6AaaD95580EdF25F8B9676f1B984e09e413d"  # Atonement Crystal
DFKSTMNPTN = "0x959ba19508827d1ed2333B1b503Bd5ab006C710e"  # Stamina Vial
DFKSWFTPTN = "0x872dD1595544CE22ad1e0174449C7ECE6F0bb01b"  # Swiftness Potion

ABI = """
        [
            {"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
            {"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"MINTER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"PAUSER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"}
        ]
        """


def wei2eth(w3, wei):
    return w3.fromWei(wei, 'ether')


def eth2wei(w3, eth):
    return w3.toWei(eth, 'ether')


def all_erc20():
    return [JEWEL, DFKTEAR, DFKAMBRTFY, DFKDRKWD, DFKGLDVN, DFKRGWD, DFKRDLF, DFKRCKRT, DFKSWFTHSL, DFKBLOATER,
            DFKIRONSCALE, DFKLANTERNEYE, DFKREDGILL, DFKSAILFISH, DFKSHIMMERSCALE, DFKSILVERFIN, DFKSHVAS, DFKBLUEEGG,
            DFKGREGG, DFKGREENEGG, PET_EGG_GOLDEN, PET_EGG_YELLOW, DFKBLUESTEM, DFKMILKWEED, DFKSPIDRFRT]


def symbol(token_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(token_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.symbol().call()


def name(token_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(token_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.name().call()


def decimals(token_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(token_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.decimals().call()


def balance_of(address, token_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(token_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.balanceOf(address).call()

    return result
