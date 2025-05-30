FROM jenkins/jenkins:lts

USER root
RUN apt-get update && apt-get install -y curl

USER jenkins

RUN jenkins-plugin-cli --plugins prometheus:2.0.10
