from web3 import Web3
from web3.logs import DISCARD

SERENDALE_CONTRACT_ADDRESS = '0x0594D86b2923076a2316EaEA4E1Ca286dAA142C1'
CRYSTALVALE_CONTRACT_ADDRESS = '0xD507b6b299d9FC835a0Df92f718920D13fA49B47'
SERENDALE2_CONTRACT_ADDRESS = '0xdbEE8C336B06f2d30a6d2bB3817a3Ae0E34f4900'

ABI = """[
    {"name": "AttunementCrystalAdded", "type": "event", "inputs": [{"name": "atunementItemAddress", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "internalType": "uint8", "indexed": false}], "anonymous": false},
    {"name": "LevelUp", "type": "event", "inputs": [{"name": "player", "type": "address", "internalType": "address", "indexed": true}, {"name": "heroId", "type": "uint256", "internalType": "uint256", "indexed": true}, {"name": "hero", "type": "tuple", "internalType": "struct IHeroTypes.Hero", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "summoningInfo", "type": "tuple", "internalType": "struct IHeroTypes.SummoningInfo", "components": [{"name": "summonedTime", "type": "uint256", "internalType": "uint256"}, {"name": "nextSummonTime", "type": "uint256", "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "summons", "type": "uint32", "internalType": "uint32"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}]}, {"name": "info", "type": "tuple", "internalType": "struct IHeroTypes.HeroInfo", "components": [{"name": "statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "rarity", "type": "uint8", "internalType": "enum IHeroTypes.Rarity"}, {"name": "shiny", "type": "bool", "internalType": "bool"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}, {"name": "class", "type": "uint8", "internalType": "uint8"}, {"name": "subClass", "type": "uint8", "internalType": "uint8"}]}, {"name": "state", "type": "tuple", "internalType": "struct IHeroTypes.HeroState", "components": [{"name": "staminaFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "hpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "mpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint16", "internalType": "uint16"}, {"name": "xp", "type": "uint64", "internalType": "uint64"}, {"name": "currentQuest", "type": "address", "internalType": "address"}, {"name": "sp", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum IHeroTypes.HeroStatus"}]}, {"name": "stats", "type": "tuple", "internalType": "struct IHeroTypes.HeroStats", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hp", "type": "uint16", "internalType": "uint16"}, {"name": "mp", "type": "uint16", "internalType": "uint16"}, {"name": "stamina", "type": "uint16", "internalType": "uint16"}]}, {"name": "primaryStatGrowth", "type": "tuple", "internalType": "struct IHeroTypes.HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "secondaryStatGrowth", "type": "tuple", "internalType": "struct IHeroTypes.HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "professions", "type": "tuple", "internalType": "struct IHeroTypes.HeroProfessions", "components": [{"name": "mining", "type": "uint16", "internalType": "uint16"}, {"name": "gardening", "type": "uint16", "internalType": "uint16"}, {"name": "foraging", "type": "uint16", "internalType": "uint16"}, {"name": "fishing", "type": "uint16", "internalType": "uint16"}]}], "indexed": false}, {"name": "oldHero", "type": "tuple", "internalType": "struct IHeroTypes.Hero", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "summoningInfo", "type": "tuple", "internalType": "struct IHeroTypes.SummoningInfo", "components": [{"name": "summonedTime", "type": "uint256", "internalType": "uint256"}, {"name": "nextSummonTime", "type": "uint256", "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "summons", "type": "uint32", "internalType": "uint32"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}]}, {"name": "info", "type": "tuple", "internalType": "struct IHeroTypes.HeroInfo", "components": [{"name": "statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "rarity", "type": "uint8", "internalType": "enum IHeroTypes.Rarity"}, {"name": "shiny", "type": "bool", "internalType": "bool"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}, {"name": "class", "type": "uint8", "internalType": "uint8"}, {"name": "subClass", "type": "uint8", "internalType": "uint8"}]}, {"name": "state", "type": "tuple", "internalType": "struct IHeroTypes.HeroState", "components": [{"name": "staminaFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "hpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "mpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint16", "internalType": "uint16"}, {"name": "xp", "type": "uint64", "internalType": "uint64"}, {"name": "currentQuest", "type": "address", "internalType": "address"}, {"name": "sp", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum IHeroTypes.HeroStatus"}]}, {"name": "stats", "type": "tuple", "internalType": "struct IHeroTypes.HeroStats", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hp", "type": "uint16", "internalType": "uint16"}, {"name": "mp", "type": "uint16", "internalType": "uint16"}, {"name": "stamina", "type": "uint16", "internalType": "uint16"}]}, {"name": "primaryStatGrowth", "type": "tuple", "internalType": "struct IHeroTypes.HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "secondaryStatGrowth", "type": "tuple", "internalType": "struct IHeroTypes.HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "professions", "type": "tuple", "internalType": "struct IHeroTypes.HeroProfessions", "components": [{"name": "mining", "type": "uint16", "internalType": "uint16"}, {"name": "gardening", "type": "uint16", "internalType": "uint16"}, {"name": "foraging", "type": "uint16", "internalType": "uint16"}, {"name": "fishing", "type": "uint16", "internalType": "uint16"}]}], "indexed": false}], "anonymous": false},
    {"name": "MeditationBegun", "type": "event", "inputs": [{"name": "player", "type": "address", "internalType": "address", "indexed": true}, {"name": "heroId", "type": "uint256", "internalType": "uint256", "indexed": true}, {"name": "meditationId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "primaryStat", "type": "uint8", "internalType": "uint8", "indexed": false}, {"name": "secondaryStat", "type": "uint8", "internalType": "uint8", "indexed": false}, {"name": "tertiaryStat", "type": "uint8", "internalType": "uint8", "indexed": false}, {"name": "attunementCrystal", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "MeditationCompleted", "type": "event", "inputs": [{"name": "player", "type": "address", "internalType": "address", "indexed": true}, {"name": "heroId", "type": "uint256", "internalType": "uint256", "indexed": true}, {"name": "meditationId", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "RoleAdminChanged", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "previousAdminRole", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "newAdminRole", "type": "bytes32", "internalType": "bytes32", "indexed": true}], "anonymous": false},
    {"name": "RoleGranted", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "account", "type": "address", "internalType": "address", "indexed": true}, {"name": "sender", "type": "address", "internalType": "address", "indexed": true}], "anonymous": false},
    {"name": "RoleRevoked", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "account", "type": "address", "internalType": "address", "indexed": true}, {"name": "sender", "type": "address", "internalType": "address", "indexed": true}], "anonymous": false},
    {"name": "StatUp", "type": "event", "inputs": [{"name": "player", "type": "address", "internalType": "address", "indexed": true}, {"name": "heroId", "type": "uint256", "internalType": "uint256", "indexed": true}, {"name": "stat", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "increase", "type": "uint8", "internalType": "uint8", "indexed": false}, {"name": "updateType", "type": "uint8", "internalType": "enum MeditationCircle.UpdateType", "indexed": false}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "DEFAULT_ADMIN_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "MODERATOR_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "_getRequiredRunes", "type": "function", "inputs": [{"name": "_level", "type": "uint16", "internalType": "uint16"}], "outputs": [{"name": "", "type": "uint16[10]", "internalType": "uint16[10]"}], "stateMutability": "pure"},
    {"name": "activeAttunementCrystals", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "addAttunementCrystal", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "adminRemove", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "completeMeditation", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getActiveMeditations", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple[]", "internalType": "struct MeditationCircle.Meditation[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "primaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "secondaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "tertiaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "attunementCrystal", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "uint8"}]}], "stateMutability": "view"},
    {"name": "getHeroMeditation", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "internalType": "struct MeditationCircle.Meditation", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "primaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "secondaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "tertiaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "attunementCrystal", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "uint8"}]}], "stateMutability": "view"},
    {"name": "getMeditation", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "internalType": "struct MeditationCircle.Meditation", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "primaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "secondaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "tertiaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "attunementCrystal", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "uint8"}]}], "stateMutability": "view"},
    {"name": "getRoleAdmin", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "grantRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "hasRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "heroToMeditation", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_heroCoreAddress", "type": "address", "internalType": "address"}, {"name": "_statScienceAddress", "type": "address", "internalType": "address"}, {"name": "_jewelTokenAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "jewelToken", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IJewelToken"}], "stateMutability": "view"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "profileActiveMeditations", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "primaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "secondaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "tertiaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "attunementCrystal", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "removeAttunementCrystal", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "renounceRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "revokeRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "runes", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "contract IInventoryItem"}], "stateMutability": "view"},
    {"name": "setFees", "type": "function", "inputs": [{"name": "_feeAddresses", "type": "address[]", "internalType": "address[]"}, {"name": "_feePercents", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setRune", "type": "function", "inputs": [{"name": "_index", "type": "uint8", "internalType": "uint8"}, {"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setStatScienceAddress", "type": "function", "inputs": [{"name": "_statScienceAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "startMeditation", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}, {"name": "_primaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "_secondaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "_tertiaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "_attunementCrystal", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "supportsInterface", "type": "function", "inputs": [{"name": "interfaceId", "type": "bytes4", "internalType": "bytes4"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"}
]
    """

ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'


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


