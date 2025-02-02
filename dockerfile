FROM nvidia/cuda:12.5.1-runtime-ubuntu24.04
RUN mkdir -p /usr/src/install/logs/
RUN touch /usr/src/install/logs/install.txt
RUN echo 'Created log file' > /usr/src/install/logs/install.txt
RUN apt-get update
RUN echo 'Updated apt-get' >> /usr/src/install/logs/install.txt
RUN apt-get install -y python3
RUN echo 'Installed python' >> /usr/src/install/logs/install.txt
RUN apt-get install -y python3-pip
RUN echo 'Installed pip' >> /usr/src/install/logs/install.txt
RUN echo 'which python' >> /usr/src/install/logs/install.txt
RUN apt install -y curl
RUN echo "Installed curl" >> /usr/src/install/logs/install.txt
RUN apt-get install -y clang
RUN echo 'Installed clang' >> /usr/src/install/logs/install.txt
RUN cat /usr/src/install/logs/install.txt
RUN echo "Home directory:" >> /usr/src/install/logs/install.txt
RUN echo ${HOME} >> /usr/src/install/logs/install.txt
RUN echo "PATH:" >> /usr/src/install/logs/install.txt
RUN echo ${PATH} >> /usr/src/install/logs/install.txt
RUN cat /usr/src/install/logs/install.txt
RUN apt install -y git
RUN echo 'Installed git' >> /usr/src/install/logs/install.txt
RUN apt install -y gh
RUN echo 'Installed gh' >> /usr/src/install/logs/install.txt
RUN apt-get install -y pipx
RUN echo 'Installed pipx' >> /usr/src/install/logs/install.txt
RUN pipx install hatch
ENV PATH="/root/.local/bin:${PATH}"
RUN echo 'Installed hatch' >> /usr/src/install/logs/install.txt
