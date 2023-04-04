from selenium.webdriver.common.by import By

class Locator:

	CLICK_ON_LOGIN = (By.CLASS_NAME,"button_button__33qZ0")                                      # клик по кнопке "Войти в аккаунт" на главной странице
	CLICK_ON_TEXT_SIGN_UP = (By.XPATH, "//p[1]/a[text()='Зарегистрироваться']")                  # клик по надписи Зарегистрироваться в форме авторизации
	CLICK_ON_BUTTON_SIGN_UP = (By.XPATH, "//form/button[text()='Зарегистрироваться']")           # клик по кнопке Зарегистрироваться
	CLICK_BUTTON_TO_COME_IN = (By.XPATH, "//button[contains(text(),'Войти')]")                   # клик по кнопке Войти в форме авторизации
	CLICK_PERSONAL_AREA_HOME_PAGE = (By.XPATH, ".//p[text()='Личный Кабинет']")                  # Клик по кнопке "Личный кабинет" на главной странице
	CLICK_BUTTON_CONSTRUCTOR_PERSONAL_OFFICE = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # клик по кнопке "Конструктор" в личном кабинете и переход в форму "Конструктор".
	CLICK_LOGO_STELLAR_BURGER = (By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]")                   # клик по лого "Stellar Burger"
	CLICK_BUTTON_EXIT = (By.XPATH, "//button[contains(text(),'Выход')]")                         # клик по кнопке "Выход" из аккаунта в личном кабинете
	CLICK_BUTTON_SAUCES = (By.XPATH, "//span[contains(text(),'Соусы')]")                         # клик на "Соусы"
	CLICK_BUTTON_BULKA = (By.XPATH, "//span[contains(text(),'Булки')]")                          # клик на "Булки"
	CLICK_BUTTON_STUFFING = (By.XPATH, "//span[contains(text(),'Начинки')]")                     # клик на "Начинки"
	CLICK_ON_TEXT_LOGIN_1 = (By.XPATH, "//a[@href='/login']")                                    # клик по надписи "Войти" в форме регистации
	CLICK_ON_TEXT_LOGIN_2 = (By.XPATH, "//a[@href='/login']")                                    # клик по надписи "Войти" в форме восстановления пароля
	CLICK_ON_TEXT_RECOVER_PASSWORD = (By.XPATH, "//a[@href='/forgot-password' and text()='Восстановить пароль']")  # клик по надписи "Восстановить пароль"

	ENTER_NAME = (By.XPATH, "//fieldset[1]/div/div/input")                                       # Поле ввода имени в форме регистации
	ENTER_EMAIL_1 = (By.XPATH, "//fieldset[1]/div/div/input")                                    # Поле ввода Е-маил форма авторизации
	ENTER_EMAIL_2 = (By.XPATH, "//fieldset[2]/div/div/input")                                    # Поле ввода Е-маил форма регистрации
	ENTER_PASSWORD = (By.XPATH, "//input[@type='password']")                                     # Поле ввода пароля форма регистрации и авторизации
	USER_ON = (By.XPATH, "//p[@class='input__error text_type_main-default']")                    # Сообщение что такой пользователь уже существует, то есть уже зарегестрирован

	WAIT_ERROR = (By.XPATH, "//fieldset[3]/div/p")                                               # Сообщение об ошибке при вводе некорректного пароля
	WAIT_BUTTON_CHECKOUT = (By.XPATH, "//button[text()='Оформить заказ']")                       # загрузка страницы с кнопкой "Оформить заказ"
	WAIT_LABEL_PROFILE = (By.XPATH, "//a[@href='/account/profile' and text()='Профиль']")        # загрузка страницы профиля, появилась надпись "ПРОФИЛЬ"
	WAIT_PAGE_CONSTRUCTOR = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")               # загрузка страницы с текстом "Соберите бургер"
	WAIT_LABEL_PROFILE_OK = (By.XPATH, "//a[@href='/account/profile' and text()='Профиль']")     # Явное ожидание загрузки профиля личного кабинета
	WAIT_LOGIN_PAGE = (By.XPATH, "//h2[contains(text(),'Вход')]")                                # явное ожидание загрузки страницы авторизации

	NAME_FOOD = (By.XPATH, '//div[contains(@class, "current")]/span')                            # переход к разделам
