bl_info = {
    "name": "Pipe Tools",
    "author": "Alexander Sidorenko",
    "version": (1, 1),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Pipe Tools",
    "description": "Tools for working with pipe curves (diameters, resolution, metadata...)",
    "category": "Object",
}

from .pipe_diameter import register as pipe_diameter_register
from .pipe_diameter import unregister as pipe_diameter_unregister

from .pipe_fillet import register as pipe_fillet_register
from .pipe_fillet import unregister as pipe_fillet_unregister

from .pipe_adapter import register as adapter_register
from .pipe_adapter import unregister as adapter_unregister

from .pipe_end import register as pipe_end_register
from .pipe_end import unregister as pipe_end_unregister

from .pipe_warnings import register as pipe_warnings_register
from .pipe_warnings import unregister as pipe_warnings_unregister

from .pipe_node_swap import register as pipe_node_swap_register
from .pipe_node_swap import unregister as pipe_node_swap_unregister

from .pipe_apply import register as apply_register
from .pipe_apply import unregister as apply_unregister

from .preferences import register as preferences_register
from .preferences import unregister as preferences_unregister


def register():
    pipe_diameter_register()
    pipe_fillet_register()
    adapter_register()
    pipe_end_register()
    pipe_warnings_register()
    pipe_node_swap_register()
    apply_register()
    preferences_register()


def unregister():
    pipe_diameter_unregister()
    pipe_fillet_unregister()
    adapter_unregister()
    pipe_end_unregister()
    pipe_warnings_unregister()
    pipe_node_swap_unregister()
    apply_unregister()
    preferences_unregister()
