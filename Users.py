from vedis import Vedis
import ast

import config


def addAccountName(user_id,name):
    with Vedis(config.db_file_users) as db:
        try:
            db[user_id] = {
                "accName": name,
                "Network":""
            }
            return True
        except:
            return False
def getAccName(user_id):
    with Vedis(config.db_file_users) as db:
        try:
            info = db[user_id]
            info_dict = ast.literal_eval(info.decode("utf-8"))
            return info_dict["accName"]
        except KeyError:
            return None
def cleareByName(user_id):
    with Vedis(config.db_file_users) as db:
        try:
            db[user_id] = {
                "accName":"",
                "Network":""
            }
            return True
        except:
            return False