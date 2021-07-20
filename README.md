### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Student2506/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```


### Примеры запросов можно посмотреть в http://127.0.0.1:8000/redoc/
