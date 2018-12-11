# -*- coding: utf-8 -*-

from wxpy import *
from reply import *

import unicodedata
import re
import time
import logging
import threading
from tempfile import NamedTemporaryFile

logging.basicConfig()  # 生成日志
#
# bot = Bot(console_qr=True, cache_path=True)  # 实例化机器人 缓存登录
bot = Bot()

bot.enable_puid()  # 每个用户定义了一个相对稳定的对象/用户id

extensions = ['.jpg', '.png', '.gif']

def send_online_notification(name):
    my_friend = ensure_one(bot.search(name))
    while True:
        my_friend.send('I\'m Still Alive!! ' + time.strftime('%y/%m/%d-%H:%M:%S', time.localtime()))
        time.sleep(600)

@bot.register(bot.self)
def reply(msg):
    if msg.text == '1':
        return 'I\'m Still Alive!! ' + time.strftime('%y/%m/%d-%H:%M:%S', time.localtime())
    else:
        return robot_reply(msg.text, msg.sender.puid)


# @bot.register(Group, SYSTEM, except_self=False)
# def incoming_student(msg):
#     print(msg)
#     print(msg.raw)
    # if u'加入' in msg.text:
    # 	msg.reply(tuling_reply('welcome'.encode('UTF-8'), msg.member.puid))
    # 	msg.reply_image('welcome.jpg')


# def group_msg(msg):
#     if msg.is_at:
#         content = re.sub('@[^\s]*', '', unicodedata.normalize('NFKC', msg.text)).strip()
#
#         if content.endswith(tuple(extensions)):
#             try:
#                 res = requests.get(emotions_reply(content[:-4]), allow_redirects=False)
#                 tmp = NamedTemporaryFile()
#                 tmp.write(res.content)
#                 tmp.flush()
#                 media_id = bot.upload_file(tmp.name)
#                 tmp.close()
#
#                 msg.reply_image('.gif', media_id=media_id)
#             except Exception as error:
#                 print(error)
#                 msg.reply("本机器人没有找到相关表情~使用文字回复：\n" + robot_reply(content, msg.member.puid))
#         else:
#             try:
#                 msg.reply(apiai_reply(content, msg.member.puid))
#             except Exception as error:
#                 print(error)
#                 msg.reply(robot_reply(content, msg.member.puid))

positiveSendingThread = threading.Thread(target=send_online_notification, args=('ZuiYee', ))
positiveSendingThread.setDaemon(True)
positiveSendingThread.start()

# embed()
bot.join()
