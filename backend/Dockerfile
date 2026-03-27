FROM python:3.14.3-alpine3.23

WORKDIR /usr/src/app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup 

COPY --chown=appuser:appgroup . .

USER appuser

EXPOSE 8080/tcp

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s \
    CMD wget --spider -q http://127.0.0.1:8080/ || exit 1

CMD [ "python", "./app.py" ]
