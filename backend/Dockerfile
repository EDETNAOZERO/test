FROM python:3-alpine
WORKDIR /usr/src/app
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
COPY --chown=appuser:appgroup . .
USER appuser
EXPOSE 3000
#HEALTHCHECK --interval=5m --timeout=5s \
#  CMD curl -f http://localhost/:3000 || exit 1
CMD [ "python", "./app.py" ]
