#!/usr/bin/env python
'''
ooiservices.controller.instrument

InstrumentController
'''

from ooiservices.controller.base import ObjectController
from ooiservices.controller.base import ListController
from ooiservices.model.instrument_deployment import InstrumentDeploymentModel
from flask import request


class InstrumentDeploymentController(ObjectController):
    model = None

    def __init__(self):
        ObjectController.__init__(self)

    def get(self,id):
        result = self.model.read(id)
        if not result:
            return self.response_HTTP204()
        return result

class InstrumentDeploymentListController(ListController):
    model = None

    def get(self):
        args = request.args
        if args:
            result = self.process_args(self.model, args,'platform_id')
        else:
            result = self.model.read()
        if not result:
            return self.response_HTTP204()
        return result


def initialize_model():
    '''
    Initializes the model for the controllers
    this function is to be called by app
    '''
    InstrumentDeploymentController.model = InstrumentDeploymentModel()
    InstrumentDeploymentListController.model = InstrumentDeploymentModel()

