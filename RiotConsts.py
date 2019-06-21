#General: https://euw1.api.riotgames.com/lol/league/v4/positions/by-summoner/zx3MATXao0uMV-q7F-_LDB_0mu5vqb4zuecBl7pXS78GTyA
#League: /lol/league/v4/positions/by-summoner/{encryptedSummonerId}

URL = {
    'base': 'https://euw1.api.riotgames.com/{url}',
    'league_by_summonerID': 'lol/league/{version}/positions/by-summoner/{encryptedSummonerId}',
    'matches_by_accountID': '/lol/match/v4/matchlists/by-account/{encryptedAccountId}',
    'match_by_matchID': '/lol/match/v4/matches/{matchId}',
    'accountID_by_summonerName': '/lol/summoner/v4/summoners/by-name/{summonerName}'
}

SUMMONERS = {
    'Sandor': 'U WAN SUM FUK',
    'Felix': 'X1LEF',
    'Bene': ['Headchoto', 'Dwarfpain'],
    'Niklas': 'maduut',
    'Khoa': ['GODAMNITLEEROY', 'Sabokun', 'Xanthe7', 'Rodalindd'],
    'Nico': ['WATISDISIDUNEVEN', 'bewail8', 'ArthurqZe'],
    'Schmauder': 'Shinsaru'
}

SUMMONER_ID = {
    'U WAN SUM FUK': '',
    'X1LEF': '',
    'Headchoto': '',
    'maduut': '',
    'GODAMNITLEEROY': '',
    'Sabokun': '',
    'Xanthe7': '',
    'Rodalindd': '',
    'WATISDISIDUNEVEN': '',
    'bewail8': '',
    'ArthurqZe': '',
    'SHîNSARU': '',
    'FreewayRBL': '',
    'Dwarfpain': '',
    'aXonEE': ''
}

ACCOUNT_ID = {
    'U WAN SUM FUK': 'mRf_Hr2eE5CIe-AVfiGEkmyIiX5KwWFH2-OeilK0m9IqdA',
    'X1LEF': 'glPJYuIppEvjF-DI2r3K38JzG5VGpyqFatB0i0PS4qwhSg',
    'Headchoto': '_Dggu7n6jpZQFr_MnM_lgMQJ_pILV1pDoCTNYFDiqSyf5g',
    'maduut': 'uXrK5v4HlHUoOU_q2K5iH448miyzXSj_hEM_qNASJklzqtg',
    'GODAMNITLEEROY': 'yecLd-vyyhJ_ENGju2wzWGEBf9ATf2MHfuyStpPtVw2Twg',
    'Sabokun': 'ScrZfJ6lwV2mgJfqCvLk0Lulupflxr1aHH0FYdKyzMlW-g',
    'Xanthe7': 'o-t2TWKvJrvA-1lEallsU7tkK9H6oOdVoCeH5OstEmD6ArM',
    'Rodalindd': 'UW2dHYXY_PC1RBjxbHaALA_I9en5CUYY92-VuTjbL-Br224',
    'WATISDISIDUNEVEN': 'X5EMFjA56oSCIO5DPDTXDZNrY35E7dbs4o7HzOy51ZxFUw',
    'bewail8': 'uNMBkvWUbuclPqECR9AjqHgXSt5au1wNKdsCj6frIOHRPZE',
    'ArthurqZe': 'QgmXWMShNCLcZO6K8wW_3lY8Ad_Ph5GWasg20qMf3rwsGPQ',
    'SHÎNSARU': 'Iha49wHtM6R8_NiFk0VoYRvuHzfvP18FonWJ8xIZKHYzng',
    'FreewayRBL': 'a5f7f-WaBlx_PphC08VNa-cL8Xiu8u8yVJeafIKBF0D1tw',
    'Dwarfpain': 'RQjWAS-4GR-qfI3C5bvdM8gqivBwiK2JqwaYwCpli802Jg',
    'aXonEE': 'bJt5EV_efoNGtfT5TAkeqgbt43m9fzVTIyVnUk3puR03rg'
}
#'U WAN SUM FUK'.encode(encoding='UTF-8',errors='strict')          (???)

#Newest Match Only
MATCH_ID = {
    'U WAN SUM FUK': '4062201614',
    'X1LEF': '',
    'Headchoto': '',
    'maduut': '',
    'GODAMNITLEEROY': '',
    'Sabokun': '',
    'Xanthe7': '',
    'Rodalindd': '',
    'WATISDISIDUNEVEN': '',
    'bewail8': '',
    'ArthurqZe': '',
    'SHÎNSARU': '',
    'FreewayRBL': '',
    'Dwarfpain': '',
    'aXonEE': ''
}

PLAYER_INDEX = {
    'U WAN SUM FUK': '0',
    'X1LEF': '1',
    'Headchoto': '2',
    'maduut': '3',
    'GODAMNITLEEROY': '4',
    'Sabokun': '5',
    'Xanthe7': '6',
    'Rodalindd': '7',
    'WATISDISIDUNEVEN': '8',
    'bewail8': '9',
    'ArthurqZe': '10',
    'SHÎNSARU': '11',
    'FreewayRBL': '12',
    'Dwarfpain': '13',
    'aXonEE': '14'
}

API_VERSIONS = {
    'summoner': 'v4'
}


