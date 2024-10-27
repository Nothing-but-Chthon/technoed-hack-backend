FROM python:3.11-slim

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY llm-api.py /llm-api.py

EXPOSE 8008

CMD ["uvicorn", "llm-api:app", "--host", "0.0.0.0", "--port", "8008"]
