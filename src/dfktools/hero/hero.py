from . import hero_core


class Hero:
    def __init__(self, contract_address, rpc_address, logger=None):
        self.contract_address = contract_address
        self.rpc_address = rpc_address
        self.logger = logger

    def transfer(self, hero_id, owner_private_key, owner_nonce, receiver_address, gas_price_gwei, tx_timeout_seconds):
        return hero_core.transfer(self.contract_address, hero_id, owner_private_key, owner_nonce, receiver_address, gas_price_gwei, tx_timeout_seconds, self.rpc_address, self.logger)

    def get_owner(self, hero_id, block_identifier="latest"):
        return hero_core.get_owner(self.contract_address, hero_id, self.rpc_address, block_identifier)

    def get_users_heroes(self, user_address, block_identifier="latest"):
        return hero_core.get_users_heroes(self.contract_address, user_address, self.rpc_address, block_identifier)

    def is_approved_for_all(self, owner, operator):
        return hero_core.is_approved_for_all(self.contract_address, owner, operator, self.rpc_address)

    def get_hero(self, hero_id, block_identifier="latest"):
        return hero_core.get_hero(self.contract_address, hero_id, self.rpc_address, block_identifier)

    @staticmethod
    def human_readable_hero(raw_hero, hero_male_first_names=None, hero_female_first_names=None, hero_last_names=None):
        return hero_core.human_readable_hero(raw_hero, hero_male_first_names, hero_female_first_names, hero_last_names)
