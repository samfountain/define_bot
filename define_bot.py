import definebot_settings
from discord.ext import commands
from PyDictionary import PyDictionary

bot = commands.Bot(command_prefix=definebot_settings.prefix(), description=definebot_settings.description())

@bot.event
async def on_ready():
    print('Logged in as', bot.user.name)

@bot.command(description='Provides the first five definitions of a word, to the maximum of five nouns and five verbs.')
async def define(word : str):
    '''
    Provides definitions of a word.
    '''
    word_dict = define_word(word)
    if word_dict:
        response = build_response(word_dict)
        await bot.say(response)
    else:
        await bot.say("Definition could not be found.")

def define_word(word : str):
    dict = PyDictionary()
    meanings = dict.meaning(word)
    return meanings

def build_response(meanings):
    noun, verb = '',''
    if 'Noun' in meanings.keys():
        count = 0
        nouns = meanings['Noun']
        noun = '*Nouns*: \n'
        while count < 5 and count < len(nouns):
            noun = noun + '- '
            noun = noun + nouns[count] + '\n'
            count = count + 1
    if 'Verb' in meanings.keys():
        count = 0
        verbs = meanings['Verb']
        verb = '*Verbs*: \n'
        while count < 5 and count < len(verbs):
            verb = verb + '- '
            verb = verb + verbs[count] + '\n'
            count = count + 1
    return noun + '\n' + verb

bot.run(definebot_settings.token())
