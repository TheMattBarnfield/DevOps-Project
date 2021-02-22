FROM python:3.9.0-slim-buster as base

EXPOSE 5000

RUN apt-get update \
    && apt-get install -y curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /app

COPY poetry.toml poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.createfalse --local &&\
    poetry install

COPY . .

FROM base as prod
CMD poetry run gunicorn --bind 0.0.0.0:$PORT "app:create_app(None)"

FROM base as dev
CMD poetry run flask run --host=0.0.0.0

FROM base as test
RUN poetry install

FROM test as unit
CMD poetry run pytest tests/unit

FROM test as integration
CMD poetry run pytest tests/integration

FROM test as e2e

# Install Chrome
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
    apt-get install ./chrome.deb -y &&\
    rm ./chrome.deb

# Install Chromium WebDriver
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` &&\
    echo "Installing chromium webdriver version ${LATEST}" &&\
    curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
    apt-get install unzip -y &&\
    unzip ./chromedriver_linux64.zip

CMD poetry run pytest tests/e2e

FROM e2e as all_tests
CMD poetry run pytest tests
