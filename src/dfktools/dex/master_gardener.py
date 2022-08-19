from web3 import Web3
from .uniswap_v2_pair import UniswapV2Pair
from .utils.utils import human_readable_user_info

SERENDALE_CONTRACT_ADDRESS = '0xDB30643c71aC9e2122cA0341ED77d09D5f99F924'
CRYSTALVALE_CONTRACT_ADDRESS = '0x57Dec9cC7f492d6583c773e2E7ad66dcDc6940Fb'


ABI = '''
    [
        {"inputs":[{"internalType":"contract JewelToken","name":"_govToken","type":"address"},{"internalType":"address","name":"_devaddr","type":"address"},{"internalType":"address","name":"_liquidityaddr","type":"address"},{"internalType":"address","name":"_comfundaddr","type":"address"},{"internalType":"address","name":"_founderaddr","type":"address"},{"internalType":"uint256","name":"_rewardPerBlock","type":"uint256"},{"internalType":"uint256","name":"_startBlock","type":"uint256"},{"internalType":"uint256","name":"_halvingAfterBlock","type":"uint256"},{"internalType":"uint256","name":"_userDepFee","type":"uint256"},{"internalType":"uint256","name":"_devDepFee","type":"uint256"},{"internalType":"uint256[]","name":"_rewardMultiplier","type":"uint256[]"},{"internalType":"uint256[]","name":"_blockDeltaStartStage","type":"uint256[]"},{"internalType":"uint256[]","name":"_blockDeltaEndStage","type":"uint256[]"},{"internalType":"uint256[]","name":"_userFeeStage","type":"uint256[]"},{"internalType":"uint256[]","name":"_devFeeStage","type":"uint256[]"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"EmergencyWithdraw","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"lockAmount","type":"uint256"}],"name":"SendGovernanceTokenReward","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw","type":"event"},
        {"inputs":[],"name":"FINISH_BONUS_AT_BLOCK","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"HALVING_AT_BLOCK","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"PERCENT_FOR_COM","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"PERCENT_FOR_DEV","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"PERCENT_FOR_FOUNDERS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"PERCENT_FOR_LP","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"PERCENT_LOCK_BONUS_REWARD","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"REWARD_MULTIPLIER","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"REWARD_PER_BLOCK","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"START_BLOCK","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_allocPoint","type":"uint256"},{"internalType":"contract IERC20","name":"_lpToken","type":"address"},{"internalType":"bool","name":"_withUpdate","type":"bool"}],"name":"add","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_toAdd","type":"address"}],"name":"addAuthorized","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"authorized","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"blockDeltaEndStage","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"blockDeltaStartStage","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_newFinish","type":"uint256"}],"name":"bonusFinishUpdate","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"claimReward","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256[]","name":"_pids","type":"uint256[]"}],"name":"claimRewards","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_newCom","type":"address"}],"name":"comUpdate","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"comfundaddr","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"address","name":"_ref","type":"address"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_devaddr","type":"address"}],"name":"dev","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"devDepFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"devFeeStage","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"devaddr","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"emergencyWithdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_newFounder","type":"address"}],"name":"founderUpdate","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"founderaddr","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getGlobalAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getGlobalRefAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_from","type":"uint256"},{"internalType":"uint256","name":"_to","type":"uint256"}],"name":"getLockPercentage","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_from","type":"uint256"},{"internalType":"uint256","name":"_to","type":"uint256"}],"name":"getMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"pid1","type":"uint256"}],"name":"getNewRewardPerBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_from","type":"uint256"},{"internalType":"uint256","name":"_to","type":"uint256"},{"internalType":"uint256","name":"_allocPoint","type":"uint256"}],"name":"getPoolReward","outputs":[{"internalType":"uint256","name":"forDev","type":"uint256"},{"internalType":"uint256","name":"forFarmer","type":"uint256"},{"internalType":"uint256","name":"forLP","type":"uint256"},{"internalType":"uint256","name":"forCom","type":"uint256"},{"internalType":"uint256","name":"forFounders","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"address","name":"_user2","type":"address"}],"name":"getRefValueOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getTotalRefs","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"govToken","outputs":[{"internalType":"contract JewelToken","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256[]","name":"_newHalving","type":"uint256[]"}],"name":"halvingUpdate","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"liquidityaddr","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256[]","name":"_newlock","type":"uint256[]"}],"name":"lockUpdate","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_newcomlock","type":"uint256"}],"name":"lockcomUpdate","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_newdevlock","type":"uint256"}],"name":"lockdevUpdate","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_newfounderlock","type":"uint256"}],"name":"lockfounderUpdate","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_newlplock","type":"uint256"}],"name":"locklpUpdate","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_newLP","type":"address"}],"name":"lpUpdate","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"massUpdatePools","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"address","name":"_user","type":"address"}],"name":"pendingReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"name":"poolExistence","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"poolId1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"poolInfo","outputs":[{"internalType":"contract IERC20","name":"lpToken","type":"address"},{"internalType":"uint256","name":"allocPoint","type":"uint256"},{"internalType":"uint256","name":"lastRewardBlock","type":"uint256"},{"internalType":"uint256","name":"accGovTokenPerShare","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"poolLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_newOwner","type":"address"}],"name":"reclaimTokenOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_toRemove","type":"address"}],"name":"removeAuthorized","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"address","name":"_user","type":"address"},{"internalType":"uint256","name":"_block","type":"uint256"}],"name":"reviseDeposit","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"address","name":"_user","type":"address"},{"internalType":"uint256","name":"_block","type":"uint256"}],"name":"reviseWithdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256[]","name":"_newMulReward","type":"uint256[]"}],"name":"rewardMulUpdate","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_newReward","type":"uint256"}],"name":"rewardUpdate","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_allocPoint","type":"uint256"},{"internalType":"bool","name":"_withUpdate","type":"bool"}],"name":"set","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_devDepFees","type":"uint256"}],"name":"setDevDepFee","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256[]","name":"_devFees","type":"uint256[]"}],"name":"setDevFeeStage","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256[]","name":"_blockEnds","type":"uint256[]"}],"name":"setStageEnds","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256[]","name":"_blockStarts","type":"uint256[]"}],"name":"setStageStarts","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_usrDepFees","type":"uint256"}],"name":"setUserDepFee","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256[]","name":"_userFees","type":"uint256[]"}],"name":"setUserFeeStage","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_newstarblock","type":"uint256"}],"name":"starblockUpdate","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"totalAllocPoint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"updatePool","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"usdOracle","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"userDelta","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"userDepFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"userFeeStage","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"userGlobalInfo","outputs":[{"internalType":"uint256","name":"globalAmount","type":"uint256"},{"internalType":"uint256","name":"totalReferals","type":"uint256"},{"internalType":"uint256","name":"globalRefAmount","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"name":"userInfo","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"rewardDebt","type":"uint256"},{"internalType":"uint256","name":"rewardDebtAtBlock","type":"uint256"},{"internalType":"uint256","name":"lastWithdrawBlock","type":"uint256"},{"internalType":"uint256","name":"firstDepositBlock","type":"uint256"},{"internalType":"uint256","name":"blockdelta","type":"uint256"},{"internalType":"uint256","name":"lastDepositBlock","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"address","name":"_ref","type":"address"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}
    ]
    '''


