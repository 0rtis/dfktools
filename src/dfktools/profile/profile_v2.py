from web3 import Web3

SERENDALE_CONTRACT_ADDRESS = '0x6391F796D56201D279a42fD3141aDa7e26A3B4A5'
CRYSTALVALE_CONTRACT_ADDRESS = '0xC4cD8C09D1A90b21Be417be91A81603B03993E81'
SERENDALE2_CONTRACT_ADDRESS = '0xe1b8C354BE50357c2ab90A962254526d08aF0D2D'

ABI = """
        [
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"string","name":"name","type":"string"},{"indexed":false,"internalType":"uint64","name":"created","type":"uint64"},{"indexed":false,"internalType":"uint256","name":"nftId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"collectionId","type":"uint256"}],"name":"ProfileCreated","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"string","name":"name","type":"string"},{"indexed":false,"internalType":"uint256","name":"nftId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"collectionId","type":"uint256"}],"name":"ProfileUpdated","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
            {"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"MAX_CHAR","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"MAX_PIC","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"MIN_CHAR","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"UPDATER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"addressToProfile","outputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint64","name":"created","type":"uint64"},{"internalType":"uint256","name":"nftId","type":"uint256"},{"internalType":"uint256","name":"collectionId","type":"uint256"},{"internalType":"string","name":"picUri","type":"string"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"string[]","name":"_uriArray","type":"string[]"}],"name":"batchSetPicURI","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"_profileAddress","type":"address"},{"internalType":"string","name":"_name","type":"string"}],"name":"changeName","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"_profileAddress","type":"address"},{"internalType":"uint256","name":"_nftId","type":"uint256"},{"internalType":"uint256","name":"_collectionId","type":"uint256"}],"name":"changePic","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"uint256","name":"_nftId","type":"uint256"},{"internalType":"uint256","name":"_collectionId","type":"uint256"}],"name":"createProfile","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"_profileAddress","type":"address"}],"name":"getProfile","outputs":[{"components":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint64","name":"created","type":"uint64"},{"internalType":"uint256","name":"nftId","type":"uint256"},{"internalType":"uint256","name":"collectionId","type":"uint256"},{"internalType":"string","name":"picUri","type":"string"}],"internalType":"struct ProfileTypes.Profile","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"_profileAddress","type":"address"}],"name":"getProfileByAddress","outputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"address","name":"_owner","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"uint64","name":"_created","type":"uint64"},{"internalType":"uint8","name":"_picId","type":"uint8"},{"internalType":"uint256","name":"_heroId","type":"uint256"},{"internalType":"uint256","name":"_points","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"string","name":"_name","type":"string"}],"name":"getProfileByName","outputs":[{"components":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint64","name":"created","type":"uint64"},{"internalType":"uint256","name":"nftId","type":"uint256"},{"internalType":"uint256","name":"collectionId","type":"uint256"},{"internalType":"string","name":"picUri","type":"string"}],"internalType":"struct ProfileTypes.Profile","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"_profileAddress","type":"address"},{"internalType":"uint256","name":"_collectionId","type":"uint256"}],"name":"getTokenUrisHeldByAddress","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"heroesNftContract","outputs":[{"internalType":"contract IHeroCore","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"identityTokenRouter","outputs":[{"internalType":"contract IIdentityTokenRouter","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"_heroCoreAddress","type":"address"},{"internalType":"address","name":"_identityTokenRouter","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"maxChar","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"maxPic","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"minChar","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"nameToAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"picUris","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"setHeroes","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"_identityTokenRouter","type":"address"}],"name":"setIdentityTokenRouter","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint8","name":"_min","type":"uint8"},{"internalType":"uint8","name":"_max","type":"uint8"}],"name":"setNameLengths","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint8","name":"_max","type":"uint8"}],"name":"setPicMax","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_picId","type":"uint256"},{"internalType":"string","name":"_picUri","type":"string"}],"name":"setPicURI","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"components":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint64","name":"created","type":"uint64"},{"internalType":"uint256","name":"nftId","type":"uint256"},{"internalType":"uint256","name":"collectionId","type":"uint256"},{"internalType":"string","name":"picUri","type":"string"}],"internalType":"struct ProfileTypes.Profile[]","name":"_profiles","type":"tuple[]"}],"name":"setProfiles","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}
        ]
        """


def get_profile(contract_address, address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    contract_entry = contract.functions.getProfileByAddress(Web3.toChecksumAddress(address)).call()

    profile = {}
    profile['id'] = contract_entry[0]
    profile['address'] = str(contract_entry[1])
    profile['name'] = contract_entry[2]
    profile['creation_time'] = contract_entry[3]
    profile['pic_id'] = contract_entry[4]
    profile['hero_id'] = contract_entry[5]
    profile['points'] = contract_entry[6]

    return profile
