# K_CHER

[![codecov](https://codecov.io/gh/lyndorind/K_CHER/graph/badge.svg)](https://codecov.io/gh/lyndorind/K_CHER)

## Опис
У цьому репозиторії зберігаються файли, створені під час виконання практичних завдань з роботи з системою контролю версій Git та платформою GitHub.

## Основні файли
- `README.md` — загальна інформація про репозиторій.
- `CHANGELOG.md` — історія змін у проєкті.
- `CONTRIBUTING.md` — рекомендації щодо внесення змін.
- `.github/` — шаблони для Issue та Pull Request.

## Робота з репозиторієм

Для роботи з проєктом використовуються окремі гілки. Зміни додаються через коміти, після чого створюється Pull Request для перевірки та подальшого об'єднання з гілкою `main`.

## Перевірка змін

Перед об'єднанням Pull Request зміни проходять review. У разі необхідності reviewer може запросити додаткові виправлення, після чого Pull Request перевіряється повторно.

## Запуск через Docker Compose

1. Створіть файл із паролем бази даних:
   ```bash
   mkdir -p secrets
   openssl rand -base64 24 | tr -d '\n' > secrets/db_password.txt
   ```
2. Запустіть сервіс:
   ```bash
   docker compose up -d
   ```
3. Перевірте: `curl http://localhost:8000/ready`

Дані PostgreSQL зберігаються в томі `pgdata`. Видалити їх разом із контейнерами: `docker compose down -v`.