def pool_length(contract_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.poolLength().call()


def pool_info(contract_address, pool_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.poolInfo(pool_id).call()


def pool_id1(contract_address, pool_address, rpc_address):
    """
    Pool id indexed at 1
    :param contract_address:
    :param pool_address:
    :param rpc_address:
    :return:
    """
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.poolId1(pool_address).call()


def user_info(contract_address, pool_id, user_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.userInfo(pool_id, user_address).call()


class Garden:
    def __init__(self, garden_contract_address, uniswap_v2_pair, rpc_address, logger):
        self.garden_contract_address = garden_contract_address
        self.uniswap_v2_pair = uniswap_v2_pair
        if type(self.uniswap_v2_pair) != UniswapV2Pair:
            raise Exception("Invalid type for uniswap_v2_pair")

        if not Garden.is_garden(garden_contract_address, uniswap_v2_pair.address, rpc_address):
            raise Exception("Pair " + uniswap_v2_pair.address + " is not a garden")

        self.rpc_address = rpc_address
        self.logger = logger

        self.id_value = None

    def id(self):
        if self.id_value is None:
            self.id_value = pool_id1(self.garden_contract_address, self.uniswap_v2_pair.address, self.rpc_address) - 1
        return self.id_value

    def symbol(self):
        return self.uniswap_v2_pair.symbol()

    def token_0(self):
        return self.uniswap_v2_pair.token_0()

    def token_1(self):
        return self.uniswap_v2_pair.token_1()

    def decimals(self):
        return self.uniswap_v2_pair.decimals()

    def total_supply(self):
        return self.uniswap_v2_pair.total_supply()

    def user_info(self, address):
        return user_info(self.garden_contract_address, self.id(), address, self.rpc_address)

    def balance(self, address):
        return Garden.user_info_lp_balance(self.user_info(address))

    @staticmethod
    def is_garden(garden_contract_address, pair_address, rpc_address):
        return pool_id1(garden_contract_address, pair_address, rpc_address) > 0

    @staticmethod
    def user_info_lp_balance(user_info):
        if user_info is None:
            return None

        if type(user_info) == tuple or type(user_info) == list:
            user_info = human_readable_user_info(user_info)

        return user_info['amount']