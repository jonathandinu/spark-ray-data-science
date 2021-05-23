FROM jupyter/pyspark-notebook:d990a62010ae

ENV HOME /home/${NB_USER}

COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

RUN rm -rf /home/jovyan/work
RUN pip install ray[tune]==1.2.0 ray[serve]==1.2.0 pandas==1.2.3

ENV JUPYTER_ENABLE_LAB='yes'