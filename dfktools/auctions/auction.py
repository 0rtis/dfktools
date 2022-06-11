from . import auction_core


class Auction:

    def __init__(self, auction_address, rpc_address, logger):
        self.auction_address = auction_address
        self.rpc_address = rpc_address
        self.logger = logger

    def bid(self, token_id, bid_amount_wei, private_key, nonce, gas_price_gwei, tx_timeout_seconds):
        return auction_core.bid(self.auction_address, token_id, bid_amount_wei, private_key, nonce, gas_price_gwei, tx_timeout_seconds, self.rpc_address, self.logger)

    def create_auction(self, token_id, starting_price_wei, ending_price_wei, duration, winner, private_key, nonce, gas_price_gwei, tx_timeout_seconds):
        return auction_core.create_auction(self.auction_address, token_id, starting_price_wei, ending_price_wei, duration, winner, private_key, nonce, gas_price_gwei,
                                           tx_timeout_seconds, self.rpc_address, self.logger)

    def cancel_auction(self, token_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds):
        return auction_core.cancel_auction(self.auction_address, token_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, self.rpc_address, self.logger)

    def is_on_auction(self, token_id):
        return auction_core.is_on_auction(self.auction_address, token_id, self.rpc_address)

    def get_auction(self, token_id):
        return auction_core.get_auction(self.auction_address, token_id, self.rpc_address)

    def get_auctions(self, token_ids):
        return auction_core.get_auctions(self.auction_address, token_ids, self.rpc_address)

    def get_user_auctions(self, user):
        return auction_core.get_user_auctions(self.auction_address, user, self.rpc_address)

    def total_auctions(self):
        return auction_core.total_auctions(self.auction_address, self.rpc_address)

    def auctions(self, index):
        return auction_core.auctions(self.auction_address, index, self.rpc_address)
