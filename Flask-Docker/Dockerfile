FROM python:3.10-alpine AS builder

WORKDIR /app

RUN apk add --no-cache --virtual .build-deps \
    build-base \
    gcc \
    musl-dev \
    pkgconfig \
    sdl2-dev \
    sdl2_image-dev \
    sdl2_mixer-dev \
    sdl2_ttf-dev \
    freetype-dev

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.10-alpine

RUN apk add --no-cache \
    sdl2 \
    sdl2_image \
    sdl2_mixer \
    sdl2_ttf \
    freetype

COPY --from=builder /install /usr/local
COPY app/ /app/

EXPOSE 5000

WORKDIR /app

CMD ["python", "app.py"]