# TelegramBotAPI

This module make requests to the Telegram API to run actions.
The actions you can run, are based on [Telegram bot API Docs](https://core.telegram.org/bots/api).

## IMPORTANT: If you want to contribute
After read all the README.md, if you want to contribute, you can start adding more functions based on the [API methods](https://core.telegram.org/bots/api#available-methods). Or create your custom function. 
__I will be grateful to everyone who wants to contribute.__



## Prerequisites

### Instalation
First you need clone the repo with `pip install TelegramBotInterface`
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

If don't return any error you're ready for use it.

[Here is my bot example](https://github.com/emaaForlin/TelegramBot) 
```

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
