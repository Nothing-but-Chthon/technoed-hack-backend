FROM python:3.11-slim

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY auth.py /auth.py
COPY conf.py /conf.py
COPY db.py /db.py
COPY main.py /main.py

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
