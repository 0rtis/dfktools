[![GitHub license](https://img.shields.io/github/license/0rtis/dfk.svg?style=flat-square)](https://github.com/0rtis/dfk/blob/master/LICENSE)
[![Follow @trwitter handle](https://img.shields.io/twitter/follow/0rtis.svg?style=flat-square)](https://twitter.com/intent/follow?screen_name=ortis95) 


## DefiKingdoms hero's contract

This is a simple toolbox to interact with the hero's contract of [DefiKingdoms](https://defikingdoms.com/)

*This software is not endorsed by, directly affiliated with, maintained, authorized, or sponsored by the DefiKingdoms team.
All product and company names are the registered trademarks of their original owners.
The use of any trade name or trademark is for identification and reference purposes only and does not imply any association with the trademark holder of their product brand.*

### Hero transfer
**I strongly recommend to wait for an official method to transfer heroes. Use the transfer function of this script at your own risk**

At the time of writing (October 3thd 2021), it is not yet possible to transfer heroes from within the game.
However, there is no limitation on the contract itself and heroes can be transferred with the `transfer` method

### Hero info
Hero's data can be retrieved with the `read_from_contract` method. A more *human-friendly* format can be generated 
by passing the result of `read_from_contract` to the `human_readable_hero` method