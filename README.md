# Парсер для сайта [kijiji.ca](https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-10/c37l1700273?ad=offering). 

Парсер стягивает следующие поля: 
  - `title` - заголовок объявления
  - `price` - цена 
  - `date` - дата/время публикации
  - `image` - картинка объявления 
  
 Для запуска необходимо выполнить следующие действия: 
  - `git clone git@github.com:aliiavgh/kijiji_parser.git`
  - `python -m venv venv` 
  - `source venv/bin/activate`
  - `pip3 install -r requirements.txt`
  - создайте и заполните .env файл по примеру [.env_example](https://github.com/aliiavgh/kijiji_parser/blob/master/.env_example).
  - `python3 main.py`
 
