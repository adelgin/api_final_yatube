# API Final Yatube

## Описание проекта

Проект **Yatube** представляет собой RESTful API для социальной сети, позволяющий пользователям взаимодействовать друг с другом, создавать посты и комментарии, а также управлять своими учетными записями.

## Эндпоинты

### Пользователи

- **Получить список пользователей**
  - **Path:** `/api/v1/users/`
  - **Method:** `GET`

- **Создать нового пользователя**
  - **Path:** `/api/v1/users/`
  - **Method:** `POST`

- **Получить информацию о текущем пользователе**
  - **Path:** `/api/v1/users/me/`
  - **Method:** `GET`

- **Обновить информацию о текущем пользователе**
  - **Path:** `/api/v1/users/me/`
  - **Method:** `PUT`

- **Частично обновить информацию о текущем пользователе**
  - **Path:** `/api/v1/users/me/`
  - **Method:** `PATCH`

- **Удалить текущего пользователя**
  - **Path:** `/api/v1/users/me/`
  - **Method:** `DELETE`

- **Получить информацию о пользователе по ID**
  - **Path:** `/api/v1/users/{id}/`
  - **Method:** `GET`

- **Обновить информацию о пользователе по ID**
  - **Path:** `/api/v1/users/{id}/`
  - **Method:** `PUT`

- **Частично обновить информацию о пользователе по ID**
  - **Path:** `/api/v1/users/{id}/`
  - **Method:** `PATCH`

- **Удалить пользователя по ID**
  - **Path:** `/api/v1/users/{id}/`
  - **Method:** `DELETE`

### Посты

- **Получить список постов**
  - **Path:** `/api/v1/posts/`
  - **Method:** `GET`

- **Создать новый пост**
  - **Path:** `/api/v1/posts/`
  - **Method:** `POST`

- **Получить информацию о посте по ID**
  - **Path:** `/api/v1/posts/{id}/`
  - **Method:** `GET`

- **Обновить пост по ID**
  - **Path:** `/api/v1/posts/{id}/`
  - **Method:** `PUT`

- **Частично обновить пост по ID**
  - **Path:** `/api/v1/posts/{id}/`
  - **Method:** `PATCH`

- **Удалить пост по ID**
  - **Path:** `/api/v1/posts/{id}/`
  - **Method:** `DELETE`

### Группы

- **Получить список групп**
  - **Path:** `/api/v1/groups/`
  - **Method:** `GET`

- **Получить информацию о группе по ID**
  - **Path:** `/api/v1/groups/{id}/`
  - **Method:** `GET`

### Подписки

- **Получить список подписок**
  - **Path:** `/api/v1/follow/`
  - **Method:** `GET`

- **Подписаться на пользователя**
  - **Path:** `/api/v1/follow/`
  - **Method:** `POST`

### Комментарии к постам

- **Получить список комментариев к посту**
  - **Path:** `/api/v1/posts/{post_id}/comments/`
  - **Method:** `GET`

- **Создать новый комментарий к посту**
  - **Path:** `/api/v1/posts/{post_id}/comments/`
  - **Method:** `POST`

- **Получить информацию о комментарии по ID**
  - **Path:** `/api/v1/posts/{post_id}/comments/{id}/`
  - **Method:** `GET`

- **Обновить комментарий по ID**
  - **Path:** `/api/v1/posts/{post_id}/comments/{id}/`
  - **Method:** `PUT`

- **Частично обновить комментарий по ID**
  - **Path:** `/api/v1/posts/{post_id}/comments/{id}/`
  - **Method:** `PATCH`

- **Удалить комментарий по ID**
  - **Path:** `/api/v1/posts/{post_id}/comments/{id}/`
  - **Method:** `DELETE`

### Аутентификация

- **Получить токен аутентификации**
  - **Path:** `/api/v1/api-token-auth/`
  - **Method:** `POST`

- **Активировать пользователя**
  - **Path:** `/api/v1/users/activation/`
  - **Method:** `POST`

- **Отправить повторную активацию**
  - **Path:** `/api/v1/users/resend_activation/`
  - **Method:** `POST`

- **Сбросить пароль**
  - **Path:** `/api/v1/users/reset_password/`
  - **Method:** `POST`

- **Подтвердить сброс пароля**
  - **Path:** `/api/v1/users/reset_password_confirm/`
  - **Method:** `POST`

- **Сбросить имя пользователя**
  - **Path:** `/api/v1/users/reset_username/`
  - **Method:** `POST`

- **Подтвердить сброс имени пользователя**
  - **Path:** `/api/v1/users/reset_username_confirm/`
  - **Method:** `POST`

- **Установить новый пароль**
  - **Path:** `/api/v1/users/set_password/`
  - **Method:** `POST`

- **Установить новое имя пользователя**
  - **Path:** `/api/v1/users/set_username/`
  - **Method:** `POST`

- **Создать JWT токен**
  - **Path:** `/api/v1/jwt/create/`
  - **Method:** `POST`

- **Обновить JWT токен**
  - **Path:** `/api/v1/jwt/refresh/`
  - **Method:** `POST`

- **Проверить JWT токен**
  - **Path:** `/api/v1/jwt/verify/`
  - **Method:** `POST`

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш_репозиторий/api_final_yatube.git
