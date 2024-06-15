FROM python:3.10-slim
LABEL authors="olegafanasev"
WORKDIR /workdir
COPY . .
RUN apt-get update \
    && apt-get install -y iputils-ping
CMD ["python3", "mtu.py", "ya.ru"]