from web3 import Web3

ITEMS = [
	("0x72Cb10C6bfA5624dD07Ef608027E366bd690048F", "JEWEL", "Jewel"),
	("0xA9cE83507D872C5e1273E745aBcfDa849DAA654F", "XJEWEL", "xJewel"),
	("0x3a4EDcf3312f44EF027acfd8c21382a5259936e7", "DFKGOLD", "Gold Pile"),
	("0x24eA0D436d3c2602fbfEfBe6a16bBc304C963D04", "DFKTEAR", "Gaia’s Tears"),
	("0x6e1bC01Cc52D165B357c42042cF608159A2B81c1", "DFKAMBRTFY", "Ambertaffy"),
	("0x68EA4640C5ce6cC0c9A1F17B7b882cB1cBEACcd7", "DFKDRKWD", "Darkweed"),
	("0x600541aD6Ce0a8b5dae68f086D46361534D20E80", "DFKGLDVN", "Goldvein"),
	("0x043F9bd9Bb17dFc90dE3D416422695Dd8fa44486", "DFKRGWD", "Ragweed"),
	("0x094243DfABfBB3E6F71814618ace53f07362a84c", "DFKRDLF", "Redleaf"),
	("0x6B10Ad6E3b99090De20bF9f95F960addC35eF3E2", "DFKRCKRT", "Rockroot"),
	("0xCdfFe898E687E941b124dfB7d24983266492eF1d", "DFKSWFTHSL", "Swift-Thistle"),
	("0x78aED65A2Cc40C7D8B0dF1554Da60b38AD351432", "DFKBLOATER", "Bloater"),
	("0xe4Cfee5bF05CeF3418DA74CFB89727D8E4fEE9FA", "DFKIRONSCALE", "Ironscale"),
	("0x8Bf4A0888451C6b5412bCaD3D9dA3DCf5c6CA7BE", "DFKLANTERNEYE", "Lanterneye"),
	("0xc5891912718ccFFcC9732D1942cCD98d5934C2e1", "DFKREDGILL", "Redgill"),
	("0xb80A07e13240C31ec6dc0B5D72Af79d461dA3A70", "DFKSAILFISH", "Sailfish"),
	("0x372CaF681353758f985597A35266f7b330a2A44D", "SHIMMERSKIN", "Shimmerskin"),
	("0x2493cfDAcc0f9c07240B5B1C4BE08c62b8eEff69", "DFKSILVERFIN", "Silverfin"),
	("0x66F5BfD910cd83d3766c4B39d13730C911b2D286", "DFKSHVAS", "Shvas Rune"),
	("0x9678518e04Fe02FB30b55e2D0e554E26306d0892", "DFKBLUEEGG", "Blue Pet Egg"),
	("0x95d02C1Dc58F05A015275eB49E107137D9Ee81Dc", "DFKGREGG", "Grey Pet Egg"),
	("0x6d605303e9Ac53C59A3Da1ecE36C9660c7A71da5", "DFKGREENEGG", "Green Pet Egg"),
	("0x9edb3Da18be4B03857f3d39F83e5C6AAD67bc148", "DFKGOLDEGG", "Golden Pet Egg"),
	("0x3dB1fd0Ad479A46216919758144FD15A21C3e93c", "DFKYELOWEGG", "Yellow Pet Egg"),
	("0xAC5c49Ff7E813dE1947DC74bbb1720c353079ac9", "DFKBLUESTEM", "Bluestem"),
	("0xc0214b37FCD01511E6283Af5423CF24C96BB9808", "DFKMILKWEED", "Milkweed"),
	("0x19B9F05cdE7A61ab7aae5b0ed91aA62FF51CF881", "DFKSPIDRFRT", "Spiderfruit"),
	("0x17f3B5240C4A71a3BBF379710f6fA66B9b51f224", "DFKGATONECR", "Greater Atonement Crystal"),
	("0x1f3F655079b70190cb79cE5bc5AE5F19dAf2A6Cf", "DFKLATONECR", "Lesser Atonement Crystal"),
	("0x27dC6AaaD95580EdF25F8B9676f1B984e09e413d", "DFKATONECR", "Atonement Crystal"),
	("0x959ba19508827d1ed2333B1b503Bd5ab006C710e", "DFKSTMNPTN", "Stamina Vial"),
	("0x872dD1595544CE22ad1e0174449C7ECE6F0bb01b", "DFKSWFTPTN", "Swiftness Potion"),
	("0x2789F04d22a845dC854145d3c289240517f2BcF0", "DFKHLTHPTN", "Health Vial"),
	("0x87361363A75c9A6303ce813D0B2656c34B68FF52", "DFKFHLTHPTN", "Full Health Potion"),
	("0xA1f8b0E88c51a45E152934686270DDF4E3356278", "DFKANTPSN", "Anti-poison Potion"),
	("0xFb03c364969a0bB572Ce62b8Cd616A7DDEb4c09A", "DFKTFNSPTN", "Toughness Potion"),
	("0x19b020001AB0C12Ffa93e1FDeF90c7C37C8C71ef", "DFKMNPTN", "Mana Vial"),
	("0xDc2C698aF26Ff935cD1c50Eef3a4A933C62AF18D", "DFKFMNPTN", "Full Mana Potion"),
	("0x7e120334D9AFFc0982719A4eacC045F78BF41C68", "DFKMGCRSPTN", "Magic Resistance Potion"),
	("0x1771dEc8D9A29F30d82443dE0a69e7b6824e2F53", "DFKANTBLND", "Anti-blinding Potion"),
	("0x8F655142104478724bbC72664042EA09EBbF7B38", "DFKMOKSHA", "Moksha Rune"),
	("0x45B53E55b5c0A10fdd4fE2079a562d5702F3A033", "DFKCHSCR", "Chaos Crystal"),
	("0xa509c34306AdF6168268A213Cc47D336630bf101", "DFKLCHSCR", "Lesser Chaos Crystal"),
	("0x3633F956410163A98D58D2D928B38C64A488654e", "DFKCHSST", "Chaos Stone"),
	("0x6D4f4bC32df561a35C05866051CbE9C92759Da29", "DFKLCHSST", "Lesser Chaos Stone"),
	("0xc6A58eFc320A7aFDB1cD662eaf6de10Ee17103F2", "DFKFINCR", "Finesse Crystal"),
	("0x39927A2CEE5580d63A163bc402946C7600300373", "DFKLFINCR", "Lesser Finesse Crystal"),
	("0xD0B689Cb5DE0c15792Aa456C89D64038C1F2EedC", "DFKFINST", "Finesse Stone"),
	("0xbb5614D466b77d50DdEd994892DFe6F0ACA4eEbb", "DFKLFINST", "Lesser Finesse Stone"),
	("0x603919AEB55EB13F9CDE94274fC54ab2Bd2DecE7", "DFKFRTICR", "Fortitude Crystal"),
	("0x3017609B9A59B77B708D783835B6fF94a3D9E337", "DFKLFRTICR", "Lesser Fortitude Crystal"),
	("0x17Fa96ba9d9C29e4B96d29A7e89a4E7B240E3343", "DFKFRTIST", "Fortitude Stone"),
	("0x1f57eb682377f5Ad6276b9315412920BdF9530f6", "DFKLFRTIST", "Lesser Fortitude Stone"),
	("0x6D777C64f0320d8A5b31BE0FdeB694007Fc3ed45", "DFKFRTUCR", "Fortune Crystal"),
	("0x13AF184aEA970Fe79E3BB7A1B0B156B195fB1f40", "DFKLFRTUCR", "Lesser Fortune Crystal"),
	("0x5da2EffE9857DcEcB786E13566Ff37B92e1E6862", "DFKFRTUST", "Fortune Stone"),
	("0x6D6eA1D2Dc1Df6Eaa2153f212d25Cf92d13Be628", "DFKLFRTUST", "Lesser Fortune Stone"),
	("0x117E60775584CdfA4f414E22b075F31cC9c3207C", "DFKINSCR", "Insight Crystal"),
	("0xc63b76f710e9973b8989678eb16234CfADc8D9DB", "DFKLINSCR", "Lesser Insight Crystal"),
	("0x9D71Bb9C781FC2eBdD3d6cb709438e3c71200149", "DFKINSST", "Insight Stone"),
	("0x762b98B3758d0A5Eb95B3E4A1E2914Ce0A80D99c", "DFKLINSST", "Lesser Insight Stone"),
	("0xb368f69bE6eDa74700763672AEB2Ae63f3d20AE6", "DFKMGHTCR", "Might Crystal"),
	("0xaB464901AFBc61bAC440a97Fa568aC42885Da58B", "DFKLMGHTCR", "Lesser Might Crystal"),
	("0xE7F6ea1cE7BbEbC9F2Cf080010dd938d2D8D8B1b", "DFKMGHTST", "Might Stone"),
	("0xe4E7C0c693d8A7FC159776a993495378705464A7", "DFKLMGHTST", "Lesser Might Stone"),
	("0x5d7f20e3B0f1406Bf038175218eA7e9B4838908c", "DFKSWFTCR", "Swiftness Crystal"),
	("0xf5c26F2F34E9245C3A9ea0B0e7Ea7B33E6404Da0", "DFKLSWFTCR",  "Lesser Swiftness Crystal"),
	("0x08f362517aD4119d93bBCd20825c2E4119abB495", "DFKSWFTST", "Swiftness Stone"),
	("0xd9A8abC0Ce1ADC23F1c1813986c9a9C21C9e7510", "DFKLSWFTST", "Lesser Swiftness Stone"),
	("0xBbA50bD111DC586Fd1f2B1476B6eC505800A3FD0", "DFKVGRCR", "Vigor Crystal"),
	("0x0d8403E47445DB9E316E36F476dacD5827220Bdd", "DFKLVGRCR", "Lesser Vigor Crystal"),
	("0x9df75917aC9747B4A70fa033E4b0182d85B62857", "DFKVGRST", "Vigor Stone"),
	("0xB00CbF5Cd5e7b321436C2D3d8078773522D2F073", "DFKLVGRST", "Lesser Vigor Stone"),
	("0x3619fc2386FbBC19DDC39d29A72457e758CFAD69", "DFKWITCR", "Wit Crystal"),
	("0x17ff2016c9ecCFBF4Fc4DA6EF95Fe646D2c9104F", "DFKLWITCR", "Lesser Wit Crystal"),
	("0x939Ea05C81aAC48F7C10BdB08615082B82C80c63", "DFKWITST", "Wit Stone"),
	("0x4Ff7A020ec1100D36d5C81F3D4815F2e9C704b59", "DFKLWITST", "Lesser Wit Stone")
 ]

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


def symbol2item(symbol):
    symbol = symbol.upper().strip()
    for item in ITEMS:
        if item[1] == symbol:
            return item
    return None


def symbol2address(symbol):
    symbol = symbol.upper().strip()
    for item in ITEMS:
        if item[1] == symbol:
            return item[0]
    return None


def address2item(address):
    address = address.upper().strip()
    for item in ITEMS:
        if item[0].upper() == address:
            return item
    return None


def address2symbol(address):
    address = address.upper().strip()
    for item in ITEMS:
        if item[0].upper() == address:
            return item[1]
    return None


def all_items():
    return ITEMS.copy()


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
