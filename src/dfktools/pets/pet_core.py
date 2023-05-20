import copy
from web3 import Web3
from .utils import utils as pet_utils

SERENDALE_CONTRACT_ADDRESS = '0xAC9AFb5900C8A27B766bCad3A37423DC0F4C22d3'
CRYSTALVALE_CONTRACT_ADDRESS = '0x1990F87d6BC9D9385917E3EDa0A7674411C3Cd7F'
SERENDALE2_CONTRACT_ADDRESS = '0x6362b205b539afb5FC369277365441c1dC6fAa28'

ABI = '''
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
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"petId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"}],"indexed":false,"internalType":"structPet","name":"pet","type":"tuple"}],"name":"PetHatched","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"petId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"},{"internalType":"address","name":"fedBy","type":"address"},{"internalType":"enumPetFoodType","name":"foodType","type":"uint8"}],"indexed":false,"internalType":"structPetV2","name":"pet","type":"tuple"}],"name":"PetHatchedV2","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"petId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"}],"indexed":false,"internalType":"structPet","name":"pet","type":"tuple"}],"name":"PetUpdated","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"petId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"},{"internalType":"address","name":"fedBy","type":"address"},{"internalType":"enumPetFoodType","name":"foodType","type":"uint8"}],"indexed":false,"internalType":"structPetV2","name":"pet","type":"tuple"}],"name":"PetUpdatedV2","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
        {"inputs":[],"name":"BRIDGE_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"MINTER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"PET_MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"baseHungryTime","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"bonusCount","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"address","name":"_to","type":"address"}],"name":"bridgeMint","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"gold","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"heroCore","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"heroToPet","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"nextPetId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"powerUpManager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint64","name":"_baseHungryTime","type":"uint64"}],"name":"setBaseHungryTime","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_gold","type":"address"}],"name":"setGold","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_heroCore","type":"address"}],"name":"setHeroCore","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"enumTreatType","name":"_treatType","type":"uint8"},{"internalType":"address[]","name":"_ingredients","type":"address[]"},{"internalType":"uint256[]","name":"_ingredientAmounts","type":"uint256[]"}],"name":"setIngredients","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_nextPetId","type":"uint256"}],"name":"setNextPetId","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_powerUpManager","type":"address"}],"name":"setPowerUpManager","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"enumTreatType","name":"_treatType","type":"uint8"},{"internalType":"address","name":"_address","type":"address"},{"internalType":"bool","name":"_active","type":"bool"},{"internalType":"uint256","name":"_goldCost","type":"uint256"}],"name":"setTreatType","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"enumTreatType","name":"","type":"uint8"}],"name":"treatInfo","outputs":[{"internalType":"address","name":"treatAddress","type":"address"},{"internalType":"uint256","name":"goldCost","type":"uint256"},{"internalType":"bool","name":"isActive","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"enumTreatType","name":"","type":"uint8"},{"internalType":"address","name":"","type":"address"}],"name":"treatIngredientRequirements","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"ReentrancyGuard__ReentrantCall","type":"error"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"enumTreatType","name":"treatType","type":"uint8"},{"indexed":false,"internalType":"uint256","name":"quantity","type":"uint256"}],"name":"BonusTreatsAwarded","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"fedBy","type":"address"},{"indexed":false,"internalType":"uint256","name":"petId","type":"uint256"},{"indexed":false,"internalType":"enumPetFoodType","name":"foodType","type":"uint8"},{"indexed":false,"internalType":"uint256","name":"hungryAt","type":"uint256"}],"name":"PetFed","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"enumTreatType","name":"treatType","type":"uint8"},{"indexed":false,"internalType":"uint256","name":"quantity","type":"uint256"},{"indexed":false,"internalType":"address","name":"item1","type":"address"},{"indexed":false,"internalType":"address","name":"item2","type":"address"}],"name":"TreatCrafted","type":"event"},
        {"inputs":[],"name":"PREMIUM_PROVISIONS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"components":[{"internalType":"enumTreatType","name":"treatType","type":"uint8"},{"internalType":"uint256","name":"treatQuantity","type":"uint256"},{"internalType":"address","name":"item1","type":"address"},{"internalType":"address","name":"item2","type":"address"}],"internalType":"structTreatCraftingInput[]","name":"_treatData","type":"tuple[]"}],"name":"craftTreats","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"components":[{"internalType":"uint256","name":"petId","type":"uint256"},{"internalType":"enumTreatType","name":"treatType","type":"uint8"}],"internalType":"structPetFeedingInput[]","name":"_feedData","type":"tuple[]"}],"name":"feedPets","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"components":[{"internalType":"uint256","name":"petId","type":"uint256"},{"internalType":"enumTreatType","name":"treatType","type":"uint8"}],"internalType":"structPetFeedingInput[]","name":"_feedData","type":"tuple[]"},{"internalType":"address","name":"_account","type":"address"}],"name":"feedPetsOnBehalf","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"}],"name":"getDuelPetData","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"},{"internalType":"uint8[]","name":"","type":"uint8[]"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"isHeroPetHungry","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_petId","type":"uint256"}],"name":"isPetHungry","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getPet","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"}],"internalType":"structPet","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getPetV2","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"},{"internalType":"address","name":"fedBy","type":"address"},{"internalType":"enumPetFoodType","name":"foodType","type":"uint8"}],"internalType":"structPetV2","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"getUserPets","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"}],"internalType":"structPet[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"getUserPetsV2","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"},{"internalType":"address","name":"fedBy","type":"address"},{"internalType":"enumPetFoodType","name":"foodType","type":"uint8"}],"internalType":"structPetV2[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"components":[{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"}],"internalType":"structPetOptions","name":"_petOptions","type":"tuple"},{"internalType":"address","name":"owner","type":"address"}],"name":"hatchPet","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_petId","type":"uint256"}],"name":"transferPetOnBehalf","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"}],"internalType":"structPet","name":"_pet","type":"tuple"}],"name":"updatePet","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"originId","type":"uint8"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint8","name":"season","type":"uint8"},{"internalType":"uint8","name":"eggType","type":"uint8"},{"internalType":"uint8","name":"rarity","type":"uint8"},{"internalType":"uint8","name":"element","type":"uint8"},{"internalType":"uint8","name":"bonusCount","type":"uint8"},{"internalType":"uint8","name":"profBonus","type":"uint8"},{"internalType":"uint8","name":"profBonusScalar","type":"uint8"},{"internalType":"uint8","name":"craftBonus","type":"uint8"},{"internalType":"uint8","name":"craftBonusScalar","type":"uint8"},{"internalType":"uint8","name":"combatBonus","type":"uint8"},{"internalType":"uint8","name":"combatBonusScalar","type":"uint8"},{"internalType":"uint16","name":"appearance","type":"uint16"},{"internalType":"uint8","name":"background","type":"uint8"},{"internalType":"uint8","name":"shiny","type":"uint8"},{"internalType":"uint64","name":"hungryAt","type":"uint64"},{"internalType":"uint64","name":"equippableAt","type":"uint64"},{"internalType":"uint256","name":"equippedTo","type":"uint256"},{"internalType":"address","name":"fedBy","type":"address"},{"internalType":"enumPetFoodType","name":"foodType","type":"uint8"}],"internalType":"structPetV2","name":"_pet","type":"tuple"}],"name":"updatePetV2","outputs":[],"stateMutability":"nonpayable","type":"function"}
    ]
    '''


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


