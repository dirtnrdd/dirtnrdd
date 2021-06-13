import discord, datetime, asyncio,random

from discord.message import Message

token = "ODUwNjM0MjI5OTMxMDQ4OTgw.YLsk3A.D280E0LFISBKm7Cgm4dZgGLHiBk"
client = discord.Client()

@client.event
async def on_ready():
    print("봇 준비 완료")
    print(client.user)
    game = discord.Game('테스트')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content == "?":
        await message.channel.send("뭐")
    if message.content == "ㄷ":
        await message.channel.send("ㄷㄷ")
    if message.content == "ㄹㅇ":
        await message.channel.send("ㅋㅋ")
    if message.content == "야":
        await message.channel.send("왜")

    

    if message.content.startswith("!삭제"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 매세지 삭제 완료!")
    


    if message.content == '내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22)+1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름:{user.name}/닉네임:{user.display_name}")
        await message.channel.send(message.author.avatar_url)


    

    if message.content == "랜덤":
        await message.channel.send(random.choice(['헤으응','ㄷㄷ','ㅋ','ㅗ']))
    




    if message.content.startswith("!타이머"):
        number = int(message.content.split(" ")[1])
        await asyncio.sleep(number)
        await message.channel.send(f"{number}초 경과") 










client.run(token)