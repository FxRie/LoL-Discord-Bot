import requests
import RiotConsts as Consts
#import Main

class RiotAPI(object):

    #def __init__(self, api_key, summ_id=Consts.SUMMONER_ID['U WAN SUM FUK'], acc_id=Consts.ACCOUNT_ID['U WAN SUM FUK'], mat_id=Consts.MATCH_ID['U WAN SUM FUK']):
    def __init__(self, api_key):
        self.api_key = api_key
        #self.summoner_id = summ_id
        #self.account_id = acc_id
        #self.match_id = mat_id

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(url=api_url),
            params=args
            )
        #print("Response URL: " + response.url)
        return response.json()

    def get_league_by_summonerID(self, s_id):
        api_url = Consts.URL['league_by_summonerID'].format(
            version=Consts.API_VERSIONS['summoner'],
            encryptedSummonerId=s_id
            )
        return self._request(api_url)

    def get_matches_by_accountID(self, a_id):
        api_url = Consts.URL['matches_by_accountID'].format(
            encryptedAccountId=a_id
            )
        return self._request(api_url)

    def get_match_by_matchID(self, m_id):
        api_url = Consts.URL['match_by_matchID'].format(
            matchId=m_id
            )
        return self._request(api_url)

    def get_accountID_by_summonerID(self, s_na):
        api_url = Consts.URL['accountID_by_summonerName'].format(
            summonerName=s_na
        )
        return self._request(api_url)
