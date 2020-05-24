import telebot
from config import *
import  logging
from req import *
import Statesdbworker
import Users
from telebot import  types
import charts
import json


bot = telebot.TeleBot(token)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

def check_parameters(net, type,  data):
    p = data.split("|")
    if(p[0]==net and p[1]==type):
        return True
    return False

def send_statistics_Instagram(res, call, name):
    keyboard = types.InlineKeyboardMarkup()
    buttonLikes = types.InlineKeyboardButton(text="Statistics likes on posts(last 12 posts)",
                                        callback_data="Instagram|likes|{}".format(name))
    buttonComms = types.InlineKeyboardButton(text="Statistics comments on posts (last 12 posts)",
                                        callback_data='Instagram|comments|{}'.format(name))
    buttonGLikes = types.InlineKeyboardButton(text="Statistics of growth of likes",
                                        callback_data='Instagram|growsLikes|{}'.format(name))
    buttonGComms = types.InlineKeyboardButton(text="Statistics of growth of comments",
                                        callback_data='Instagram|growcomments|{}'.format(name))
    buttonGFollowers = types.InlineKeyboardButton(text="Statistics of growth of followers",
                                        callback_data='Instagram|growfollowers|{}'.format(name))
    keyboard.add(buttonLikes)
    keyboard.add(buttonComms)
    keyboard.add(buttonGLikes)
    keyboard.add(buttonGComms)
    keyboard.add(buttonGFollowers)
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Name : {}*".format(res["name"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="{}".format(res["pic"]))
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Comments *: {}".format(res["comments"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Followers *: {}".format(res["followers"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Followers *: {}".format(res["followers"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Likes *: {}".format(res["likes"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Max comments count*: {}".format(res["max_comments"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="{}".format(res["max_comments_pic"]))
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Min comments count*: {}".format(res["min_comments"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="{}".format(res["min_comments_pic"]))
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Max likes count*: {}".format(res["max_likes"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="{}".format(res["max_likes_pic"]))
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Min likes count*: {}".format(res["min_likes"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="{}".format(res["min_likes_pic"]),
                     reply_markup=keyboard)

def send_statistics_YouTube(res, call, name):
    keyboard = types.InlineKeyboardMarkup()
    buttonLikes = types.InlineKeyboardButton(text="Statistics likes on videos(last 5 videos)",
                                             callback_data="YouTube|likes|{}".format(name))
    buttonDisLikes = types.InlineKeyboardButton(text="Statistics dislikes on videos(last 5 videos)",
                                             callback_data="YouTube|dislikes|{}".format(name))
    buttonComms = types.InlineKeyboardButton(text="Statistics views on videos(last 5 videos)",
                                             callback_data='YouTube|views|{}'.format(name))
    buttonGViews = types.InlineKeyboardButton(text="Statistics of growth of views",
                                              callback_data='Instagram|growviews|{}'.format(name))
    keyboard.add(buttonLikes)
    keyboard.add(buttonDisLikes)
    keyboard.add(buttonComms)
    keyboard.add(buttonGViews)
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Name : {}*".format(res["name"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Subscribers : {}*".format(res["subscribers"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Total views : {}*".format(res["views"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Max likes count : {}*".format(res["mostLiked"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Max dislikes count : {}*".format(res["mostDisliked"]),
                     parse_mode='Markdown',
                     reply_markup=keyboard)
def send_statistics_Twitter(res, call, name):
    keyboard = types.InlineKeyboardMarkup()
    buttonGRetweets = types.InlineKeyboardButton(text="Statistics of growth of retweets",
                                              callback_data='Twitter|growsretweets|{}'.format(name))
    buttonGFollowers = types.InlineKeyboardButton(text="Statistics of growth of followers",
                                              callback_data='Twitter|growfollowers|{}'.format(name))
    keyboard.add(buttonGFollowers, buttonGRetweets)
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Name : @{}*".format(res["name"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="{}".format(res["pic"]))
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Followers *: {}".format(res["followerCount"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Followers *: {}".format(res["retweetsCount"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Max retweets count *: {}".format(res["maxRetweets"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="{}".format(res["maxRetweets_Text"]))
    bot.send_message(chat_id=call.message.chat.id,
                     text="*Min retweets count *: {}".format(res["maxRetweets"]),
                     parse_mode='Markdown')
    bot.send_message(chat_id=call.message.chat.id,
                     text="{}".format(res["minRetweets_Text"]),
                     reply_markup=keyboard)
#start of dialog
@bot.message_handler(commands=["start"])
def start(message):
    token, is_exist = GetOrCreate(message.from_user.id)
    if(is_exist):
        bot.send_message(message.chat.id, "This bot allows you to monitor various accounts on social networks. To add an account, call the command /addaccount and the bot will start tracking account information for you. To get a list of accounts call the command /accslist.")
    else:
        bot.send_message(message.chat.id, "Hi!You new Here! This bot allows you to monitor various accounts on social networks. To add an account, call the command /addaccount and the bot will start tracking account information for you. To get a list of accounts call the command /accslist.")
    Statesdbworker.set_state(message.chat.id, config.States.S_START.value)

@bot.message_handler(func=lambda message: Statesdbworker.get_current_state(message.chat.id)==config.States.S_WAIT_FOR_MONITOR_NAME.value)
def addMonitor(message):
    #Проверка названия

    token, is_exist = GetOrCreate(message.from_user.id)
    if (is_exist == False):
        return None
    status = postAddMonitor(token, message.text)
    if(status==None):
        print("None in MainBot.addmonitor")
    if (status == True):
        bot.send_message(message.chat.id, "Added!")
        Statesdbworker.set_state(message.chat.id, config.States.S_START.value)
    else:
        bot.send_message(message.chat.id, "This list already exist!")

@bot.message_handler(commands=["addaccount"])
def addAccount1(message):
    bot.send_message(message.chat.id, "Send me name of account and name of social network.First the name then the network, in different messages")
    Statesdbworker.set_state(message.chat.id, config.States.S_WAIT_FOR_ACCOUNT.value)
#@bot.message_handler(func=lambda message: Statesdbworker.get_current_state(message.chat.id)==config.States.S_WAIT_FOR_MONITOR.value)
#def addAccount2(message):
    #bot.send_message(message.chat.id, "Send me account name ")
    #Statesdbworker.set_state(message.chat.id, config.States.S_WAIT_FOR_ACCOUNT.value)
@bot.message_handler(func=lambda message: Statesdbworker.get_current_state(message.chat.id)==config.States.S_WAIT_FOR_ACCOUNT.value)
def addAccount2(message):
    #bot.send_message(message.chat.id, "And what social network is it?")
    Users.addAccountName(message.from_user.id,message.text)
    Statesdbworker.set_state(message.chat.id, config.States.S_WAIT_FOR_SOC.value)
    
@bot.message_handler(func=lambda message: Statesdbworker.get_current_state(message.chat.id)==config.States.S_WAIT_FOR_SOC.value)
def addAccount3(message):
    #bot.send_message(message.chat.id, "And what social network is it?")
    token, is_exist = GetOrCreate(message.from_user.id)

    if(message.text !="Instagram" and message.text !="Twitter" and message.text !="Youtube"  ):
        bot.send_message(message.chat.id, "Send correct social network!")
        return
    monitors=getMonitors(token)
    print(monitors[0])
    print(Users.getAccName(message.from_user.id))
    res = postAddAccount(token=token,
                         monitorName=monitors[0],
                         accountName=Users.getAccName(message.from_user.id)
                         ,accountType=message.text )
    if res:
        bot.send_message(message.chat.id, "Added! Adding account information to the list may take a few minutes")
    else :
        bot.send_message(message.chat.id, "No such name")
    Statesdbworker.set_state(message.chat.id, config.States.S_START.value)
    Users.cleareByName(message.from_user.id)
@bot.message_handler(commands=["accslist"])
def accsList(message):
    token, is_exist = GetOrCreate(message.from_user.id)
    monitors = getMonitors(token)
    print("Show list in monitor {}".format(monitors[0]))
    res = getAccList(token , monitors[0])
    if(res==None): print("None in accsList!")
    bot.send_message(message.chat.id, "Instagram")

    for i in res["Instagram"]:
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Statistics", callback_data="Instagram|statistics|{}".format(i))
        keyboard.add(button)
        bot.send_message(message.chat.id, "@"+i, reply_markup=keyboard)

    bot.send_message(message.chat.id, "YouTube")
    for k in res["YouTube"]:
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Statistics", callback_data="YouTube|statistics|{}".format(k))
        keyboard.add(button)
        bot.send_message(message.chat.id, "@" + k, reply_markup=keyboard)

    bot.send_message(message.chat.id, "Twitter")
    for j in res["Twitter"]:
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Statistics", callback_data="Twitter|statistics|{}".format(j) )
        keyboard.add(button)
        bot.send_message(message.chat.id, "@"+j,  reply_markup=keyboard)

@bot.callback_query_handler(func = lambda call : check_parameters(net="Instagram", type="statistics", data=call.data)==True)
def callback_InstagramStatisticas(call):
    token, is_exist = GetOrCreate(call.from_user.id)
    monitors = getMonitors(token)
    print(monitors)
    name = call.data.split("|")[2]
    res = getAccount(token=token,
                           monitorName=monitors[0],
                          accountName=name,
                          accountType="Instagram")
    send_statistics_Instagram(res, call, name)
@bot.callback_query_handler(func = lambda call : check_parameters(net="YouTube", type="statistics", data=call.data)==True)
def callback_InstagramStatisticas(call):
    token, is_exist = GetOrCreate(call.from_user.id)
    monitors = getMonitors(token)
    print(monitors)
    name = call.data.split("|")[2]
    res = getAccount(token=token,
                           monitorName=monitors[0],
                          accountName=name,
                          accountType="YouTube")
    send_statistics_YouTube(res, call, name)
@bot.callback_query_handler(func = lambda call : check_parameters(net="Twitter", type="statistics", data=call.data)==True)
def callback_InstagramStatisticas(call):
    token, is_exist = GetOrCreate(call.from_user.id)
    monitors = getMonitors(token)
    print(monitors)
    name = call.data.split("|")[2]
    res = getAccount(token=token,
                           monitorName=monitors[0],
                          accountName=name,
                          accountType="Twitter")
    send_statistics_Twitter(res, call, name)
@bot.callback_query_handler(func =lambda call :  check_parameters(net="Instagram", type="likes", data=call.data)==True)
def callback_InstaLikes(call):
    name = call.data.split("|")[2]
    token, is_exist = GetOrCreate(call.from_user.id)
    monitors = getMonitors(token)
    response =  getAccount(token=token,
                            monitorName=monitors[0],
                            accountName=name,
                            accountType="Instagram")
    list = response["likesList"]
    img = charts.getChart_OneAxis(name,list, "Statistics likes on posts @{}".format(name))
    photo = open(img, "rb")
    bot.send_photo(call.message.chat.id, photo)

@bot.callback_query_handler(func = lambda call : check_parameters(net="Instagram", type="comments", data=call.data)==True)
def callback_InstaComments(call):
    name = call.data.split("|")[2]
    token, is_exist = GetOrCreate(call.from_user.id)
    monitors = getMonitors(token)
    response =  getAccount(token=token,
                            monitorName=monitors[0],
                            accountName=name,
                            accountType="Instagram")
    list = response["commentsList"]
    img = charts.getChart_OneAxis(name,list, "Statistics comments on posts @{}".format(name))
    photo = open(img, "rb")
    bot.send_photo(call.message.chat.id, photo)


@bot.callback_query_handler(func = lambda call : check_parameters(net="Instagram", type="growsLikes", data=call.data)==True)
def callback_InstaComments(call):
    name = call.data.split("|")[2]
    token, is_exist = GetOrCreate(call.from_user.id)
    monitors = getMonitors(token)
    response =  getAccount(token=token,
                            monitorName=monitors[0],
                            accountName=name,
                            accountType="Instagram")
    x_axis, y_axis= charts.structureData(response["growsLikes"])
    img = charts.getChart(name, x_axis, y_axis, "Statistics of growth of likes @{}".format(name))
    photo = open(img, "rb")
    bot.send_photo(call.message.chat.id, photo)
@bot.callback_query_handler(func = lambda call : check_parameters(net="Instagram", type="growcomments", data=call.data)==True)
def callback_InstaComments(call):
    name = call.data.split("|")[2]
    token, is_exist = GetOrCreate(call.from_user.id)
    monitors = getMonitors(token)
    response =  getAccount(token=token,
                            monitorName=monitors[0],
                            accountName=name,
                            accountType="Instagram")
    x_axis, y_axis= charts.structureData(response["growsComments"])
    img = charts.getChart(name, x_axis, y_axis, "Statistics of growth of comments @{}".format(name))
    photo = open(img, "rb")
    bot.send_photo(call.message.chat.id, photo)
@bot.callback_query_handler(func = lambda call : check_parameters(net="Instagram", type="growfollowers", data=call.data)==True)
def callback_InstaComments(call):
    name = call.data.split("|")[2]
    token, is_exist = GetOrCreate(call.from_user.id)
    monitors = getMonitors(token)
    response =  getAccount(token=token,
                            monitorName=monitors[0],
                            accountName=name,
                            accountType="Instagram")
    x_axis, y_axis= charts.structureData(response["growsFollowers"])
    img = charts.getChart(name, x_axis, y_axis, "Statistics of growth of followers @{}".format(name))
    photo = open(img, "rb")
    bot.send_photo(call.message.chat.id, photo)

@bot.callback_query_handler(func = lambda call : check_parameters(net="YouTube", type="likes", data=call.data)==True)
def callback_YouTubeLikes(call):
    name = call.data.split("|")[2]
    token, is_exist = GetOrCreate(call.from_user.id)
    monitors = getMonitors(token)
    response =  getAccount(token=token,
                            monitorName=monitors[0],
                            accountName=name,
                            accountType="YouTube")
    list= response["likes"]
    img = charts.getChart_OneAxis(name,list, "Statistics of likes on videos {}".format(name))
    photo = open(img, "rb")
    bot.send_photo(call.message.chat.id, photo)
@bot.callback_query_handler(func = lambda call : check_parameters(net="YouTube", type="dislikes", data=call.data)==True)
def callback_YouTubeLikes(call):
    name = call.data.split("|")[2]
    token, is_exist = GetOrCreate(call.from_user.id)
    monitors = getMonitors(token)
    response =  getAccount(token=token,
                            monitorName=monitors[0],
                            accountName=name,
                            accountType="YouTube")
    list= response["dislikes"]
    img = charts.getChart_OneAxis(name,list, "Statistics of dislikes on videos {}".format(name))
    photo = open(img, "rb")
    bot.send_photo(call.message.chat.id, photo)
@bot.callback_query_handler(func = lambda call : check_parameters(net="YouTube", type="views", data=call.data)==True)
def callback_YouTubeLikes(call):
    name = call.data.split("|")[2]
    token, is_exist = GetOrCreate(call.from_user.id)
    monitors = getMonitors(token)
    response =  getAccount(token=token,
                            monitorName=monitors[0],
                            accountName=name,
                            accountType="YouTube")
    list= response["viewsList"]
    img = charts.getChart_OneAxis(name,list, "Statistics of views on last videos {}".format(name))
    photo = open(img, "rb")
    bot.send_photo(call.message.chat.id, photo)


@bot.callback_query_handler(
    func=lambda call: check_parameters(net="Instagram", type="growviews", data=call.data) == True)
def callback_YouTubeGrows(call):
    name = call.data.split("|")[2]
    token, is_exist = GetOrCreate(call.from_user.id)
    monitors = getMonitors(token)
    response = getAccount(token=token,
                          monitorName=monitors[0],
                          accountName=name,
                          accountType="YouTube")
    x_axis, y_axis = charts.structureData(response["growViews"])
    img = charts.getChart(name, x_axis, y_axis, "Statistics of growth of views @{}".format(name))
    photo = open(img, "rb")
    bot.send_photo(call.message.chat.id, photo)
@bot.callback_query_handler(
    func=lambda call: check_parameters(net="Twitter", type="growsretweets", data=call.data) == True)
def callback_TwitterGrowsRetweets(call):
    name = call.data.split("|")[2]
    token, is_exist = GetOrCreate(call.from_user.id)
    monitors = getMonitors(token)
    response = getAccount(token=token,
                          monitorName=monitors[0],
                          accountName=name,
                          accountType="Twitter")
    x_axis, y_axis = charts.structureData(response["growsRetweets"])
    img = charts.getChart(name, x_axis, y_axis, "Statistics of growth of retweets @{}".format(name))
    photo = open(img, "rb")
    bot.send_photo(call.message.chat.id, photo)
@bot.callback_query_handler(
    func=lambda call: check_parameters(net="Twitter", type="growfollowers", data=call.data) == True)
def callback_TwitterGrowsFollowers(call):
    name = call.data.split("|")[2]
    token, is_exist = GetOrCreate(call.from_user.id)
    monitors = getMonitors(token)
    response = getAccount(token=token,
                          monitorName=monitors[0],
                          accountName=name,
                          accountType="Twitter")
    x_axis, y_axis = charts.structureData(response["growsFollowers"])
    img = charts.getChart(name, x_axis, y_axis, "Statistics of growth of followers @{}".format(name))
    photo = open(img, "rb")
    bot.send_photo(call.message.chat.id, photo)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://searchingbotfront.herokuapp.com/' + token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

#bot.polling(none_stop=True)