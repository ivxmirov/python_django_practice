FROM python:3.9
WORKDIR /app

# Устанавливаем uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Копируем файлы зависимостей из корня
COPY pyproject.toml uv.lock /app/

# Устанавливаем зависимости
RUN uv sync --frozen --no-dev

# Копируем код бэкенда
COPY backend/ /app/

# Добавляем venv в PATH
ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8888", "foodgram.wsgi"]
