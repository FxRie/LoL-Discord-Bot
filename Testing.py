import json
from RiotAPI import RiotAPI
import RiotConsts as Consts
import sys, getopt
import time

#Private file for individual use
import Private

api = RiotAPI(Private.apiKey)

inputFile = ''
outputFile = ''

defaultJsonFile = "Testing2.json"

url = {
    'base': 'https://euw1.api.riotgames.com/{url}',
    'league_by_summonerID': 'lol/league/{version}/positions/by-summoner/{encryptedSummonerId}',
    'matches_by_accountID': '/lol/match/v4/matchlists/by-account/{encryptedAccountId}',
    'match_by_matchID': '/lol/match/v4/matches/{matchId}',
    'accountID_by_summonerName': '/lol/summoner/v4/summoners/by-name/{summonerName}'
}

def ReadInputParams(argv):
    global inputFile
    global outputFile
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputFile> -o <outputFile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputFile> -o <outputFile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg
    if not outputFile and not inputFile:
        outputFile = defaultJsonFile
        inputFile = defaultJsonFile
    if not inputFile and outputFile:
        inputFile = outputFile
    if not outputFile and inputFile:
        outputFile = inputFile

    print('Input file is "%s"', inputFile)
    print('Output file is "', outputFile)

def WriteUsersToJson(fileName, root):
    with open(fileName, "w") as write_file:
        json.dump(root, write_file, indent=5)

def ReadUsersFromJson(fileName):
    with open(fileName, "r") as read_file:
        return(json.load(read_file))

def EvaluateAccountInformationForAccountFromApi(account):
    result = api.get_accountID_by_summonerID(account["summonerName"])
    account["summonerId"] = result["id"]
    account["accountId"] = result["accountId"]
    WriteUsersToJson("Testing2.json", root)

#In Progress
def EvaluateMatchListForAccountFromApi(account):
    result = api.get_matches_by_accountID(account["accountId"])
    if (account["lastMatchId"] == None) or (account["lastMatchId"] != result["matches"][0]["gameId"]):
        account["lastMatchId"] = result["matches"][0]["gameId"]

#In Progress
def EvaluateMatchFromMatchIdFromApi(matchId):
    result = api.get_match_by_matchID(account["lastMatchId"])

def EvaluateAccountInformationForUsers(users):
    for user in users:
        for account in user["accounts"]:
            if (account["summonerId"] == None or account["accountId"] == None):
                EvaluateAccountInformationForAccountFromApi(account)
            EvaluateMatchListForAccountFromApi(account)

def EvaluateMostRecentMatchForAccounts(users):
    pass


ReadInputParams(sys.argv[1:])
#Global object in Testing.py with name "root"
root = ReadUsersFromJson(inputFile)
EvaluateAccountInformationForUsers(root["users"])
WriteUsersToJson(outputFile, root)









