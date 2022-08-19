from web3 import Web3

CONTRACT_ADDRESS = '0x5100Bd31b822371108A0f63DCFb6594b9919Eaf4'

ABI = """
    [
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questTypeId","type":"uint256"},{"indexed":true,"internalType":"address","name":"questAddress","type":"address"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"contract IQuest","name":"quest","type":"address"},{"internalType":"uint8","name":"status","type":"uint8"},{"internalType":"uint8","name":"minHeroes","type":"uint8"},{"internalType":"uint8","name":"maxHeroes","type":"uint8"},{"internalType":"uint256","name":"level","type":"uint256"},{"internalType":"uint8","name":"maxAttempts","type":"uint8"}],"indexed":false,"internalType":"struct IQuestTypes.QuestType","name":"questType","type":"tuple"}],"name":"QuestAdded","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"contract IQuest","name":"quest","type":"address"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct IQuestTypes.Quest","name":"quest","type":"tuple"}],"name":"QuestCanceled","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"contract IQuest","name":"quest","type":"address"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct IQuestTypes.Quest","name":"quest","type":"tuple"}],"name":"QuestCompleted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"address","name":"rewardItem","type":"address"},{"indexed":false,"internalType":"uint256","name":"itemQuantity","type":"uint256"}],"name":"QuestReward","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"profession","type":"uint8"},{"indexed":false,"internalType":"uint16","name":"skillUp","type":"uint16"}],"name":"QuestSkillUp","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"indexed":false,"internalType":"uint16","name":"staminaSpent","type":"uint16"}],"name":"QuestStaminaSpent","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"contract IQuest","name":"quest","type":"address"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct IQuestTypes.Quest","name":"quest","type":"tuple"}],"name":"QuestStarted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questTypeId","type":"uint256"},{"indexed":true,"internalType":"address","name":"questAddress","type":"address"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"contract IQuest","name":"quest","type":"address"},{"internalType":"uint8","name":"status","type":"uint8"},{"internalType":"uint8","name":"minHeroes","type":"uint8"},{"internalType":"uint8","name":"maxHeroes","type":"uint8"},{"internalType":"uint256","name":"level","type":"uint256"},{"internalType":"uint8","name":"maxAttempts","type":"uint8"}],"indexed":false,"internalType":"struct IQuestTypes.QuestType","name":"questType","type":"tuple"}],"name":"QuestUpdated","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint64","name":"xpEarned","type":"uint64"}],"name":"QuestXP","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
        {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
        {"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_questAddress","type":"address"}],"name":"addQuestType","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"cancelQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"cleanQuests","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_profile","type":"address"}],"name":"cleanQuestsForPlayer","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"completeQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"getActiveQuests","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"contract IQuest","name":"quest","type":"address"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct IQuestTypes.Quest[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"getCurrentStamina","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_genes","type":"uint256"},{"internalType":"uint8","name":"_pos","type":"uint8"},{"internalType":"uint8","name":"_val","type":"uint8"}],"name":"getGeneBonus","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"getHero","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"struct IHeroTypes.SummoningInfo","name":"summoningInfo","type":"tuple"},{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enum IHeroTypes.Rarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"struct IHeroTypes.HeroInfo","name":"info","type":"tuple"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enum IHeroTypes.HeroStatus","name":"status","type":"uint8"}],"internalType":"struct IHeroTypes.HeroState","name":"state","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStats","name":"stats","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStatGrowth","name":"primaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStatGrowth","name":"secondaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"}],"internalType":"struct IHeroTypes.HeroProfessions","name":"professions","type":"tuple"}],"internalType":"struct IHeroTypes.Hero","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"getHeroQuest","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"contract IQuest","name":"quest","type":"address"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct IQuestTypes.Quest","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getQuest","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"contract IQuest","name":"quest","type":"address"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct IQuestTypes.Quest","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_questId","type":"uint256"}],"name":"getQuestData","outputs":[{"components":[{"internalType":"uint256","name":"uint1","type":"uint256"},{"internalType":"uint256","name":"uint2","type":"uint256"},{"internalType":"uint256","name":"uint3","type":"uint256"},{"internalType":"uint256","name":"uint4","type":"uint256"},{"internalType":"int256","name":"int1","type":"int256"},{"internalType":"int256","name":"int2","type":"int256"},{"internalType":"string","name":"string1","type":"string"},{"internalType":"string","name":"string2","type":"string"},{"internalType":"address","name":"address1","type":"address"},{"internalType":"address","name":"address2","type":"address"},{"internalType":"address","name":"address3","type":"address"},{"internalType":"address","name":"address4","type":"address"}],"internalType":"struct IQuestTypes.QuestData","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"getQuestType","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"contract IQuest","name":"quest","type":"address"},{"internalType":"uint8","name":"status","type":"uint8"},{"internalType":"uint8","name":"minHeroes","type":"uint8"},{"internalType":"uint8","name":"maxHeroes","type":"uint8"},{"internalType":"uint256","name":"level","type":"uint256"},{"internalType":"uint8","name":"maxAttempts","type":"uint8"}],"internalType":"struct IQuestTypes.QuestType","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"heroToQuest","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"_heroCoreAddress","type":"address"},{"internalType":"address","name":"_statScienceAddress","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"contract IQuest","name":"quest","type":"address"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct IQuestTypes.Quest","name":"_quest","type":"tuple"},{"internalType":"uint256","name":"_heroId","type":"uint256"},{"components":[{"internalType":"contract IInventoryItem","name":"item","type":"address"},{"internalType":"int64","name":"expBonus","type":"int64"},{"internalType":"int64","name":"skillUpChance","type":"int64"},{"internalType":"int64","name":"smallSkillUpMod","type":"int64"},{"internalType":"int64","name":"mediumSkillUpMod","type":"int64"},{"internalType":"int64","name":"largeSkillUpMod","type":"int64"},{"internalType":"int64","name":"baseChance","type":"int64"},{"internalType":"int64","name":"skillMod","type":"int64"},{"internalType":"int64","name":"statMod","type":"int64"},{"internalType":"int64","name":"luckMod","type":"int64"}],"internalType":"struct IQuestTypes.RewardItem","name":"_reward","type":"tuple"},{"internalType":"uint256","name":"_quantity","type":"uint256"}],"name":"logReward","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"contract IQuest","name":"quest","type":"address"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct IQuestTypes.Quest","name":"_quest","type":"tuple"},{"internalType":"uint256","name":"_heroId","type":"uint256"},{"internalType":"uint8","name":"_profession","type":"uint8"},{"internalType":"uint16","name":"_skillUp","type":"uint16"}],"name":"logSkillUp","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"contract IQuest","name":"quest","type":"address"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"internalType":"struct IQuestTypes.Quest","name":"_quest","type":"tuple"},{"internalType":"uint256","name":"_heroId","type":"uint256"},{"internalType":"uint64","name":"_xpEarned","type":"uint64"}],"name":"logXp","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"profileActiveQuests","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"contract IQuest","name":"quest","type":"address"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"uint8","name":"status","type":"uint8"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"questAddressToType","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256","name":"_timePerStamina","type":"uint256"}],"name":"setTimePerStamina","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"},{"internalType":"address","name":"_questAddress","type":"address"},{"internalType":"uint8","name":"_attempts","type":"uint8"}],"name":"startQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"},{"internalType":"address","name":"_questAddress","type":"address"},{"internalType":"uint8","name":"_attempts","type":"uint8"},{"components":[{"internalType":"uint256","name":"uint1","type":"uint256"},{"internalType":"uint256","name":"uint2","type":"uint256"},{"internalType":"uint256","name":"uint3","type":"uint256"},{"internalType":"uint256","name":"uint4","type":"uint256"},{"internalType":"int256","name":"int1","type":"int256"},{"internalType":"int256","name":"int2","type":"int256"},{"internalType":"string","name":"string1","type":"string"},{"internalType":"string","name":"string2","type":"string"},{"internalType":"address","name":"address1","type":"address"},{"internalType":"address","name":"address2","type":"address"},{"internalType":"address","name":"address3","type":"address"},{"internalType":"address","name":"address4","type":"address"}],"internalType":"struct IQuestTypes.QuestData","name":"_questData","type":"tuple"}],"name":"startQuestWithData","outputs":[],"stateMutability":"nonpayable","type":"function"},        {"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"timePerStamina","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"components":[{"internalType":"uint256","name":"summonedTime","type":"uint256"},{"internalType":"uint256","name":"nextSummonTime","type":"uint256"},{"internalType":"uint256","name":"summonerId","type":"uint256"},{"internalType":"uint256","name":"assistantId","type":"uint256"},{"internalType":"uint32","name":"summons","type":"uint32"},{"internalType":"uint32","name":"maxSummons","type":"uint32"}],"internalType":"struct IHeroTypes.SummoningInfo","name":"summoningInfo","type":"tuple"},{"components":[{"internalType":"uint256","name":"statGenes","type":"uint256"},{"internalType":"uint256","name":"visualGenes","type":"uint256"},{"internalType":"enum IHeroTypes.Rarity","name":"rarity","type":"uint8"},{"internalType":"bool","name":"shiny","type":"bool"},{"internalType":"uint16","name":"generation","type":"uint16"},{"internalType":"uint32","name":"firstName","type":"uint32"},{"internalType":"uint32","name":"lastName","type":"uint32"},{"internalType":"uint8","name":"shinyStyle","type":"uint8"},{"internalType":"uint8","name":"class","type":"uint8"},{"internalType":"uint8","name":"subClass","type":"uint8"}],"internalType":"struct IHeroTypes.HeroInfo","name":"info","type":"tuple"},{"components":[{"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"internalType":"uint256","name":"hpFullAt","type":"uint256"},{"internalType":"uint256","name":"mpFullAt","type":"uint256"},{"internalType":"uint16","name":"level","type":"uint16"},{"internalType":"uint64","name":"xp","type":"uint64"},{"internalType":"address","name":"currentQuest","type":"address"},{"internalType":"uint8","name":"sp","type":"uint8"},{"internalType":"enum IHeroTypes.HeroStatus","name":"status","type":"uint8"}],"internalType":"struct IHeroTypes.HeroState","name":"state","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hp","type":"uint16"},{"internalType":"uint16","name":"mp","type":"uint16"},{"internalType":"uint16","name":"stamina","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStats","name":"stats","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStatGrowth","name":"primaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"strength","type":"uint16"},{"internalType":"uint16","name":"intelligence","type":"uint16"},{"internalType":"uint16","name":"wisdom","type":"uint16"},{"internalType":"uint16","name":"luck","type":"uint16"},{"internalType":"uint16","name":"agility","type":"uint16"},{"internalType":"uint16","name":"vitality","type":"uint16"},{"internalType":"uint16","name":"endurance","type":"uint16"},{"internalType":"uint16","name":"dexterity","type":"uint16"},{"internalType":"uint16","name":"hpSm","type":"uint16"},{"internalType":"uint16","name":"hpRg","type":"uint16"},{"internalType":"uint16","name":"hpLg","type":"uint16"},{"internalType":"uint16","name":"mpSm","type":"uint16"},{"internalType":"uint16","name":"mpRg","type":"uint16"},{"internalType":"uint16","name":"mpLg","type":"uint16"}],"internalType":"struct IHeroTypes.HeroStatGrowth","name":"secondaryStatGrowth","type":"tuple"},{"components":[{"internalType":"uint16","name":"mining","type":"uint16"},{"internalType":"uint16","name":"gardening","type":"uint16"},{"internalType":"uint16","name":"foraging","type":"uint16"},{"internalType":"uint16","name":"fishing","type":"uint16"}],"internalType":"struct IHeroTypes.HeroProfessions","name":"professions","type":"tuple"}],"internalType":"struct IHeroTypes.Hero","name":"_hero","type":"tuple"}],"name":"updateHero","outputs":[],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[{"internalType":"address","name":"_questAddress","type":"address"},{"internalType":"uint8","name":"_status","type":"uint8"}],"name":"updateQuestType","outputs":[],"stateMutability":"nonpayable","type":"function"}
    ]
        """


