# [Ваша кулинарная книга](https://github.com/ivxmirov/python_django_practice.git) 🍳

Это платформа для обмена рецептами ваших любимых блюд с другими пользователями. Пользователи могут публиковать свои рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Зарегистрированным пользователям также доступен сервис «Список покупок»: он создает список продуктов, которые нужно купить для приготовления выбранных блюд.
<br><hr>

## Возможности:
- **Главная страница:** список рецептов с постраничной пагинацией и сортировкой по дате публикации.
- **Страница рецепта:** подробная информация о рецепте с возможностью добавить в избранное или покупки.
- **Страница пользователя:** список рецептов конкретного автора с возможностью подписки.
- **Избранное:** управление списком любимых рецептов.
- **Список покупок:** формирование и скачивание списка необходимых ингредиентов для выбранных рецептов.
- **Создание рецептов:** доступно авторизованным пользователям с полным контролем над своими публикациями.
- **Фильтрация по тегам:** удобный поиск рецептов по категориям.
- **Регистрация и авторизация:** включая возможность восстановления пароля.

---

## Уровни доступа:
- **Гости:** могут просматривать рецепты и страницы пользователей.
- **Авторизованные пользователи:** имеют доступ ко всем возможностям, включая создание рецептов, добавление в избранное и покупки, подписки.
- **Администраторы:** полный контроль над системой, включая редактирование и удаление любого контента.

---

