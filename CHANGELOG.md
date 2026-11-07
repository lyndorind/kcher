# Changelog

## [1.5.1] - 2026-11-07
### Added
- `docker-compose.observability.yml`: стек Grafana, Loki, Tempo, Prometheus та OpenTelemetry Collector (contrib) з томами для персистентності даних; пароль адміністратора Grafana передається через Docker secret
- Конфігурація OpenTelemetry Collector (`observability/otel-collector.yaml`): приймає OTLP від сервісу, трейси надсилає в Tempo, метрики в Prometheus, логи в Loki
- Автоматичне додавання джерел даних Grafana (provisioning): Prometheus, Loki, Tempo

### Changed
- Інструментування бази даних: замість `opentelemetry-instrumentation-sqlalchemy` (не підтримує SQLAlchemy 2.1) використано `opentelemetry-instrumentation-psycopg`, у трейсах з'явились спани SQL-запитів
- Запити `/health` виключено з трейсів (`OTEL_PYTHON_FASTAPI_EXCLUDED_URLS`)

## [1.5.0] - 2026-11-07
### Added
- Інструментування сервісу OpenTelemetry: автоматичні трейси FastAPI і SQLAlchemy, експорт логів, власні метрики `kcher.calculations` та `kcher.calculation_errors`
- Налаштування логування застосунку (`k_cher.logging_config`) і тести логування

### Changed
- Dockerfile: запуск через `opentelemetry-instrument`, змінні `OTEL_*` (експорт вимкнено за замовчуванням)
- Додано залежності `opentelemetry-*`

## [1.4.4] - 2026-11-01
### Added
- Конфігурація навантажувального тестування Apache JMeter: `jmeter/kcher-load-test.jmx` (параметри користувачів, розгону і тривалості через `-J`)
- Job `load test (JMeter)` у воркфлоу `PR Docker Build`: запускається паралельно з іншими перевірками PR, зберігає результати й HTML-звіт JMeter як артефакт `load-test-results`
- Скрипт `scripts/monitor-containers.sh` для моніторингу CPU та пам'яті контейнерів під час тесту
- Скрипт `scripts/summarize-load-test.py`: підсумок у GitHub Step Summary та контроль частки помилок (не більше 1 %)

## [1.4.3] - 2026-11-01
### Added
- `docker-compose.yml` для розгортання сервісу разом із PostgreSQL 16: том `pgdata` для персистентності даних і Docker secret `db_password` для пароля бази даних
- Розділ «Запуск через Docker Compose» у README

### Changed
- `.gitignore`: каталог `secrets/` не потрапляє в репозиторій

## [1.4.2] - 2026-11-01
### Added
- Інтеграційні тести API у Postman: колекція `postman/kcher.postman_collection.json` (11 запитів з перевірками)
- Job `integration (Postman)` у воркфлоу `PR Docker Build`: запускає Newman проти тимчасового образу `pr-<номер>-<sha>` і PostgreSQL, які піднімаються через блок `services`, паралельно з unit-тестами
- HTML-звіт Newman (htmlextra) зберігається як артефакт `newman-report`

### Changed
- Воркфлоу `PR Docker Build` передає посилання на тимчасовий образ наступним job

## [1.4.1] - 2026-11-01
### Added
- Воркфлоу `PR Docker Build`: збірка й публікація Docker-образу в pull request із тимчасовим тегом `pr-<номер>-<sha>` та smoke-тестом

## [1.4.0] - 2026-11-01
### Added
- API журналу обчислень із зберіганням у PostgreSQL: `POST /calculations`, `GET /calculations`, `GET /calculations/{id}`, `DELETE /calculations/{id}`
- Ендпоінт `GET /ready` для перевірки підключення до бази даних
- Налаштування підключення до бази даних через змінні середовища, включно з паролем із файлу (Docker secret)
- Тести нового API на SQLite у пам'яті

### Changed
- Додано залежності `sqlalchemy` і `psycopg`

## [1.3.3] - 2026-10-26
### Fixed
- Підпис образу cosign виконується у форматі, сумісному з Docker Hub (без Referrers API)

## [1.3.2] - 2026-10-26
### Fixed
- Воркфлоу публікації образу: виправлено версію cosign-installer (v4.1.2)
- Сповіщення про публікацію образу налаштовано через інтеграцію GitHub для Slack

## [1.3.1] - 2026-10-26
### Added
- Підпис образу cosign (keyless) та перевірка підпису у воркфлоу публікації
- Сповіщення про публікацію образу в Slack
- Планове та ручне сканування образу (Trivy, Grype, Snyk) зі звітами SARIF у Code Scanning

## [1.3.0] - 2026-10-26
### Added
- Dockerfile та .dockerignore для збірки контейнерного образу
- Воркфлоу публікації образу в Docker Hub при створенні релізу

## [1.2.0] - 2026-10-25
### Added
- REST API на FastAPI (`/health`, `/version`, `/hello/{name}`, `/add`, `/divide`) і тести до нього
- Керування залежностями через uv (`uv.lock`)
- Dependabot для GitHub Actions та uv
### Changed
- Оновлено версії GitHub Actions (checkout v7, upload-artifact v7, setup-uv v10)
- Воркфлоу збірки й релізу використовують uv
### Fixed
- Виправлення зауважень викладача: REST-додаток, uv у воркфлоу, актуальні версії actions
- Release workflow більше не падає, якщо тег уже існує

## [1.1.0] - 2026-10-08
### Added
- Python-пакет `k_cher` з функцією `hello`
- Воркфлоу збірки пакету на Pull Request (артефакти + SHA-256)
- Автоматичний реліз при злитті в `main`

## [1.0.0]
- Initial setup
- Додано README.md
- Додано Issue та Pull Request шаблони