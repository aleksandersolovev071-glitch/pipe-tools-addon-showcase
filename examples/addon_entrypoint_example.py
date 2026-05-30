"""Illustrative Pipe Tools add-on entry point.

This file documents the registration shape of the private add-on. It is not a
runnable distribution because the feature modules are intentionally not included
in this showcase repository.
"""

bl_info = {
    "name": "Pipe Tools",
    "author": "Alexander Sidorenko",
    "version": (1, 1),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Pipe Tools",
    "description": "Tools for working with pipe curves, metadata, and Geometry Nodes.",
    "category": "Object",
}


# In the private add-on these features are imported from separate modules:
FEATURE_MODULES = (
    "pipe_diameter",
    "pipe_fillet",
    "pipe_adapter",
    "pipe_end",
    "pipe_warnings",
    "pipe_node_swap",
    "pipe_apply",
    "preferences",
)


def register():
    """Register feature modules in the order used by the private add-on."""
    raise RuntimeError("Showcase example only: full Pipe Tools source is private.")


def unregister():
    """Unregister feature modules in the reverse order."""
    raise RuntimeError("Showcase example only: full Pipe Tools source is private.")
