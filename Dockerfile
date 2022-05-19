FROM python:3.9

ARG USER_ID
ARG GROUP_ID

COPY requirements/requirements.txt /tmp/requirements.txt

RUN set -x \
    && python -m venv /opt/mmapi \
    && /opt/mmapi/bin/python -m pip install -U pip wheel setuptools \
    && /opt/mmapi/bin/python -m pip install --no-cache-dir -q -r /tmp/requirements.txt \
    && mkdir -p /workspace && chown -R $USER_ID:$GROUP_ID /workspace && chown -R $USER_ID:$GROUP_ID /opt/mmapi

RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user

USER user

WORKDIR /workspace

ENV PATH="/opt/mmapi/bin:${PATH}"

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /workspace/src