FROM python:3-alpine
WORKDIR /usr/src/app
RUN addgroup -S appgroup && adduser -S appuser -G appgroup && \
    apk --no-cache add curl
COPY --chown=appuser:appgroup . .
USER appuser
EXPOSE 3000/tcp
HEALTHCHECK --interval=1m --timeout=5s --start-period=1m \
    CMD curl -f http://localhost:3000/ || exit 1
CMD [ "python", "./app.py" ]
