#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
#  Copyright Kitware Inc.
#
#  Licensed under the Apache License, Version 2.0 ( the "License" );
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
##############################################################################


class DanesfieldJobKey(object):
    """
    Keys for metadata attached to Danesfield jobs and related objects.
    """
    ID = 'danesfieldJobId'
    STEP_NAME = 'danesfieldJobStep'


class DanesfieldStep(object):
    """
    Names to identify steps in the Danesfield workflow.
    """
    INIT = 'init'
    FIT_DTM = 'fit-dtm'
    SELECT_BEST = 'select-best'
    GENERATE_DSM = 'generate-dsm'
    GENERATE_POINT_CLOUD = 'generate-point-cloud'
    MSI_TO_RGB = 'msi-to-rgb'
    ORTHORECTIFY = 'orthorectify'
    PANSHARPEN = 'pansharpen'
    SEGMENT_BY_HEIGHT = 'segment-by-height'
    UNET_SEMANTIC_SEGMENTATION = 'unet-semantic-segmentation'
    BUILDING_SEGMENTATION = 'building-segmentation'
    CLASSIFY_MATERIALS = 'classify-materials'
    ROOF_GEON_EXTRACTION = 'roof-geon-extraction'
    BUILDINGS_TO_DSM = 'buildings-to-dsm'
    GET_ROAD_VECTOR = 'get-road-vector'


class DockerImage(object):
    """
    Names of Docker images to run Danesfield algorithms.
    """
    DANESFIELD = 'gitlab.kitware.com:4567/core3d/danesfield-app/danesfield'
    P3D = 'gitlab.kitware.com:4567/core3d/danesfield-app/p3d_gw'
