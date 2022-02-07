FROM python:3.9-slim

RUN adduser --disabled-password --gecos '' python;\
    mkdir /opt/python;\
    chown python:python /opt/python

RUN apt-get update && apt-get -y --no-install-recommends install\
      binutils \
      build-essential \
      curl \
      fiona \
      gdal-bin \
      git \
      libgdal-dev \
      libpq-dev \
      libproj-dev \
      # for django DB graph
      python3-pygraphviz \
      wget \
      zlib1g-dev \
      && python3 -m pip install --upgrade pip \
      && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
      && rm -rf /var/lib/apt/lists/*
# rm -rf /var/lib/apt/lists/* command cleans up apt cache


# switch from root user to python
USER python
WORKDIR /opt/python

# create staticfiles directory
RUN mkdir -p staticfiles \
             media/rasters

# prevent from writing pycfiles
ENV PYTHONDONTWRITEBYTECODE=1

# Show messages on the console
ENV PYTHONUNBUFFERED=1

COPY --chown=python:python requirements.txt ./
ENV PATH="/home/python/.local/bin:$PATH"
RUN pip3 install -r requirements.txt

COPY --chown=python:python . .
RUN chmod +x start.sh
CMD ./start.sh