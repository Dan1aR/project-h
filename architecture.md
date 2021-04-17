# How architecture looks like

We have two servers that work all the time. ("manager" and master)  
Manager serves the clients.   
Master serves the models and queries.  
Master gets queries and distributes load between workers (master, controls workers)  
When we have a lot of queries more workers are demanded.  

## What happens when client comes for the first time (what "manager" does)
Manager's job is to save data about models to MongoDB (guess it is the best choice)
Also it serves the website.

When client comes, we ask him to provide the model and some additional information about it.
The information may include things like 

We also can estimate FLOPs required to serve the model and suggest the best worker.
We can estimate the delay between query and response. 

## What happens when we get query (How workers are launched and how do they get data from queries)


## How the query gets processed (how workers do their job)



## Requests

В идеале нужен простой сервер который ждет запроса, когда приходит запрос - он выполняет другой скрипт, который все обрабатывает.  
Это упростит переезд на облачные сервисы и работу с контейнерами.  

Какая нам нужна информация?  
1) Секретный ключ для каждой модели пользователя  
2) Данные  
    Самое интересное.  

    Поскольку входов может быть много нам нужен JSON для передачи этой информации.  
    Ключ - название входа, значение - данные передаваемые на вход.  

    Основные типы:  
    Изображения можно сериализовать в последовательность байтов и все будет отлично.  
    Табличные данные можно передавать в виде JSON, удобно для всех (сюда входит и текст).  
    Звуки тоже можно сериализовать в последовательность байтов и все тоже будет отлично.  

    Специфичные типы (хз пока как их передавать):  
    Графовые данные, рекомендательные системы.  

    Нужен способ передавать все это через HTTP, с примерами работы и парсингом со стороны сервера.  
    Пока напишем сервер-приемник на Flask - работает быстро, писать немного, потом переедем на более быстрые фреймворки.  

    Уточнение: нужен клиент и сервер, клиент передает картинки, сервер разбирает запросы.  
    Желательно сделать обработчики для всех.  
