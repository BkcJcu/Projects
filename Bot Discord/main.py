import discord # Discord API
from discord import app_commands
import asyncio
from discord.interactions import Interaction
from discord.ext import commands, tasks
import time
import threading
from datetime import timedelta
from discord.ui import View, Button
from discordrp import Presence
import random
from typing import Union


#--------------------------#
import sys # Gère les processus
from PySide6 import QtCore, QtWidgets, QtGui


# Form implementation generated from reading ui file 'botgui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global serverlistflag

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1003, 575)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(166, 166, 166))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(166, 166, 166))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(166, 166, 166))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(166, 166, 166))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(166, 166, 166))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(166, 166, 166))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(166, 166, 166))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(166, 166, 166))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(166, 166, 166))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonServer = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonServer.setGeometry(QtCore.QRect(100, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.pushButtonServer.setFont(font)
        self.pushButtonServer.setObjectName("pushButtonServer")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 80, 281, 21))
        self.comboBox.setObjectName("comboBox")
        self.plainTextEditToServer = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEditToServer.setGeometry(QtCore.QRect(30, 140, 281, 161))
        self.plainTextEditToServer.setObjectName("plainTextEditToServer")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setGeometry(QtCore.QRect(30, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.label1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(30, 60, 121, 21))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(30, 120, 121, 21))
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(350, 60, 121, 21))
        self.label3.setObjectName("label3")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(350, 80, 281, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.plainTextEditToDM = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEditToDM.setGeometry(QtCore.QRect(350, 140, 281, 161))
        self.plainTextEditToDM.setObjectName("plainTextEditToDM")
        self.pushButtonDM = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDM.setGeometry(QtCore.QRect(430, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.pushButtonDM.setFont(font)
        self.pushButtonDM.setObjectName("pushButtonDM")
        self.pushButtonServer.raise_()
        self.comboBox.raise_()
        self.title.raise_()
        self.label1.raise_()
        self.label2.raise_()
        self.plainTextEditToServer.raise_()
        self.label3.raise_()
        self.comboBox_2.raise_()
        self.plainTextEditToDM.raise_()
        self.pushButtonDM.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1003, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        while serverlistflag == False:
            time.sleep(1.3)
            print("Waiting for server list")
        self.comboBox.addItems(serverlist_name)
        self.comboBox.show()

        # Button functions
        self.pushButton.clicked.connect(self.message)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.title.setText(_translate("MainWindow", "Bot GUI"))


    def message(self):
        target_server = self.comboBox.currentText()
        if target_server in serverlist_name:
            indexserver = serverlist_name.index(target_server)
            target_server = serverlist_id[indexserver]
        
        messagetosend = self.plainTextEdit.toPlainText()
        
        future = asyncio.run_coroutine_threadsafe(send_discord_message(messagetosend, target_server), bot.loop)

        try:
            result = future.result()
        except Exception as e:
            print(f"An error occurred: {e}")


def startbotui():
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        app.exec()

if __name__ == "__main__":
    
    intents = discord.Intents.default() # Intents (sert au bot)
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)
    intents.presences = True
    intents.members = True
    intents.message_content = True
    intents.guilds = True
    intents.typing = True

    serverlist_name = []
    serverlist_id = []
    serverlistflag = False


    # Modifier un message envoyé par await interaction.channel.send()
        # sent_message = await interaction.channel.send("Salut")
        # # Modifier le message initial envoyé
        # await sent_message.edit(content="Bonjour")

    josh_whitelist = [360850540990562304]
    nuke_whitelist = []
    spamping_whitelist = [360850540990562304]

    # Friend list #
    friendlist = [551789791830736906, 448228750782496779, 425710945936080897]

    discord_token = "MTE3NjgxNDk3NTkzNTg1NjY5MA.GZKo6m.p-Zn783pjDU-Ud7p2HUhbp1vvOCw9XBe7kfUxY"
    app_id = "1176814975935856690"

    bot = commands.Bot(
    command_prefix="/",
    description="",
    intents=discord.Intents.all()
    )


    # Initalisation des boutons discord #
    class View(discord.ui.View):
        def __init__(self):
            super().__init__()
    # --------------------------------- #



    @bot.event
    async def on_ready():

        global serverlist_name
        global serverlist_id
        global serverlistflag

        print(f"Logged in as {bot.user}")

        print('Guilds:')
        for guild in bot.guilds:
            print(f'- {guild.name} ({guild.id})')
            serverlist_name.append(guild.name), serverlist_id.append(guild.id)
            print(serverlist_name)

        serverlistflag = True


        print("Building Malveillance...")
        print("Malveillance MAXIMALE !")

        try:
            synced = await bot.tree.sync()
            print(synced)
        except Exception as e: print(e, "exc")

        await bot.change_presence(status=discord.Status.do_not_disturb, activity = discord.Activity(type=discord.ActivityType.listening, name = "Flo Rida - Whistle"))


        
        guildlist = []
        for guild in bot.guilds:
            guildlist.append(app_commands.Choice(name=guild.id, value=guild.name))

    
    #---------- Starting UI ----------#
    startbotui_thread = threading.Thread(target=startbotui)
    startbotui_thread.start()

    # ---- Async functions used in my GUI ---- #

    async def send_discord_message(message: str, target_server: str):
        targetguild = bot.get_guild(int(target_server))
        welcomechannel = targetguild.system_channel
        await welcomechannel.send(content=message)




    # ----- Listen DM to Dump Channel ----- #

    @bot.event
    async def on_message(message: str):
        # If the message is a Private Message
        if isinstance(message.channel, discord.DMChannel):
            dump_channel = bot.get_channel(1177299998036197387)
            content = f"**({message.author.id}) - {message.author} :** {message.content}"
            # Send msg to channel
            await dump_channel.send(content)


    # ---- Commands of my Bot ---- #

    @bot.tree.command(name = 'josh', description="Josh quelqu'un")
    @app_commands.describe(member="La personne à josh", nombre = "Nombre de Josh")

    async def josh(interaction:discord.Interaction, member: discord.User, nombre: int):
        if interaction.user.id in josh_whitelist:
            if member is not None:
                if nombre <= 0:
                    timeoutduration = timedelta(seconds=60)
                    await interaction.user.timeout(timeoutduration, reason="T'es con ou quoi ?")
                    await interaction.user.send("T'es con ou quoi ?")
                await interaction.response.send_message(content=f"Joshing {member.mention} {nombre} fois", ephemeral=True)
                for i in range(nombre):
                    await member.send(f"https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGRyYnRwNGxyb2R0NDZiNWZ3cDFieWxiNnVoMGN5Zmd0eDVmbDF1dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TNwX48Ear64uWmN7t3/giphy.gif")
                    time.sleep(0.2)
        else:
            await interaction.response.send_message(content="Tu n'as malheureusement pas la permission de Josh...", ephemeral=True)


    @commands.has_permissions(ban_members=True, kick_members=True)
    @bot.tree.command(name = 'bozifier' , description="Bozifie la personne de ton choix")
    @app_commands.describe (member = "La personne à bozifier", type = "Type de bozification", reason = "Raison de la bozification")
    @app_commands.choices(type=[
            app_commands.Choice(name="Ban", value="ban"),
            app_commands.Choice(name="Kick", value="kick"),
            ])

    async def bozofier(interaction:discord.Interaction, type: app_commands.Choice[str], member: discord.User, reason : str = None,):
        if member is not None:
            type_val = type.value
            if type_val == "ban":
                if interaction.permissions.ban_members:
                    await interaction.guild.ban(user=member, reason=reason)
                    await interaction.response.send_message(content=f"# {member.mention} a été BOZIFIÉ !")
                else:
                    await interaction.response.send_message(content="Tu n'as pas la permission de ban...", ephemeral=True)
            elif type_val == "kick":
                if interaction.permissions.kick_members:
                    await interaction.guild.kick(user=member, reason=reason)
                    await interaction.response.send_message(content=f"# {member.mention} a été BOZIFIÉ !")
                else:
                    await interaction.response.send_message(content="Tu n'as pas la permission de kick...", ephemeral=True)
            else:
                await interaction.response.send_message(content= "No valid type found", ephemeral=True)


    @commands.has_permissions(moderate_members=True)
    @bot.tree.command(name = 'tagueule' , description="Fait ferme la gueule à la personne de ton choix")
    @app_commands.describe(member = "La personne à faire taire", duration = "Durée du mute", reason = "Raison du mute")

    async def tagueule(interaction:discord.Interaction, member: discord.User, duration: str, reason: str = None):
        if member is not None:
            if duration is not None:
                if interaction.permissions.moderate_members:
                    duration = timedelta(seconds=int(duration))
                    target_user = interaction.guild.get_member(member.id)
                    await target_user.timeout(duration, reason=reason)
                    await interaction.response.send_message(content=f"# {member.mention} a fermé sa gueule !")
                else:
                    await interaction.response.send_message(content="Tu n'as pas la permission de timeout...", ephemeral=True)


    @commands.has_permissions(manage_messages=True)
    @bot.tree.command(name = 'clear_messages' , description="Supprime un nombre n de messages")
    @app_commands.describe(nombre = "Nombre de messages à supprimer")

    async def clear_messages(interaction:discord.Interaction, nombre: int):
        if interaction.permissions.manage_messages:
            if nombre is not None:
                await interaction.response.send_message(content=f"{nombre} messages supprimés", ephemeral=True) 
                await interaction.channel.purge(limit=nombre)
            else:
                await interaction.response.send_message(content="Tu n'as pas la permission d'utiliser cette commande...", ephemeral=True)



    @commands.has_permissions(manage_channels=True, manage_roles=True)
    @bot.tree.command(name = 'lasolutionfinale', description="On reproduit la shoah par balle")
    @app_commands.describe(guildid = "Serveur à détruire", last_words = "Le dernier message avant la destruction", password = "Mot de passe")
    # @app_commands.choices(guildlist = [])

    async def lasolutionfinale(interaction:discord.Interaction, guildid: str, last_words: str, password: str):
        if interaction.user.id in nuke_whitelist:
            if guildid is not None:
                target_guild = bot.get_guild(int(guildid))
                welcomechannel = target_guild.system_channel

            if password == "JeDetesteLesJuifs#39-45":
                await interaction.response.send_message(content= "Destruction du serveur en cours...", ephemeral=True)

                #--------------------------------------------#
                await welcomechannel.send(f"# {last_words}")
                asyncio.sleep(2)
                await welcomechannel.send(f"## 3...")
                asyncio.sleep(1)
                await welcomechannel.send(f"## 2...")
                asyncio.sleep(1)
                await welcomechannel.send(f"## 1...")
                asyncio.sleep(1)
                await welcomechannel.send(f"# ALLAHU AKBAR")

                for channel in target_guild.channels:
                    try:
                        # await channel.delete()
                        # Ajouter la suppression des rôles
                        # Ajouter la suppression des emojis
                        # Ajouter le bannissement des membres
                        print("caca")
                    except:
                        pass
            else:
                await interaction.response.send_message(content= "Mot de passe incorrect, va te pendre", ephemeral=True)
        else:
            await interaction.response.send_message(content="# BOZO")





    @commands.has_permissions(moderate_members = True)
    @bot.tree.command(name = 'jeutropcool', description="Test")
    @app_commands.describe(user1 = "User 1", user2 = "User 2", duration = "Durée du timeout")

    async def jeutropcool(interaction:discord.Interaction, user1: discord.User, user2: discord.User, duration: int):
        if interaction.permissions.moderate_members:


            try:
                await interaction.response.send_message(content= "Lancement du jeu...", ephemeral=True)
            except:
                pass

            embed = discord.Embed(
            title='Lancé de dés',
            description='Pair ou impair ?',
            color=discord.Color.red()
            )

            embed.add_field(name="(Pas prêt) Joueur 1", value=f"{user1.mention}", inline=True)
            embed.add_field(name="(Pas prêt) Joueur 2", value=f"{user2.mention}", inline=True)

            flagplayer1 = False
            flagplayer2 = False

            participer1 = discord.ui.Button(label="Ready Player 1", style=discord.ButtonStyle.green)
            participer2 = discord.ui.Button(label="Ready Player 2", style=discord.ButtonStyle.green)


            async def participer_1_callback(interaction:discord.Interaction,):
                    user = interaction.user
                    nonlocal flagplayer1
                    if user == user1:
                        embed.set_field_at(index=0, name="(Prêt) Joueur 1", value=f"{user1.mention}", inline=True)
                        view.remove_item(participer1)
                        flagplayer1 = True
                    else:
                        await interaction.response.send_message(content= "On t'as pas sonné sale bozo...", ephemeral=True)

                    await message_sent.edit(embed=embed)
                    try:
                        await interaction.response.send_message(content= "")
                    except:
                        pass

            async def participer_2_callback(interaction:discord.Interaction,):
                    user = interaction.user
                    nonlocal flagplayer2
                    if user == user2:
                        embed.set_field_at(index=1, name="(Prêt) Joueur 2", value=f"{user2.mention}", inline=True)
                        view.remove_item(participer2)
                        flagplayer2 = True
                    else:
                        await interaction.response.send_message(content= "On t'as pas sonné sale bozo...", ephemeral=True)

                    await message_sent.edit(embed=embed)
                    try:
                        await interaction.response.send_message(content= "")
                    except:
                        pass


            participer1.callback = participer_1_callback
            participer2.callback = participer_2_callback
            view = View()
            view.add_item(participer1)
            view.add_item(participer2)

            message_sent = await interaction.channel.send(embed=embed, view=view)

            await asyncio.sleep(15)
            if flagplayer1 == True and flagplayer2 == True:
                embed.add_field(name="Lancement des dés", value=":one: :two: :three: :four:", inline=False)
                await message_sent.edit(embed=embed)
                await asyncio.sleep(1)
                embed.set_field_at(index=2, name="Lancement des dés", value=":two: :four: :one: :six:", inline=False)
                await message_sent.edit(embed=embed)
                await asyncio.sleep(1)
                embed.set_field_at(index=2, name="Lancement des dés", value=":three: :five: :two: :one:", inline=False)
                await message_sent.edit(embed=embed)
                await asyncio.sleep(1)
                embed.set_field_at(index=2, name="Lancement des dés", value=":five: :six: :five: :two:", inline=False)
                await message_sent.edit(embed=embed)
                await asyncio.sleep(1)
                embed.set_field_at(index=2, name="Lancement des dés", value=":four: :three: :six: :three:", inline=False)
                await message_sent.edit(embed=embed)
                await asyncio.sleep(1)
                rand = []
                for i in range(4):
                    rand.append(random.randint(1,6))
                num_str = []
                for number in rand:
                    if number == 1:
                        num_str.append("one")
                    elif number == 2:
                        num_str.append("two")
                    elif number == 3:
                        num_str.append("three")
                    elif number == 4:
                        num_str.append("four")
                    elif number == 5:
                        num_str.append("five")
                    elif number == 6:
                        num_str.append("six")
                    else:
                        print("Error, number not included in [1;6]")
                    

                print(num_str)

                embed.set_field_at(index=2, name="Résultat", value=f":{num_str[0]}: :{num_str[1]}: :{num_str[2]}: :{num_str[3]}:", inline=False)
                await message_sent.edit(embed=embed)

                somme = 0
                for number in rand:
                    somme = somme + number

                if somme % 2 == 0:
                    durationtimeout = timedelta(seconds=duration)
                    target_user = interaction.guild.get_member(user1.id)
                    await target_user.timeout(durationtimeout)
                else:
                    durationtimeout = timedelta(seconds=duration)
                    target_user = interaction.guild.get_member(user2.id)
                    await target_user.timeout(durationtimeout)
                    
            else:
                embed.add_field(name= "BOZO", value="Aucun des deux joueurs n'ont participé, la punition est doublée...", inline=False)
                await message_sent.edit(embed=embed)
                durationtimeout = timedelta(seconds=(duration)*2)
                target_user = interaction.guild.get_member(user1.id)
                await target_user.timeout(durationtimeout)
                target_user = interaction.guild.get_member(user2.id)
                await target_user.timeout(durationtimeout)
        else:
            await interaction.response.send_message(content="Pas la permission ")



    @bot.tree.command(name='rename', description="Rename la personne de ton choix")
    @app_commands.describe(member="Cible", pseudo="Pseudo")

    async def rename(interaction: discord.Interaction,pseudo: str, member: discord.User = None, ):
        if interaction.permissions.change_nickname:
            if member is None:
                server_member = interaction.guild.members
                await interaction.response.send_message(content=":thumbsup:", ephemeral=True)
                for user in server_member:
                    try:
                        await user.edit(nick=pseudo)
                    except:
                        pass
            else:
                user = interaction.guild.get_member(member.id)
                try:
                    await user.edit(nick=pseudo)
                except:
                    await interaction.response.send_message(content="Tu ne peux pas rename cette personne", ephemeral= True)
        else:
            await interaction.response.send_message(content="Tu n'as pas la permission de renommer...", ephemeral=True)


    @bot.tree.command(name='spamping', description="Spam ping la personne de ton choix")
    @app_commands.describe(member="Cible", count="Nombre de ping")

    async def spamping(interaction:discord.Interaction, member: discord.User, count: int):
        if interaction.user.id in spamping_whitelist:
            await interaction.response.send_message(content=f"Spamming {member}", ephemeral=True)
            for i in range(count):
                await interaction.channel.send(content=f"{member.mention}")
        else:
            await interaction.response.send_message(content="Tu n'as pas la permission de spamping...", ephemeral=True)


    @bot.tree.command(name='rep', description="Répond à la personne de ton choix")
    @app_commands.describe(message="Message cible", answer="Réponse")

    async def rep(interaction:discord.Interaction, message: str, answer: str):
        try:
            await interaction.response.send_message(content= "Fait.", ephemeral=True)
        except:
            pass
        msg = await interaction.channel.fetch_message(message)
        await msg.reply(content=answer)



        


    # ---- Run bot ---- #


    try:
        bot.run(discord_token)
    except Exception as e:
        print(f"An error occurred, can't launch the bot : {e}")