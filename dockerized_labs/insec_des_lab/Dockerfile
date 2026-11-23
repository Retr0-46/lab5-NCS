FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 8080

ENTRYPOINT ["./entrypoint.sh"]
