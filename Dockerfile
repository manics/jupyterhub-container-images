FROM python:3.6.3-alpine3.6
RUN pip3 install --no-cache jupyterhub==0.8.0
ENV LANG=en_US.UTF-8


