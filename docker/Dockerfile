ARG PYTHON_BASE=slim-buster
ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}-${PYTHON_BASE} AS python

ENV INSTALL_PATH /app
WORKDIR $INSTALL_PATH

COPY requirements.txt ${INSTALL_PATH}
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/*.py ./src/*.conf ${INSTALL_PATH}/

#--------------------------------#
# Run pytest to validate our app #
#--------------------------------#
FROM python as test_image

RUN pip install --no-cache-dir \
        pytest==6.2.4 \
        pytest-asyncio==0.15.1 \
        httpx==0.18.2 \
    && pytest

#-----------------------------#
# Construct our runtime image #
#-----------------------------#
FROM python as runtime_image

LABEL \
  org.opencontainers.image.title="Diagnostics Tools API" \
  org.opencontainers.image.description="An HTTP responder for testing web infrastructure" \
  org.opencontainers.image.authors="rfenn@vt.edu" \
  org.opencontainers.image.vendor="Virginia Tech / Enterprise Systems" \
  org.opencontainers.image.source="https://code.vt.edu/es/" \
  org.opencontainers.image.version="v1.0"

USER nobody
EXPOSE 10000

# ENTRYPOINT ["/usr/local/bin/gunicorn", \
#             "-b", "0.0.0.0:10000", \
#             "--worker-tmp-dir", "/dev/shm", \
#             "--log-config", "logging.conf", \
#             "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker"]

HEALTHCHECK --interval=30s --timeout=15s --start-period=5s --retries=3 CMD [ "/usr/local/bin/python", "/app/healthcheck.py" ]

ENTRYPOINT ["/usr/local/bin/uvicorn", \
            "--host", "0.0.0.0", \
            "--port", "10000", \
            "--no-access-log"]
CMD ["api:app"]
