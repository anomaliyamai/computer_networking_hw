## СР 2 ##


- Реализован поиск минимального MTU в канале между локальным пользователем и хостом
- Код обёрнут в docker контейнер
- Скрипт проверен на macos и на ubuntu

### Как запустить:
Клонируем репозиторий и заходим в папку lab2.

Собираем образ и запускаем контейнер:
```
$ docker build . -t mtuchecker
$ docker run -i -t mtuchecker
Host: ya.ru
MTU 737 is ok
MTU 1105 is ok
MTU 1289 is ok
MTU 1381 is ok
MTU 1427 bad
MTU 1404 is ok
MTU 1415 is ok
MTU 1421 is ok
MTU 1424 bad
MTU 1422 is ok
MTU 1423 bad
minimal MTU for ya.ru = 1422
```
Готово!