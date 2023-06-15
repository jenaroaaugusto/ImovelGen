# syntax=docker/dockerfile:1
ARG PLONE_VERSION=6.0.5
FROM plone/server-builder:${PLONE_VERSION} as builder

WORKDIR /app

# Add local code
COPY . .

# Install local requirements and pre-compile mo files
RUN <<EOT
    bin/pip install mxdev
    mv requirements-docker.txt requirements.txt
    bin/mxdev -c mx.ini
    bin/pip install -r requirements-mxdev.txt
    bin/python /compile_mo.py
    rm -Rf src/
EOT

FROM plone/server-prod-config:${PLONE_VERSION}

LABEL maintainer="Jenaro Augusto <jenaroaaugusto@outlook.com>" \
      org.label-schema.name="ImovelGen-backend" \
      org.label-schema.description="ImovelGen backend image." \
      org.label-schema.vendor="Jenaro Augusto"

# Copy /app from builder
COPY --from=builder /app /app

RUN <<EOT
    ln -s /data /app/var
EOT
