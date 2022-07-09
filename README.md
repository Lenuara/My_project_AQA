# My_project_AQA
__

Пишу тесты на сайт [https://demoqa.com/](https://demoqa.com/) 
Работаю с двух машин, синхронизируясь между ними и этим репозиторием.  
Использую паттерн проектирования Page Object Model (POM)  

### *Структура проекта*:  
Папки:
- data  
- generator  
- locators  
- pages    
- tests   

Файлы:  
- data.py - декоратор для работы с данными  
- generator.py - генератор данных модулем faker (ФИО, емайл, адрес)  
- elements_page_locators.py 
  - класс, собирающий входные и выходные данные для текстового поля  
  -
- elements_test.py 
  - функция теста текстовых полей ввода  
  - 
- elements_page.py - функции заполнения и проверок полей  
- base_page - типы проверок элементов, ожидание явное  
- requirements.txt  - для всех импортов  
- conftest.py - для фикстур  
- 