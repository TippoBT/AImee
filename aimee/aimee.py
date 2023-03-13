# This is a copy-paste from the Discord Red documentation on how to start this file, I have no clue on Python atm so naming will be screwed up
# Test comment

import os
from redbot.core import commands
from redbot.cogs.audio.core.commands.controller import PlayerControllerCommands
from dotenv import load_dotenv
from elevenlabslib import *
import lavalink
import requests
import os
import json


from typing import List

load_dotenv()



class AIMEE(commands.Cog):

    def __init__(self, bot):
        self.default_voice = 'David'
        self.bot = bot
        

    def _parse(self, text) -> List[tuple]:
        lines = text.split('&&')

        messages = []
        for line in lines:
            line_parts = line.split('::')
            content = ' '.join(line_parts[1:])
            if len(line_parts) < 2: 
                voice = self.default_voice
            else:
                voice = line_parts[0]
            messages.append((voice, content))
        
        return messages
    
    # def 

    @commands.command()
    async def aisay(self, ctx, text):
        #Should repeat voicename and the message
        ## wait self.bot(text)

        # split up the multi-line shit

        lines = text.split('&&')

        
        

        # if self.bot:
        await ctx.send(text)
        await ctx.send(ctx)

        

        # Summon bitch-tits
        audio_controller = PlayerControllerCommands()

        audio_controller.command_summon(ctx)
        # else:
        #     pass

    # @commands.command()
    # async def aivoices(self, ctx):
    #     # Return a list of all possible voices to the caller
    #     pass

# class ElevenLabs:
#     def __init__(self) -> None:
#         self.api_key = os.environ['ELEVENLABS_API_KEY']
#         self._voices = self.voices()

#     # def get_voice()

#     def tts(self, voice_name, text):
#         # voice_id = filter(lambda x: x['name'] == voice, self._voices)
#         print(json.dumps(self._voices, indent=4))
#         voice_id = next(voice['voice_id'] for voice in self._voices if voice['name'] == voice_name)

#         if not voice_id:
#             print("Could not find id for supplied voice. Terminating")
#             return
        
#         body = {
#             "text": text
#         }
#         tts = requests.post(f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}', body)

#         print(tts)

#     def voices(self):
#         voices = requests.get('https://api.elevenlabs.io/v1/voices')
#         return voices.json()['voices']


def main():
    # bot = AIMEE(None)

    # text = "Domi::Text && Rachel::Cum in my ass"

    # messages = bot._parse(text)

    # print(messages)

    # eleven = ElevenLabsUser(os.environ['ELEVENLABS_API_KEY'])

    # voice = eleven.get_voices_by_name("Rachel")[0]


    # voice.generate_and_play_audio("Rory is gay", playInBackground=False)

    # audio = voice.generate_audio_bytes('Some text')

    # with open('sameple.txt', 'wb')

    with open('sample.txt', 'rb') as file:
        audio = file.read()

    

    # print(audio)


    # voices = eleven.tts('Domi', 'Testing')

    # print(json.dumps(voices.json(), indent=4))

    




if __name__ == '__main__':
    main()
