FROM python:3.9.0a2-alpine3.10

WORKDIR /usr/src/app

COPY . .

RUN apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN apk add --no-cache --upgrade bash
RUN apk add --no-cache postgresql-client
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x ./entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]

CMD ["172.20.0.10", "172.20.0.11"]


