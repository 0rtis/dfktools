import copy
from web3 import Web3
from .utils import utils as hero_utils

SERENDALE_CONTRACT_ADDRESS = '0x5F753dcDf9b1AD9AabC1346614D1f4746fd6Ce5C'
CRYSTALVALE_CONTRACT_ADDRESS = '0xEb9B61B145D6489Be575D3603F4a704810e143dF'
SERENDALE2_CONTRACT_ADDRESS = '0x268CC8248FFB72Cd5F3e73A9a20Fa2FF40EfbA61'


ABI = """
           [
                {"anonymous":false,"inputs":[{"components":[{"internalType":"address","name":"facetAddress","type":"address"},{"internalType":"enumIDiamondCut.FacetCutAction","name":"action","type":"uint8"},{"internalType":"bytes4[]","name":"functionSelectors","type":"bytes4[]"}],"indexed":false,"internalType":"structIDiamondCut.FacetCut[]","name":"_diamondCut","type":"tuple[]"},{"indexed":false,"internalType":"address","name":"_init","type":"address"},{"indexed":false,"internalType":"bytes","name":"_calldata","type":"bytes"}],"name":"DiamondCut","type":"event"},
                {"inputs":[{"components":[{"internalType":"address","name":"facetAddress","type":"address"},{"internalType":"enumIDiamondCut.FacetCutAction","name":"action","type":"uint8"},{"internalType":"bytes4[]","name":"functionSelectors","type":"bytes4[]"}],"internalType":"structIDiamondCut.FacetCut[]","name":"_diamondCut","type":"tuple[]"},{"internalType":"address","name":"_init","type":"address"},{"internalType":"bytes","name":"_calldata","type":"bytes"}],"name":"diamondCut","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"bytes4","name":"_functionSelector","type":"bytes4"}],"name":"facetAddress","outputs":[{"internalType":"address","name":"facetAddress_","type":"address"}],"stateMutability":"view","type":"function"},
                {"inputs":[],"name":"facetAddresses","outputs":[{"internalType":"address[]","name":"facetAddresses_","type":"address[]"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"address","name":"_facet","type":"address"}],"name":"facetFunctionSelectors","outputs":[{"internalType":"bytes4[]","name":"facetFunctionSelectors_","type":"bytes4[]"}],"stateMutability":"view","type":"function"},
                {"inputs":[],"name":"facets","outputs":[{"components":[{"internalType":"address","name":"facetAddress","type":"address"},{"internalType":"bytes4[]","name":"functionSelectors","type":"bytes4[]"}],"internalType":"structIDiamondLoupe.Facet[]","name":"facets_","type":"tuple[]"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"bytes4","name":"_interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},
                {"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"owner_","type":"address"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"address","name":"_newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"summonerId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"assistantId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"statGenes","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"visualGenes","type":"uint256"}],"name":"HeroDarkSummoned","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"address","name":"quest","type":"address"}],"name":"HeroQuestUpdated","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"staminaFullAt","type":"uint256"}],"name":"HeroStaminaFullAtUpdated","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enumHeroStatus","name":"status","type":"uint8"}],"indexed":false,"internalType":"structHeroState","name":"heroState","type":"tuple"}],"name":"HeroStateUpdated","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"summonerId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"assistantId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"statGenes","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"visualGenes","type":"uint256"}],"name":"HeroSummoned","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"structSummoningInfo","name":"summoningInfo","type":"tuple"},{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enumRarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"structHeroInfo","name":"info","type":"tuple"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enumHeroStatus","name":"status","type":"uint8"}],"internalType":"structHeroState","name":"state","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"structHeroStats","name":"stats","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"primaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"secondaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"}],"internalType":"structHeroProfessions","name":"professions","type":"tuple"}],"indexed":false,"internalType":"structHero","name":"hero","type":"tuple"}],"name":"HeroUpdated","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"structSummoningInfo","name":"summoningInfo","type":"tuple"},{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enumRarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"structHeroInfo","name":"info","type":"tuple"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enumHeroStatus","name":"status","type":"uint8"}],"internalType":"structHeroState","name":"state","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"structHeroStats","name":"stats","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"primaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"secondaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"},{"internalType":"uint16","name":"craft1","type":"uint16"},{"internalType":"uint16","name":"craft2","type":"uint16"}],"internalType":"structHeroProfessionsV2","name":"professions","type":"tuple"},{"components":[{"internalType":"uint256","name":"equippedSlots","type":"uint256"},{"internalType":"uint256","name":"petId","type":"uint256"},{"internalType":"uint256","name":"weapon1Id","type":"uint256"},{"internalType":"uint256","name":"weapon2Id","type":"uint256"},{"internalType":"uint256","name":"offhand1Id","type":"uint256"},{"internalType":"uint256","name":"offhand2Id","type":"uint256"},{"internalType":"uint256","name":"armorId","type":"uint256"},{"internalType":"uint256","name":"accessoryId","type":"uint256"}],"internalType":"structHeroEquipment","name":"equipment","type":"tuple"}],"indexed":false,"internalType":"structHeroV2","name":"hero","type":"tuple"}],"name":"HeroUpdatedV2","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
                {"inputs":[],"name":"BRIDGE_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
                {"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
                {"inputs":[],"name":"HERO_MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
                {"inputs":[],"name":"MINTER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
                {"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"address","name":"_to","type":"address"}],"name":"bridgeMint","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"heroes","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"structSummoningInfo","name":"summoningInfo","type":"tuple"},{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enumRarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"structHeroInfo","name":"info","type":"tuple"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enumHeroStatus","name":"status","type":"uint8"}],"internalType":"structHeroState","name":"state","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"structHeroStats","name":"stats","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"primaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"secondaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"},{"internalType":"uint16","name":"craft1","type":"uint16"},{"internalType":"uint16","name":"craft2","type":"uint16"}],"internalType":"structHeroProfessionsV2","name":"professions","type":"tuple"},{"components":[{"internalType":"uint256","name":"equippedSlots","type":"uint256"},{"internalType":"uint256","name":"petId","type":"uint256"},{"internalType":"uint256","name":"weapon1Id","type":"uint256"},{"internalType":"uint256","name":"weapon2Id","type":"uint256"},{"internalType":"uint256","name":"offhand1Id","type":"uint256"},{"internalType":"uint256","name":"offhand2Id","type":"uint256"},{"internalType":"uint256","name":"armorId","type":"uint256"},{"internalType":"uint256","name":"accessoryId","type":"uint256"}],"internalType":"structHeroEquipment","name":"equipment","type":"tuple"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
                {"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
                {"inputs":[],"name":"nextHeroId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
                {"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
                {"inputs":[],"name":"petCoreAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"setPetCoreAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
                {"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"equipmentId","type":"uint256"},{"indexed":false,"internalType":"enumHeroEquipmentSlot","name":"slot","type":"uint8"}],"name":"EquipmentChanged","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"equippedSlots","type":"uint256"},{"internalType":"uint256","name":"petId","type":"uint256"},{"internalType":"uint256","name":"weapon1Id","type":"uint256"},{"internalType":"uint256","name":"weapon2Id","type":"uint256"},{"internalType":"uint256","name":"offhand1Id","type":"uint256"},{"internalType":"uint256","name":"offhand2Id","type":"uint256"},{"internalType":"uint256","name":"armorId","type":"uint256"},{"internalType":"uint256","name":"accessoryId","type":"uint256"}],"indexed":false,"internalType":"structHeroEquipment","name":"equipment","type":"tuple"}],"name":"HeroEquipmentSet","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"petId","type":"uint256"}],"name":"PetEquipped","type":"event"},
                {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"petId","type":"uint256"}],"name":"PetUnequipped","type":"event"},
                {"inputs":[{"components":[{"internalType":"uint256","name":"heroId","type":"uint256"},{"internalType":"uint256","name":"equipmentId","type":"uint256"},{"internalType":"enumHeroEquipmentSlot","name":"slot","type":"uint8"}],"internalType":"structHeroChangeEquipmentInput","name":"_input","type":"tuple"}],"name":"changeEquipment","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"components":[{"internalType":"uint256","name":"heroId","type":"uint256"},{"internalType":"uint256","name":"equipmentId","type":"uint256"},{"internalType":"enumHeroEquipmentSlot","name":"slot","type":"uint8"}],"internalType":"structHeroChangeEquipmentInput","name":"_input","type":"tuple"},{"internalType":"address","name":"_account","type":"address"}],"name":"changeEquipmentOnBehalf","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"components":[{"internalType":"uint256","name":"heroId","type":"uint256"},{"internalType":"uint256","name":"equipmentId","type":"uint256"},{"internalType":"enumHeroEquipmentSlot","name":"slot","type":"uint8"}],"internalType":"structHeroChangeEquipmentInput[]","name":"_inputs","type":"tuple[]"}],"name":"multiChangeEquipment","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_newOwner","type":"address"},{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"transferHeroAndEquipmentFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"},{"internalType":"address","name":"_account","type":"address"}],"name":"unequipEverythingOnBehalf","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"equippedSlots","type":"uint256"},{"internalType":"uint256","name":"petId","type":"uint256"},{"internalType":"uint256","name":"weapon1Id","type":"uint256"},{"internalType":"uint256","name":"weapon2Id","type":"uint256"},{"internalType":"uint256","name":"offhand1Id","type":"uint256"},{"internalType":"uint256","name":"offhand2Id","type":"uint256"},{"internalType":"uint256","name":"armorId","type":"uint256"},{"internalType":"uint256","name":"accessoryId","type":"uint256"}],"internalType":"structHeroEquipment","name":"_heroEquipment","type":"tuple"}],"name":"updateHeroEquipment","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getHeroEquipment","outputs":[{"components":[{"internalType":"uint256","name":"equippedSlots","type":"uint256"},{"internalType":"uint256","name":"petId","type":"uint256"},{"internalType":"uint256","name":"weapon1Id","type":"uint256"},{"internalType":"uint256","name":"weapon2Id","type":"uint256"},{"internalType":"uint256","name":"offhand1Id","type":"uint256"},{"internalType":"uint256","name":"offhand2Id","type":"uint256"},{"internalType":"uint256","name":"armorId","type":"uint256"},{"internalType":"uint256","name":"accessoryId","type":"uint256"}],"internalType":"structHeroEquipment","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getHeroInfo","outputs":[{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enumRarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"structHeroInfo","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getHeroPrimaryStatGrowth","outputs":[{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getHeroProfessionsV2","outputs":[{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"},{"internalType":"uint16","name":"craft1","type":"uint16"},{"internalType":"uint16","name":"craft2","type":"uint16"}],"internalType":"structHeroProfessionsV2","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getHeroSecondaryStatGrowth","outputs":[{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getHeroState","outputs":[{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enumHeroStatus","name":"status","type":"uint8"}],"internalType":"structHeroState","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getHeroStats","outputs":[{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"structHeroStats","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getHeroSummoningInfo","outputs":[{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"structSummoningInfo","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getHeroV2","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"structSummoningInfo","name":"summoningInfo","type":"tuple"},{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enumRarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"structHeroInfo","name":"info","type":"tuple"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enumHeroStatus","name":"status","type":"uint8"}],"internalType":"structHeroState","name":"state","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"structHeroStats","name":"stats","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"primaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"secondaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"},{"internalType":"uint16","name":"craft1","type":"uint16"},{"internalType":"uint16","name":"craft2","type":"uint16"}],"internalType":"structHeroProfessionsV2","name":"professions","type":"tuple"},{"components":[{"internalType":"uint256","name":"equippedSlots","type":"uint256"},{"internalType":"uint256","name":"petId","type":"uint256"},{"internalType":"uint256","name":"weapon1Id","type":"uint256"},{"internalType":"uint256","name":"weapon2Id","type":"uint256"},{"internalType":"uint256","name":"offhand1Id","type":"uint256"},{"internalType":"uint256","name":"offhand2Id","type":"uint256"},{"internalType":"uint256","name":"armorId","type":"uint256"},{"internalType":"uint256","name":"accessoryId","type":"uint256"}],"internalType":"structHeroEquipment","name":"equipment","type":"tuple"}],"internalType":"structHeroV2","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"getUserHeroes","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getHero","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"structSummoningInfo","name":"summoningInfo","type":"tuple"},{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enumRarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"structHeroInfo","name":"info","type":"tuple"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enumHeroStatus","name":"status","type":"uint8"}],"internalType":"structHeroState","name":"state","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"structHeroStats","name":"stats","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"primaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"secondaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"}],"internalType":"structHeroProfessions","name":"professions","type":"tuple"}],"internalType":"structHero","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
                {"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"structSummoningInfo","name":"summoningInfo","type":"tuple"},{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enumRarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"structHeroInfo","name":"info","type":"tuple"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enumHeroStatus","name":"status","type":"uint8"}],"internalType":"structHeroState","name":"state","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"structHeroStats","name":"stats","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"primaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"secondaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"}],"internalType":"structHeroProfessions","name":"professions","type":"tuple"}],"internalType":"structHero","name":"_hero","type":"tuple"}],"name":"updateHero","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_statGenes","type":"uint256"},{"internalType":"uint256","name":"_visualGenes","type":"uint256"},{"internalType":"enumRarity","name":"_rarity","type":"uint8"},{"internalType":"bool","name":"_shiny","type":"bool"},{"components":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint256","name":"createdBlock","type":"uint256"},{"internalType":"uint256","name":"heroId","type":"uint256"},{"internalType":"uint8","name":"summonerTears","type":"uint8"},{"internalType":"uint8","name":"assistantTears","type":"uint8"},{"internalType":"address","name":"enhancementStone","type":"address"},{"internalType":"uint32","name":"maxSummons","type":"uint32"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"bool","name":"darkSummoned","type":"bool"},{"internalType":"uint8","name":"rarityBonusCharges","type":"uint8"}],"internalType":"structHeroCrystal","name":"_crystal","type":"tuple"},{"internalType":"uint256","name":"_crystalId","type":"uint256"}],"name":"createHero","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"},{"internalType":"address","name":"_quest","type":"address"},{"internalType":"address","name":"_owner","type":"address"}],"name":"updateHeroQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"},{"internalType":"uint256","name":"_staminaFullAt","type":"uint256"},{"internalType":"address","name":"_owner","type":"address"}],"name":"updateHeroStaminaFullAt","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enumHeroStatus","name":"status","type":"uint8"}],"internalType":"structHeroState","name":"_heroState","type":"tuple"}],"name":"updateHeroState","outputs":[],"stateMutability":"nonpayable","type":"function"},
                {"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"structSummoningInfo","name":"summoningInfo","type":"tuple"},{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enumRarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"structHeroInfo","name":"info","type":"tuple"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enumHeroStatus","name":"status","type":"uint8"}],"internalType":"structHeroState","name":"state","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"structHeroStats","name":"stats","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"primaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"structHeroStatGrowth","name":"secondaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"},{"internalType":"uint16","name":"craft1","type":"uint16"},{"internalType":"uint16","name":"craft2","type":"uint16"}],"internalType":"structHeroProfessionsV2","name":"professions","type":"tuple"},{"components":[{"internalType":"uint256","name":"equippedSlots","type":"uint256"},{"internalType":"uint256","name":"petId","type":"uint256"},{"internalType":"uint256","name":"weapon1Id","type":"uint256"},{"internalType":"uint256","name":"weapon2Id","type":"uint256"},{"internalType":"uint256","name":"offhand1Id","type":"uint256"},{"internalType":"uint256","name":"offhand2Id","type":"uint256"},{"internalType":"uint256","name":"armorId","type":"uint256"},{"internalType":"uint256","name":"accessoryId","type":"uint256"}],"internalType":"structHeroEquipment","name":"equipment","type":"tuple"}],"internalType":"structHeroV2","name":"_hero","type":"tuple"}],"name":"updateHeroV2","outputs":[],"stateMutability":"nonpayable","type":"function"}
            ]
             """


