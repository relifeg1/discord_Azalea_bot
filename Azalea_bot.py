import discord # discord.py-1.7.3.dist-info , discord.py
from discord.ui import Select,View, Button #discord_ui-5.1.6.dist-info,py_cord-2.0.0b5.dist-info
from discord.ext import commands
from zmq import ctx_opts
#from soupsieve import select





intents = discord.Intents.all()
AZALEA = commands.Bot(command_prefix='-', intents=intents)


#Check if Bot on
@AZALEA.event
async def on_ready():
    print(f"Bot is HERE -{AZALEA.user}-")


#Send "انا بخير" if Someone Write ok
@AZALEA.command()
async def ok(ctx):
    await ctx.send("انا بخير")


#Button_test
@AZALEA.command(name='td')
async def td(ctx):
    button = Button(label='Clic Me',style= discord.ButtonStyle.blurple, emoji= "❤")
    view = View()
    view.add_item(button)
    await ctx.send("Hi!",view=view)

#Embeds_test
@AZALEA.command()
async def te(ctx):
    embed = discord.Embed(title="dog",url="https://google.com",description="I love you",color=0x002200)
    embed.set_author(name =  ctx.author.display_name, icon_url= ctx.author.display_avatar.url)
    
    await ctx.send(embed=embed)


#List
class MySelect(Select):
    def __init__(self):
        super().__init__(    
            #min_values=2,
            #max_values=4,
            placeholder= "Team SUB",
            options = [
                discord.SelectOption(label= "Be-kon Fansub",
                                    value= "Be_kon_Fansub", 
                                    emoji= "🔴",
                                    description= "Sub Team",
                                    
                                    ),
                
                discord.SelectOption(label= "JSEKAI FANSUB", 
                                    value= "JSEKAI_FANSUB",
                                    emoji= "🟣",
                                    description= "Sub Team",
                                    
                                    ),
                
                discord.SelectOption(label= "MINTO Fansub",
                                    value= "MINTO_Fansub", 
                                    emoji= "🔵",
                                    description= "Sub Team", 
                                    
                                    ),
                discord.SelectOption(label= "Akisubs",
                                    value= "Akisubs", 
                                    emoji= "🟢",
                                    description= "Sub Team",
                                    
                                    ),
                
                discord.SelectOption(label= "BjooDrama",
                                    value= "Bjoo_Drama", 
                                    emoji= "🟡",
                                    description= "Sub Team",
                                    
                                    ),
                
                discord.SelectOption(label= "Midnight Walk",
                                    value= "Midnight_Walk", 
                                    emoji= "🟠",
                                    description= "Sub Team",
                                    
                                    ),
                ]
            
        )
    async def callback(self, interaction: discord.Interaction):
        
        if self.values[0] == "Be_kon_Fansub":
            print("Done be")
            
            #Embed
            
            embed = discord.Embed(
                title = 'Be-kon Fansub',
                description = 'Big team',
                colour = discord.Colour.blurple()
                )
            embed.set_footer(text= f"Team {self.values[0]}")
            #embed.set_author(name = "Reply")
            embed.set_author(name =  embed.author.display_name, icon_url= embed.author.display_avatar)

            
            #Button
            Twitter=Button  (label='Twitter',
                            style= discord.ButtonStyle.blurple,
                            emoji= "🐦",url="https://twitter.com/Bekonfansub"
            )
            instagram=Button (label='instgram'
                            ,style= discord.ButtonStyle.blurple, 
                            emoji= "🖼",url="https://www.instagram.com/bekonfansub/"
            )
            Web =   Button  (label='Web'
                            ,style= discord.ButtonStyle.blurple, 
                            emoji= "🌐",url="https://beautifulsub.wordpress.com"
            )
            
            
            view = View()
            view.add_item(Twitter)
            view.add_item(instagram)
            view.add_item(Web)
            await interaction.response.send_message("Hi!",embed=embed,view=view)
            await interaction.response.send_message(f"Team {self.values}")
            
        elif self.values[0] == "0x2" :
            print("i'm Reading 1")
            

@AZALEA.command()
async def tt(ctx): 
    
    select = MySelect()
    
    view = View()
    view.add_item(select)
    await ctx.send("Choose Team :",view=view)



#!import Token , #run bot
from Token import _Token
AZALEA.run(_Token)





