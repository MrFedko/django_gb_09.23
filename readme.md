# Фреймворк Django (семинары)
## Урок 1. Первое Знакомство с Django
Задание
- Создайте [пару представлений](myapp/views.py) в вашем первом приложении:
  - главная
  - о себе 
```python
class MainPageView(TemplateView):
    template_name = 'myapp/index.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['name'] = 'Михаил Федько'
        contex['email'] = 'miklerst@mail.ru'
        contex['phone'] = '+79618518825'
        logger.info(f'посещение страницы index в: {datetime.now()}')
        return contex


class AboutView(TemplateView):
    template_name = 'myapp/about.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['name'] = 'Михаил Федько'
        contex['email'] = 'miklerst@mail.ru'
        contex['phone'] = '+79618518825'
        logger.info(f'посещение страницы about в: {datetime.now()}')
        return contex
```
- Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.
```python
def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой первый Django-сайт</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }
            
            h1 {
                color: #333;
            }
            
            p {
                color: #777;
            }
        </style>
    </head>
    <body>
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    
        <h2>О сайте</h2>
        <p>Этот сайт разработан с использованием Django, мощного фреймворка для создания веб-приложений на языке Python. Здесь я могу создавать и отображать различные страницы и данные в удобном формате.</p>
    
        <h2>Обо мне</h2>
        <p>Привет, меня зовут Федько Михаил. Я являюсь начинающим веб-разработчиком и увлекаюсь созданием интерактивных и красивых веб-сайтов. Мои навыки включают HTML, CSS, JavaScript, а также Python и Django.</p>
    
        <footer>
            <p>Свяжитесь со мной: miklerst@mail.ru | +79618518825</p>
        </footer>
    </body>
    </html>
    """
    logger.info(f'посещение страницы index в: {datetime.now()}')
    return HttpResponse(html)
```

- Сохраняйте в логи данные о посещении страниц.

