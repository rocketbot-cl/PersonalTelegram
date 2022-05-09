# PersonalTelegram Manual

Este módulo se conecta con [Telegram API](https://my.telegram.org/apps). Puedes conectarte con Telegram, obtener IDs de contactos, grupos y canales, enviar mensajes y leer canales de Telegram

![banner](img/banner_PersonalTelegram.png)

## Como instalar este módulo

**Descarga** e **instala** el contenido en la carpeta `modules` en la ruta de rocketbot.

## Cómo usar este módulo

Para utilizar este módulo tienes que entrar en [http://my.telegram.org/apps](http://my.telegram.org/apps) y completar tu número de telefono con el código de país (`+54` por ejemplo).

Telegram te enviará un código a tu teléfono y lo tienes que completar en la web.

Una vez logueado, tienes que copiar el `api_id` y el `api_hash` para vincular rocketbot con tu Telegram.

## Descripción de los comandos

### Conectar con Telegram

Conectará a Rocketbot con la cuenta indicada en `API ID`, `API hash` y `Número de teléfono`.

| Parámetros         | Descripción                                                            | Ejemplo                          |
| ------------------ | ---------------------------------------------------------------------- | -------------------------------- |
| API ID             | Código obtenido de [my.telegram.org/apps](http://my.telegram.org/apps) | 12345678                         |
| API hash           | Código obtenido de [my.telegram.org/apps](http://my.telegram.org/apps) | abcdefghigklmnop1234567890abcde0 |
| Número de teléfono | Número de teléfono de la cuenta                                        | +99 1234 5678                    |

### Obtener IDs de chats

Este comando devolverá en una variable y en la terminal de Rocketbot la lista de todos los chats con su correspondientes IDs.

| Parámetros | Descripción                                                      | Ejemplo |
| ---------- | ---------------------------------------------------------------- | ------- |
| Resultado  | Nombre de la variable donde se asignará el resultado del comando | result  |

### Enviar mensaje

Este commando enviará el mensaje al chat ID indicado

| Parámetros | Descripción                                       | Ejemplo      |
| ---------- | ------------------------------------------------- | ------------ |
| Mensaje    | Cuerpo del mensaje                                | Hello World! |
| Chat ID    | Número de ID del chat donde se enviará el mensaje | -10435435    |

### Leer mensajes

Este commando leerá todos los mensajes del correspondiente Chat ID.

Para devolver solo los mensajes, seleccionar `Just the messages`, para devolver toda la metadata seleccionar `all the metadata`

| Parámetros | Descripción                                                      | Ejemplo           |
| ---------- | ---------------------------------------------------------------- | ----------------- |
| Chat ID    | Número de ID del chat donde se leerá el chat                     | -10435435         |
| Resultado  | Nombre de la variable donde se asignará el resultado del comando | result            |
| Descargar  | Elegir solo descargar mensajes o toda la metadata                | Just the messages |
