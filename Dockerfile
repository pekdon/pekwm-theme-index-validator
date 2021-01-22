# Container image that runs your code
FROM alpine:3.13

# Copies your code file from your action repository to the filesystem
# path `/` of the container
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip

COPY entrypoint.py /entrypoint.py
COPY validate_theme.py /validate_theme.py
COPY requirements.txt /requirements.txt

RUN python3 -m pip install -r /requirements.txt

# Code file to execute when the docker container starts up (`entrypoint.py`)
ENTRYPOINT ["/entrypoint.py"]
