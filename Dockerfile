FROM public.ecr.aws/docker/library/alpine:3.14
RUN apk add py3-pip \
    && pip install --upgrade pip

WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt --ignore-installed
ARG RDS_HOST
ARG RDS_DATABASE
ARG RDS_PASSWORD
ARG RDS_USERNAME
RUN python3 -m pytest

EXPOSE 5000
CMD ["python3", "application.py"]

# Configuración New relic

RUN pip install newrelic

ENV NEW_RELIC_APP_NAME="blacklist"
ENV NEW_RELIC_LOG=stdout
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
ENV NEW_RELIC_LICENSE_KEY=bf22d45ad67f8b2431717a33da5cc28917d9NRAL
ENV NEW_RELIC_LOG_LEVEL=info

ENTRYPOINT ["newrelic-admin", "run-program"]