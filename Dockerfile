FROM tinsirius/ece4078_prac:focal-a8c0557

RUN python3 -m pip install --no-cache-dir notebook==6.4.8 jupyterlab==4.0.3 ipympl==0.9.3 ipywidgets==8.0.7

ARG NB_USER=tokyo-rl
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}

WORKDIR ${HOME}
USER ${NB_USER}
