FROM python:3.9.15-alpine

ARG requirement

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR code
RUN apk update && apk add postgresql-dev gcc python3-dev py3-setuptools musl-dev curl
RUN apk add tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
    libxcb-dev libpng-dev

COPY ./requirements requirements
RUN pip install -U pip
RUN pip install -r requirements/$requirement.txt

COPY . /code/
WORKDIR /code/src
ENV PORT=8000
EXPOSE $PORT
