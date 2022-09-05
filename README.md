
[![Pypi_repo](https://img.shields.io/pypi/v/dfktools?style=flat-square)](https://pypi.org/project/dfktools/)
[![GitHub license](https://img.shields.io/github/license/0rtis/dfktools.svg?style=flat-square)](https://github.com/0rtis/dfktools/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/0rtis?style=flat-square)](https://github.com/0rtis)
[![Join Discord](https://img.shields.io/discord/932350221256638564?label=discord&style=flat-square)](https://discord.gg/BMWKgZSXqJ)
[![Follow @twitter handle](https://img.shields.io/twitter/follow/Knockturn_io.svg?style=flat-square)](https://twitter.com/intent/follow?screen_name=ortis95)


## DefiKingdoms contract

This is a simple toolbox to interact with the contracts of [DefiKingdoms](https://defikingdoms.com/)

*This software is not endorsed by, directly affiliated with, maintained, authorized, or sponsored by the DefiKingdoms team.
All product and company names are the registered trademarks of their original owners.
The use of any trade name or trademark is for identification and reference purposes only and does not imply any association with the trademark holder of their product brand.*

<br/>

**Like this project ? Consider supporting future developments by:**
- Delegating AVAX to our Avalanche node **NodeID-4btZGj8TmrycK22kwgBK5wJEFighAFWiZ**
- Delegating ADA to our [Cardano node [KTA]](https://pooltool.io/pool/991a64a6e3d866f4af4e0a2bfd61c15486a47ccc352e61e8a6b4fef8) **991a64a6e3d866f4af4e0a2bfd61c15486a47ccc352e61e8a6b4fef8**
- Making a donation to **0xA68fBfa3E0c86D1f3fF071853df6DAe8753095E2**


### Code guidelines
1. Indent with Tab
2. 1 empty line within a function, 2 empty lines between function
3. Use *trait(s)* to name any or all of the 8 value `strength, agility, intelligence, wisdom, luck, vitality, endurance, dexterity`
4. Use *ability(ies)* to name any or all of the 4 value `passive1, passive2, active1, active2`
5. Use *stat(s)* as a generic term for any or all the characteristics of a hero (traits, abilities, HP, MP, stamina, etc)
6. A function should support all realms, except if contracts differs across realms
7. All hardcoded addresses should be [CheckSummed](https://ethsum.netlify.app/)
8. Use `logging`, not `print`
9. No other third-party libraries (if really needed, please explain why in the PR)
10. A short & meaningful comment is superior to a long & unfathomable documentation

<br/>

### Hero contract
The hero contract is accessible with [hero/hero.py](src/dfktools/hero/hero.py)

#### Quickstart
[hero_example.py](src/dfktools/hero_example.py)

#### Transfer
Transfer a hero from one address to another

#### Info
Hero's data can be retrieved with the `get_hero` method. A more *human-friendly* format can be generated 
by passing the result of `get_hero` to the `human_readable_hero` method.

#### Owner
The owner of a hero can be retrieved with the method `get_owner`


### Profile contract
The profile contract is accessible with [profile/profile_v2.py](src/dfktools/profile/profile_v2.py)

#### Quickstart
[profile_example.py](src/dfktools/profile_example.py)

#### In-game profile
In-game profile can be retrieved with the `get_profile` method


### Summoning contract
The summoning contract is accessible with [summoning/summoning.py](src/dfktools/summoning/summoning.py)

#### Quickstart
[summoning_example.py](src/dfktools/summoning_example.py)

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
The gene science contract is accessible with [genes/gene_science_v2.py](src/dfktools/genes/gene_science_v2.py)

#### Quickstart
[genes_example.py](src/dfktools/genes_example.py)

#### Mix genes
Statistics and visual of summoned hero can be forecasted with the `mix_genes` method.
Note that `mix_genes` is pseudo random and the resulting traits will be different for each block.
However, a statistical analysis can be used to optimize the summoning of desirable traits

### Auction contract
The hero sale auction contract is accessible with [auctions/hero/sale_auctions.py](src/dfktools/auctions/hero/sale_auctions.py)
The hero rent auction contract is accessible with [auctions/hero/rent_auctions.py](src/dfktools/auctions/hero/rent_auctions.py)
Generic sale auction (ex: land) contract are accessible with [auctions/auction.py](src/dfktools/auctions/auction.py)

#### Quickstart
[auction_example.py](src/dfktools/auction_example.py)
[land_example.py](src/dfktools/land_example.py)
#### Sale auction
`bid_hero` and `get_auction` interact directly with the contract.

`get_recent_open_auctions` and `get_hero_open_auctions` use Graphql.

#### Rent auction
`get_recent_open_auctions` and `get_hero_open_auctions` use Graphql.



### Quest
All quest contracts are located in module [quests](src/dfktools/quests)

#### Quickstart
[quest_example.py](src/dfktools/quest_example.py)

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
[wishing_well_quest_example.py](src/dfktools/wishing_well_quest_example.py)


### DEX & tokens
In game tokens and AMM exchange are available in module [dex](src/dfktools/dex)

#### Quickstart
[dex_example.py](src/dfktools/dex_example.py)

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
Meditation circle contract is accessible with [meditation/meditation.py](src/dfktools/meditation/meditation.py)

#### Quickstart
[meditation_example.py](src/dfktools/meditation_example.py)

#### Hero level up
Use `start_meditation` and `complete_meditation` to level up a hero. Make sure to have enough rune for the hero's level with `get_required_runes`


### Duel
All duel contracts are located in module [duel](src/dfktools/duel)

#### Quickstart
[duel_example.py](src/dfktools/duel_example.py)


### Raffle master
All raffle contracts are located in module [raffle](src/dfktools/raffle)

#### Quickstart
[raffle_example.py](src/dfktools/raffle_example.py)


### Pets
All pet related contracts are located in module [pets](src/dfktools/pets)

Use [pet.py](src/dfktools/pets/pet.py) to manage pet NFT

Use [hatchery.py](src/dfktools/pets/hatchery.py) to hatch pet egg

Use [exchange.py](src/dfktools/pets/exchange.py) to exchange 2 pets for an egg

#### Quickstart
[pet_example.py](src/dfktools/pet_example.py)

### Bridge
All bridge contracts are located in module [bridge](src/dfktools/bridge)

**Be careful to not mix up RPCs when dealing with multichain transaction**

#### Quickstart
[bridge_example.py](src/dfktools/bridge_example.py)



