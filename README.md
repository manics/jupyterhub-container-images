# JupyterHub Container Images

[![Build](https://github.com/jupyterhub/jupyterhub-container-images/actions/workflows/build.yml/badge.svg)](https://github.com/jupyterhub/jupyterhub-container-images/actions/workflows/build.yml)

Definitions and workflows for publishing JupyterHub container images.

## How this works

All pushes to `main` (and any designated backport branches) are built and published.
Pushes to `main` are assumed to always be the latest, so images are always tagged with

- `MAJOR.MINOR.PATCH-BUILDNUMBER`
- `MAJOR.MINOR.PATCH`
- `MAJOR.MINOR`
- `MAJOR`
- `latest`

where `MAJOR.MINOR.PATCH` is the JupyterHub version.

## Publishing backports

Backports are published in their own branches.
For example, see https://github.com/jupyterhub/jupyterhub-container-images/compare/main..4.x

## Images

The following images are published by this repository:

- [jupyterhub/jupyterhub](https://quay.io/repository/jupyterhub/jupyterhub?tab=tags)
- [jupyterhub/jupyterhub-onbuild](https://quay.io/repository/jupyterhub/jupyterhub-onbuild?tab=tags)
- [jupyterhub/jupyterhub-demo](https://quay.io/repository/jupyterhub/jupyterhub-demo?tab=tags)
- [jupyterhub/singleuser](https://quay.io/repository/jupyterhub/singleuser?tab=tags)
