#dicord.pyを読み込む
#https://github.com/Rapptz/discord.py
import discord
import re
import random

#diecordのclientを使用してbotを管理するクラスです
#discord.pyのapiは下記リファレンスサイトを参照してください
#https://discordpy.readthedocs.io/ja/latest/index.html

class Client:
    def __init__(self, token):
        #discordのクライアント
        self.base = discord.Client()
        #botのアクセストークン
        self.token = token
        #テストちゃんねるID
        self.chl_id = 615090311252803584

    def boot_and_run(self):
        #基本discordのapiはここで使う
        
        #discordのclient取得
        client = self.base

        #ndnパターンチェック
        def check_ndn_pattern(str):
            pattern = '/\d{1,2}d\d{1,4}'
            content = re.compile(pattern)
            result = content.fullmatch(str)
            if result is not None:
                return True
            else:
                return False
        def split_ndn(str):
            result = re.sub('/', "", str)
            return re.split('d', result)
        #nteamsパターンチェック
        def check_teams_pattern(str):
            pattern = '/teams:'
            content = re.compile(pattern)
            result = re.match(content, str)
            if result is not None:
                return True
            else:
                return False


        @client.event
        async def on_ready():
            print("boot bot")
            chl = client.get_channel(self.chl_id)
            await chl.send("偉大なるユーミ！")

        @client.event
        async def on_message(msg):
            #メッセージ送信者がbotの場合無視
            if msg.author.bot:
                return

            #テスト
            if msg.content == "/yuumi":
                await msg.channel.send("ファッ!?")
                return
            if msg.content == "book":
                await msg.channel.send("ブック、どうしちゃったの？")
                return

            #ndn
            if check_ndn_pattern(msg.content):
                nums = []
                total = 0
                role = split_ndn(msg.content)
                role_cnt = int(role[0])
                dice_max = int(role[1])
                for i in range(role_cnt):
                    tmp = random.randint(0, dice_max)
                    nums.append(tmp)
                    total += tmp
                result = "ダイス："
                for s in nums:
                    result += str(s) + " "
                result += "合計："+ str(total)
                await msg.channel.send(result)
                return

            #teams
            if check_teams_pattern(msg.content):
                result = re.sub('/teams:', "", msg.content)
                names = re.split(':', result)
                random.shuffle(names)
                rand_idx = []
                active_num = len(names)
                limit = int(float(active_num ) / 2)
                result = "ブルー\n"
                for i in range(0, limit):
                    result += names[i] + " "
                result += "\nレッド\n"
                for i in range(limit, active_num):
                    result += names[i] + " "
                await msg.channel.send(result)
                return

        #botの起動とDiscordサーバーへの接続
        client.run(self.token)