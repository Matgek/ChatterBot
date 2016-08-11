#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from chatterbot import ChatBot
from chatterbot.training.trainers import ListTrainer
from chatterbot.training.trainers import ChatterBotCorpusTrainer

# Create a new instance of a ChatBot
bot = ChatBot("Terminal",
    storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter",
        "chatterbot.adapters.logic.ClosestMatchAdapter"
    ],
    input_adapter="chatterbot.adapters.input.TerminalAdapter",
    output_adapter="chatterbot.adapters.output.TerminalAdapter",
    database="../database.db"
)
#
# conversation = [
#     u"你好",
#     u"你好! 今天过得怎样？",
#     u"不错啊，谢谢！",
#     ]
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
       bot_input  = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break


