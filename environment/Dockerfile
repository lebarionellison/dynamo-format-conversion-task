FROM python:3.11-slim@sha256:49811f43477eefcbdfb09339e0839e55a02e6c86fa10b9044d18ec06e57924ce

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    jq \
    coreutils \
    binutils \
    && rm -rf /var/lib/apt/lists/*

COPY generate_corrupt_asset.py /app/
RUN python3 generate_corrupt_asset.py && rm generate_corrupt_asset.py

RUN mkdir -p /app/output
