- Реализован поиск минимального MTU в канале между локальным пользователем и хостом
- код обёрнут в docker контейнер
- так же присутствует возможность отдельно запустить скрипт на macos или ubuntu

### Тестирование:
копируем репозиторий
```
$ git clone git@github.com:evlampiy-lavrentiev/hse-networks-hw.git
$ cd lab2
```

билдим и запускаем докер
```
$ docker build . -f Dockerfile -t MTU-finder
$ docker run MTU-finder
```
Готово!