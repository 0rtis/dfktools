from . import quest_core_v3


class Quest:
    def __init__(self, quest_core_contract_address, rpc_address, logger):
        self.quest_core_contract_address = quest_core_contract_address
        self.rpc_address = rpc_address
        self.logger = logger

    def start_quest(self, hero_ids, quest_type, attempts, level, quest_param, private_key, nonce, gas_price_gwei,
                    tx_timeout_seconds):
        return quest_core_v3.start_quest(self.quest_core_contract_address, hero_ids, quest_type, attempts, level, quest_param,private_key, nonce, gas_price_gwei, tx_timeout_seconds, self.rpc_address, self.logger)

    def complete_quest(self, hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds):
        return quest_core_v3.complete_quest(self.quest_core_contract_address, hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds,
                                            self.rpc_address, self.logger)

    def parse_complete_quest_receipt(self, tx_receipt):
        return quest_core_v3.parse_complete_quest_receipt(self.quest_core_contract_address, tx_receipt, self.rpc_address)

    def cancel_quest(self, hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds):
        return quest_core_v3.cancel_quest(self.quest_core_contract_address, hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds,
                                          self.rpc_address, self.logger)

    def hero_to_quest_id(self, hero_id):
        return quest_core_v3.hero_to_quest_id(self.quest_core_contract_address, hero_id, self.rpc_address)

    def is_hero_questing(self, hero_id):
        return self.hero_to_quest_id(hero_id) > 0

    def get_active_quests(self, address):
        return quest_core_v3.get_active_quests(self.quest_core_contract_address, address, self.rpc_address)

    def get_hero_quest(self, hero_id):
        return quest_core_v3.get_hero_quest(self.quest_core_contract_address, hero_id, self.rpc_address)

    def get_current_stamina(self, hero_id):
        return quest_core_v3.get_current_stamina(self.quest_core_contract_address, hero_id, self.rpc_address)