def get_required_runes(contract_address, level, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions._getRequiredRunes(level).call()


def active_attunement_crystals(contract_address, address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.activeAttunementCrystals(address).call()


def add_attunement_crystal(contract_address, address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.addAttunementCrystal(address).call()


def start_meditation(contract_address, hero_id, trait1, trait2, trait3, attunement_crystal_address, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):

    if type(trait1) == str:
        trait1 = trait2id(trait1)

    if type(trait2) == str:
        trait2 = trait2id(trait2)

    if type(trait3) == str:
        trait3 = trait2id(trait3)

    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.startMeditation(hero_id, trait1, trait2, trait3, attunement_crystal_address)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.buildTransaction({'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

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


def complete_meditation(contract_address, hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.completeMeditation(hero_id)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.buildTransaction({'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

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


def parse_meditation_results(contract_address, tx_receipt, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    meditation_result = {}
    level_up = contract.events.LevelUp().processReceipt(tx_receipt, errors=DISCARD)
    new_level = level_up[0]['args']["hero"][3][3]
    
    stat_up = contract.events.StatUp().processReceipt(tx_receipt, errors=DISCARD)

    hero_id = None
    for stat in stat_up:
        hero_id = stat['args']['heroId']

        if hero_id not in meditation_result:
            meditation_result[hero_id] = {}
        
        if not id2stat(stat['args']['stat']) in meditation_result[hero_id]:
            meditation_result[hero_id][id2stat(stat['args']['stat'])] = {"increase": 0}

        meditation_result[hero_id][id2stat(stat['args']['stat'])]["increase"] += stat['args']['increase']

    if hero_id:
        meditation_result[hero_id]["new level"] = new_level
    
    return meditation_result


def get_active_meditations(contract_address, address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getActiveMeditations(address).call()


def get_hero_meditation(contract_address, hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    result = contract.functions.getHeroMeditation(hero_id).call()
    if result[0] == 0:
        return None
    return result


def get_meditation(contract_address, meditation_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    result = contract.functions.getMeditation(meditation_id).call()
    if result[0] == 0:
        return None
    return result


def hero_to_meditation_id(contract_address, hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.heroToMeditation(hero_id).call()


def profile_active_meditations(contract_address, address, id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.profileActiveMeditations(address, id).call()


def trait2id(label):
    stats = {
        'strength': 0,
        'agility': 1,
        'intelligence': 2,
        'wisdom': 3,
        'luck': 4,
        'vitality': 5,
        'endurance': 6,
        'dexterity': 7
    }
    return stats.get(label, None)


def id2stat(label):
    stats = {
        0: 'STR',
        1: 'AGI',
        2: 'INT',
        3: 'WIS',
        4: 'LCK',
        5: 'VIT',
        6: 'END',
        7: 'DEX',
        8: 'HP',
        9: 'MP',
        10: 'STAMINA'
    }
    return stats.get(label, None)


def xp_per_level(level):
    next_level = level + 1
    if level < 6:
        return next_level * 1000
    elif level < 9:
        return 4000 + (next_level - 5) * 2000
    elif level < 16:
        return 12000 + (next_level - 9) * 4000
    elif level < 36:
        return 40000 + (next_level - 16) * 5000
    elif level < 56:
        return 140000 + (next_level - 36) * 7500
    else:
        return 290000 + (next_level - 56) * 10000
