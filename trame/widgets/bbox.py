from trame_bbox.widgets.bbox import *


def initialize(server):
    from trame_bbox import module

    server.enable_module(module)
