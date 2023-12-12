import discord
import os
import requests

from discord.ext import commands

intents = discord.Intents().all()

api_key = "e8e5f99d0db14b838e292140231112"
base_url = "http://api.weatherapi.com/v1/current.json?"

bot = commands.Bot(command_prefix='!', intents=intents)

def get_weather_json(city_name: str):
    city_name = city_name
    complete_url = base_url + "key=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    return x

# Command: !humidity
@bot.command(name='humidity', help='Get humidity at a certain city')
async def hello(ctx, *, city: str):
    x = get_weather_json(city)

    if "error" not in x:
        humidity = x["current"]["humidity"]
        await ctx.send(f"The humidity in {city} is {humidity}%!")
    else:
        await ctx.send(f"There were no results for the city {city}!")
    

# Command: !temperature
@bot.command(name='temperature', help='Get temperature at a certain city')
async def say(ctx, *, city: str):
    x = get_weather_json(city)

    if "error" not in x:
        current_temperature = x["current"]["temp_f"]
        await ctx.send(f"The temperature in {city} is {current_temperature} degrees Fahrenheit!")
    else:
        await ctx.send(f"There were no results for the city {city}!")
    

# Command: !weather
@bot.command(name='weather', help='Get Weather data at a certain city')
async def weather(ctx, *, city: str):
    x = get_weather_json(city)
    channel = ctx.message.channel

    if "error" not in x:
        y = x["current"]
        current_temperature = y["temp_f"]
        humidity = y["humidity"]

        embed = discord.Embed(
            title=f"Weather Forecast - {city}",
            timestamp=ctx.message.created_at,
        )
        embed.add_field(
            name="Current Temperature",
            value=f"**{current_temperature}\N{DEGREE SIGN}F**",
            inline=True)
        embed.add_field(
            name="Current Humidity",
            value=f"**{humidity}%**",
            inline=True)
        
        await channel.send(embed=embed)
    else:
        await ctx.send(f"There were no results for the city {city}!")


bot.run('MTE4MzY2NTM5OTA4MzA1NzE5Mg.GJi0mu.A3CqDsyqKUIkjkzKw9NUGbr8doRMZf-uYTj9sI')