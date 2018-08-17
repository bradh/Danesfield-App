# Danesfield App

Application to run Danesfield algorithms.

# Server

## Requirements

- [Girder](https://github.com/girder/girder)
- [Girder Worker](https://github.com/girder/girder_worker) at revision [ad3e384](https://github.com/girder/girder_worker/commit/ad3e384f4894b8fb747b3bab87e39376e3701049) or later
- [Girder Geospatial](https://github.com/OpenGeoscience/girder_geospatial)
- [Docker](https://www.docker.com/)

## Setup

### On Girder host

Install the Girder plugin by running:
```bash
girder-install plugin /path/to/danesfield-app/danesfield-server
```

### On Girder Worker host

Ensure that the following Docker images are available:
- `gitlab.kitware.com:4567/core3d/danesfield-app/danesfield`
- `gitlab.kitware.com:4567/core3d/danesfield-app/p3d_gw`

These images may be pulled from the [container registry](https://gitlab.kitware.com/core3d/danesfield-app/container_registry).

Ensure that the [GTOPO 30 data](https://data.kitware.com/#folder/5aa993db8d777f068578d08c) is
available in `/mnt/GTOPO30`. This data is a requirement of P3D.

#### Building the Docker images

Currently, these Docker images are not automatically built. Follow the steps below to build them when necessary.

To build `gitlab.kitware.com:4567/core3d/danesfield-app/danesfield`:
- Run `docker build -t gitlab.kitware.com:4567/core3d/danesfield-app/danesfield .` in the `danesfield` repository root.

To build `gitlab.kitware.com:4567/core3d/danesfield-app/p3d_gw`:
- Follow the linked instructions to build the [p3d Docker image](https://data.kitware.com/#collection/59c1963d8d777f7d33e9d4eb/folder/5aa933de8d777f068578c303).
- Run `docker build -t  gitlab.kitware.com:4567/core3d/danesfield-app/p3d_gw .` in [support/docker/p3d_gw](./support/docker/p3d_gw).

To archive an image for transfer to another system, run `docker save IMAGE_NAME | gzip > image.gz`.

To load an archived image, run `gzip -d -c image.gz | docker load`.

## Configuration

### UNet Semantic Segmentation

- Upload the configuration and model files referenced in the tool documentation
  (TBD).
- Set the `danesfield.unet_semantic_segmentation_config_file_id` and
  `danesfield.unet_semantic_segmentation_model_file_id` settings to the IDs of
  those files.

### Material Classification

- Upload the model file referenced in the [tool documentation](
https://gitlab.kitware.com/core3d/danesfield/tree/master/tools#material-classification)
to Girder.
- Set the `danesfield.material_classifier_model_file_id` setting to the ID of that file.

# Client Setup
See [here](client/README.md)
