# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
   sudo pip install <package> -t .

"""


base_path = tmp_global_obj["basepath"]  # type: ignore
cur_path = (
    base_path + "modules" + os.sep + "PersonalTelegram" + os.sep + "libs" + os.sep  # type: ignore
)
if cur_path not in sys.path:  # type: ignore
    sys.path.append(cur_path)  # type: ignore

import telethon  # type: ignore
from telethon.tl.functions.messages import GetHistoryRequest  # type: ignore
from telethon import TelegramClient  # type: ignore

global api_id, api_hash, client

module = GetParams("module")  # type: ignore

if module == "connect":
    api_id = GetParams("api_id")  # type: ignore
    api_hash = GetParams("api_hash")  # type: ignore
    phone_number = GetParams("phone_number")  # type: ignore

    try:
        client = TelegramClient("session_file", api_id=api_id, api_hash=api_hash)
        client.start(phone=phone_number)

    except Exception as e:
        PrintException()  # type: ignore
        raise e

if module == "get_chats_ids":
    result = GetParams("result")  # type: ignore

    try:

        async def get_chats_ids():
            global mylist
            mylist = []
            async for dialog in client.iter_dialogs():
                contact = dialog.name + " has ID " + str(dialog.id)
                print(contact)
                mylist.append(contact)

        client.loop.run_until_complete(get_chats_ids())
        SetVar(result, mylist)  # type: ignore

    except Exception as e:
        PrintException()  # type: ignore
        raise e


if module == "send_message":
    msg = GetParams("msg")  # type: ignore
    # el chat id se convierte a int para que funcione
    chat_id = int(GetParams("chat_id"))  # type: ignore

    try:
        from telethon.tl.functions.contacts import ResolveUsernameRequest  # type: ignore
        from telethon import TelegramClient, events, sync  # type: ignore
        from telethon.tl.functions.messages import GetHistoryRequest  # type: ignore
        from telethon.tl.types import InputPeerUser  # type: ignore

        with TelegramClient("session_file", api_id, api_hash) as client:
            client.start()
            # Save the User, Chat or Channel into entity var
            entity = client.get_entity(chat_id)
            client.send_message(entity=entity, message=msg)

    except Exception as e:
        PrintException()  # type: ignore
        raise e


if module == "read_message":
    channel_id = int(GetParams("channel_id"))  # type: ignore
    res = GetParams("res")  # type: ignore
    option = GetParams("option_")  # type: ignore

    from telethon import sync  # type: ignore

    try:
        channel_entity = client.get_entity(channel_id)
        history = client(
            GetHistoryRequest(
                peer=channel_entity,
                limit=100,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0,
            )
        )
        all_messages = []
        messages = history.messages
        for message in messages:
            all_messages.append(message.to_dict())

        msg_returned = []

        if option == "messages_only":
            for element in all_messages:
                msg_returned.append(element["message"])
        elif option == "all_metadata":
            msg_returned = all_messages
        else:
            raise Exception(f"Option: {option} wasn t parsed")

        SetVar(res, msg_returned)  # type: ignore
    except Exception as e:
        PrintException()  # type: ignore
        raise e
