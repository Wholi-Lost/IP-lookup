import requests
import discord
import json
import re

client = discord.Client()
weather_api_key = "Your.api"  # API key from https://openweathermap.org/
discord_api_key = "Your.token"  # Regenerate your bot token from Discord Developer Portal

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    
    await client.change_presence(activity=discord.Game(name="L'omerta🐍"))

@client.event
async def on_message(message):
    
    regex = re.compile(r"(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})")
    result_list = re.findall(regex, message.content)

    result_list = list(set(result_list))  

    
    if result_list and len(result_list) <= 10:
        print(result_list)

        for ip in result_list:  
            print(ip) 
            
            ip_api_response = requests.get(f"http://ip-api.com/json/{ip}")
            json_ip_data = json.loads(ip_api_response.text)

            try:
                if json_ip_data["status"] == "success":
                    lat = str(json_ip_data["lat"])
                    lon = str(json_ip_data["lon"])
                    coords = lat + ", " + lon

                    
                    embed = discord.Embed(title="IP Info", description=ip, color=0xcccccc)
                    embed.add_field(name="Country: ", value=json_ip_data["country"], inline=False)
                    embed.add_field(name="Region/State: ", value=json_ip_data["regionName"], inline=True)
                    embed.add_field(name="City: ", value=json_ip_data["city"], inline=True)
                    embed.add_field(name="ZIP Code: ", value=json_ip_data["zip"], inline=True)
                    embed.add_field(name="Coordinates: ", value=coords, inline=True)
                    embed.add_field(name="ISP: ", value=json_ip_data["isp"], inline=False)

                    try:  
                        weather_api_response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={weather_api_key}&units=metric")
                        json_weather_data = json.loads(weather_api_response.text)
                        temp = str(json_weather_data["main"]["temp"]) + "°C"

                        embed.add_field(name="Temp: ", value=temp, inline=False)
                    except:
                        print("Error retrieving temperature") 

                    embed.set_footer(text="Powered by ip-api.com and openweathermap.org")
                    
                    await message.channel.send(embed=embed)  
            except KeyError:
                print("Partial IP result")
            except: 
                print("Error")

client.run(discord_api_key)  