## Технологии:
- **Backend:**
  - ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  - ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
  - ![Django REST Framework](https://img.shields.io/badge/Django%20REST-092E20?style=for-the-badge&logo=django&logoColor=white)
  - ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
  - ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
- **Frontend:**
  - ![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=white)
- **Инфраструктура:**
  - ![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
  - ![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
  - ![Docker Compose](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
  - ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
  
---

## Разворачивание проекта:
Деплой проекта осуществляется автоматически при внесении изменений и пуше 
в ветку **main** репозитория на GitHub.

### Разворачивание сервиса автоматически
1. Настройка окружения:
Создайте файл `.env` в корне проекта со следующими переменными:
```env
SECRET_KEY=<секретный_ключ>
DEBUG=False
ALLOWED_HOSTS=<разрешенные_хосты>
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=<имя_базы>
POSTGRES_USER=<пользователь_базы>
POSTGRES_PASSWORD=<пароль>
DB_HOST=db
DB_PORT=5432
```

2. **При пуше в ветку `main`:**
    - Запускаются тесты и линтеры для проверки качества кода.
    - Собираются Docker-образы приложения.
    - Образы пушатся на Docker Hub.
  
3. **После успешной сборки:**
    - Подключается сервер.
    - Копируется и запускается файл `docker-compose.production.yml`.
    - Выполняются миграции и сборка статики.
  
4. **Уведомление:**
    - После успешного деплоя отправляется уведомление в Telegram-бот о завершении процесса.

### Разворачивание сервиса на сервере вручную

1. Подготовьте файл `.env` в корне проекта с переменными.
2. Запустите проект, используя файл `docker-compose.production.yml`:
 ```bash
    docker compose -f docker-compose.production.yml up -d
 ```
3. Выполните миграции базы данных:
 ```bash
    docker compose -f docker-compose.production.yml exec backend python manage.py migrate
 ```
4. При необходимости наполните БД Списком ингредиентов (backend/data/):
 ```bash
    docker compose -f docker-compose.production.yml exec backend python manage.py imort_data
 ```
5. Соберите и скопируйте статику:
 ```bash
    docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
    docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/
 ```
---

## Некоторые примеры запросов к API 

### Профиль пользователя

Доступно всем пользователям

__GET__ http://localhost/api/users/{id}/

Response:
```
{
    "email": "user@example.com",
    "id": 0,
    "username": "string",
    "first_name": "Вася",
    "last_name": "Иванов",
    "is_subscribed": false,
    "avatar": "http://python_django_practice.example.org/media/users/image.png"
}
```

### Создание рецепта

Доступно только авторизованным пользователям

__POST__ http://localhost/api/recipes/

Request:
```
{
    "ingredients": [
        {
            "id": 1123,
            "amount": 10
        }
    ],
    "tags": [
        1,
        2
    ],
    "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
    "name": "string",
    "text": "string",
    "cooking_time": 1
}
```

Response:
```
{
  "id": 0,
  "tags": [
    {
      "id": 0,
      "name": "Завтрак",
      "slug": "breakfast"
    }
  ],
  "author": {
    "email": "user@example.com",
    "id": 0,
    "username": "string",
    "first_name": "Вася",
    "last_name": "Иванов",
    "is_subscribed": false,
    "avatar": "http://python_django_practice.example.org/media/users/image.png"
  },
  "ingredients": [
    {
      "id": 0,
      "name": "Картофель отварной",
      "measurement_unit": "г",
      "amount": 1
    }
  ],
  "is_favorited": true,
  "is_in_shopping_cart": true,
  "name": "string",
  "image": "http://python_django_practice.example.org/media/recipes/images/image.png",
  "text": "string",
  "cooking_time": 1
}
```

### Добавить рецепт в список покупок

Доступно только авторизованным пользователям

__POST__ http://localhost/api/recipes/{id}/shopping_cart/

Response:
```
{
  "id": 0,
  "name": "string",
  "image": "http://python_django_practice.example.org/media/recipes/images/image.png",
  "cooking_time": 1
}
```

### Добавить рецепт в избранное

Доступно только авторизованным пользователям

__POST__ http://localhost/api/recipes/{id}/favorite/

Response:
```
{
  "id": 0,
  "name": "string",
  "image": "http://python_django_practice.example.org/media/recipes/images/image.png",
  "cooking_time": 1
}
```

### Подписаться на пользователя

Доступно только авторизованным пользователям

__POST__ http://localhost/api/users/{id}/subscribe/

Response:
```
{
  "email": "user@example.com",
  "id": 0,
  "username": "string",
  "first_name": "Вася",
  "last_name": "Иванов",
  "is_subscribed": true,
  "recipes": [
    {
      "id": 0,
      "name": "string",
      "image": "http://python_django_practice.example.org/media/recipes/images/image.png",
      "cooking_time": 1
    }
  ],
  "recipes_count": 0,
  "avatar": "http://python_django_practice.example.org/media/users/image.png"
}
```

## Структура

```
python_django_practice
├─ .pre-commit-config.yaml
├─ backend
│  ├─ .dockerignore
│  ├─ api
│  │  ├─ apps.py
│  │  ├─ docs
│  │  │  ├─ openapi-schema.yml
│  │  │  └─ redoc.html
│  │  ├─ filters.py
│  │  ├─ pagination.py
│  │  ├─ permissions.py
│  │  ├─ serializers.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ data
│  │  ├─ ingredients.csv
│  │  └─ ingredients.json
│  ├─ Dockerfile
│  ├─ foodgram
│  │  ├─ asgi.py
│  │  ├─ constants.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  │  └─ __init__.py
│  ├─ manage.py
│  ├─ recipes
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ management
│  │  │  ├─ commands
│  │  │  │  ├─ import_data.py
│  │  │  │  └─ __init__.py
│  │  │  └─ __init__.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_alter_recipe_cooking_time_and_more.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  └─ __init__.py
│  ├─ requirements.txt
│  └─ users
│     ├─ admin.py
│     ├─ apps.py
│     ├─ migrations
│     │  ├─ 0001_initial.py
│     │  ├─ 0002_alter_user_username.py
│     │  ├─ 0003_alter_user_options_alter_user_username.py
│     │  ├─ 0004_alter_user_username.py
│     │  └─ __init__.py
│     ├─ models.py
│     └─ __init__.py
├─ frontend
│  ├─ .dockerignore
│  ├─ Dockerfile
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  │  ├─ favicon.ico
│  │  ├─ favicon.png
│  │  ├─ index.html
│  │  ├─ logo192.png
│  │  ├─ logo512.png
│  │  ├─ manifest.json
│  │  └─ robots.txt
│  ├─ src
│  │  ├─ api
│  │  │  └─ index.js
│  │  ├─ App.css
│  │  ├─ App.js
│  │  ├─ App.test.js
│  │  ├─ components
│  │  │  ├─ account
│  │  │  │  └─ index.js
│  │  │  ├─ account-menu
│  │  │  │  └─ index.js
│  │  │  ├─ account-menu-mobile
│  │  │  │  └─ index.js
│  │  │  ├─ account-mobile
│  │  │  │  └─ index.js
│  │  │  ├─ avatar-popup
│  │  │  │  └─ index.js
│  │  │  ├─ button
│  │  │  │  └─ index.js
│  │  │  ├─ card
│  │  │  │  └─ index.js
│  │  │  ├─ card-list
│  │  │  │  └─ index.js
│  │  │  ├─ change-password-text
│  │  │  │  └─ index.js
│  │  │  ├─ checkbox
│  │  │  │  └─ index.js
│  │  │  ├─ checkbox-group
│  │  │  │  └─ index.js
│  │  │  ├─ container
│  │  │  │  └─ index.js
│  │  │  ├─ file-input
│  │  │  │  └─ index.js
│  │  │  ├─ footer
│  │  │  │  └─ index.js
│  │  │  ├─ form
│  │  │  │  └─ index.js
│  │  │  ├─ form-title
│  │  │  │  └─ index.jsx
│  │  │  ├─ header
│  │  │  │  └─ index.js
│  │  │  ├─ icons
│  │  │  │  ├─ add-avatar
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ add-user
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ arrow-expand
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ arrow-left
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ arrow-right
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ cart
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ check
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ clock
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ copy-link
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ delete-avatar
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ done
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ index.js
│  │  │  │  ├─ ingredient-delete
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ like
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ like-active
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ logout-menu
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ pagination-arrow
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ plus
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ popup-close
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ receipt-delete
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ reset-password-menu
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ saved-menu
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ star
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ star-active
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ subscriptions-menu
│  │  │  │  │  └─ index.js
│  │  │  │  └─ user
│  │  │  │     └─ index.js
│  │  │  ├─ index.js
│  │  │  ├─ ingredients-search
│  │  │  │  └─ index.js
│  │  │  ├─ input
│  │  │  │  └─ index.js
│  │  │  ├─ link
│  │  │  │  └─ index.js
│  │  │  ├─ main
│  │  │  │  └─ index.js
│  │  │  ├─ nav
│  │  │  │  └─ index.js
│  │  │  ├─ nav-menu
│  │  │  │  └─ index.js
│  │  │  ├─ notification
│  │  │  │  └─ index.js
│  │  │  ├─ orders
│  │  │  │  └─ index.js
│  │  │  ├─ pagination
│  │  │  │  └─ index.js
│  │  │  ├─ popup
│  │  │  │  └─ index.js
│  │  │  ├─ protected-route
│  │  │  │  └─ index.js
│  │  │  ├─ purchase
│  │  │  │  └─ index.js
│  │  │  ├─ purchase-list
│  │  │  │  └─ index.js
│  │  │  ├─ subscription
│  │  │  │  └─ index.js
│  │  │  ├─ subscription-list
│  │  │  │  └─ index.js
│  │  │  ├─ tag
│  │  │  │  └─ index.js
│  │  │  ├─ tags-container
│  │  │  │  └─ index.js
│  │  │  ├─ textarea
│  │  │  │  └─ index.js
│  │  │  └─ title
│  │  │     └─ index.js
│  │  ├─ configs
│  │  │  ├─ colors.js
│  │  │  └─ navigation.js
│  │  ├─ contexts
│  │  │  ├─ auth-context.js
│  │  │  ├─ index.js
│  │  │  ├─ recipes-context.js
│  │  │  └─ user-context.js
│  │  ├─ fonts
│  │  │  └─ SanFranciscoProDisplay
│  │  │     ├─ COPYRIGHT.txt
│  │  │     ├─ fonts.css
│  │  │     ├─ SF-Pro-Display-Black.otf
│  │  │     ├─ SF-Pro-Display-Black.woff2
│  │  │     ├─ SF-Pro-Display-BlackItalic.otf
│  │  │     ├─ SF-Pro-Display-BlackItalic.woff2
│  │  │     ├─ SF-Pro-Display-Bold.otf
│  │  │     ├─ SF-Pro-Display-Bold.woff2
│  │  │     ├─ SF-Pro-Display-BoldItalic.otf
│  │  │     ├─ SF-Pro-Display-BoldItalic.woff2
│  │  │     ├─ SF-Pro-Display-Light.otf
│  │  │     ├─ SF-Pro-Display-Light.woff2
│  │  │     ├─ SF-Pro-Display-LightItalic.otf
│  │  │     ├─ SF-Pro-Display-LightItalic.woff2
│  │  │     ├─ SF-Pro-Display-Medium.otf
│  │  │     ├─ SF-Pro-Display-Medium.woff2
│  │  │     ├─ SF-Pro-Display-MediumItalic.otf
│  │  │     ├─ SF-Pro-Display-MediumItalic.woff2
│  │  │     ├─ SF-Pro-Display-Regular.otf
│  │  │     ├─ SF-Pro-Display-Regular.woff2
│  │  │     ├─ SF-Pro-Display-RegularItalic.otf
│  │  │     ├─ SF-Pro-Display-RegularItalic.woff2
│  │  │     ├─ SF-Pro-Display-Semibold.otf
│  │  │     ├─ SF-Pro-Display-Semibold.woff2
│  │  │     ├─ SF-Pro-Display-SemiboldItalic.otf
│  │  │     ├─ SF-Pro-Display-SemiboldItalic.woff2
│  │  │     └─ SFPro_Font_License.rtf
│  │  ├─ images
│  │  │  ├─ avatar-icon.png
│  │  │  ├─ change-password-text-icon.svg
│  │  │  ├─ hamburger-menu-close.png
│  │  │  ├─ hamburger-menu.png
│  │  │  ├─ home-screen-bg.jpg
│  │  │  ├─ logo-footer.png
│  │  │  ├─ logo-header.png
│  │  │  ├─ not-found.png
│  │  │  └─ userpic-icon.jpg
│  │  ├─ index.css
│  │  ├─ index.js
│  │  ├─ logo.svg
│  │  ├─ pages
│  │  │  ├─ about
│  │  │  │  └─ index.js
│  │  │  ├─ cart
│  │  │  │  └─ index.js
│  │  │  ├─ change-password
│  │  │  │  └─ index.js
│  │  │  ├─ favorites
│  │  │  │  └─ index.js
│  │  │  ├─ index.js
│  │  │  ├─ main
│  │  │  │  └─ index.js
│  │  │  ├─ not-found
│  │  │  │  └─ index.js
│  │  │  ├─ password-reset
│  │  │  │  └─ index.js
│  │  │  ├─ recipe-create
│  │  │  │  └─ index.js
│  │  │  ├─ recipe-edit
│  │  │  │  └─ index.js
│  │  │  ├─ signin
│  │  │  │  └─ index.js
│  │  │  ├─ signup
│  │  │  │  └─ index.js
│  │  │  ├─ single-card
│  │  │  │  ├─ description
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ index.js
│  │  │  │  └─ ingredients
│  │  │  │     └─ index.js
│  │  │  ├─ subscriptions
│  │  │  │  └─ index.js
│  │  │  ├─ technologies
│  │  │  │  └─ index.js
│  │  │  ├─ update-avatar
│  │  │  │  └─ index.js
│  │  │  └─ user
│  │  │     └─ index.js
│  │  ├─ reportWebVitals.js
│  │  ├─ setupTests.js
│  │  └─ utils
│  │     ├─ hex-to-rgba.js
│  │     ├─ index.js
│  │     ├─ use-recipe.js
│  │     ├─ use-recipes.js
│  │     ├─ use-subscriptions.js
│  │     ├─ use-tags.js
│  │     └─ validation.js
│  └─ yarn.lock
├─ infra
│  ├─ docker-compose.production.yml
│  ├─ docker-compose.yml
│  ├─ Dockerfile
│  └─ nginx.conf
├─ postman_collection
│  ├─ clear_db.sh
│  ├─ foodgram.postman_collection.json
│  └─ README.md
├─ pyproject.toml
├─ README.md
└─ uv.lock

```

## Автор
ivxmirov - [GitHub](https://github.com/ivxmirov)

