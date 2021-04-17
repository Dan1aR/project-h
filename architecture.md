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

какая нам нужна информация?
1) Название модели
2) Секретный ключ, или иные пути идентификации, нужно что-то придумать
3) Данные
    Самое интересное
    Поскольку их может быть огромное множество видов нужен плюс минус универсальный подход к сериализации

    Поскольку входов может быть много нам нужен json для передачи этой информации
    Ключ - название входа
    Значение - данные передаваемые на вход

    Изображения можно сериализовать в последовательность байтов и все будет отлично
    Табличные данные можно передавать в виде json, удобно для всех (сюда входит и текст)
    Звуки тоже можно сериализовать в последовательность байтов и все тоже будет отлично
    
    Графовые данные, рекомендательные системы...