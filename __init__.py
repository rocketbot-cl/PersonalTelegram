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

base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + \
    "PersonalTelegram" + os.sep + "libs" + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from telethon.tl.functions.messages import GetHistoryRequest
from telethon import TelegramClient, events

global api_id, api_hash


module = GetParams("module")
if module == "connect":
    api_id = GetParams("api_id")
    api_hash = GetParams("api_hash")
    print(api_id, api_hash)
    try:
        client = TelegramClient(
            "session_file", api_id=api_id, api_hash=api_hash)
        client.start(phone="+543875951753")
        
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "send_message":
    msg = GetParams("msg")
    chat_id = GetParams("chat_id")
    try:
        if chat_id.startswith("g"):
            chat_id = int("-" + chat_id[1:len(chat_id)])
        from telethon.tl.functions.contacts import ResolveUsernameRequest
        from telethon import TelegramClient, events, sync
        from telethon.tl.functions.messages import GetHistoryRequest
        from telethon.tl.types import InputPeerUser

        with TelegramClient('session_file', api_id, api_hash) as client:
            client.start()
            print(client.get_me().stringify())
            entity=client.get_entity(chat_id)
            client.send_message(entity=entity, message=msg)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e


if module == "read_message":
    channel_username = GetParams("channel_username")
    res = GetParams("res")
    try:
        channel_entity=client.get_entity(channel_username)
        posts = client(GetHistoryRequest(
            peer=channel_entity,
            limit=100,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0))
        posts = posts.to_dict()
        list_messages = posts['messages']
        all_msgs = []
        for msg in list_messages:
            all_msgs.append(msg['message'])
        SetVar(res, all_msgs)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e