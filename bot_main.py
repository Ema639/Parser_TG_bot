from telethon import TelegramClient, events

api_id = 28724427  # Замените на ваш API ID
api_hash = '1177050ef2d7b58520d48048a93a1868'  # Замените на ваш API Hash
client = TelegramClient('session_name', api_id, api_hash)

target_user = 'https://t.me/Smileftw1337'  # Замените на юзернейм или ID целевого пользователя

# Список чатов, которые нужно мониторить (укажите юзернеймы или ID чатов)
source_chats = [
    'https://t.me/phangano',
    'https://t.me/phangan_koh',
    'https://t.me/GlavPangan',
    'https://t.me/SamuiChat_INF',
    'https://t.me/khopangan',
    'https://t.me/phangan55',
    'https://t.me/SamuiChat_INF'
]


# Обработчик событий на новые сообщения в нескольких чатах
@client.on(events.NewMessage(chats=source_chats))  # Мониторим несколько чатов
async def message_handler(event):
    # Проверяем, содержится ли в тексте сообщения слово "байк"
    if 'байк' or 'скутер' in event.raw_text.lower():  # Сравнение текста с регистронезависимой проверкой
        # Получаем информацию о чате
        chat_entity = await client.get_entity(event.chat_id)
        chat_title = chat_entity.title if hasattr(chat_entity, 'title') else 'Чат'

        # Проверяем, есть ли у чата публичный username
        if hasattr(chat_entity, 'username') and chat_entity.username:
            chat_link = f"https://t.me/{chat_entity.username}"
        else:
            # Если у чата нет публичного username, используем ID
            chat_link = f"tg://resolve?domain={event.chat_id}"

        # Формируем текст с ссылкой на чат
        info_text = f"Сообщение переслано из чата: [{chat_title}]({chat_link})\n"

        # Отправляем сообщение с информацией о чате
        await client.send_message(target_user, info_text, parse_mode='md')  # Используем Markdown для ссылки

        # Пересылаем сообщение с "байком" целевому пользователю
        await event.forward_to(target_user)


async def main():
    # Запускаем бота
    await client.start()
    print("Бот запущен и слушает сообщения...")

    # Ожидание новых событий
    await client.run_until_disconnected()


# Запуск основной функции
with client:
    client.loop.run_until_complete(main())