def balance_of(contract_address, account, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.balanceOf(Web3.to_checksum_address(account)).call()


def get_pet_v1(contract_address, pet_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getPet(pet_id).call()


def get_pet_v2(contract_address, pet_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getPetV2(pet_id).call()

def get_user_pets_v1(contract_address, account, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getUserPets(account).call()


def get_user_pets_v2(contract_address, account, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getUserPetsV2(account).call()

def owner_of(contract_address, pet_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.ownerOf(pet_id).call()


def next_pet_id(contract_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.nextPetId().call()


def is_approved_for_all(contract_address, owner, operator, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.isApprovedForAll(Web3.to_checksum_address(owner), Web3.to_checksum_address(operator)).call()


def safe_transfer_from(contract_address, _from, to, egg_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):

    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.from_key(private_key)
    w3.eth.default_account = account.address
    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.safeTransferFrom(_from, to, egg_id)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.build_transaction(
            {'maxFeePerGas': w3.to_wei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.to_wei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.build_transaction({'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info("Waiting for transaction " + block_explorer_link(contract_address, signed_tx.hash.hex()) + " to be mined")

    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def transfer_from(contract_address, receiver_address, egg_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):

    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.from_key(private_key)
    w3.eth.default_account = account.address
    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    owner = contract.functions.ownerOf(egg_id).call()
    if logger is not None:
        logger.info("Pet {} owner {}".format(egg_id, owner))

    if owner != account.address:
        raise Exception("Owner mismatch")

    tx = contract.functions.transferFrom(owner, receiver_address, egg_id)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.build_transaction(
            {'maxFeePerGas': w3.to_wei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.to_wei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.build_transaction({'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info("Waiting for transaction " + block_explorer_link(contract_address, signed_tx.hash.hex()) + " to be mined")

    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def human_readable_pet(raw_pet):
    readable_pet = {}

    readable_pet['id'] = raw_pet[0]
    readable_pet['originId'] = raw_pet[1]
    readable_pet['name'] = raw_pet[2]
    readable_pet['season'] = raw_pet[3]
    readable_pet['eggType'] = pet_utils.parse_egg_type(raw_pet[4])
    readable_pet['rarity'] = pet_utils.parse_egg_rarity(raw_pet[5])
    readable_pet['element'] = pet_utils.parse_egg_element(raw_pet[6])
    readable_pet['bonusCount'] = raw_pet[7]
    readable_pet['profBonus'] = pet_utils.parse_bonus_type(readable_pet['eggType'], raw_pet[8])
    readable_pet['profBonusScalar'] = raw_pet[9]
    readable_pet['craftBonus'] = raw_pet[10]
    readable_pet['craftBonusScalar'] = raw_pet[11]
    readable_pet['combatBonus'] = raw_pet[12]
    readable_pet['combatBonusScalar'] = raw_pet[13]
    readable_pet['appearance'] = raw_pet[14]
    readable_pet['background'] = pet_utils.parse_background(raw_pet[15])
    readable_pet['shiny'] = raw_pet[16]
    readable_pet['hungryAt'] = raw_pet[17]
    readable_pet['equippableAt'] = raw_pet[18]
    readable_pet['equippedTo'] = raw_pet[19]
    if len(raw_pet) > 20:
        readable_pet['fedBy'] = raw_pet[20]
        readable_pet['foodType'] = pet_utils.parse_food_type(raw_pet[21]) #TODO: overwrite with -1 when hungry so food type is 'none'

    return readable_pet
