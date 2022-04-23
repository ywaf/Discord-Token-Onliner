# Made By Leho | leho.dev
import json
import time
from websocket import WebSocket
from json import dumps, load
import random
import threading

tokens = open("tokens.txt", "r").read().split("\n") # tokens
status = open("status.txt", "r").read().split("\n") # profile status

games = ['Minecraft', 'Rust', 'VRChat', 'MORDHAU', 'Fortnite', 'Apex Legends', 'Escape from Tarkov', 'Rainbow Six Siege', 'Counter-Strike: Global Offense', 'Sinner: Sacrifice for Redemption', 'Minion Masters', 'King of the Hat', 'Bad North', 'Moonlighter', 'Frostpunk', 'Starbound', 'Masters of Anima', 'Celeste', 'Dead Cells', 'CrossCode', 'Omensight', 'Into the Breach', 'Battle Chasers: Nightwar', 'Red Faction Guerrilla Re-Mars-tered Edition', 'Spellforce 3', 'This is the Police 2', 'Hollow Knight', 'Subnautica', 'The Banner Saga 3', 'Pillars of Eternity II: Deadfire', 'This War of Mine', 'Last Day of June', 'Ticket to Ride', 'RollerCoaster Tycoon 2: Triple Thrill Pack', '140', 'Shadow Tactics: Blades of the Shogun', 'Pony Island', 'Lost Horizon', 'Metro: Last Light Redux', 'Unleash', 'Guacamelee! Super Turbo Championship Edition', 'Brutal Legend', 'Psychonauts', 'The End Is Nigh', 'Seasons After Fall', 'SOMA', 'Trine 2: Complete Story', 'Trine 3: The Artifacts of Power', 'Trine Enchanted Edition', 'Slime-San', 'The Inner World', 'Bridge Constructor', 'Bridge Constructor Medieval', 'Dead Age', 'Risk of Rain', "Wasteland 2: Director's Cut", 'The Metronomicon: Slay The Dance Floor', 'TowerFall Ascension + Expansion', 'Nidhogg', 'System Shock: Enhanced Edition', 'System Shock 2', "Oddworld:New 'n' Tasty!", 'Out of the Park Baseball 18', 'Hob', 'Destiny 2', 'Torchlight', 'Torchlight 2', 'INSIDE', 'LIMBO', "Monaco: What's Yours Is Mine", 'Tooth and Tail', 'Dandara', 'GoNNER', 'Kathy Rain', 'Kingdom: Classic', 'Kingdom: New Lands', 'Tormentor X Punisher', 'Chaos Reborn', 'Ashes of the Singularity: Escalation', 'Galactic Civilizations III', 'Super Meat Boy', 'Super Hexagon', 'de Blob 2', 'Darksiders II Deathinitive Edition', 'Darksiders Warmastered Edition', 'de Blob', 'Red Faction 1', 'Dungeon Defenders']


def maketokenOnline(token, game, custom_status, custom_idle):
    socket = WebSocket()
    socket.connect("wss://gateway.discord.gg/?v=9&encoding=json")
    recv = socket.recv()
    hb_json = json.loads(recv)
    heartbeat = int(hb_json["d"]["heartbeat_interval"]) / 1000
    print(heartbeat)
    socket.send(dumps({"op": 2, "d": {"token": token,
                                      "properties": {"$os": "windows", "$browser": "Discord", "$device": "desktop"}}}))
    socket.send(dumps({"op": 1, "d": 0}))
    socket.send(
        dumps({"op": 3, "d": {"status": custom_idle, "game": {"name": game, "type": 0}, "since": 0, "activities": [
            {"name": "Custom Status", "type": 4, "state": custom_status,
             "emoji": {"id": None, "animated": False}}, ],
                              "afk": False}}))
    while True:
        socket.send(dumps({"op": 1, "d": 0}))
        print("waiting")
        time.sleep(heartbeat)
        print("resending")


for x in range(len(tokens)):
    custom_idle_status = random.choice(["idle", "dnd", "online"])
    custom_status = random.choice(status)
    custom_game = random.choice(games)

    threading.Thread(target=maketokenOnline, args=(tokens[x], custom_game, custom_status, custom_idle_status)).start()
    print(tokens[x] + " is online")
