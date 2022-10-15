### Описание 
Бот скачивает через API и публикует фото космической тематики в телеграм-канал 
каждые n-часов из заданной директории. 

Поддерживаются следующие источники фото:
APOD(https://api.nasa.gov/)
EPIC(https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY)
spacex(https://api.spacexdata.com/v5/launches/)
### Запуск
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