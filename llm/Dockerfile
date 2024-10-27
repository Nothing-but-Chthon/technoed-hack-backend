FROM python:3.11-slim

COPY requirements.txt /requirements.txt
COPY llm-api.py /llm-api.py
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "llm-api:app", "--host", "0.0.0.0", "--port", "8000"]
