[![GitHub license](https://img.shields.io/github/license/0rtis/dfk.svg?style=flat-square)](https://github.com/0rtis/dfk/blob/master/LICENSE)
[![Follow @trwitter handle](https://img.shields.io/twitter/follow/ortis95.svg?style=flat-square)](https://twitter.com/intent/follow?screen_name=ortis95) 


## DefiKingdoms contract

This is a simple toolbox to interact with the contracts of [DefiKingdoms](https://defikingdoms.com/)

*This software is not endorsed by, directly affiliated with, maintained, authorized, or sponsored by the DefiKingdoms team.
All product and company names are the registered trademarks of their original owners.
The use of any trade name or trademark is for identification and reference purposes only and does not imply any association with the trademark holder of their product brand.*


### Hero contract

#### Quickstart
```
if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK hero")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'

    logger.info("Using RPC server " + rpc_server)

    with open('hero.abi', 'r') as f:
        hero_abi_json = f.read()
    logger.info("Hero contract ABI loaded")

    with open('femaleFirstName.json', 'r') as f:
        female_first_names = json.load(f)
    logger.info("Female hero first name loaded")

    with open('maleFirstName.json', 'r') as f:
        male_first_names = json.load(f)
    logger.info("Male hero first name loaded")

    with open('lastName.json', 'r') as f:
        last_names = json.load(f)
    logger.info("Hero last name loaded")

    # transfer(1, 'private key of the owner', 'next nonce of owner account', 'receiver address', 200, rpc_server, hero_abi_json, logger)

    for i in range(1, 2074):
        logger.info("Processing hero #"+str(i))
        owner = get_owner(i, rpc_server, hero_abi_json)
        hero = get_hero(i, rpc_server, hero_abi_json)
        readable_hero = human_readable_hero(hero, male_first_names, female_first_names, last_names)
        logger.info(json.dumps(readable_hero, indent=4, sort_keys=False) + "\n Owned by " + owner)
```

#### Transfer
**It is strongly recommended to wait for an official method to transfer heroes. Use the transfer function of this script at your own risk**

At the time of writing (October 3thd 2021), it is not yet possible to transfer heroes from within the game.
However, there is no limitation on the contract itself and heroes can be transferred with the `transfer` method

#### Info
Hero's data can be retrieved with the `get_hero` method. A more *human-friendly* format can be generated 
by passing the result of `get_hero` to the `human_readable_hero` method.

#### Owner
The owner of a hero can be retrieved with the method `get_owner`


### Profile contract

#### Quickstart
```
if __name__ == "__main__":
    log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

    logger = logging.getLogger("DFK profile")
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

    rpc_server = 'https://api.harmony.one'

    logger.info("Using RPC server " + rpc_server)

    with open('profile.abi', 'r') as f:
        profile_abi_json = f.read()
    logger.info("Profile contract ABI loaded")

    profile = get_profile('0x2E7669F61eA77F02445A015FBdcFe2DE47083E02', rpc_server, profile_abi_json)

    logger.info(json.dumps(profile, indent=4, sort_keys=False))
```

#### In-game profile
In-game profile can be retrieved with the `get_profile` method


<br/>
<br/>


*If you like this project, consider supporting future developments with a donation 0xA68fBfa3E0c86D1f3fF071853df6DAe8753095E2*


