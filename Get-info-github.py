import requests

user= input('Enter GitHub UserName : ')
api_url = f"https://api.github.com/users/{user}"

def GetInfo():
    re = requests.get(url=api_url).json()
    id = str(re['id'])
    followers = str(re['followers'])
    following = str(re['following'])
    created_at = str(re['created_at'])
    updated_at = str(re['updated_at'])
    bio = str(re['bio'])
    name = str(re['name'])
    twitter_username = str(re['twitter_username'])
    public_repos = str(re['public_repos'])
    print('Id : '+id)
    print('Followers : '+followers)
    print('Following : '+following)
    print('Created At : '+ created_at)
    print('Updated At : ' + updated_at)
    print('Bio : '+bio)
    print('Name : '+ name)
    print('Twitter Username : '+twitter_username)
    print('Public Repos : ' +public_repos)

GetInfo()