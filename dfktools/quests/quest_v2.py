from . import quest_core_v2


class Quest:
    def __init__(self, quest_core_contract_address, rpc_address, logger):
        self.quest_core_contract_address = quest_core_contract_address
        self.rpc_address = rpc_address
        self.logger = logger

    def start_quest(self, quest_address, hero_ids, attempts, level, private_key, nonce, gas_price_gwei,
                    tx_timeout_seconds):
        return quest_core_v2.start_quest(self.quest_core_contract_address, quest_address, hero_ids, attempts, level, private_key, nonce, gas_price_gwei,
                                         tx_timeout_seconds, self.rpc_address, self.logger)

    def complete_quest(self, hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds):
        return quest_core_v2.complete_quest(self.quest_core_contract_address, hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds,
                                            self.rpc_address, self.logger)

    def parse_complete_quest_receipt(self, tx_receipt):
        return quest_core_v2.parse_complete_quest_receipt(self.quest_core_contract_address, tx_receipt, self.rpc_address)

    def cancel_quest(self, hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds):
        return quest_core_v2.cancel_quest(self.quest_core_contract_address, hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds,
                                          self.rpc_address, self.logger)

    def hero_to_quest_id(self, hero_id):
        return quest_core_v2.hero_to_quest_id(self.quest_core_contract_address, hero_id, self.rpc_address)

    def is_hero_questing(self, hero_id):
        return self.hero_to_quest_id(hero_id) > 0

    def get_active_quest(self, address):
        return quest_core_v2.get_active_quest(self.quest_core_contract_address, address, self.rpc_address)

    def get_hero_quest(self, hero_id):
        return quest_core_v2.get_hero_quest(self.quest_core_contract_address, hero_id, self.rpc_address)

    def get_quest(self, quest_id):
        return quest_core_v2.get_quest(self.quest_core_contract_address, quest_id, self.rpc_address)

    def get_quest_data(self, quest_id):
        return quest_core_v2.get_quest_data(self.quest_core_contract_address, quest_id, self.rpc_address)

    def quest_address_to_type(self, quest_address):
        return quest_core_v2.quest_address_to_type(self.quest_core_contract_address, quest_address, self.rpc_address)

    def get_current_stamina(self, hero_id):
        return quest_core_v2.get_current_stamina(self.quest_core_contract_address, hero_id, self.rpc_address)