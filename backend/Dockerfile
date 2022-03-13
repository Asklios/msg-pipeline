FROM python:alpine3.14

RUN apk add curl

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN python -m ensurepip --upgrade
RUN pip install -r requirements.txt

COPY ./backend ./backend
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl --fail http://127.0.0.1:5000/api/v1/messages/health || exit 1
    
ENTRYPOINT ["python", "./backend/wsgi.py"]
