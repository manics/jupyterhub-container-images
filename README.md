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
- [jupyterhub/jupyterhub-demo](https://quay.io/repository/jupyterhub/jupyterhub-demo?tab=tags)
- [jupyterhub/singleuser](https://quay.io/repository/jupyterhub/singleuser?tab=tags)

## Using these images

The Hub images run jupyterhub in the `/srv/jupyterhub` directory.
If you place your `jupyterhub_config.py` there,
either by mounting `/srv/jupyterhub` as a volume, or adding

```dockerfile
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
```

in your Dockerfile for your derived image.

### jupyterhub-onbuild

We no longer publish the `jupyterhub-onbuild` image,
starting with jupyterhub 5.3.
If you used `jupyterhub-onbuild` before,

```dockerfile
FROM quay.io/jupyterhub/jupyterhub-onbuild:5.2.1
```

can be replaced with

```dockerfile
FROM quay.io/jupyterhub/jupyterhub:5.2.1
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
```
