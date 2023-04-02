Проект автоматизации тестирования сервиса Stellar Burgers

Нужно проверить:

Регистрация
  Проверь:
    1) Успешную регистрацию. 
        - Поле «Имя» должно быть не пустым; 
        - В поле Email введён email в формате логин@домен: например, 123@ya.ru. 
        - Минимальный пароль — шесть символов.

    2) Ошибку для некорректного пароля.
Вход
    Проверь:
        - вход по кнопке «Войти в аккаунт» на главной,
        - вход через кнопку «Личный кабинет»,
        - вход через кнопку в форме регистрации,
        - вход через кнопку в форме восстановления пароля.

Переход в личный кабинет 
    Проверь переход по клику на «Личный кабинет».

Переход из личного кабинета в конструктор 
    Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.

Выход из аккаунта
    Проверь выход по кнопке «Выйти» в личном кабинете.

Раздел «Конструктор»
    Проверь, что работают переходы к разделам:
        - «Булки»,
        - «Соусы»,
        - «Начинки».

URL адрес тестируемого приложения  https://stellarburgers.nomoreparties.site/

1. основа для написания автотестов - Selenium

2. В директории tests рассположены файлы с тестами
- tests page registration.py ------------- проверка регистрации
- tests page entry.py -------------------- проверка входа
- tests page go to personal account.py --- переход в личный кабинет
- tests page transition from personal account to the constructor.py --- переход из личного кабинета в конструктор
- tests page logout.py ------------------- выход из аккаунта
- tests page section constructor.py ------ раздел конструктор

3. В файле conftest.py - прописаны фикстуры к тестам проекта
4. В файле locator.py - прописаны локаторы и тестовые данные 



