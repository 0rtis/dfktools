import requests

AUCTIONS_OPEN_GRAPHQL_QUERY = """
                        query {
                          assistingAuctions(skip: %d, first: %d, orderBy: startedAt, orderDirection: desc, where: {open: true}) {
                            id
                            seller {
                                name
                            }
                            tokenId {
                              id
                              owner {
                                owner
                              }                        
                              statGenes
                              generation
                              rarity
                              mainClass
                              subClass
                              summons
                              maxSummons
                              summonerId {
                                id
                              }
                              assistantId {
                                id
                              }
                            }
                            startingPrice
                            endingPrice
                            startedAt
                            duration
                            winner {
                              id
                              name
                            }
                            open
                            
                          }
                          
                        }
                        """


def get_open_auctions(graphql_address, skip=0, count=1000):

    r = requests.post(graphql_address, json={'query': AUCTIONS_OPEN_GRAPHQL_QUERY % (skip, count)})
    if r.status_code != 200:
        raise Exception("HTTP error " + str(r.status_code) + ": " + r.text)
    data = r.json()
    return data['data']['assistingAuctions']
