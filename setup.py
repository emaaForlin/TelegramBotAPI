from distutils.core import setup

README = '''
# TelegramBotAPI

This module make requests to the Telegram API to run actions.
The actions you can run, are based on [Telegram bot API Docs](https://core.telegram.org/bots/api).

## IMPORTANT: If you want to contribute
After read all the README.md, if you want to contribute, you can start adding more functions based on the [API methods](https://core.telegram.org/bots/api#available-methods). Or create your custom function. 
__I will be grateful to everyone who wants to contribute.__



## Prerequisites

### Instalation
First you need install the module `pip install TelegramBotInterface`
### Getting the tokens
For use it, you need a __bot_token__ like `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11` and your __chat_id__ that looks like `1003456789`.

#### Getting the bot token:
Open Telegram and go to the `@BotFather` and send this command `/newbot`. __IMPORTANT:__ Don't delete the chat, you will need it for save the __bot_user__ and others.
Follow the instructions and you will get the __bot_token__. Remember save it.

#### Getting the chat id:
Search your bot in telegram with the user that you set and send it a random message.
After this we need manually make a request to find the __chat_id__. The docs of Telegram Bot API tell us how. `https://api.telegram.org/bot<token>/METHOD_NAME`
Replace `<token>` with your __bot_token__ and in `METHOD_NAME` we use `getUpdates`.
For example `https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getUpdates`

If we put this in the browser that returns a `json`, we need to find the `id` field. That contents we __chat_id__

### First run
Now we have to test if everything is ok.

Save this script as `test.py` and run it.
```
from telegramapi import TelegramAPI 

tb = TelegramAPI('YOUR_BOT_TOKEN')
tb.sendMessage('YOUR_CHAT_ID', 'Hello world!')
```
If don't return any error you're ready for use it.

[Here is my bot example](https://github.com/emaaForlin/TelegramBot) 


## Methods
```
Update()
```
Returns a __dict__ with data of the chat.


```
readLastMessage()
```
Return a __dict__ with `message`, `fromName` and `fromLastName` of the last message .


```
getMe()
```
Simple method for test your token. Return info of that.


```
sendMessage(chat_id, message)
```
Make `sendMessage` request.


```
getCommands()
```
Return a __list__ with your bot's commands.


```
sendDice(chat_id)
```
Just send a dice to your chat.


#### You can read the [available methods](https://core.telegram.org/bots/api#available-methods) of this API and add it to the module.
'
'''

setup(
  name = 'TelegramBotInterface',         # How you named your package folder (MyLib)
  packages = ['TelegramBotInterface'],   # Chose the same as "name"
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='GPL-3.0-only',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This a module who is work like an interface to telegram bot API',   # Give a short description about your library
  long_description = README,
  long_description_content_type="text/markdown",
  author = 'Emanuel Forlin',                   # Type in your name
  author_email = 'emaforlin@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/emaaForlin/TelegramBotInterface',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/emaaForlin/TelegramBotInterface/archive/v0.3.tar.gz',    # I explain this later on
  keywords = ['API', 'BOT', 'TELEGRAM', 'INTERFACE'],   # Keywords that define your package best
  install_requires=['requests', 'json'],            # I get to this in a second
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
    ],
)
