### Описание 
Бот скачивает через API и публикует фото космической тематики в телеграм-канал 
каждые n-часов из заданной директории. 

Поддерживаются следующие источники фото:
APOD(https://api.nasa.gov/)
EPIC(https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY)
spacex(https://api.spacexdata.com/v5/launches/)
### Запуск скрипта main.py
Клонировать репозиторий: 
```
git clone https://github.com/alexdiptan/dvmn_space.git
```
Установить зависимости:
```
pip install -r requirements.txt
```
Переименовать файл `.env_template -> .env` и задать все настройки в файле `.env`.

Запустить скрипт: 
```
python3 main.py
```
### Запуск вспомогательных скриптов
Скрипты fetch_apod_images.py fetch_spacex_images.py и fetch_epic_images.py можно запускать по отдельности.
#### Пример запуска скрипта fetch_apod_images.py
```
python3 fetch_apod_images.py
```
Нужно помнить - для работы, скрипту требуется заполненная переменная APOD_API_KEY. Находится в файле .env
#### Пример запуска скрипта fetch_spacex_images.py
```
python3 fetch_spacex_images.py
```
По-умолчанию, скрипт пытается получить фото последнего запуска spacex. Может быть так, что фото запуска нет.
Если нужно получить фото с определенного запуска, используйте ключ `-l` или `--launch_id`. 

Например, вот так можно получить фото с запуска 5eb87d47ffd86e000604b38a:
```
python3 fetch_spacex_images.py --launch_id 5eb87d47ffd86e000604b38a
```
#### Пример запуска скрипта fetch_epic_images.py
```
python3 fetch_epic_images.py
```
