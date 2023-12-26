from selenium.webdriver.common.by import By


class Locators:
    PERSONAL_AREA = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # Главная страница, кнопка перехода в Личный кабинет
    ENTRANCE_HEADER = (By.XPATH, ".//h2[text()='Вход']")  # Заголовок формы логина
    REGISTRATION_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Форма логина, гиперссылка для регистрации
    REGISTRATION_HEADER = (By.XPATH, ".//h2[text()='Регистрация']")  # Заголовок формы регистрации

    NAME_INPUT_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::*")  # Поле ввода имени пользователя
    EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::*")  # Поле ввода e-mail
    PASSWORD_INPUT_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::*")  # Поле ввода пароля

    INPUT_ERROR = (By.CLASS_NAME, "input__error")  # Текстовый лейбл с ошибкой заполнения формы регистрации
    CONFIRM_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка подтверждения
    # регистрации на форме регистрации

    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа на форме логина
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка на главной странице, доступная
    # только после входа пользователя в аккаунт

    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка Войти в аккаунт на гл. странице

    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")  # Гиперссылка для восстановления пароля
    HEADER_RESTORE_PASSWORD = (By.XPATH, ".//h2[text()='Восстановление пароля']")  # Хедер формы восстан. пароля
    BUTTON_ENTER_ACCOUNT_FROM_RESTORE_FORM = (By.XPATH, "//a[text()='Войти']")  # Кнопка входа в аккаунт на форме
    # восстановления пароля

    HEADER_ACCOUNT_PROFILE = (By.XPATH, ".//a[@href='/account/profile']")  # Заголовок в личном кабинете
    BUTTON_EXIT_ACCOUNT = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода из аккаунта

    MENU_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']")  # Кнопка КОнструктор на хедере главной страницы
    LOGO = (By.XPATH, "//*[@class='AppHeader_header__logo__2D0X2']")  # Логотип-гиперссылка

    MAKE_A_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Заголовок на главной форме
    BUTTON_SAUCES = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Соусы']")  # Навигация по табам
    HEADER_SAUCES = (By.XPATH, ".//h2[text()='Соусы']")   # Заголовок таба
    BUTTON_FILLINGS = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Начинки']")  # Навигация
    # по табам
    HEADER_FILLINGS = (By.XPATH, ".//h2[text()='Начинки']")  # Заголовок таба
    BUTTON_BUNS = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Булки']")  # Навигация по табам
    HEADER_BUNS = (By.XPATH, ".//h2[text()='Булки']")  # Заголовок таба
