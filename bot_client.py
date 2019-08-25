#dicord.pyを読み込む
#https://github.com/Rapptz/discord.py
import discord
import re
import misc

#diecordのclientを使用してbotを管理するクラスです
#discord.pyのapiは下記リファレンスサイトを参照してください
#https://discordpy.readthedocs.io/ja/latest/index.html

class Client:
    def __init__(self, token):
        #discordのクライアント
        self.base = discord.Client()
        #botのアクセストークン
        self.token = token
        #LOL/テストちゃんねるのID
        self.chl_id = 615022488740429824

    def boot_and_run(self):
        #基本discordのapiはここで使う
        client = self.base
        def check_pattern(str):
            print(str)
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

            #ndn
            if check_pattern(msg.content):
                nums = []
                total = 0
                role = split_ndn(msg.content)
                role_cnt = int(role[0])
                dice_max = int(role[1])
                for i in range(role_cnt):
                    tmp = misc.randint(0, dice_max)
                    nums.append(tmp)
                    total += tmp
                result = "ダイス："
                for s in nums:
                    result += str(s) + " "
                result += "合計："+ str(total)
                await msg.channel.send(result)

        #botの起動とDiscordサーバーへの接続
        client.run(self.token)