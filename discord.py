#導入Discord.py
import discord
#client是我們與Discord連結的橋樑
client = discord.Client()

#調用event函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',client.user)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    print(message.content)
    if message.author == client.user:
        return
    #如果以「say」開頭
    if message.content.startswith("say"):
      #將訊息切一刀，也就是變成兩份
      tmp = message.content.split(" ",1)
      #如果分割後串列長度只有1，代表沒有輸入後面要說的內容
      print(tmp)
      if len(tmp) == 1:
        await message.channel.send(f"{message.author.mention} 你要我說什麼啦？")

      else:
        await message.channel.send(f"{message.author.mention} 他逼得我說「{tmp[1]}」")

client.run('') #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面
