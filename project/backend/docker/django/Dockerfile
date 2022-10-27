ARG PYTHON_VERSION=3.10.8
ARG APP_ENV=prod

FROM python:${PYTHON_VERSION}-bullseye AS base-builder

ENV VIRTUAL_ENV=/opt/venv \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.14 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local'

SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

# hadolint ignore=DL3008, DL3009
RUN apt-get update \
    && apt-get install --no-install-recommends -y curl \
    && curl -sSL 'https://install.python-poetry.org' | python - \
    && poetry --version \
    && python -m venv ${VIRTUAL_ENV}

# ----------------------------------------------------------------------------------------------------------------------

FROM base-builder as dev-builder

WORKDIR /

COPY pyproject.toml poetry.lock ./
COPY --from=base-builder /usr/local/bin/poetry /usr/local/bin/poetry

# hadolint ignore=SC2086
RUN poetry export --dev --without-hashes -o requirements.txt \
    && ${VIRTUAL_ENV}/bin/pip install -r requirements.txt

# ----------------------------------------------------------------------------------------------------------------------

FROM base-builder as prod-builder

WORKDIR /

COPY pyproject.toml poetry.lock ./
COPY --from=base-builder /usr/local/bin/poetry /usr/local/bin/poetry

# hadolint ignore=SC2086
RUN poetry export --without-hashes -o requirements.txt \
    && ${VIRTUAL_ENV}/bin/pip install -r requirements.txt

# ---------------------------------------------------------------

# hadolint ignore=DL3006
FROM ${APP_ENV}-builder AS builder

# ---------------------------------------------------------------
FROM python:${PYTHON_VERSION}-slim-bullseye AS build

ARG APP_ROOT=/opt/app
ARG APP_USER=appuser
ARG APP_GROUP=appgroup
ARG APP_USER_UID=1000
ARG APP_USER_GID=1000

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR ${APP_ROOT}

RUN groupadd -g "${APP_USER_GID}" -r ${APP_GROUP} \
  && useradd -d ${APP_ROOT} -g ${APP_GROUP} -l -r -u "${APP_USER_UID}" ${APP_USER} \
  && chown ${APP_USER}:${APP_GROUP} -R ${APP_ROOT} \
  && mkdir -p '/var/www/django/static' '/var/www/django/media' \
  && chown ${APP_USER}:${APP_GROUP} '/var/www/django/static' '/var/www/django/media' \
  && mkdir -p ${VIRTUAL_ENV} \
  && chown ${APP_USER}:${APP_GROUP} ${VIRTUAL_ENV}

COPY --from=builder --chown=${APP_USER}:${APP_GROUP} ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY --chown=${APP_USER}:${APP_GROUP} ./backend ${APP_ROOT}

USER ${APP_USER}

RUN SECRET_KEY=empty DOMAIN_NAME=empty python manage.py collectstatic --noinput
