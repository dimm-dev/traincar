FROM ubuntu:20.04

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y dist-upgrade && apt-get install -y dpkg-dev sudo git-core && \
    apt-get install -y python3 python3-pip python3-pygame pylint python3-autopep8 && \
    apt-get install -y python3-keras python3-keras-applications python3-keras-preprocessing python3-lasagne && \
    apt-get install -y python-all python3-setuptools python3-stdeb dh-python && \
    apt-get clean && \
    groupadd --gid $USER_GID $USERNAME && \
    adduser --shell /bin/bash --uid $USER_UID --gid $USER_GID $USERNAME && \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME

# WORKDIR /home/developer/project
