# -*- coding: utf-8 -*-
import requests
import json
import random
import apiai
from lxml import etree


TULING_TOKEN = '87e9a5015fdb455faf26823e6f20d0eb'  # 图灵机器人key

APIAI_TOKEN = '63ae6dcab54343efac3ac31c845aa7fe'
#
# bot = Bot(console_qr=True, cache_path=True)  # 实例化机器人 缓存登录
# bot.enable_puid()  # 每个用户定义了一个相对稳定的对象/用户id
# data = {
#     'key'    : TULING_TOKEN,
#     'info'   : msg.text, # 收到消息的文字内容
#     'userid' : msg.member.puid, # 使用群聊中发送者的 puid 作为 userid 传送给图灵接口， 如果是私聊可以使用 msg.sender.puid
# }



def robot_reply(msg_content, user_id):
    url_api = 'http://www.tuling123.com/openapi/api'
    print(msg_content)
    print(user_id)
    data = {
        'key': TULING_TOKEN,
        'info': msg_content,  # 收到的文字内容
        'userid': user_id
    }
    print("use Tuling reply")
    s = requests.post(url_api, data=data,).json()




    print('s:', s)
    print('return code:' + str(s['code']))
    if s['code'] == 100000:
        return s['text']
    if s['code'] == 200000:
        return s['text'] + s['url']
    if s['code'] == 302000:
        news = random.choice(s['list'])
        return news['article'] + '\n' + news['detailurl']
    if s['code'] == 308000:
        menu = random.choice(s['list'])
        return menu['name'] + '\n' + menu['detailurl'] + '\n' + menu['info']


def apiai_reply(msg_content, user_id):
    print("try API AI reply..")
    ai = apiai.ApiAI(APIAI_TOKEN)
    request = ai.text_request()
    request.lang = 'zh-CN'
    request.session_id = user_id
    request.query = msg_content

    response = request.getresponse()
    s = json.load(response.read().decode('utf-8'))

    if s['result']['action'] == 'input.unknown':
        raise Exception('api.ai cannot reply this message')
    if s['status']['code'] == 200:
        print("use APIAI reply")
        print('return code: ' + str(s['status']['code']))
        return s['result']['fulfillment']['speech']

#
# def emotions_reply(keyword):
#     print("try gif reply...")
#     res = requests.get('https://www.doutula.com/search', {'keyword': keyword})
#     html = etree.HTML(res.text)
#     urls = html.xpath('//div[@class="image-container"][1]//img[contains(@class, "img-responsive")]/@data-original')
#     if len(urls) < 1:
#         raise Exception('doutula cannot reply this message')
#     url = 'http:' + random.choice(urls)
#     return url