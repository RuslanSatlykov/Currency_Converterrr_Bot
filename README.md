# Currency_Converterrr_Bot
<h2>Телеграм бот для конвертации валюты</h2>

> **Статус проекта:**
>
> 🟢 Поддерживается (активный) 

## Описание
Цель: помочь пользователям конвертировать валюту Рубли в валюту других стран.

Основные функции:  
✅ Конвертация RUB в 10 валют (USD, EUR, TRY, THB, KZT и другие)  
✅ Автоматическое обновление курсов через API exchangerate-api.com  
✅ Удобный интерфейс с инлайн-кнопками (не нужно вводить коды валют вручную)  
✅ Подробный вывод с точным курсом и результатом конвертации  
✅ Обработка ошибок (некорректный ввод суммы, проблемы с API и т. д.)

Как пользоваться:  
1️⃣ Введите сумму в рублях (например: 5000 или `500.50`)  
2️⃣ Выберите валюту из списка (появится меню с кнопками)  
3️⃣ Получите результат конвертации с актуальным курсом

## 🖼 Скриншоты

Стартовое меню:

![image](https://raw.githubusercontent.com/RuslanSatlykov/Currency_Converterrr_Bot/refs/heads/main/first.jpg)

После ввода суммы в Рублях:

![image](https://raw.githubusercontent.com/RuslanSatlykov/Currency_Converterrr_Bot/refs/heads/main/second.jpg)

После выбора валюты:
![image](https://raw.githubusercontent.com/RuslanSatlykov/Currency_Converterrr_Bot/refs/heads/main/third.jpg)

## 💻 Технологии

* Python
* Библиотека `telebot`
* Библиотека `python-telegram-bot`
* Библиотека `requests`
* `Библиотека `nest_asyncio`
  
## ⏬ Установка на локальном компьютере

1. Скачать проект
   
2. Создать бота и через [@BotFather](https://t.me/BotFather) и вставить в проекте свой токен от бота, вставить API ключ из https://www.exchangerate-api.com

3. Создаём виртуальное окружение внутри папки проекта.
Далее команды для MacOS (для windows инуструкция [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```
4. Устанавливаем библиотеки

``` markdown
python3 -m pip install pip install python-telegram-bot requests
```

``` markdown
python3 -m pip install pip install python-telegram-bot --upgrade
```

``` markdown
python3 -m pip install nest-asyncio
```

5. Запускаем
``` markdown
python3 main.py
```

## Автор

Руслан Сатлыков ([@ruslan_satlykovv](https://t.me/ruslan_satlykovv))
