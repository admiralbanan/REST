## Реализация авторизации и прав доступа

### 1. Настройка прав в `settings.py`
![image](https://github.com/user-attachments/assets/ef6baf8a-2f1e-45a6-8ecf-7125485f33ea)

---

### 2. Обновил `views.py`
![image](https://github.com/user-attachments/assets/06e0e458-023a-4277-a36c-1b52349a8ad2)

---

### 3. Редактирую `permissions.py`
![image](https://github.com/user-attachments/assets/26e36df6-483b-4e78-9c1b-fa5589ad4320)

---

### 4. Добавил права в аккаунты
![image](https://github.com/user-attachments/assets/57036b80-092e-4777-a306-f565168e4de2)

---

### 5. Проверка прав — скрытие информации для неавторизованных
![image](https://github.com/user-attachments/assets/cf016fc4-3a53-49e2-8bd6-96579a371e96)

---

## Реализация авторизации по токену

- Установлены библиотеки:
  ```
  pip install djangorestframework
  pip install djangorestframework-simplejwt
  ```

- Добавлен `rest_framework.authtoken` в `INSTALLED_APPS`

- Выполнена миграция:
  ```
  python manage.py migrate
  ```
  ![image](https://github.com/user-attachments/assets/92a25576-e044-4613-ba11-77c3c124ca83)

- Подключён `obtain_auth_token` в `urls.py`

---

### Получение токена для пользователя `admin/admin`
![image](https://github.com/user-attachments/assets/1005bc5c-c91e-4c02-b28a-93cd822f3e4c)

---

### Проверка доступа к API с токеном
![image](https://github.com/user-attachments/assets/cab0bf65-3c83-4f01-a687-47c7df9760fe)

---

### Тестирование через Django shell
```bash
python manage.py shell
```
![image](https://github.com/user-attachments/assets/778caba8-c0c1-4900-93ad-3b51a3614a4d)

---

Все шаги выполнены, создаю пул реквест.
