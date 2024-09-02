# Асинхронный пинг-понг
## Краткое описание проекта
Проект реализует простое серверное взаимодействие между сервером и двумя клиентами, с симуляцией нескольких ситуаций.
Используются встроенные библиотеки asyncio и logger для ведения логов, а также Python версии 3.10. 
## Содержимое проекта
1. Папка app - все исполняемые файлы
    1. `client.py` - клиент, запускается в 2х экземплярах
    2. `logger.py` - логгер 
    3. `server.py` - сервер
2. Папка logs - логи, создается автоматически при запуске проекта. Содержит две подпапки client и server, 
для соответствующих логов 
3. `client.Dockerfile` и `server.Dockerfile` - dockerfile'ы для клиента и сервера
4. `docker-compose.yaml` - docker-compose-файл; используется для запуска проекта
## Запуск проекта
### Через Docker
1. Запустить Docker Desktop
2. В директории проекта выполнить `docker compose up --build`
### Локально (без Docker)
1. Заменить в `app/server.py` строку 
`server: asyncio.Server = await asyncio.start_server(handle_client, '0.0.0.0', 8888)`
на `server: asyncio.Server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)`
2. Заменить в app/client.py строку 
`reader, writer = await asyncio.open_connection('server', 8888)`
на `reader, writer = await asyncio.open_connection('127.0.0.1', 8888)`
3. Открыть три экземпляра терминала, в первом выполнить `app/server.py`, 
в двух других - `app/client.py`
