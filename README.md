[![GitHub license](https://img.shields.io/github/license/0rtis/dfk.svg?style=flat-square)](https://github.com/0rtis/dfk/blob/master/LICENSE)
[![Follow @trwitter handle](https://img.shields.io/twitter/follow/ortis95.svg?style=flat-square)](https://twitter.com/intent/follow?screen_name=ortis95) 


## DefiKingdoms contract

This is a simple toolbox to interact with the contracts of [DefiKingdoms](https://defikingdoms.com/)

*This software is not endorsed by, directly affiliated with, maintained, authorized, or sponsored by the DefiKingdoms team.
All product and company names are the registered trademarks of their original owners.
The use of any trade name or trademark is for identification and reference purposes only and does not imply any association with the trademark holder of their product brand.*

<br/>

**Like this project ? Consider supporting future developments by:**
- Delegating AVAX to our Avalanche node **NodeID-4btZGj8TmrycK22kwgBK5wJEFighAFWiZ**
- Delegating ONE to our Harmony node **one1s7v3eq6l03zvjlt4h05pz8l6nmq306hyqf6hk0**
- Delegating ADA to our [Cardano node [WRLP]](https://pooltool.io/pool/991a64a6e3d866f4af4e0a2bfd61c15486a47ccc352e61e8a6b4fef8) **991a64a6e3d866f4af4e0a2bfd61c15486a47ccc352e61e8a6b4fef8**
- Making a donation to **0xA68fBfa3E0c86D1f3fF071853df6DAe8753095E2**


<br/>

### Hero contract
The hero contract is accessible with [hero/hero.py](https://github.com/0rtis/dfk/blob/master/hero/hero.py)

#### Quickstart
[hero_example.py](https://github.com/0rtis/dfk/blob/master/hero_example.py)

#### Transfer
Transfer a hero from one address to another

#### Info
Hero's data can be retrieved with the `get_hero` method. A more *human-friendly* format can be generated 
by passing the result of `get_hero` to the `human_readable_hero` method.

#### Owner
The owner of a hero can be retrieved with the method `get_owner`


### Profile contract
The profile contract is accessible with [profile/profile.py](https://github.com/0rtis/dfk/blob/master/profile/profile.py)

#### Quickstart
[profile_example.py](https://github.com/0rtis/dfk/blob/master/profile_example.py)

#### In-game profile
In-game profile can be retrieved with the `get_profile` method


### Summoning contract
The summoning contract is accessible with [summoning/summoning.py](https://github.com/0rtis/dfk/blob/master/summoning/summoning.py)

#### Quickstart
[summoning_example.py](https://github.com/0rtis/dfk/blob/master/summoning_example.py)

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
The gene science contract is accessible with [genes/gene_science_v2.py](https://github.com/0rtis/dfk/blob/master/genes/gene_science_v2.py)

#### Quickstart
[genes_example.py](https://github.com/0rtis/dfk/blob/master/genes_example.py)

#### Mix genes
Statistics and visual of summoned hero can be forecasted with the `mix_genes` method.
Note that `mix_genes` is pseudo random and the resulting traits will be different for each block.
However, a statistical analysis can be used to optimize the summoning of desirable traits

### Auction contract
The hero sale auction contract is accessible with [auctions/hero/sale_auctions.py](https://github.com/0rtis/dfk/blob/master/auctions/hero/sale_auctions.py)
The hero rent auction contract is accessible with [auctions/hero/rent_auctions.py](https://github.com/0rtis/dfk/blob/master/auctions/hero/rent_auctions.py)
Generic sale auction (ex: land) contract are accessible with [auctions/auction.py](https://github.com/0rtis/dfk/blob/master/auctions/auction.py)

#### Quickstart
[auction_example.py](https://github.com/0rtis/dfk/blob/master/auction_example.py)
[land_example.py](https://github.com/0rtis/dfk/blob/master/land_example.py)
#### Sale auction
`bid_hero` and `get_auction` interact directly with the contract.

`get_recent_open_auctions` and `get_hero_open_auctions` use Graphql.

#### Rent auction
`get_recent_open_auctions` and `get_hero_open_auctions` use Graphql.



### Quest
All quest contracts are located in module [quests](https://github.com/0rtis/dfk/blob/master/quests)

#### Quickstart
[quest_example.py](https://github.com/0rtis/dfk/blob/master/quest_example.py)

#### Foraging & Fishing quest
Each quest requires at least 7 stamina to complete. Check the current stamina of any given hero with `get_current_stamina`.
Start the quest with `start_quest`. The second parameter is the number of attempt. To optimize the cost of gas, it is recommended
to use a hero at full stamina and do 3 attempts every call.

Uses V2 quest


#### Gardening & Mining quest
Gardening and mining quest can be started with just one stamina. 
Mining quest can be done with up to 6 heroes while only 1 hero at a time can be sent on a gardening quest to a specific garden (liquidity pool).

Uses V1 quest

#### Legacy wishing well quest
[wishing_well_quest_example.py](https://github.com/0rtis/dfk/blob/master/wishing_well_quest_example.py)


### DEX & tokens
In game tokens and AMM exchange are available in module [dex](https://github.com/0rtis/dfk/blob/master/dex)

#### Quickstart
[dex_example.py](https://github.com/0rtis/dfk/blob/master/dex_example.py)

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
Meditation circle contract is accessible with [meditation/meditation.py](https://github.com/0rtis/dfk/blob/master/meditation/meditation.py)

#### Quickstart
[meditation_example.py](https://github.com/0rtis/dfk/blob/master/meditation_example.py)

#### Hero level up
Use `start_meditation` and `complete_meditation` to level up a hero. Make sure to have enough rune for the hero's level with `get_required_runes`




