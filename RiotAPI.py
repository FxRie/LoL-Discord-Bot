import requests
import RiotConsts as Consts
import time
#import Main

class RiotAPI:

    global apiRequestsCounter1
    global apiRequestsCounter2
    apiRequestsCounter1 = 0
    apiRequestsCounter2 = 0
    global intervalStartTimeStamp1
    global intervalStartTimeStamp2
    intervalStartTimeStamp1 = None
    intervalStartTimeStamp2 = None

    def __init__(self, api_key):
        self.api_key = api_key

    def ResetRequestCounter1(self):
        global apiRequestsCounter1
        apiRequestsCounter1 = 0

    def ResetRequestCounter2(self):
        global apiRequestsCounter2
        apiRequestsCounter2 = 0

    #Limit: 20 requests every 1 seconds & 100 requests every 2 minutes
    def EnsureRateLimitCondition(self, resetGlobalVariableMethod, intervalStartTimeStamp, timeFrame, apiRequestsCounter, allowedRequestsForCondition):
        if intervalStartTimeStamp == None:
            intervalStartTimeStamp = time.time()
        timePassed = intervalStartTimeStamp - time.time()
        if (timePassed > timeFrame):
            intervalStartTimeStamp = time.time()
        if (timePassed < timeFrame) and apiRequestsCounter >= allowedRequestsForCondition:
            print("Time Sleeper is active for " + str(timeFrame - (timePassed)) + " Seconds.")
            time.sleep(timeFrame - (timePassed))
            intervalStartTimeStamp = time.time()
            resetGlobalVariableMethod()
            #self.apiRequestsCounter = 0

    def EnsureRateLimit(self):
        global intervalStartTimeStamp1
        global apiRequestsCounter1
        self.EnsureRateLimitCondition(self.ResetRequestCounter1, intervalStartTimeStamp1, 1, apiRequestsCounter1, 20)
        global intervalStartTimeStamp2
        global apiRequestsCounter2
        self.EnsureRateLimitCondition(self.ResetRequestCounter2, intervalStartTimeStamp2, 120, apiRequestsCounter2, 100)

    def _request(self, api_url, params={}):
        global apiRequestsCounter1
        global apiRequestsCounter2
        self.EnsureRateLimit()
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(url=api_url),
            params=args
            )
        apiRequestsCounter1 += 1
        apiRequestsCounter2 += 1
        print(str(apiRequestsCounter1) + " API Request(s) were performed in a timespan of 1 second.")
        print(str(apiRequestsCounter2) + " API Request(s) were performed in a timespan of 2 minutes.")
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
