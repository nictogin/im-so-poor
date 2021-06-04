import discord
import os
import random 
import pandas_datareader as web

client = discord.Client()

monkey = ['收嗲啦!屌你老母馬志建','好人好姐學咩人聽歌啊']
no = ['唔係囉','唔係囉','唔係囉','我唔理 總之就唔係','咩啊 輸唔起啊依家']
TOKEN = 'your token'

@client.event
async def on_connect():
    print("Bot connected to the server!")
    #channel = client.get_channel(849023011776757780) 
    #await channel.send('Bot connected to the server!')
    
@client.event
async def on_message(message):

    if message.author == client.user:
        return 
    if message.content == '我想中出你':
        await message.channel.send('我屌鳩爆你屎眼啊') 
        return
    if str(message.author) == 'andy0922#6404':
        if message.content.startswith('!play') or message.content.startswith('!Play'):
            await message.channel.send(monkey[random.randint(0,1)])
            return
        if message.content.startswith('!fs'):
            await message.channel.send('臭Bi 又要播歌又要skip') 
            return
        if 'dllm' in message.content or '屌' in message.content:
            await message.channel.send('講唔贏爆粗啊 係囉係囉係囉') 
            return
        await message.channel.send(no[random.randint(0,4)])

    if message.content.startswith('!!'):
    	await message.channel.send('!play '+ message.content[2:])


    if message.content.startswith('$stockprice'):
        if len(message.content.split(' ')) == 2:
            ticker = message.content.split(' ')[1]
            price = await get_stock_price(ticker) # **** we have to await this function as well
            await message.channel.send(f'Price of {ticker} now is {price}')

@client.event 
async def get_stock_price(ticker): 
    data = web.DataReader(ticker, 'yahoo')
    return data['Close'].iloc[-1]

client.run(TOKEN) 
