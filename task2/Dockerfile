FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -r appuser && \
    useradd -r -g appuser -d /app appuser

WORKDIR /app

RUN pip3 install requests

COPY --chown=appuser:appuser script.py /app/script.py

USER appuser

CMD ["python3", "script.py"]