def block_explorer_link(txid):
    return 'https://explorer.harmony.one/tx/' + str(txid)


def start_quest(quest_address, hero_ids, attempts, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.startQuest(hero_ids, quest_address, attempts)

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
    logger.info(
        "Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")

    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def start_quest_with_data(quest_address, data, hero_ids, attempts, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    if type(data) != tuple:
        raise Exception("Quest data must be a tuple")

    if len(data) != 12:
        raise Exception("Invalid quest data length (expected 12 but was "+str(len(data))+")")

    tx = contract.functions.startQuestWithData(hero_ids, quest_address, attempts, data)

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
    logger.info(
        "Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")

    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def complete_quest(hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.completeQuest(hero_id)

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
    logger.info(
        "Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def parse_complete_quest_receipt(tx_receipt, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    quest_result = {}

    quest_reward = contract.events.QuestReward().processReceipt(tx_receipt)
    quest_result['reward'] = quest_reward

    quest_xp = contract.events.QuestXP().processReceipt(tx_receipt)
    quest_result['xp'] = quest_xp

    quest_skill_up = contract.events.QuestSkillUp().processReceipt(tx_receipt)
    quest_result['skillUp'] = quest_skill_up

    return quest_result


def cancel_quest(hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.cancelQuest(hero_id)

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
    logger.info(
        "Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def hero_to_quest_id(hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.heroToQuest(hero_id).call()

    return result


def get_active_quest(address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.getActiveQuests(address).call()

    return result


def get_hero_quest(hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.getHeroQuest(hero_id).call()

    if result[0] <= 0:
        return None

    return result


def get_quest(quest_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.getQuest(quest_id).call()

    if result[0] <= 0:
        return None

    return result


def get_quest_data(quest_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.getQuestData(quest_id).call()

    return result


def quest_address_to_type(quest_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.questAddressToType(quest_address).call()

    return result


def get_current_stamina(hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.getCurrentStamina(hero_id).call()

    return result



