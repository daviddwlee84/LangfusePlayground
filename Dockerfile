# https://docs.streamlit.io/deploy/tutorials/docker

FROM python:3.9-slim

WORKDIR /app

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY Overview.py .

EXPOSE 8501

# This can make Traefik identify this as unhealthy container
# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "Overview.py", "--server.port=8501", "--server.address=0.0.0.0"]
