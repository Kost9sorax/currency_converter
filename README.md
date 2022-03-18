### Запуск

Используя poetry: ```make build && make run```

Используя pip: ```make build-pip && make run-pip```

По умолчанию сервис запущен на 0.0.0.0:8081 и подключается к редису redis://localhost

#### Пример запроса на локалхосте: ```GET http://0.0.0.0:8081/convert?from=USD&&to=EUR&&amount=4```
