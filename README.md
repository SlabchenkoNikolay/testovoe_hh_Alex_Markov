# testovoe_hh_Alex_Markov
Задействованные технологии
- python 3.9
- django
- django REST framework
- SQLite
- Docker-compose

Руководство к использованию.
*GET*/api/counter/   -Показать все записи статистики в БД.

Отобразит данные следующиъ полей модели - 

date - дата события
views - количество показов 
clicks - количество кликов 
cost - стоимость кликов 
cpc - cost/clicks 
cpm - cost/views * 1000 
(Поля cpc и cpm вычисляются по условию добавления ненулевых производных для вычисления записей)

Пример возвращаемых данных (json)

{
    "id": 1,
    "date": "2021-12-20",
    "views": 1,
    "clicks": 1,
    "cost": "1.00",
    "cpc": "1.00",
    "cpm": "1000.00"
}


Запросу может быть задан параметр-

      Формат даты YYYY-MM-DD
      -date: string - вывести статистику по событию за указанную дату
      -from_date: string - вывести статистику по событиям начиная с указанной даты
      -to_date: string - вывести статистику по событиям по указанную дату
      -date_range: string - статистика за период. 
      
      Возможные варианьты-
      - ordering: string - отсортировать события по выбранному полю
      Возможные варианьты:
      id - по возрастанию(id), по убыванию(-id)
      date - по возрастанию(date), по убыванию(-date) 
      views - по возрастанию(views), по убыванию(-views) 
      clicks - по возрастанию(clicks), по убыванию(-clicks) 
      cost - по возрастанию(cost), по убыванию(-cost) 
      cpc - по возрастанию(cpc), по убыванию(-cpc) 
      cpm - по возрастанию(cpm), по убыванию(-cpm) 

*POST*/api/counter/   -Добавить записье в БД

Параметры запроса

{
date*: string(date)
views: integer
clicks:	integer
cost:	string(decimal)
}

Ответ

{
    "id": 12,
    "date": "2021-12-20",
    "views": 10,
    "clicks": 5,
    "cost": "12.50"
}

*DELETE*/api/сounter/   -удаление всех записей из БД
Ответ

{
    "status": 204,
    "data": "Данные успешно удалены"
}


*Запуск в Docker*

Клонировать репозиторий
https://github.com/SlabchenkoNikolay/testovoe_hh_Alex_Markov.git

Перейти в директорию testovoe_hh_Alex_Markov
cd testovoe_hh_Alex_Markov

Выполнить билд проекта
docker-compose build

Запустить контейнер
docker-compose up -d

Перейти на
http://127.0.0.1:8000/api/counter/
