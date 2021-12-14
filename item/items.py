from web3 import Web3

JEWEL = "0x72Cb10C6bfA5624dD07Ef608027E366bd690048F"
DFKTEAR = "0xf0e28E7c46F307954490fB1134c8D437e23D55fb"
DFKAMBRTFY = "0x6e1bC01Cc52D165B357c42042cF608159A2B81c1"
DFKBLOATER = "0x78aED65A2Cc40C7D8B0dF1554Da60b38AD351432"
DFKGLDVN = "0x600541aD6Ce0a8b5dae68f086D46361534D20E80"
DFKIRONSCALE = "0xe4Cfee5bF05CeF3418DA74CFB89727D8E4fEE9FA"
DFKLANTERNEYE = "0x8Bf4A0888451C6b5412bCaD3D9dA3DCf5c6CA7BE"
PET_EGG_BLUE = "0x9678518e04Fe02FB30b55e2D0e554E26306d0892"
PET_EGG_GOLDEN = "0x9edb3Da18be4B03857f3d39F83e5C6AAD67bc148"
PET_EGG_GREY = "0x95d02C1Dc58F05A015275eB49E107137D9Ee81Dc"
DFKRGWD = "0x043F9bd9Bb17dFc90dE3D416422695Dd8fa44486"
DFKREDGILL = "0xc5891912718ccFFcC9732D1942cCD98d5934C2e1"
DFKRDLF = "0x094243DfABfBB3E6F71814618ace53f07362a84c"
DFKRCKRT = "0x6B10Ad6E3b99090De20bF9f95F960addC35eF3E2"
DFKSAILFISH = "0xb80A07e13240C31ec6dc0B5D72Af79d461dA3A70"
DFKSHIMMERSCALE = "0x372CaF681353758f985597A35266f7b330a2A44D"
SHVAS_RUNE = "0x66F5BfD910cd83d3766c4B39d13730C911b2D286"
DFKSILVERFIN = "0x2493cfDAcc0f9c07240B5B1C4BE08c62b8eEff69"
DFKSWFTHSL = "0xCdfFe898E687E941b124dfB7d24983266492eF1d"


ABI = """
        [{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]
        """


def eth2gwei(eth):
    return eth * 1000000000000000000


def gwei2eth(gwei):
    return gwei / 1000000000000000000


def balance(address, token_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(token_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.balanceOf(address).call()

    return result
