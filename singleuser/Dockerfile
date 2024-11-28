# Build as jupyterhub/singleuser
# Run with the DockerSpawner in JupyterHub

ARG BASE_IMAGE=quay.io/jupyter/base-notebook
FROM $BASE_IMAGE
LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

ARG JUPYTERHUB_VERSION=""
RUN if [ -n "$JUPYTERHUB_VERSION" ]; then python3 -mpip install --no-cache --upgrade --upgrade-strategy only-if-needed jupyterhub=="$JUPYTERHUB_VERSION"; fi
