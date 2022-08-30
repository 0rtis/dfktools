import requests
from web3 import Web3

SERENDALE_CONTRACT_ADDRESS = '0x13a65B9F8039E2c032Bc022171Dc05B30c3f2892'
CRYSTALVALE_CONTRACT_ADDRESS = '0xc390fAA4C7f66E4D62E59C231D5beD32Ff77BEf0'


ABI = """
        [
            {"inputs":[{"internalType":"address","name":"_heroCoreAddress","type":"address"},{"internalType":"address","name":"_geneScienceAddress","type":"address"},{"internalType":"address","name":"_jewelTokenAddress","type":"address"},{"internalType":"address","name":"_gaiaTearsAddress","type":"address"},{"internalType":"address","name":"_statScienceAddress","type":"address"},{"internalType":"uint256","name":"_cut","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"auctionId","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"AuctionCancelled","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"auctionId","type":"uint256"},{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"startingPrice","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"endingPrice","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"duration","type":"uint256"},{"indexed":false,"internalType":"address","name":"winner","type":"address"}],"name":"AuctionCreated","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"auctionId","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalPrice","type":"uint256"},{"indexed":false,"internalType":"address","name":"winner","type":"address"}],"name":"AuctionSuccessful","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"crystalId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"CrystalOpen","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"crystalId","type":"uint256"},{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"summonerId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"assistantId","type":"uint256"},{"indexed":false,"internalType":"uint16","name":"generation","type":"uint16"},{"indexed":false,"internalType":"uint256","name":"createdBlock","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"summonerTears","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"assistantTears","type":"uint8"},{"indexed":false,"internalType":"address","name":"bonusItem","type":"address"}],"name":"CrystalSummoned","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
            {"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"auctionHeroCore","outputs":[{"internalType":"contract IHeroCore","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"baseCooldown","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"baseSummonFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint256","name":"_bidAmount","type":"uint256"}],"name":"bid","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"struct IHeroTypes.SummoningInfo","name":"summoningInfo","type":"tuple"},{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enum IHeroTypes.Rarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"struct IHeroTypes.HeroInfo","name":"info","type":"tuple"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enum IHeroTypes.HeroStatus","name":"status","type":"uint8"}],"internalType":"struct IHeroTypes.HeroState","name":"state","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStats","name":"stats","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStatGrowth","name":"primaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStatGrowth","name":"secondaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"}],"internalType":"struct IHeroTypes.HeroProfessions","name":"professions","type":"tuple"}],"internalType":"struct IHeroTypes.Hero","name":"_hero","type":"tuple"}],"name":"calculateSummoningCost","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"cancelAuction","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"cancelAuctionWhenPaused","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"cooldownPerGen","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"uint128","name":"_startingPrice","type":"uint128"},{"internalType":"uint128","name":"_endingPrice","type":"uint128"},{"internalType":"uint64","name":"_duration","type":"uint64"},{"internalType":"address","name":"_winner","type":"address"}],"name":"createAuction","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"crystals","outputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint256","name":"createdBlock","type":"uint256"},{"internalType":"uint256","name":"heroId","type":"uint256"},{"internalType":"uint8","name":"summonerTears","type":"uint8"},{"internalType":"uint8","name":"assistantTears","type":"uint8"},{"internalType":"address","name":"bonusItem","type":"address"},{"internalType":"uint32","name":"maxSummons","type":"uint32"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_rarityRoll","type":"uint256"},{"internalType":"uint256","name":"_rarityMod","type":"uint256"}],"name":"determineRarity","outputs":[{"internalType":"enum IHeroTypes.Rarity","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},
            {"inputs":[],"name":"enabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"randomNumber","type":"uint256"},{"internalType":"uint256","name":"digits","type":"uint256"},{"internalType":"uint256","name":"offset","type":"uint256"}],"name":"extractNumber","outputs":[{"internalType":"uint256","name":"result","type":"uint256"}],"stateMutability":"pure","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getAuction","outputs":[{"internalType":"uint256","name":"auctionId","type":"uint256"},{"internalType":"address","name":"seller","type":"address"},{"internalType":"uint256","name":"startingPrice","type":"uint256"},{"internalType":"uint256","name":"endingPrice","type":"uint256"},{"internalType":"uint256","name":"duration","type":"uint256"},{"internalType":"uint256","name":"startedAt","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_crystalId","type":"uint256"}],"name":"getCrystal","outputs":[{"components":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint256","name":"createdBlock","type":"uint256"},{"internalType":"uint256","name":"heroId","type":"uint256"},{"internalType":"uint8","name":"summonerTears","type":"uint8"},{"internalType":"uint8","name":"assistantTears","type":"uint8"},{"internalType":"address","name":"bonusItem","type":"address"},{"internalType":"uint32","name":"maxSummons","type":"uint32"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"}],"internalType":"struct ICrystalTypes.HeroCrystal","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getCurrentPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"getUserAuctions","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"getUserCrystals","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"increasePerGen","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"increasePerSummon","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"isOnAuction","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"jewelToken","outputs":[{"internalType":"contract IJewelToken","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"newSummonCooldown","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_crystalId","type":"uint256"}],"name":"open","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"ownerCut","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_crystalId","type":"uint256"}],"name":"rechargeCrystal","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address[]","name":"_feeAddresses","type":"address[]"},{"internalType":"uint256[]","name":"_feePercents","type":"uint256[]"}],"name":"setFees","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"_geneScienceAddress","type":"address"}],"name":"setGeneScienceAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"_statScienceAddress","type":"address"}],"name":"setStatScienceAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_newSummonCooldown","type":"uint256"},{"internalType":"uint256","name":"_baseCooldown","type":"uint256"},{"internalType":"uint256","name":"_cooldownPerGen","type":"uint256"}],"name":"setSummonCooldowns","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_baseSummonFee","type":"uint256"},{"internalType":"uint256","name":"_increasePerSummon","type":"uint256"},{"internalType":"uint256","name":"_increasePerGen","type":"uint256"}],"name":"setSummonFees","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"statScience","outputs":[{"internalType":"contract IStatScience","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_summonerId","type":"uint256"},{"internalType":"uint256","name":"_assistantId","type":"uint256"},{"internalType":"uint16","name":"_summonerTears","type":"uint16"},{"internalType":"uint16","name":"_assistantTears","type":"uint16"},{"internalType":"address","name":"_bonusItem","type":"address"}],"name":"summonCrystal","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"toggleEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"userAuctions","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"userCrystals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"vrf","outputs":[{"internalType":"bytes32","name":"result","type":"bytes32"}],"stateMutability":"view","type":"function"}
        ]
        """

