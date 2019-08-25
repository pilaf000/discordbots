import sys
import bot_client

def main():
    #コマンドライン引数でアクセストークンを貰う
    bot = bot_client.Client(sys.argv[1])
    bot.boot_and_run()
    
if __name__ == "__main__":
    main()