FROM public.ecr.aws/docker/library/alpine:3.14
RUN apk add py3-pip \
    && pip install --upgrade pip

WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt --ignore-installed
RUN python -m pytest

EXPOSE 5000
CMD ["python3", "application.py"]