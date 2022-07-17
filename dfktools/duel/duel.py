from web3 import Web3
from .utils import utils as duel_utils

CONTRACT_ADDRESS = '0xE97196f4011dc9DA0829dd8E151EcFc0f37EE3c7'

ABI = """
    [{"inputs":[{"internalType":"bytes4","name":"_functionSelector","type":"bytes4"}],"name":"facetAddress","outputs":[{"internalType":"address","name":"facetAddress_","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"facetAddresses","outputs":[{"internalType":"address[]","name":"facetAddresses_","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_facet","type":"address"}],"name":"facetFunctionSelectors","outputs":[{"internalType":"bytes4[]","name":"facetFunctionSelectors_","type":"bytes4[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"facets","outputs":[{"components":[{"internalType":"address","name":"facetAddress","type":"address"},{"internalType":"bytes4[]","name":"functionSelectors","type":"bytes4[]"}],"internalType":"struct IDiamondLoupe.Facet[]","name":"facets_","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"_interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_duelId","type":"uint256"}],"name":"completeDuel","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_type","type":"uint256"},{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"},{"internalType":"uint256","name":"_jewelFee","type":"uint256"},{"internalType":"uint8","name":"_background","type":"uint8"},{"internalType":"uint8","name":"_stat","type":"uint8"}],"name":"enterDuelLobby","outputs":[],"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"duelId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player1","type":"address"},{"indexed":true,"internalType":"address","name":"player2","type":"address"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"player1","type":"address"},{"internalType":"address","name":"player2","type":"address"},{"internalType":"uint256","name":"player1DuelEntry","type":"uint256"},{"internalType":"uint256","name":"player2DuelEntry","type":"uint256"},{"internalType":"address","name":"winner","type":"address"},{"internalType":"uint256[]","name":"player1Heroes","type":"uint256[]"},{"internalType":"uint256[]","name":"player2Heroes","type":"uint256[]"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint8","name":"duelType","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct IDuelTypes.Duel","name":"duel","type":"tuple"}],"name":"DuelCompleted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"duelId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player1","type":"address"},{"indexed":true,"internalType":"address","name":"player2","type":"address"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"player1","type":"address"},{"internalType":"address","name":"player2","type":"address"},{"internalType":"uint256","name":"player1DuelEntry","type":"uint256"},{"internalType":"uint256","name":"player2DuelEntry","type":"uint256"},{"internalType":"address","name":"winner","type":"address"},{"internalType":"uint256[]","name":"player1Heroes","type":"uint256[]"},{"internalType":"uint256[]","name":"player2Heroes","type":"uint256[]"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint8","name":"duelType","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct IDuelTypes.Duel","name":"duel","type":"tuple"}],"name":"DuelCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"heroIds","type":"uint256[]"}],"name":"DuelEntryCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"duelId","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"duelEntryId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player1","type":"address"},{"indexed":false,"internalType":"address","name":"player2","type":"address"}],"name":"DuelEntryMatched","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"duelId","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"player1HeroId","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"player2HeroId","type":"uint256"},{"components":[{"internalType":"uint16","name":"turn","type":"uint16"},{"internalType":"uint256","name":"player1HeroId","type":"uint256"},{"internalType":"uint256","name":"player2HeroId","type":"uint256"},{"internalType":"uint8","name":"stat","type":"uint8"},{"internalType":"uint8","name":"background","type":"uint8"},{"components":[{"internalType":"uint8","name":"roll","type":"uint8"},{"internalType":"uint16","name":"elementBonus","type":"uint16"},{"internalType":"uint16","name":"statValue","type":"uint16"},{"internalType":"uint16","name":"backgroundBonus","type":"uint16"},{"internalType":"uint16","name":"total","type":"uint16"}],"internalType":"struct IDuelTypes.HeroTurnScore","name":"hero1Score","type":"tuple"},{"components":[{"internalType":"uint8","name":"roll","type":"uint8"},{"internalType":"uint16","name":"elementBonus","type":"uint16"},{"internalType":"uint16","name":"statValue","type":"uint16"},{"internalType":"uint16","name":"backgroundBonus","type":"uint16"},{"internalType":"uint16","name":"total","type":"uint16"}],"internalType":"struct IDuelTypes.HeroTurnScore","name":"hero2Score","type":"tuple"},{"internalType":"uint256","name":"winnerHeroId","type":"uint256"},{"internalType":"address","name":"winnerPlayer","type":"address"}],"indexed":false,"internalType":"struct IDuelTypes.TurnResult","name":"turnResult","type":"tuple"}],"name":"TurnOutcome","type":"event"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"getActiveDuels","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"player1","type":"address"},{"internalType":"address","name":"player2","type":"address"},{"internalType":"uint256","name":"player1DuelEntry","type":"uint256"},{"internalType":"uint256","name":"player2DuelEntry","type":"uint256"},{"internalType":"address","name":"winner","type":"address"},{"internalType":"uint256[]","name":"player1Heroes","type":"uint256[]"},{"internalType":"uint256[]","name":"player2Heroes","type":"uint256[]"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint8","name":"duelType","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct IDuelTypes.Duel[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_profile","type":"address"}],"name":"getChallenges","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"player1","type":"address"},{"internalType":"address","name":"player2","type":"address"},{"internalType":"uint256","name":"player1DuelEntry","type":"uint256"},{"internalType":"uint256","name":"player2DuelEntry","type":"uint256"},{"internalType":"address","name":"winner","type":"address"},{"internalType":"uint256[]","name":"player1Heroes","type":"uint256[]"},{"internalType":"uint256[]","name":"player2Heroes","type":"uint256[]"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint8","name":"duelType","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct IDuelTypes.Duel[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getDuel","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"player1","type":"address"},{"internalType":"address","name":"player2","type":"address"},{"internalType":"uint256","name":"player1DuelEntry","type":"uint256"},{"internalType":"uint256","name":"player2DuelEntry","type":"uint256"},{"internalType":"address","name":"winner","type":"address"},{"internalType":"uint256[]","name":"player1Heroes","type":"uint256[]"},{"internalType":"uint256[]","name":"player2Heroes","type":"uint256[]"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint8","name":"duelType","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct IDuelTypes.Duel","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getDuelEntry","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"score","type":"uint256"},{"internalType":"uint256","name":"scoreAfter","type":"uint256"},{"internalType":"uint256","name":"jewelFee","type":"uint256"},{"internalType":"uint256","name":"duelId","type":"uint256"},{"internalType":"uint256","name":"custom1","type":"uint256"},{"internalType":"uint256","name":"custom2","type":"uint256"},{"internalType":"uint8","name":"duelType","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct IDuelTypes.DuelEntry","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_profile","type":"address"}],"name":"getDuelHistory","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"player1","type":"address"},{"internalType":"address","name":"player2","type":"address"},{"internalType":"uint256","name":"player1DuelEntry","type":"uint256"},{"internalType":"uint256","name":"player2DuelEntry","type":"uint256"},{"internalType":"address","name":"winner","type":"address"},{"internalType":"uint256[]","name":"player1Heroes","type":"uint256[]"},{"internalType":"uint256[]","name":"player2Heroes","type":"uint256[]"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint8","name":"duelType","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct IDuelTypes.Duel[100]","name":"","type":"tuple[100]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_duelId","type":"uint256"}],"name":"getDuelIndexP1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getDuelRewards","outputs":[{"components":[{"internalType":"address","name":"item","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"qty","type":"uint256"}],"internalType":"struct IDuelTypes.DuelReward[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getDuelTurns","outputs":[{"components":[{"internalType":"uint16","name":"turn","type":"uint16"},{"internalType":"uint256","name":"player1HeroId","type":"uint256"},{"internalType":"uint256","name":"player2HeroId","type":"uint256"},{"internalType":"uint8","name":"stat","type":"uint8"},{"internalType":"uint8","name":"background","type":"uint8"},{"components":[{"internalType":"uint8","name":"roll","type":"uint8"},{"internalType":"uint16","name":"elementBonus","type":"uint16"},{"internalType":"uint16","name":"statValue","type":"uint16"},{"internalType":"uint16","name":"backgroundBonus","type":"uint16"},{"internalType":"uint16","name":"total","type":"uint16"}],"internalType":"struct IDuelTypes.HeroTurnScore","name":"hero1Score","type":"tuple"},{"components":[{"internalType":"uint8","name":"roll","type":"uint8"},{"internalType":"uint16","name":"elementBonus","type":"uint16"},{"internalType":"uint16","name":"statValue","type":"uint16"},{"internalType":"uint16","name":"backgroundBonus","type":"uint16"},{"internalType":"uint16","name":"total","type":"uint16"}],"internalType":"struct IDuelTypes.HeroTurnScore","name":"hero2Score","type":"tuple"},{"internalType":"uint256","name":"winnerHeroId","type":"uint256"},{"internalType":"address","name":"winnerPlayer","type":"address"}],"internalType":"struct IDuelTypes.TurnResult[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"getHeroDuel","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"player1","type":"address"},{"internalType":"address","name":"player2","type":"address"},{"internalType":"uint256","name":"player1DuelEntry","type":"uint256"},{"internalType":"uint256","name":"player2DuelEntry","type":"uint256"},{"internalType":"address","name":"winner","type":"address"},{"internalType":"uint256[]","name":"player1Heroes","type":"uint256[]"},{"internalType":"uint256[]","name":"player2Heroes","type":"uint256[]"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint8","name":"duelType","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct IDuelTypes.Duel","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getHighestScore","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_profile","type":"address"}],"name":"getPlayerDuelEntries","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"score","type":"uint256"},{"internalType":"uint256","name":"scoreAfter","type":"uint256"},{"internalType":"uint256","name":"jewelFee","type":"uint256"},{"internalType":"uint256","name":"duelId","type":"uint256"},{"internalType":"uint256","name":"custom1","type":"uint256"},{"internalType":"uint256","name":"custom2","type":"uint256"},{"internalType":"uint8","name":"duelType","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct IDuelTypes.DuelEntry[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_profile","type":"address"}],"name":"getPlayerScore","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_type","type":"uint256"},{"internalType":"uint8","name":"_rank","type":"uint8"}],"name":"getPracticeEntry","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"score","type":"uint256"},{"internalType":"uint256","name":"scoreAfter","type":"uint256"},{"internalType":"uint256","name":"jewelFee","type":"uint256"},{"internalType":"uint256","name":"duelId","type":"uint256"},{"internalType":"uint256","name":"custom1","type":"uint256"},{"internalType":"uint256","name":"custom2","type":"uint256"},{"internalType":"uint8","name":"duelType","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct IDuelTypes.DuelEntry","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalDuelEntries","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalDuels","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_lobby","type":"uint256"}],"name":"getTotalOpenDuelEntries","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_profile","type":"address"}],"name":"getTotalPlayerDuels","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_profile","type":"address"}],"name":"getTotalPlayerWins","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"struct IHeroTypes.SummoningInfo","name":"summoningInfo","type":"tuple"},{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enum IHeroTypes.Rarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"struct IHeroTypes.HeroInfo","name":"info","type":"tuple"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enum IHeroTypes.HeroStatus","name":"status","type":"uint8"}],"internalType":"struct IHeroTypes.HeroState","name":"state","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStats","name":"stats","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStatGrowth","name":"primaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStatGrowth","name":"secondaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"}],"internalType":"struct IHeroTypes.HeroProfessions","name":"professions","type":"tuple"}],"internalType":"struct IHeroTypes.Hero","name":"_hero","type":"tuple"}],"name":"_heroMMScore","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"struct IHeroTypes.SummoningInfo","name":"summoningInfo","type":"tuple"},{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enum IHeroTypes.Rarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"struct IHeroTypes.HeroInfo","name":"info","type":"tuple"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enum IHeroTypes.HeroStatus","name":"status","type":"uint8"}],"internalType":"struct IHeroTypes.HeroState","name":"state","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStats","name":"stats","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStatGrowth","name":"primaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStatGrowth","name":"secondaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"}],"internalType":"struct IHeroTypes.HeroProfessions","name":"professions","type":"tuple"}],"internalType":"struct IHeroTypes.Hero[]","name":"_heroes","type":"tuple[]"}],"name":"_partyMMScore","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_lobby","type":"uint256"}],"name":"matchMake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_duelId","type":"uint256"},{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"},{"internalType":"uint8","name":"_background","type":"uint8"},{"internalType":"uint8","name":"_stat","type":"uint8"}],"name":"acceptChallenge","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_type","type":"uint256"},{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"},{"internalType":"uint8","name":"_rank","type":"uint8"},{"internalType":"uint8","name":"_background","type":"uint8"},{"internalType":"uint8","name":"_stat","type":"uint8"}],"name":"startPracticeDuel","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_type","type":"uint256"},{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"},{"internalType":"address","name":"_opponent","type":"address"},{"internalType":"uint8","name":"_background","type":"uint8"},{"internalType":"uint8","name":"_stat","type":"uint8"}],"name":"startPrivateDuel","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_heroCoreAddress","type":"address"},{"internalType":"address","name":"_statScienceAddress","type":"address"},{"internalType":"address","name":"_duelRaffleTicket","type":"address"},{"internalType":"address","name":"_dfkGold","type":"address"},{"internalType":"address","name":"_jewelToken","type":"address"},{"internalType":"address","name":"_goldPot","type":"address"}],"name":"init","outputs":[],"stateMutability":"nonpayable","type":"function"}]
    """


