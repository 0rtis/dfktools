import logging
from web3 import Web3
import sys
import time
import hero.hero as heroes
import hero.utils.utils as hero_utils
import genes.gene_science as genes


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
