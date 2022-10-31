FROM debian:stable-slim
RUN apt-get update     --assume-yes \
    && apt-get install --assume-yes --no-install-recommends \
               build-essential \
               ca-certificates \
               curl \
               git \
               libbz2-dev \
               libffi-dev \
               liblzma-dev \
               libncurses-dev \
               libreadline-dev \
               libsqlite3-dev \
               libssl-dev \
               vim \
               zlib1g-dev \
    && apt-get upgrade --assume-yes
ARG ASDF_GITREF=v0.10.2
RUN git config --global advice.detachedHead false; \
    git clone  --single-branch \
               --branch ${ASDF_GITREF} \
    "https://github.com/asdf-vm/asdf.git" "${HOME}/.asdf"
ARG RUNTIMES_VERSIONS="python:latest"
# ARG RUNTIMES_VERSIONS=""
ENV PATH="/root/.asdf/bin:$PATH"
RUN for ELECTED in ${RUNTIMES_VERSIONS}; do RUNTIME=${ELECTED%:*}; VERSION=${ELECTED#*:}; \
    asdf plugin list | grep --quiet ${RUNTIME} || asdf plugin add ${RUNTIME} \
    && asdf install ${RUNTIME} ${VERSION} || exit; done

RUN echo ". ${HOME}/.asdf/asdf.sh" >> ${HOME}/.bashrc
RUN echo ". ${HOME}/.asdf/completions/asdf.bash" >> ${HOME}/.bashrc
WORKDIR /usr/src