AUCTIONS_OPEN_GRAPHQL_QUERY = """
                        query {
                          saleAuctions(skip: %d, first: %d, orderBy: startedAt, orderDirection: desc, where: {open: true, winner: null}) {
                            id
                            seller {
                                name
                            }
                            tokenId {
                              id
                              owner {
                                owner
                              }
                              statGenes
                              generation
                              rarity
                              mainClass
                              subClass
                              strength
                              intelligence
                              wisdom
                              luck
                              agility
                              vitality
                              endurance
                              dexterity
                              level
                              summons
                              maxSummons
                              summonerId {
                                id
                              }
                              assistantId {
                                id
                              }
                            }
                            startingPrice
                            endingPrice
                            startedAt
                            duration
                            winner {
                              id
                              name
                            }
                            open
                            
                          }
                          
                        }
                        """

AUCTIONS_TOKEN_IDS_GRAPHQL_QUERY = """
                        query {
                          saleAuctions(orderBy: startedAt, orderDirection: desc, where: {open: true, tokenId_in: %s }) {
                            id
                            seller {
                                name
                            }
                            tokenId {
                              id
                              owner {
                                owner
                              }
                              
                              statGenes
                              generation
                              rarity
                              mainClass
                              subClass
                              summons
                              maxSummons
                              summonerId {
                                id
                              }
                              assistantId {
                                id
                              }
                            }
                            startingPrice
                            endingPrice
                            startedAt
                            duration
                            winner {
                              id
                              name
                            }
                            open

                          }

                        }
                        """


def block_explorer_link(txid):
    return 'https://explorer.harmony.one/tx/' + str(txid)


