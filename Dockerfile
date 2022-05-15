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