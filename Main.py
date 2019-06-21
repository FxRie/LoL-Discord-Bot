from RiotAPI import RiotAPI
import RiotConsts as Consts
import time

Summoner_ID = 'zx3MATXao0uMV-q7F-_LDB_0mu5vqb4zuecBl7pXS78GTyA'
Account_ID = 'mRf_Hr2eE5CIe-AVfiGEkmyIiX5KwWFH2-OeilK0m9IqdA'
Match_ID = '4062201614'

#CSV-Datei
import csv
Excel = csv.reader(open('LastMatchInfo.csv', encoding='utf-8-sig'))
lines = list(Excel)

def Get_League(Summoner_Name):
    api = RiotAPI(API_key)
    r1 = api.get_league_by_summonerID(Summoner_ID)
    print(r1[0]["tier"] + " " + r1[0]["rank"])
    #print(r[0]['summonerName'] + " - " + r[0]['tier'] + " " + r[0]['rank'] + " - " + str(r[0]['leaguePoints']) + " League Points.")

def Get_LastMatch(Summoner_Name):
    api = RiotAPI(API_key)
    r2 = api.get_matches_by_accountID(Consts.ACCOUNT_ID[Summoner_Name])
    # r2 = api.get_matches_by_accountID(Account_ID)
    # import csv
    # Excel = csv.reader(open('LastMatchInfo.csv'))
    # lines = list(Excel)
    try:
        if int(lines[int(Consts.PLAYER_INDEX[Summoner_Name])][1]) != r2["matches"][0]["gameId"]:
            lines[int(Consts.PLAYER_INDEX[Summoner_Name])][1] = int(r2["matches"][0]["gameId"])
            writer = csv.writer(open('LastMatchInfo.csv', 'w', newline='', encoding='utf-8-sig'))
            writer.writerows(lines)
            print(Summoner_Name + " has played a new match with ID: " + str(r2["matches"][0]["gameId"]))
        else:
            return
    except: print("Error: " + Summoner_Name)

def Get_LastMatch_KDA(Summoner_Name):
    api = RiotAPI(API_key)
    r3 = api.get_match_by_matchID(lines[int(Consts.PLAYER_INDEX[Summoner_Name])][1])
    print(r3["participantIdentities"][6]["player"]["summonerName"])
    for index in range(9):
        if r3["participantIdentities"][index]["player"]["summonerName"] == Summoner_Name:
            pID = r3["participantIdentities"][index]["participantId"]
            K = r3["participants"][pID-1]["stats"]["kills"]
            D = r3["participants"][pID-1]["stats"]["deaths"]
            A = r3["participants"][pID-1]["stats"]["assists"]
            Score = (K + A)/max(D,1)
            print("Summoner: " + Summoner_Name + ", KDA: " + str(K) + "/" + str(D) + "/" + str(A) + ", Score: " + str(Score))
        else:
            return

if __name__ == "__main__":


    #Auslesen der gespeicherten Datei und Generierung
    while True:
        for acc_id in Consts.ACCOUNT_ID:
            Get_LastMatch(str(acc_id))
            Get_LastMatch_KDA(acc_id[0]) #wird zu oft abgerufen, nur wenn ein last_match da ist
            time.sleep(10)
        # for mat_id in lines:
        #     Get_LastMatch_KDA(mat_id[0])
        #     time.sleep(2)

    # for mat_id in lines:
    #     print(mat_id[0])
    #     Get_LastMatch_KDA(mat_id[0])
    #     time.sleep(2)