def bid_hero(contract_address, token_id, bid_amount_wei, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger=None):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    sales_auction_contract_address = Web3.toChecksumAddress(contract_address)
    sales_auction_contract = w3.eth.contract(sales_auction_contract_address, abi=ABI)

    if logger is not None:
        logger.info("Biding " + str(wei2ether(bid_amount_wei)) + " on hero id " + str(token_id))
    tx = sales_auction_contract.functions.bid(token_id, bid_amount_wei).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    if logger is not None:
        logger.info("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    if logger is not None:
        logger.info("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    if logger is not None:
        logger.info("Transaction successfully sent !")
        logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds, poll_latency=2)

    if logger is not None:
        logger.info("Transaction mined !")
        logger.info(str(tx_receipt))

    return tx_receipt


def create_auction(contract_address, token_id, starting_price_wei, ending_price_wei, duration, winner, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger=None):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    sales_auction_contract_address = Web3.toChecksumAddress(contract_address)
    sales_auction_contract = w3.eth.contract(sales_auction_contract_address, abi=ABI)

    if logger is not None:
        logger.info("Auctioning " + str(token_id) + " (starting price=" + str(wei2ether(starting_price_wei)) + ", ending price=" + str(wei2ether(ending_price_wei)) + ", duration=" + str(duration) + ", private sale buyer=" + str(winner) + ")")
    tx = sales_auction_contract.functions.createAuction(token_id, starting_price_wei, ending_price_wei, duration, winner).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})
    if logger is not None:
        logger.info("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    if logger is not None:
        logger.info("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    if logger is not None:
        logger.info("Transaction successfully sent !")
        logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds, poll_latency=2)
    if logger is not None:
        logger.info("Transaction mined !")
        logger.info(str(tx_receipt))
    return tx_receipt


def cancel_auction(contract_address, token_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger=None):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    sales_auction_contract_address = Web3.toChecksumAddress(contract_address)
    sales_auction_contract = w3.eth.contract(sales_auction_contract_address, abi=ABI)

    tx = sales_auction_contract.functions.cancelAuction(token_id).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})
    if logger is not None:
        logger.info("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    if logger is not None:
        logger.info("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    if logger is not None:
        logger.info("Transaction successfully sent !")
        logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds, poll_latency=2)
    if logger is not None:
        logger.info("Transaction mined !")
        logger.info(str(tx_receipt))
    return tx_receipt


def is_on_auction(contract_address, token_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    sales_auction_contract_address = Web3.toChecksumAddress(contract_address)
    sales_auction_contract = w3.eth.contract(sales_auction_contract_address, abi=ABI)
    return sales_auction_contract.functions.isOnAuction(token_id).call()


def get_auction(contract_address, token_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    sales_auction_contract_address = Web3.toChecksumAddress(contract_address)
    sales_auction_contract = w3.eth.contract(sales_auction_contract_address, abi=ABI)
    result = sales_auction_contract.functions.getAuction(token_id).call()
    auction = {}
    auction['id'] = result[0]
    auction['owner'] = result[1]
    auction['startingPrice'] = result[2]
    auction['endingPrice'] = result[3]
    auction['duration'] = result[4]
    auction['startedAt'] = result[5]

    return auction


def get_open_auctions(graphql_address, skip=0, count=1000):

    r = requests.post(graphql_address, json={'query': AUCTIONS_OPEN_GRAPHQL_QUERY % (skip, count)})

    if r.status_code != 200:
        raise Exception("HTTP error " + str(r.status_code) + ": " + r.text)
    data = r.json()
    return data['data']['saleAuctions']


def get_hero_open_auctions(graphql_address, hero_ids):
    str_hero_ids = "["
    for id in hero_ids:
        str_hero_ids = str_hero_ids + "\"" + str(id) + "\", "
    str_hero_ids = str_hero_ids + "]"

    r = requests.post(graphql_address, json={'query': AUCTIONS_TOKEN_IDS_GRAPHQL_QUERY % str_hero_ids})
    if r.status_code != 200:
        raise Exception("HTTP error " + str(r.status_code) + ": " + r.text)
    data = r.json()
    return data['data']['saleAuctions']


def auction2hero(auction):
    ah = auction['tokenId']

    hero = {}
    hero['id'] = ah['id']
    hero['info'] = {}
    hero['info']['class'] = ah['mainClass'].lower()
    hero['info']['subClass'] = ah['subClass'].lower()
    hero['info']['rarity'] = ah['rarity']
    hero['info']['level'] = ah['level']
    hero['info']['statGenes'] = ah['statGenes']
    hero['info']['generation'] = ah['generation']

    hero['stats'] = {}
    hero['stats']['strength'] = ah['strength']
    hero['stats']['agility'] = ah['agility']
    hero['stats']['intelligence'] = ah['intelligence']
    hero['stats']['wisdom'] = ah['wisdom']
    hero['stats']['luck'] = ah['luck']
    hero['stats']['vitality'] = ah['vitality']
    hero['stats']['endurance'] = ah['endurance']
    hero['stats']['dexterity'] = ah['dexterity']

    hero['summoningInfo'] = {}
    hero['summoningInfo']['summonerId'] = ah['summonerId']
    hero['summoningInfo']['assistantId'] = ah['assistantId']
    hero['summoningInfo']['maxSummons'] = ah['maxSummons']
    hero['summoningInfo']['summons'] = ah['summons']

    return hero


def wei2ether(wei):
    return float(wei) / 1000000000000000000


def ether2wei(ether):
    return int(ether * 1000000000000000000)

