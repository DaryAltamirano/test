FROM python:3.8-slim-buster

LABEL maintainer="Darien Altamirano <altamiranodary16@gmail.com>"

WORKDIR /python-docker
COPY requirements.txt requirements.txt

RUN apt-get update
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x boot.sh

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
