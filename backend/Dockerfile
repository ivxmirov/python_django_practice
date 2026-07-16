FROM python:3.9
WORKDIR /app

# Устанавливаем uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Копируем только файлы с зависимостями (для кеширования слоёв)
COPY pyproject.toml uv.lock /app/

# Устанавливаем зависимости
RUN uv sync --frozen --no-dev

# Копируем весь проект
COPY . .

# Команда запуска — теперь через uv run, чтобы подхватить виртуальное окружение
CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8888", "foodgram.wsgi"]
