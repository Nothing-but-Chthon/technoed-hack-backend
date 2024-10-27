FROM python:3.11-slim

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY auth.py /auth.py

ARG CONF

RUN echo "$CONF" > /conf.py

RUN mkdir -p /etc/letsencrypt/live/chthon.servebeer.com

ARG FULLCHAIN
ARG PRIVKEY

RUN echo "$FULLCHAIN" > /etc/letsencrypt/live/chthon.servebeer.com/fullchain.pem && \
    echo "$PRIVKEY" > /etc/letsencrypt/live/chthon.servebeer.com/privkey.pem

COPY db.py /db.py
COPY main.py /main.py

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--ssl-keyfile", "/etc/letsencrypt/live/chthon.servebeer.com/privkey.pem", "--ssl-certfile", "/etc/letsencrypt/live/chthon.servebeer.com/fullchain.pem"]
