from enum import Enum


token = "1194153913:AAFxPrdFa9ckRbLdZms6_y3yVyppmbY9dLw"
db_file = "database.vdb"
db_file_users = "users.vdb"

URL ="https://searchinggram20200523105614.azurewebsites.net/"

class States(Enum):
    S_START = "0"  # Начало нового диалога
    S_WAIT_FOR_MONITOR_NAME = "1"
    S_WAIT_FOR_MONITOR= "2"
    S_WAIT_FOR_ACCOUNT ="3"
    S_WAIT_FOR_SOC = "4"