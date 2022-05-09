# PersonalTelegram Manual

This module connects the [Telegram API](https://my.telegram.org/apps) with Rocketbot. You can connect with Telegram, get chats, groups and channels IDs, send messages and read chats from every channel in Telegram.

![banner](img/banner_PersonalTelegram.png)

## How to install this module

**Download** and **install** the content in `modules` folder in Rocketbot path

## How to use this module

To use this module you need to register your bot in [http://my.telegram.org/apps](http://my.telegram.org/apps) and fill your phone number with the country code (`+54` for example).

Telegram will send you a code and you have to copy it on the prompt.

Once logged in, you have to copy the `api_id` and `api_hash` to link rocketbot with Telegram.

## Description of commands

### Connect with Telegram

It will connect Telegram with Rocketbot via `API ID`, `API hash` and `Número de teléfono`.

| Parameters       | Description                                                       | Example                          |
| ---------------- | ----------------------------------------------------------------- | -------------------------------- |
| API ID           | Obtained from [my.telegram.org/apps](http://my.telegram.org/apps) | 12345678                         |
| API hash         | Obtained from [my.telegram.org/apps](http://my.telegram.org/apps) | abcdefghigklmnop1234567890abcde0 |
| Telephone Number | Telephone number of the account                                   | +99 1234 5678                    |

### Get chats IDs

This command will get the all the chats IDs, then it will save it to a variable and print them on the terminal.

| Parameters | Description                                                | Example |
| ---------- | ---------------------------------------------------------- | ------- |
| Result     | Name of the variable where the return value will be stored | result  |

### Send Message

This will send a message to the mentioned Chat ID

| Parameters | Description                            | Example      |
| ---------- | -------------------------------------- | ------------ |
| Message    | Body of the message                    | Hello World! |
| Chat ID    | Chat ID where the message will be sent | -10435435    |

### Read Messages

This command will read all the messages of the Chat ID and return them in a variable.

If you only want the messages, select `Just the messages`, to get all the metadata, select `all the metadata`

| Parameters | Description                                                | Example           |
| ---------- | ---------------------------------------------------------- | ----------------- |
| Chat ID    | Chat ID which will be read                                 | -10435435         |
| Result     | Name of the variable where the return value will be stored | result            |
| Download   | Select to download just the messages or all the metadata   | Just the messages |
