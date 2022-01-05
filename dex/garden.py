from .master_gardener import pool_id1 as master_gardener_pool_id1
from .master_gardener import user_info as master_gardener_user_info
from .pool import Pool
from .utils.utils import human_readable_user_info


class Garden(Pool):
    def __init__(self, pool_address, rpc_address, logger):
        super(Garden, self).__init__(pool_address, rpc_address, logger)

        self.id_value = None

    def id(self):
        if self.id_value is None:
            self.id_value = master_gardener_pool_id1(self.pool_address, self.rpc_address) - 1
        return self.id_value

    def user_info(self, address):
        return master_gardener_user_info(self.id(), address, self.rpc_address)

    @staticmethod
    def user_info_lp_balance(user_info):
        if user_info is None:
            return None

        if type(user_info) == tuple or type(user_info) == list:
            user_info = human_readable_user_info(user_info)

        return user_info['amount']

