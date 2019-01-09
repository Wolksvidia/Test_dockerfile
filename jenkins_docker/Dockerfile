FROM jenkins/jenkins:lts

USER root

RUN curl -L https://get.docker.com/ | sh

RUN usermod -aG staff,docker jenkins

USER jenkins