def block_explorer_link(contract_address, txid):
    if hasattr(contract_address, 'address'):
        contract_address = str(contract_address.address)
    contract_address = str(contract_address).upper()
    if contract_address == SERENDALE_CONTRACT_ADDRESS.upper():
        return 'https://explorer.harmony.one/tx/' + str(txid)
    elif contract_address == CRYSTALVALE_CONTRACT_ADDRESS.upper():
        return 'https://subnets.avax.network/defi-kingdoms/dfk-chain/explorer/tx/' + str(txid)
    elif contract_address == SERENDALE2_CONTRACT_ADDRESS.upper():
        return 'https://scope.klaytn.com/tx/' + str(txid)
    else:
        return str(txid)


def transfer_from(contract_address, hero_id, receiver_address, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger=None):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.from_key(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    owner = contract.functions.ownerOf(hero_id).call()
    if logger is not None:
        logger.info("Hero's owner " + str(owner))

    if owner != account.address:
        raise Exception("Owner mismatch")

    tx = contract.functions.transferFrom(owner, receiver_address, hero_id)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.build_transaction(
            {'maxFeePerGas': w3.to_wei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.to_wei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.build_transaction({'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    if logger is not None:
        logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    if logger is not None:
        logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    if logger is not None:
        logger.debug("Transaction successfully sent !")
        logger.info("Waiting for transaction " + block_explorer_link(contract_address, signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds, poll_latency=2)
    if logger is not None:
        logger.info("Transaction mined !")
    logger.info(str(tx_receipt))


def get_owner(contract_address, hero_id, rpc_address, block_identifier="latest"):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return str(contract.functions.ownerOf(hero_id).call(block_identifier=block_identifier))


def get_users_heroes(contract_address, user_address, rpc_address, block_identifier="latest"):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getUserHeroes(Web3.to_checksum_address(user_address)).call(block_identifier=block_identifier)


def is_approved_for_all(contract_address, owner, operator, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.isApprovedForAll(Web3.to_checksum_address(owner), Web3.to_checksum_address(operator)).call()


def get_hero_v1(contract_address, hero_id, rpc_address, block_identifier="latest"):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    contract_entry = contract.functions.getHero(hero_id).call(block_identifier=block_identifier)

    hero = {}
    tuple_index = 0

    hero['id'] = contract_entry[tuple_index]
    tuple_index = tuple_index + 1

    # SummoningInfo
    summoning_info = {}
    summoning_info['summonedTime'] = contract_entry[tuple_index][0]
    summoning_info['nextSummonTime'] = contract_entry[tuple_index][1]
    summoning_info['summonerId'] = contract_entry[tuple_index][2]
    summoning_info['assistantId'] = contract_entry[tuple_index][3]
    summoning_info['summons'] = contract_entry[tuple_index][4]
    summoning_info['maxSummons'] = contract_entry[tuple_index][5]

    hero['summoningInfo'] = summoning_info
    tuple_index = tuple_index + 1

    # HeroInfo
    hero_info = {}
    hero_info['statGenes'] = contract_entry[tuple_index][0]
    hero_info['visualGenes'] = contract_entry[tuple_index][1]
    hero_info['rarity'] = contract_entry[tuple_index][2]
    hero_info['shiny'] = contract_entry[tuple_index][3]
    hero_info['generation'] = contract_entry[tuple_index][4]
    hero_info['firstName'] = contract_entry[tuple_index][5]
    hero_info['lastName'] = contract_entry[tuple_index][6]
    hero_info['shinyStyle'] = contract_entry[tuple_index][7]
    hero_info['class'] = contract_entry[tuple_index][8]
    hero_info['subClass'] = contract_entry[tuple_index][9]

    hero['info'] = hero_info
    tuple_index = tuple_index + 1

    # HeroState
    hero_state = {}
    hero_state['staminaFullAt'] = contract_entry[tuple_index][0]
    hero_state['hpFullAt'] = contract_entry[tuple_index][1]
    hero_state['mpFullAt'] = contract_entry[tuple_index][2]
    hero_state['level'] = contract_entry[tuple_index][3]
    hero_state['xp'] = contract_entry[tuple_index][4]
    hero_state['currentQuest'] = contract_entry[tuple_index][5]
    hero_state['sp'] = contract_entry[tuple_index][6]
    hero_state['status'] = contract_entry[tuple_index][7]

    hero['state'] = hero_state
    tuple_index = tuple_index + 1

    # HeroStats
    hero_stats = {}
    hero_stats['strength'] = contract_entry[tuple_index][0]
    hero_stats['intelligence'] = contract_entry[tuple_index][1]
    hero_stats['wisdom'] = contract_entry[tuple_index][2]
    hero_stats['luck'] = contract_entry[tuple_index][3]
    hero_stats['agility'] = contract_entry[tuple_index][4]
    hero_stats['vitality'] = contract_entry[tuple_index][5]
    hero_stats['endurance'] = contract_entry[tuple_index][6]
    hero_stats['dexterity'] = contract_entry[tuple_index][7]
    hero_stats['hp'] = contract_entry[tuple_index][8]
    hero_stats['mp'] = contract_entry[tuple_index][9]
    hero_stats['stamina'] = contract_entry[tuple_index][10]

    hero['stats'] = hero_stats
    tuple_index = tuple_index + 1

    # primary HeroStatGrowth
    hero_primary_stat_growth = {}
    hero_primary_stat_growth['strength'] = contract_entry[tuple_index][0]
    hero_primary_stat_growth['intelligence'] = contract_entry[tuple_index][1]
    hero_primary_stat_growth['wisdom'] = contract_entry[tuple_index][2]
    hero_primary_stat_growth['luck'] = contract_entry[tuple_index][3]
    hero_primary_stat_growth['agility'] = contract_entry[tuple_index][4]
    hero_primary_stat_growth['vitality'] = contract_entry[tuple_index][5]
    hero_primary_stat_growth['endurance'] = contract_entry[tuple_index][6]
    hero_primary_stat_growth['dexterity'] = contract_entry[tuple_index][7]
    hero_primary_stat_growth['hpSm'] = contract_entry[tuple_index][8]
    hero_primary_stat_growth['hpRg'] = contract_entry[tuple_index][9]
    hero_primary_stat_growth['hpLg'] = contract_entry[tuple_index][10]
    hero_primary_stat_growth['mpSm'] = contract_entry[tuple_index][11]
    hero_primary_stat_growth['mpRg'] = contract_entry[tuple_index][12]
    hero_primary_stat_growth['mpLg'] = contract_entry[tuple_index][13]

    hero['primaryStatGrowth'] = hero_primary_stat_growth
    tuple_index = tuple_index + 1

    # secondary HeroStatGrowth
    hero_secondary_stat_growth = {}
    hero_secondary_stat_growth['strength'] = contract_entry[tuple_index][0]
    hero_secondary_stat_growth['intelligence'] = contract_entry[tuple_index][1]
    hero_secondary_stat_growth['wisdom'] = contract_entry[tuple_index][2]
    hero_secondary_stat_growth['luck'] = contract_entry[tuple_index][3]
    hero_secondary_stat_growth['agility'] = contract_entry[tuple_index][4]
    hero_secondary_stat_growth['vitality'] = contract_entry[tuple_index][5]
    hero_secondary_stat_growth['endurance'] = contract_entry[tuple_index][6]
    hero_secondary_stat_growth['dexterity'] = contract_entry[tuple_index][7]
    hero_secondary_stat_growth['hpSm'] = contract_entry[tuple_index][8]
    hero_secondary_stat_growth['hpRg'] = contract_entry[tuple_index][9]
    hero_secondary_stat_growth['hpLg'] = contract_entry[tuple_index][10]
    hero_secondary_stat_growth['mpSm'] = contract_entry[tuple_index][11]
    hero_secondary_stat_growth['mpRg'] = contract_entry[tuple_index][12]
    hero_secondary_stat_growth['mpLg'] = contract_entry[tuple_index][13]

    hero['secondaryStatGrowth'] = hero_secondary_stat_growth
    tuple_index = tuple_index + 1

    # HeroProfessions
    hero_professions = {}
    hero_professions['mining'] = contract_entry[tuple_index][0]
    hero_professions['gardening'] = contract_entry[tuple_index][1]
    hero_professions['foraging'] = contract_entry[tuple_index][2]
    hero_professions['fishing'] = contract_entry[tuple_index][3]

    hero['professions'] = hero_professions

    return hero



def get_hero_v2(contract_address, hero_id, rpc_address, block_identifier="latest"):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    contract_entry = contract.functions.getHeroV2(hero_id).call(block_identifier=block_identifier)

    hero = {}
    tuple_index = 0

    hero['id'] = contract_entry[tuple_index]
    tuple_index = tuple_index + 1

    # SummoningInfo
    summoning_info = {}
    summoning_info['summonedTime'] = contract_entry[tuple_index][0]
    summoning_info['nextSummonTime'] = contract_entry[tuple_index][1]
    summoning_info['summonerId'] = contract_entry[tuple_index][2]
    summoning_info['assistantId'] = contract_entry[tuple_index][3]
    summoning_info['summons'] = contract_entry[tuple_index][4]
    summoning_info['maxSummons'] = contract_entry[tuple_index][5]

    hero['summoningInfo'] = summoning_info
    tuple_index = tuple_index + 1

    # HeroInfo
    hero_info = {}
    hero_info['statGenes'] = contract_entry[tuple_index][0]
    hero_info['visualGenes'] = contract_entry[tuple_index][1]
    hero_info['rarity'] = contract_entry[tuple_index][2]
    hero_info['shiny'] = contract_entry[tuple_index][3]
    hero_info['generation'] = contract_entry[tuple_index][4]
    hero_info['firstName'] = contract_entry[tuple_index][5]
    hero_info['lastName'] = contract_entry[tuple_index][6]
    hero_info['shinyStyle'] = contract_entry[tuple_index][7]
    hero_info['class'] = contract_entry[tuple_index][8]
    hero_info['subClass'] = contract_entry[tuple_index][9]

    hero['info'] = hero_info
    tuple_index = tuple_index + 1

    # HeroState
    hero_state = {}
    hero_state['staminaFullAt'] = contract_entry[tuple_index][0]
    hero_state['hpFullAt'] = contract_entry[tuple_index][1]
    hero_state['mpFullAt'] = contract_entry[tuple_index][2]
    hero_state['level'] = contract_entry[tuple_index][3]
    hero_state['xp'] = contract_entry[tuple_index][4]
    hero_state['currentQuest'] = contract_entry[tuple_index][5]
    hero_state['sp'] = contract_entry[tuple_index][6]
    hero_state['status'] = contract_entry[tuple_index][7]

    hero['state'] = hero_state
    tuple_index = tuple_index + 1

    # HeroStats
    hero_stats = {}
    hero_stats['strength'] = contract_entry[tuple_index][0]
    hero_stats['intelligence'] = contract_entry[tuple_index][1]
    hero_stats['wisdom'] = contract_entry[tuple_index][2]
    hero_stats['luck'] = contract_entry[tuple_index][3]
    hero_stats['agility'] = contract_entry[tuple_index][4]
    hero_stats['vitality'] = contract_entry[tuple_index][5]
    hero_stats['endurance'] = contract_entry[tuple_index][6]
    hero_stats['dexterity'] = contract_entry[tuple_index][7]
    hero_stats['hp'] = contract_entry[tuple_index][8]
    hero_stats['mp'] = contract_entry[tuple_index][9]
    hero_stats['stamina'] = contract_entry[tuple_index][10]

    hero['stats'] = hero_stats
    tuple_index = tuple_index + 1

    # primary HeroStatGrowth
    hero_primary_stat_growth = {}
    hero_primary_stat_growth['strength'] = contract_entry[tuple_index][0]
    hero_primary_stat_growth['intelligence'] = contract_entry[tuple_index][1]
    hero_primary_stat_growth['wisdom'] = contract_entry[tuple_index][2]
    hero_primary_stat_growth['luck'] = contract_entry[tuple_index][3]
    hero_primary_stat_growth['agility'] = contract_entry[tuple_index][4]
    hero_primary_stat_growth['vitality'] = contract_entry[tuple_index][5]
    hero_primary_stat_growth['endurance'] = contract_entry[tuple_index][6]
    hero_primary_stat_growth['dexterity'] = contract_entry[tuple_index][7]
    hero_primary_stat_growth['hpSm'] = contract_entry[tuple_index][8]
    hero_primary_stat_growth['hpRg'] = contract_entry[tuple_index][9]
    hero_primary_stat_growth['hpLg'] = contract_entry[tuple_index][10]
    hero_primary_stat_growth['mpSm'] = contract_entry[tuple_index][11]
    hero_primary_stat_growth['mpRg'] = contract_entry[tuple_index][12]
    hero_primary_stat_growth['mpLg'] = contract_entry[tuple_index][13]

    hero['primaryStatGrowth'] = hero_primary_stat_growth
    tuple_index = tuple_index + 1

    # secondary HeroStatGrowth
    hero_secondary_stat_growth = {}
    hero_secondary_stat_growth['strength'] = contract_entry[tuple_index][0]
    hero_secondary_stat_growth['intelligence'] = contract_entry[tuple_index][1]
    hero_secondary_stat_growth['wisdom'] = contract_entry[tuple_index][2]
    hero_secondary_stat_growth['luck'] = contract_entry[tuple_index][3]
    hero_secondary_stat_growth['agility'] = contract_entry[tuple_index][4]
    hero_secondary_stat_growth['vitality'] = contract_entry[tuple_index][5]
    hero_secondary_stat_growth['endurance'] = contract_entry[tuple_index][6]
    hero_secondary_stat_growth['dexterity'] = contract_entry[tuple_index][7]
    hero_secondary_stat_growth['hpSm'] = contract_entry[tuple_index][8]
    hero_secondary_stat_growth['hpRg'] = contract_entry[tuple_index][9]
    hero_secondary_stat_growth['hpLg'] = contract_entry[tuple_index][10]
    hero_secondary_stat_growth['mpSm'] = contract_entry[tuple_index][11]
    hero_secondary_stat_growth['mpRg'] = contract_entry[tuple_index][12]
    hero_secondary_stat_growth['mpLg'] = contract_entry[tuple_index][13]

    hero['secondaryStatGrowth'] = hero_secondary_stat_growth
    tuple_index = tuple_index + 1

    # HeroProfessions V2
    hero_professions = {}
    hero_professions['mining'] = contract_entry[tuple_index][0]
    hero_professions['gardening'] = contract_entry[tuple_index][1]
    hero_professions['foraging'] = contract_entry[tuple_index][2]
    hero_professions['fishing'] = contract_entry[tuple_index][3]
    hero_professions['craft1'] = contract_entry[tuple_index][2]
    hero_professions['craft2'] = contract_entry[tuple_index][3]

    hero['professions'] = hero_professions
    tuple_index = tuple_index + 1

    # HeroEquipment
    hero_equipment = {}
    hero_equipment['equippedSlots'] = contract_entry[tuple_index][0]
    hero_equipment['petId'] = contract_entry[tuple_index][1]
    hero_equipment['weapon1Id'] = contract_entry[tuple_index][2]
    hero_equipment['weapon2Id'] = contract_entry[tuple_index][3]
    hero_equipment['offhand1Id'] = contract_entry[tuple_index][4]
    hero_equipment['offhand2Id'] = contract_entry[tuple_index][5]
    hero_equipment['armorId'] = contract_entry[tuple_index][6]
    hero_equipment['accessoryId'] = contract_entry[tuple_index][7]

    hero['equipment'] = hero_equipment

    return hero

def human_readable_hero(raw_hero, hero_male_first_names=None, hero_female_first_names=None, hero_last_names=None):
    readable_hero = copy.deepcopy(raw_hero)

    readable_hero['info']['rarity'] = hero_utils.parse_rarity(readable_hero['info']['rarity'])
    readable_hero['info']['class'] = hero_utils.parse_class(readable_hero['info']['class'])
    readable_hero['info']['subClass'] = hero_utils.parse_class(readable_hero['info']['subClass'])

    # visualGenes
    readable_hero['info']['visualGenes'] = hero_utils.parse_visual_genes(readable_hero['info']['visualGenes'])

    # statsGenes
    readable_hero['info']['statGenes'] = hero_utils.parse_stat_genes(readable_hero['info']['statGenes'])

    if 'craft1' in readable_hero['professions']:
        readable_hero['professions']['craft1'] = hero_utils.parse_craft(readable_hero['professions']['craft1'])
        readable_hero['professions']['craft2'] = hero_utils.parse_craft(readable_hero['professions']['craft2'])


    # names
    if readable_hero['info']['visualGenes']['gender'] == 'male':
        if hero_male_first_names is not None:
            readable_hero['info']['firstName'] = hero_male_first_names[readable_hero['info']['firstName']]
    else:
        if hero_female_first_names is not None:
            readable_hero['info']['firstName'] = hero_female_first_names[readable_hero['info']['firstName']]

    if hero_last_names is not None:
        readable_hero['info']['lastName'] = hero_last_names[readable_hero['info']['lastName']]

    return readable_hero
