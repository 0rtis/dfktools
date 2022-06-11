from web3 import Web3

CONTRACT_ADDRESS = '0xbabb4af8c707e2850e902f73c14c992e83cfcb57'

ABI = '''
        [
            {"constant":false,"inputs":[{"name":"_genes1","type":"uint256"},{"name":"_genes2","type":"uint256"},{"name":"_targetBlock","type":"uint256"},{"name":"_crystalId","type":"uint256"}],"name":"mixGenes","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},
            {"constant":true,"inputs":[{"name":"_traits","type":"uint8[]"}],"name":"encode","outputs":[{"name":"_genes","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},
            {"constant":true,"inputs":[{"name":"_genes","type":"uint256"}],"name":"decode","outputs":[{"name":"","type":"uint8[]"}],"payable":false,"stateMutability":"pure","type":"function"},
            {"constant":true,"inputs":[{"name":"_genes","type":"uint256"}],"name":"expressingTraits","outputs":[{"name":"","type":"uint8[12]"}],"payable":false,"stateMutability":"pure","type":"function"},
            {"constant":true,"inputs":[],"name":"isGeneScience","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},
            {"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}
         ]
        '''


def mix_genes(genes1, genes2, block_number, crystal_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.mixGenes(genes1, genes2, crystal_id, block_number).call()


def decode(genes, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.decode(genes).call()


def expressing_traits(genes, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.expressingTraits(genes).call()