def block_explorer_link(txid):
    return 'https://explorer.harmony.one/tx/' + str(txid)


def get_duel(duel_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    contract_entry = contract.functions.getDuel(duel_id).call()

    duel = {}
    duel['id'] = contract_entry[0]
    duel['player1'] = str(contract_entry[1])
    duel['player2'] = str(contract_entry[2])
    duel['player1DuelEntry'] = contract_entry[3]
    duel['player2DuelEntry'] = contract_entry[4]
    duel['winner'] = str(contract_entry[5])
    duel['player1Heroes'] = contract_entry[6]
    duel['player2Heroes'] = contract_entry[7]
    duel['startBlock'] = contract_entry[8]
    duel['duelType'] = contract_entry[9]
    duel['status'] = contract_entry[10]

    return duel


def get_duel_entry(duel_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    contract_entry = contract.functions.getDuelEntry(duel_id).call()

    duel = {}
    duel['id'] = contract_entry[0]
    duel['player'] = str(contract_entry[1])
    duel['heroes'] = contract_entry[2]
    duel['startBlock'] = contract_entry[3]
    duel['score'] = contract_entry[4]
    duel['scoreAfter'] = contract_entry[5]
    duel['jewelFee'] = contract_entry[6]
    duel['duelId'] = contract_entry[7]
    duel['custom1'] = contract_entry[8]
    duel['custom2'] = contract_entry[9]
    duel['duelType'] = contract_entry[10]
    duel['status'] = contract_entry[11]

    return duel


def get_duel_history(address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    contract_entry = contract.functions.getDuelHistory(Web3.toChecksumAddress(address)).call()

    duels = []

    for item in contract_entry:
        duel = {}
        if item[0] == 0:
            continue
        duel['id'] = item[0]
        duel['player1'] = str(item[1])
        duel['player2'] = str(item[2])
        duel['player1DuelEntry'] = item[3]
        duel['player2DuelEntry'] = item[4]
        duel['winner'] = str(item[5])
        duel['player1Heroes'] = item[6]
        duel['player2Heroes'] = item[7]
        duel['startBlock'] = item[8]
        duel['duelType'] = item[9]
        duel['status'] = item[10]

        duels.append(duel)

    return duels


def get_active_duels(address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    contract_entry = contract.functions.getActiveDuels(Web3.toChecksumAddress(address)).call()

    duels = []

    for item in contract_entry:
        duel = {}
        if item[0] == 0:
            continue
        duel['id'] = item[0]
        duel['player1'] = str(item[1])
        duel['player2'] = str(item[2])
        duel['player1DuelEntry'] = item[3]
        duel['player2DuelEntry'] = item[4]
        duel['winner'] = str(item[5])
        duel['player1Heroes'] = item[6]
        duel['player2Heroes'] = item[7]
        duel['startBlock'] = item[8]
        duel['duelType'] = item[9]
        duel['status'] = item[10]

        duels.append(duel)

    return duels


def get_challenges(address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    contract_entry = contract.functions.getChallenges(Web3.toChecksumAddress(address)).call()

    duels = []

    for item in contract_entry:
        duel = {}
        if item[0] == 0:
            continue
        duel['id'] = item[0]
        duel['player1'] = str(item[1])
        duel['player2'] = str(item[2])
        duel['player1DuelEntry'] = item[3]
        duel['player2DuelEntry'] = item[4]
        duel['winner'] = str(item[5])
        duel['player1Heroes'] = item[6]
        duel['player2Heroes'] = item[7]
        duel['startBlock'] = item[8]
        duel['duelType'] = item[9]
        duel['status'] = item[10]

        duels.append(duel)

    return duels


def get_duel_index_p1(duel_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getDuelIndexP1(duel_id).call()


def get_duel_turns(duel_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    contract_entry = contract.functions.getDuelTurns(duel_id).call()

    duels = []

    for item in contract_entry:
        duel = {}
        duel['turn'] = item[0]
        duel['player1HeroId'] = item[1]
        duel['player2HeroId'] = item[2]
        duel['stat'] = item[3]
        duel['background'] = item[4]

        hero1Score = {}
        hero1Score['roll'] = item[5][0]
        hero1Score['elementBonus'] = item[5][1]
        hero1Score['statValue'] = item[5][2]
        hero1Score['backgroundBonus'] = item[5][3]
        hero1Score['total'] = item[5][4]
        duel['hero1Score'] = hero1Score

        hero2Score = {}
        hero2Score['roll'] = item[6][0]
        hero2Score['elementBonus'] = item[6][1]
        hero2Score['statValue'] = item[6][2]
        hero2Score['backgroundBonus'] = item[6][3]
        hero2Score['total'] = item[6][4]
        duel['hero2Score'] = hero2Score

        duel['winnerHeroId'] = item[7]
        duel['winnerPlayer'] = str(item[8])

        duels.append(duel)

    return duels


def get_hero_duel(hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    contract_entry = contract.functions.getHeroDuel(hero_id).call()

    duel = {}
    duel['id'] = contract_entry[0]
    duel['player1'] = str(contract_entry[1])
    duel['player2'] = str(contract_entry[2])
    duel['player1DuelEntry'] = contract_entry[3]
    duel['player2DuelEntry'] = contract_entry[4]
    duel['winner'] = str(contract_entry[5])
    duel['player1Heroes'] = contract_entry[6]
    duel['player2Heroes'] = contract_entry[7]
    duel['startBlock'] = contract_entry[8]
    duel['duelType'] = contract_entry[9]
    duel['status'] = contract_entry[10]

    return duel


def get_highest_score(rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getHighestScore().call()


def get_player_score(address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getPlayerScore(Web3.toChecksumAddress(address)).call()


def get_total_duel_entries(rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getTotalDuelEntries().call()


def get_total_duels(rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getTotalDuels().call()


def get_total_open_duel_entries(lobby_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getTotalOpenDuelEntries(lobby_id).call()


def get_total_player_duels(address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getTotalPlayerDuels(Web3.toChecksumAddress(address)).call()


def get_total_player_wins(address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    return contract.functions.getTotalPlayerWins(Web3.toChecksumAddress(address)).call()


def start_private_duel(duel_type, hero_ids, opponent, background, stat, private_key, nonce, gas_price_gwei,
                       tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.startPrivateDuel(duel_utils.string2id('type', duel_type), hero_ids, opponent,
                                             duel_utils.string2id('background', background),
                                             duel_utils.string2id('stat', stat)
                                             ).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def enter_duel_lobby(duel_type, hero_ids, jewel_fee, background, stat, private_key, nonce, gas_price_gwei,
                     tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.enterDuelLobby(duel_utils.string2id('type', duel_type), hero_ids,
                                           w3.toWei(jewel_fee, 'ether'),
                                           duel_utils.string2id('background', background),
                                           duel_utils.string2id('stat', stat)
                                           ).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def complete_duel(duel_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.completeDuel(duel_id).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def accept_challenge(duel_id, hero_ids, background, stat, private_key, nonce, gas_price_gwei, tx_timeout_seconds,
                     rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.acceptChallenge(duel_id, hero_ids, duel_utils.string2id('background', background),
                                            duel_utils.string2id('stat', stat)
                                            ).buildTransaction(
        {'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt
