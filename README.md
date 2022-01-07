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

#### Rent auction
Put a hero up for hire with `put_hero_for_rent`  and cancel with `cancel_rent`
Use `is_on_rent` and `get_rent_auction` to monitor auction


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
However, a statistical analysis can be used to optimize the summoning of desirable traits

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



### Quest
All quest contracts are located in module `quest`

#### Quickstart
```
if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-quest")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    private_key = None  # set private key
    gas_price_gwei = 15
    tx_timeout = 30
    w3 = Web3(Web3.HTTPProvider(rpc_server))
    account_address = w3.eth.account.privateKeyToAccount(private_key).address

    quest = Quest(rpc_server, logger)

    quest_contract = fishing.CONTRACT_ADDRESS  # foraging.CONTRACT_ADDRESS
    my_heroes_id = [1, 2, 3, 4]
    quest.start_quest(quest_contract, my_heroes_id, 3, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, tx_timeout)
    quest_info = quest_utils.human_readable_quest(quest.get_hero_quest(my_heroes_id[0]))

    logger.info(
        "Waiting " + str(quest_info['completeAtTime'] - time.time()) + " secs to complete quest " + str(quest_info))
    while time.time() < quest_info['completeAtTime']:
        time.sleep(2)

    tx_receipt = quest.complete_quest(my_heroes_id[0], private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, tx_timeout)
    quest_result = quest.parse_complete_quest_receipt(tx_receipt)
    logger.info("Rewards: " + str(quest_result))


    # gardening quest
    pool_id = 0  # See gardens.master_gardener
    quest_data = (pool_id, 0, 0, 0, 0, 0, '', '', ZERO_ADDRESS, ZERO_ADDRESS, ZERO_ADDRESS, ZERO_ADDRESS)
    my_gardener_heroes_id = [5]
    quest.start_quest_with_data(gardening.CONTRACT_ADDRESS, quest_data, my_gardener_heroes_id, 1, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, tx_timeout)
    quest_info = quest_utils.human_readable_quest(quest.get_hero_quest(my_heroes_id[0]))

    logger.info(
        "Waiting " + str(quest_info['completeAtTime'] - time.time()) + " secs to complete gardening quest " + str(quest_info))
    while time.time() < quest_info['completeAtTime']:
        time.sleep(2)

    quest.complete_quest(my_gardener_heroes_id[0], private_key, w3.eth.getTransactionCount(account_address),
                                      gas_price_gwei, tx_timeout)
```

#### Foraging & Fishing quest
Each quest requires at least 7 stamina to complete. Check the current stamina of any given hero with `get_current_stamina`.
Start the quest with `start_quest`. The second parameter is the number of attempt. To optimize the cost of gas, it is recommended
to use a hero at full stamina and do 3 attempts every call.


#### Gardening & Mining quest
Gardening and mining quest can be started with just one stamina. 
Mining quest can be done with up to 6 heroes while only 1 hero at a time can be sent on a gardening quest to a specific garden (liquidity pool).


#### Legacy wishing well quest
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

    hero_id = 1  # <your hero id here>
    stamina = wishing_well.get_current_stamina(hero_id, rpc_server)
    logger.info("Current stamina on hero " + str(hero_id) + ": " + str(stamina))

    #w3 = Web3(Web3.HTTPProvider(rpc_server))
    #gas_price_gwei = 10
    #private_key = # set private key
    #account_address = w3.eth.account.privateKeyToAccount(private_key).address
    #wishing_well.start_quest(hero_id, 5, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, 30, rpc_server, logger)
    #time.sleep(60)
    #tx_receipt = wishing_well.complete_quest(hero_id, private_key, w3.eth.getTransactionCount(account_address), gas_price_gwei, 30, rpc_server, logger)

    #quest_result = wishing_well.parse_complete_quest_receipt(tx_receipt, rpc_server)
    #logger.info("Quest earned " + str(quest_result['tear']) + " tears and " + str(quest_result['xp']) + " xp")

```


### DEX & tokens
In game tokens and AMM exchange are available in module `dex`

#### Quickstart
```
if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-DEX")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    w3 = Web3(Web3.HTTPProvider(rpc_server))

    user_address = '0x2E7669F61eA77F02445A015FBdcFe2DE47083E02'

    # Automated Market Making pool
    logger.info("Liquidity pool count:\t" + str(market_place_factory.all_pairs_length(rpc_server)))
    liquidity_pool_id = 0
    liquidity_pool_address = market_place_factory.all_pairs(liquidity_pool_id, rpc_server)
    liquidity_pool = pool.UniswapV2Pair(liquidity_pool_address, rpc_server, logger)
    liquidity_pool_symbol = liquidity_pool.symbol()
    liquidity_pool_token0_address = liquidity_pool.token_0()
    liquidity_pool_token0 = erc20.symbol(liquidity_pool_token0_address, rpc_server)
    logger.info(liquidity_pool_token0 + " user balance:\t" + str(erc20.wei2eth(w3, erc20.balance_of(user_address, liquidity_pool_token0_address, rpc_server))))
    liquidity_pool_token1_address = liquidity_pool.token_1()
    liquidity_pool_token1 = erc20.symbol(liquidity_pool_token1_address, rpc_server)
    logger.info(liquidity_pool_token1 + " user balance:\t" + str(erc20.wei2eth(w3, erc20.balance_of(user_address, liquidity_pool_token1_address, rpc_server))))
    amount_token1 = 1
    amount_token0 = erc20.wei2eth(w3, liquidity_pool.expected_amount0(erc20.eth2wei(w3, amount_token1)))
    logger.info(liquidity_pool_symbol + " " + liquidity_pool_token0 + "-" + liquidity_pool_token1 + " @ " + str(amount_token0) + " " + liquidity_pool_token0 + " per " + liquidity_pool_token1)

    liquidity_pool_balance = liquidity_pool.balance_of(user_address)
    logger.info("LP user balance:\t" + str(erc20.wei2eth(w3, liquidity_pool_balance)))

    # Garden staking
    logger.info("Staking pool count:\t" + str(gardens.pool_length(rpc_server)))
    staking_pool = gardens.Garden(liquidity_pool, rpc_server, logger)
    staking_pool_symbol = staking_pool.symbol()
    staking_pool_token0 = erc20.symbol(staking_pool.token_0(), rpc_server)
    staking_pool_token1 = erc20.symbol(staking_pool.token_1(), rpc_server)
    staking_pool_total_supply = staking_pool.total_supply()
    logger.info(staking_pool_symbol + " " + staking_pool_token0 + "-" + staking_pool_token1 + ", total supply="
                + str(erc20.wei2eth(w3,staking_pool_total_supply)))
    staking_pool_user = utils.human_readable_user_info(staking_pool.user_info(user_address))
    staking_pool_balance = gardens.Garden.user_info_lp_balance(staking_pool_user)
    staking_pool_share = staking_pool_balance/staking_pool_total_supply
    logger.info("LP staked user balance:\t" + str(erc20.wei2eth(w3, staking_pool_balance)) + " (pool share " + str(round(100 * staking_pool_share, 2)) + "%)")

    # Swap JEWEL for ONE
    #private_key = None #set private key of to swap coin from
    #account_address = w3.eth.account.privateKeyToAccount(private_key).address
    #market_place_router.swap_exact_tokens_for_eth(erc20.eth2wei(w3, 1), 60, [erc20.JEWEL, market_place_router.weth(rpc_server)], account_address,
    #                                 int(time.time() + 60), private_key, w3.eth.getTransactionCount(account_address),
    #                                 w3.fromWei(w3.eth.gas_price, 'gwei'), 30, rpc_server, logger)
```
#### Balance of token
Use `dex.erc20.balance_of` to retrieve the balance of an item for the specified address

#### Liquidity pool
Use wrapper class `dex.uniswap_v2_pair.UniswapV2Pair` and call  `expected_amount0` to get the estimated amount of `token0` received in exchange of `token1`.
Alternatively, call `dex.uniswap_v2_router.quote`

#### Swap token
Use call `dex.uniswap_v2_router.swap_exact_tokens_for_eth` to swap erc20 token for ONE.
Use call `dex.uniswap_v2_router.swap_exact_tokens_for_tokens` to swap erc20 tokens for other erc20 tokens.

#### Staking pool
Use wrapper class `dex.master_gardener.Garden` to retrieve staking pool info


### Meditation circle
Meditation circle contract is available in module `meditation`

#### Quickstart
```
if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK-meditation")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'
    logger.info("Using RPC server " + rpc_server)

    private_key = None  # set private key
    account_address = '0x2E7669F61eA77F02445A015FBdcFe2DE47083E02'
    gas_price_gwei = 10
    tx_timeout_seconds = 30
    w3 = Web3(Web3.HTTPProvider(rpc_server))

    active_meditations = meditation.get_active_meditations(account_address, rpc_server)
    logger.info("Pending meditation on address " + str(account_address) + ": "+str(active_meditations))

    level = 1
    hero_id = 1
    required_runes = meditation.get_required_runes(level, rpc_server)
    meditation.start_meditation(1, meditation.stat2id('strength'), meditation.stat2id('endurance'), meditation.stat2id('luck'),
                               meditation.ZERO_ADDRESS, private_key, w3.eth.getTransactionCount(account_address),
                               gas_price_gwei, tx_timeout_seconds, rpc_server, logger)
    hero_meditation = meditation.get_hero_meditation(hero_id, rpc_server)
    logger.info("Pending meditation "+str(hero_meditation))
    time.sleep(5)
    meditation.complete_meditation(hero_id, private_key, w3.eth.getTransactionCount(account_address),
                                  gas_price_gwei, tx_timeout_seconds, rpc_server, logger)
```
#### Hero level up
Use `start_meditation` and `complete_meditation` to level up a hero. Make sure to have enough rune for the hero's level with `get_required_runes`




