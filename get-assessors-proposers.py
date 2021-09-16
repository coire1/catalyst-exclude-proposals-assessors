import random
import json
import requests
from github import Github


def loadOptions(goptions = {}):
    try:
        with open('./options.json', 'r') as f:
            options = json.load(f)
            for k in options:
                goptions[k] = options[k]
    except Exception as e:
        print(e)
        print("Error loading options.json")
    return goptions

def getUsers(goptions):
    headers = {
        'api_token': goptions["ideascale_api_token"]
    }
    users = []
    for group in goptions["group_ids"]:
        url = goptions["ideascale_base_api_url"] + \
            goptions["members_endpoint"].format(group)
        print("Requesting url: {}".format(url))
        r = requests.get(url, headers=headers)
        response = r.json()
        if (r.status_code == 200):
            for user in response:
                tempUser = {
                    "id": user["id"],
                    "email": user["email"],
                    "proposals": [],
                    "campaigns": []
                }
                if "userName" in user:
                    tempUser["userName"] = user["userName"]
                users.append(tempUser)
    # Get only first 10 users
    for user in users[:10]:
    # Get all users
    #for user in users:
        url = goptions["ideascale_base_api_url"] + \
            goptions["single_member_endpoint"].format(user["id"])
        print("Requesting url: {}".format(url))
        r = requests.get(url, headers=headers)
        response = r.json()
        proposals = []
        campaigns = []
        if (r.status_code == 200):
            for idea in response:
                proposals.append(idea["id"])
                campaigns.append(idea["campaignId"])
            user["proposals"] = list(set(proposals))
            user["campaigns"] = list(set(campaigns))

    return users

def main():
    goptions = loadOptions()
    users = getUsers(goptions)
    with open('users.json', 'w') as outfile:
        json.dump(users, outfile)

main()
