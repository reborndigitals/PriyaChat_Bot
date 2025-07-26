import asyncio
from os import getenv
from config import OWNER_ID
from dotenv import load_dotenv
from pyrogram import Client
import config


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="Apple_Ponnu",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=False,
            plugins=dict(root="ANJALI.ANJALI"),
        )
        

    async def start(self):
        print(f"Starting HEARTBEAT...")

        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("HeartBeat_Fam")
                await self.one.join_chat("HeartBeat_Fam")
                await self.one.join_chat("HeartBeat_Fam")
                await self.one.join_chat("HeartBeat_Fam")

            except:
                pass
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
     
            print(f"HEARTBEAT Started as {self.one.me.first_name}")
            
        

    async def stop(self):
        LOGGER(__name__).info(f"Stopping HEARTBEAT...")
        try:
            if config.STRING1:
                await self.one.stop()
        except:
            pass
