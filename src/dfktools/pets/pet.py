from . import pet_core

class Pet:
    def __init__(self, contract_address, rpc_address, logger=None):
        self.contract_address = contract_address
        self.rpc_address = rpc_address
        self.logger = logger

    def transfer_from(self, pet_id, receiver_address, private_key, nonce, gas_price_gwei, tx_timeout_seconds):
        return pet_core.transfer_from(self.contract_address, receiver_address, pet_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, self.rpc_address, self.logger)

    def get_owner(self, pet_id):
        return pet_core.owner_of(self.contract_address, pet_id, self.rpc_address)

    def get_user_pets(self, user_address):
        return pet_core.get_user_pets_v2(self.contract_address, user_address, self.rpc_address)

    def is_approved_for_all(self, owner, operator):
        return pet_core.is_approved_for_all(self.contract_address, owner, operator, self.rpc_address)

    def get_pet(self, pet_id):
        return pet_core.get_pet_v2(self.contract_address, pet_id, self.rpc_address)

    @staticmethod
    def human_readable_pet(raw_pet):
        return pet_core.human_readable_pet(raw_pet)
