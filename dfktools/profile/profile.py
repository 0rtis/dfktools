from web3 import Web3

CONTRACT_ADDRESS = '0xabD4741948374b1f5DD5Dd7599AC1f85A34cAcDD'

ABI = """
        [
            {"inputs":[],"stateMutability":"nonpayable","type":"constructor"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"profileId","type":"uint256"},{"indexed":false,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"string","name":"name","type":"string"},{"indexed":false,"internalType":"uint64","name":"created","type":"uint64"},{"indexed":false,"internalType":"uint8","name":"picId","type":"uint8"}],"name":"ProfileCreated","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"profileId","type":"uint256"},{"indexed":false,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"string","name":"name","type":"string"},{"indexed":false,"internalType":"uint64","name":"created","type":"uint64"},{"indexed":false,"internalType":"uint8","name":"picId","type":"uint8"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"ProfileUpdated","type":"event"},
            {"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"addressToIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"addresses","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"profileId","type":"uint256"},{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"changeHeroPic","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"profileId","type":"uint256"},{"internalType":"string","name":"_name","type":"string"}],"name":"changeName","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"profileId","type":"uint256"},{"internalType":"uint8","name":"_picId","type":"uint8"}],"name":"changePic","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"uint8","name":"_picId","type":"uint8"}],"name":"createProfile","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"string","name":"name","type":"string"}],"name":"getAddressByName","outputs":[{"internalType":"address","name":"profileAddress","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"profileAddress","type":"address"}],"name":"getProfileByAddress","outputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"address","name":"_owner","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"uint64","name":"_created","type":"uint64"},{"internalType":"uint8","name":"_picId","type":"uint8"},{"internalType":"uint256","name":"_heroId","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"string","name":"name","type":"string"}],"name":"getProfileByName","outputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"address","name":"_owner","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"uint64","name":"_created","type":"uint64"},{"internalType":"uint8","name":"_picId","type":"uint8"},{"internalType":"uint256","name":"_heroId","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"getProfileCount","outputs":[{"internalType":"uint256","name":"count","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"heroesNftContract","outputs":[{"internalType":"contract IHeroCore","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"string","name":"name","type":"string"}],"name":"nameTaken","outputs":[{"internalType":"bool","name":"taken","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"nameToIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"profileAddress","type":"address"}],"name":"profileExists","outputs":[{"internalType":"bool","name":"exists","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"profiles","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint64","name":"created","type":"uint64"},{"internalType":"uint8","name":"picId","type":"uint8"},{"internalType":"uint256","name":"heroId","type":"uint256"},{"internalType":"bool","name":"set","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"setHeroes","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint8","name":"_min","type":"uint8"},{"internalType":"uint8","name":"_max","type":"uint8"}],"name":"setNameLengths","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint8","name":"_max","type":"uint8"}],"name":"setPicMax","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}
        ]
        """


def get_profile(address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    contract_entry = contract.functions.getProfileByAddress(Web3.toChecksumAddress(address)).call()

    profile = {}
    profile['id'] = contract_entry[0]
    profile['address'] = str(contract_entry[1])
    profile['name'] = contract_entry[2]
    profile['creation_time'] = contract_entry[3]
    profile['pic_id'] = contract_entry[4]
    profile['hero_id'] = contract_entry[5]

    return profile
