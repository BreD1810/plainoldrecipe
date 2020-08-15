from debian:buster-slim

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

WORKDIR /app

EXPOSE 5000

COPY requirements.txt ./
COPY plainoldrecipe ./plainoldrecipe

RUN pip3 install --no-cache-dir -r requirements.txt && pip3 install gunicorn

ENV SCRIPT_NAME /recipes

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "plainoldrecipe:app"]
