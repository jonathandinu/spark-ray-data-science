FROM jupyter/pyspark-notebook:d990a62010ae

ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
RUN wget -nc -P code/data/ https://jonathans.estate/data/crossvalidated/Posts.xml
USER ${NB_USER}

RUN rm -rf /home/jovyan/work
RUN pip install --no-cache-dir notebook==5.*
RUN pip install pyspark ray[tune]==1.2.0 ray[serve]==1.2.0 pandas==1.2.3

ENV JUPYTER_ENABLE_LAB='yes'
