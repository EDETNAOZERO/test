FROM python:3.14.3-alpine3.23

WORKDIR /usr/src/app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup 

COPY --chown=appuser:appgroup . .

USER appuser

EXPOSE 3000/tcp

HEALTHCHECK --interval=60s --timeout=5s --start-period=60s \
    CMD wget --spider -q http://127.0.0.1:3000/ || exit 1

CMD [ "python", "./app.py" ]
