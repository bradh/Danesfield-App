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

import re

from ..algorithms import buildingsToDsm
from ..constants import DanesfieldStep
from ..workflow import DanesfieldWorkflowException
from ..workflow_step import DanesfieldWorkflowStep
from ..workflow_utilities import (
    getOptions,
    getWorkingSet,
    isObj)


class BuildingsToDsmStep(DanesfieldWorkflowStep):
    """
    Step that runs Purdue and Columbia's roof geon extraction.

    Supports the following options:
    - <none>
    """
    def __init__(self):
        super(BuildingsToDsmStep, self).__init__(
            DanesfieldStep.BUILDINGS_TO_DSM)
        self.addDependency(DanesfieldStep.ROOF_GEON_EXTRACTION)
        self.addDependency(DanesfieldStep.FIT_DTM)

    def run(self, jobInfo, outputFolder):
        # Get working sets
        initWorkingSet = getWorkingSet(DanesfieldStep.INIT, jobInfo)
        roofGeonExtractionWorkingSet = getWorkingSet(
            DanesfieldStep.ROOF_GEON_EXTRACTION,
            jobInfo)
        dtmWorkingSet = getWorkingSet(DanesfieldStep.FIT_DTM, jobInfo)

        # Get OBJ files
        objFiles = self.getFiles(roofGeonExtractionWorkingSet, isObj)

        # Get DTM
        dtmFile = self.getSingleFile(dtmWorkingSet)

        # Get options
        buildingsToDsmOptions = getOptions(self.name, jobInfo)

        # Set output prefix; replacing whitespace with underscores
        outputPrefix = re.sub("\\s", "_", initWorkingSet['name'])

        # Run algorithm
        buildingsToDsm(
            initWorkingSetName=initWorkingSet['name'],
            stepName=self.name,
            requestInfo=jobInfo.requestInfo,
            jobId=jobInfo.jobId,
            outputFolder=outputFolder,
            objFiles=objFiles,
            dtmFile=dtmFile,
            outputPrefix=outputPrefix,
            **buildingsToDsmOptions)
