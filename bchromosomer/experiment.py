#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#@created: 17.01.2015
#@author: Aleksey Komissarov
#@contact: ad3002@gmail.com 

import sys, os    
from PyExp import AbstractExperiment
from PyExp import run_app
from PyExp import ProjectManager
from PyExp import ProjectManagerException
from PyExp import AbstractExperimentSettings
from PyExp import AbstractModel
from bchromosomer.core_assembly import cf_assembly_chains
from bchromosomer.projects import get_all_microdissections

class BChromosomerExperiment(AbstractExperiment):
    '''
    '''

    def init_steps(self):
        
        self.all_steps = [

            ## MANAGING
            # {
            #     'pre': None,
            #     'stage': "Manage",
            #     'name': "upload",
            #     'cf': cf_upload_project,
            #     'check': None,
            #     'desc': 'Upload project data to webserver.',
            # },
            # {
            #     'pre': None,
            #     'stage': "Manage",
            #     'name': "map_lg",
            #     'cf': cf_map_linkage_group,
            #     'check': None,
            #     'desc': 'Upload project data to webserver.',
            # },
            {
                'pre': None,
                'stage': "Manage",
                'name': "chains",
                'cf': cf_assembly_chains,
                'check': None,
                'desc': 'Create and annotate microdissection chains.',
            },
        ]

class BChromosomerExperimentSettings(AbstractExperimentSettings):
    '''
    '''

    def __init__(self):
      super(BChromosomerExperimentSettings, self).__init__()

      self.folders = {
        "mapping": "mapping",
      }

      self.files = {
      }

      self.other = {
      }


class BChromosomerProjectManager(ProjectManager):
    '''
    '''
    
    def _init_project(self, project_data):
        """Add initial data to project data dictionary."""

        mandatory_params = ["path_to",
                            "pid",
                            ]

        project = {}
        for param in mandatory_params:
            if not param in project_data:
                raise ProjectManagerException("Add '%s' parameter to project data" % param)
            setattr(self, param, project_data[param])
            project[param] = project_data[param]
        for key in project_data:
            project[key] = project_data[key]
        return project


if __name__ == '__main__':
    
    exp_settings_class = BChromosomerExperimentSettings
    exp_class = BChromosomerExperiment
    manager_class = BChromosomerProjectManager

    dataset_dict = {
        "microdissections": get_all_microdissections,
    }

    run_app(exp_class, exp_settings_class, manager_class, dataset_dict)