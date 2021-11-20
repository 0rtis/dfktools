[![GitHub license](https://img.shields.io/github/license/0rtis/dfk.svg?style=flat-square)](https://github.com/0rtis/dfk/blob/master/LICENSE)
[![Follow @trwitter handle](https://img.shields.io/twitter/follow/ortis95.svg?style=flat-square)](https://twitter.com/intent/follow?screen_name=ortis95) 


## DefiKingdoms contract

This is a simple toolbox to interact with the contracts of [DefiKingdoms](https://defikingdoms.com/)

*This software is not endorsed by, directly affiliated with, maintained, authorized, or sponsored by the DefiKingdoms team.
All product and company names are the registered trademarks of their original owners.
The use of any trade name or trademark is for identification and reference purposes only and does not imply any association with the trademark holder of their product brand.*

<br/>

*If you like this project, consider supporting future developments with a donation **0xA68fBfa3E0c86D1f3fF071853df6DAe8753095E2***

<br/>

### Hero contract
The hero contract is accessible with `hero/hero.py`

#### Quickstart
```
if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-hero")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    with open('hero/femaleFirstName.json', 'r') as f:
        female_first_names = hero_utils.parse_names(f.read())
    logger.info("Female hero first name loaded")

    with open('hero/maleFirstName.json', 'r') as f:
        male_first_names = hero_utils.parse_names(f.read())
    logger.info("Male hero first name loaded")

    with open('hero/lastName.json', 'r') as f:
        last_names = hero_utils.parse_names(f.read())
    logger.info("Hero last name loaded")

    # transfer(1, 'private key of the owner', 'next nonce of owner account', 'receiver address', 200, rpc_server, hero_abi_json, logger)

    for i in range(1, 100):
        logger.info("Processing hero #"+str(i))
        owner = heroes.get_owner(i, rpc_server)
        hero = heroes.get_hero(i, rpc_server)
        readable_hero = heroes.human_readable_hero(hero, male_first_names, female_first_names, last_names)
        logger.info(json.dumps(readable_hero, indent=4, sort_keys=False) + "\n Owned by " + owner)

```

#### Transfer
Transfer a hero from one address to another

#### Info
Hero's data can be retrieved with the `get_hero` method. A more *human-friendly* format can be generated 
by passing the result of `get_hero` to the `human_readable_hero` method.

#### Owner
The owner of a hero can be retrieved with the method `get_owner`


### Profile contract
The profile contract is accessible with `profile/profile.py`

#### Quickstart
```
if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-profile")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    profile = profiles.get_profile('0x2E7669F61eA77F02445A015FBdcFe2DE47083E02', rpc_server)

    logger.info(json.dumps(profile, indent=4, sort_keys=False))
```

#### In-game profile
In-game profile can be retrieved with the `get_profile` method


### Summoning contract
The summoning contract is accessible with `summoning/summoning.py`

#### Quickstart
```
if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-summoning")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    #summoning.summon_crystal(hero_id_1, hero_id_2, hero1_tears, hero2_tears, private_key, nonce, gas_price_gwei, 30, rpc_address, logger)

    crystals = summoning.get_user_crystal_ids('0x2E7669F61eA77F02445A015FBdcFe2DE47083E02', rpc_server)
    logger.info("Crystal ids: " + str(crystals))

    #summoning.open_crystal(crystals[0], private_key, nonce, gas_price_gwei, 30, rpc_address, logger)
```

#### Create crystal
Summoning crystal are created with `summon_crystal` method

#### Crystal id
Crystal id can be retrieved with `get_user_crystal_ids` method

#### Open summoning crystal
Summoning crystal can be open with `open_crystal` method


### Gene science contract
The gene science contract is accessible with `genes/gene_science.py`

#### Quickstart
```
if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-genes")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)
    w3 = Web3(Web3.HTTPProvider(rpc_server))

    hero1 = heroes.get_hero(1, rpc_server)
    hero2 = heroes.get_hero(2, rpc_server)

    bnum = w3.eth.block_number
    for i in range(10):
        print(str(bnum))
        offspring_stat_genes = genes.mix_genes(hero1['info']['statGenes'], hero2['info']['statGenes'], bnum, rpc_server)
        offspring_visual_genes = genes.mix_genes(hero1['info']['visualGenes'], hero2['info']['visualGenes'], bnum, rpc_server)
        stats = hero_utils.parse_stat_genes(offspring_stat_genes)
        visual = hero_utils.parse_visual_genes(offspring_visual_genes)
        logger.info("Iteration " + str(i) + "\n\tStats:\t" + str(stats) + "\n\tVisual:\t" + str(visual))
        while w3.eth.block_number == bnum:
            time.sleep(2)
        bnum = w3.eth.block_number
```

#### Mix genes
Statistics and visual of summoned hero can be forecasted with the `mix_genes` method.
Note that `mix_genes` is pseudo random and the resulting traits will be different for each block.
However, a statistical analysis can be used to optimize the summoning the desirable traits

### Auction contract
The sale auction contract is accessible with `auction/sale/sale_auctions.py`

Rent auctions can be listed with `auction/rent/rent_auctions.py`

#### Quickstart
```
if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-auctions")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    graphql = 'http://graph3.defikingdoms.com/subgraphs/name/defikingdoms/apiv5'

    auctions = sales.get_recent_open_auctions(graphql, 10)
    logger.info("Recent sale auctions:")
    for auction in auctions:
        logger.info(str(auction))

    # sale.bid_hero(hero_id, ether2wei(100), prv_key, nonce, gas_price_gwei, rpc_server, logger)

    logger.info("\n")
    logger.info("Recent rental auctions:")
    auctions = rental.get_recent_open_auctions(graphql, 10)
    for auction in auctions:
        logger.info(str(auction))
```

#### Sale auction
`bid_hero` and `get_auction` interact directly with the contract.

`get_recent_open_auctions` and `get_hero_open_auctions` use Graphql.

#### Rent auction
`get_recent_open_auctions` and `get_hero_open_auctions` use Graphql.



### Wishing well quest contract
The wishing well quest contract is accessible with `quest/wishing_well.py`

#### Quickstart
```
if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-wishing well quest")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    level = wishing_well.quest_level(rpc_server)
    logger.info("Quest level "+str(level))

    hero_id = 1
    stamina = wishing_well.get_current_stamina(hero_id, rpc_server)
    logger.info("Current stamina on hero " + str(hero_id) + ": " + str(stamina))

    # w3 = Web3(Web3.HTTPProvider(rpc_server))
    # account_address = w3.eth.account.privateKeyToAccount(private_key).address
    # w3.eth.getTransactionCount(account_address)
    # wishing_well.start_quest(hero_id, 5, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, rpc_server, logger)
    # quest_id = hero_to_quest(hero_id, rpc_server)
    # time.sleep(30)
    # complete_quest(hero_id, prv, w3.eth.getTransactionCount(account_address), gas_price_gwei, rpc_server, logger)
```

#### Questing flow
The wishing well quest requires at least 5 stamina to complete. Check the current stamina of any given hero with `get_current_stamina`.
Start the quest with `start_quest`. The second parameter is the number of attempt. To optimize the cost of gas, it is recommended
to use a hero at full stamina (25) and do 5 attempts every call.

Once the quest is started, you can retrieve the quest_id with `hero_to_quest`.
There is a delay of 10-30 seconds before you can complete the quest with `complete_quest`





