import requests
import config

def GetOrCreate(user_id):
    token = _getToken(user_id)   
    if(token == None):
        token = _postNewUser(user_id)
        res = postAddMonitor(token=token, monitor="init{}".format(user_id))
        print(res)
        return token, False
    if(len(getMonitors(token))==0):
        res = postAddMonitor(token=token, monitor="init{}".format(user_id))
        print(res)
    return token, True

def AddMonitor(user_id, monitor_name):
    """None if user not exist"""
    token, is_exist = GetOrCreate(user_id)
    if(is_exist==false):
        return None
    status = _postAddMonitor(token, monitor_name)
    if (status == True):
        bot.send_message(message.chat.id, "Added!")
    else:
        bot.send_message(message.chat.id, "This list already exist!")
    

#/Token
def _getToken(user_id):
    """Token if user exist; None if not"""

    data={
        "username" : user_id,
        "password" : user_id
    }

    response = requests.get(config.URL+"Token/", data = data, verify=False)
    res=response.json()
    print(res)
    if(res["is_exist"]):
        return res["token"]
    else:
        return None
def _postNewUser(user_id):
    """Token if not exist; None if exist"""
    data = {
        "username": user_id,
        "password": user_id
    }
    response = requests.post(config.URL+"Token/create", data = data, verify=False)
    res=response.json()
    print(response.text)
    if (not res["is_exist"]):
        return res["access_token"]
    else:
        return res["access_token"]


#Values
def postAddMonitor(token,monitor ):
    """None - no user exist; false - monitor exist; true - monitor added"""
    data ={
        "token" : token,
        "monitorName" : monitor
    }
    #response = requests.post(config.URL+ "Values/addmonitor", data = data,verify=False)
    response = requests.post(config.URL + "Values/addmonitor?token="+str(token)+"&monitorName="+str(monitor), verify=False)
    res=response.json()
    print("postAddAccount")
    print(response.url)
    print(response.text)
    if(response.status_code==404):
        print("postAddAccount")
        print(response.url)

        print(response.text)
        return None
    if(response.text=="None"):
        print(response.text)
        return None
    if(response.text=="false"):
        print("postAddAccount")
        print(response.url)
        print(response.text)
        return False
    if(response.text=="true"):
        return True
def postAddAccount(token, monitorName, accountName, accountType):
    """False-no account; True - Added"""
    data={
        "token" : token,
        "monitorName": monitorName,
        "accountName": accountName,
        "accountType" : accountType
    }
    response = requests.post(config.URL + "Values/addaccount?token="+str(token)+"&monitorName="+str(monitorName)+"&accountName="+str(accountName)+"&accountType="+str(accountType), verify=False)
    print(response.text)
    if (response.status_code == 404):
        print(response.text)
        return None
    

    if(response.text=="No user" or response.text=="No monitor"):
        return False
    return True
def getAccList(token, monitorName):
    """None - no such monitor"""
    data ={
        "token" : token,
        "monitorName" : monitorName
    }
    response = requests.get(config.URL + "Values/getaccslist?token={}&monitorName={}".format(token, monitorName), verify=False)
    print(config.URL + "Values/getaccslist?token={}&monitorName{}".format(token, monitorName))
    print(response.text)
    if (response.status_code == 404):
        return None
    return response.json()
def getAccsInfo(token, monitorName):
    """None - no such monitor"""
    data = {
        "token": token,
        "monitorName": monitorName
    }
    response = requests.get(config.URL + "Values/get_accs_Info?token={}&monitorName={}".format(token, monitorName), verify=False)
    res = response.json()
    if (res.status_code == 404):
        return None
    return res.json()
def getMonitors(token):
    data={
        "token" : token
    }
    response = requests.get(config.URL + "Values/get_monitors?token="+str(token), verify=False)
    res = response.json()
    if (response .status_code == 404):
        print("From get monitors")
        print(config.URL + "Values/get_monitors?token="+str(token))
        print(response.text)
        return None
    return res["Monitors"]
def getAccount(token, monitorName, accountName, accountType):
    response = requests.get(config.URL + "Values/get_account_Info?token={}&monitorName={}&accountName={}&accountType={}".format(token, monitorName, accountName, accountType), verify=False)
    if(response.status_code == 404):
        print("from getAccount")
        print(config.URL + "Values/get_account_Info?token={}&monitorName={}&accountName={}&accountType={}".format(token, monitorName, accountName, accountType))
        return None
    return response.json()[0]