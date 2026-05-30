# Pipe Tools Add-on Structure

This document describes the internal structure of the private Pipe Tools add-on.
The source code itself is not included in this showcase repository.

```text
pipe-tools-addon/
|-- __init__.py
|-- .gitignore
|-- preferences/
|   |-- __init__.py
|   |-- pref_properties.py
|   `-- pref_logic.py
|-- assets/
|   `-- pipe_fillet_nodes.blend
|-- core/
|   |-- __init__.py
|   |-- data_loader.py
|   `-- utils.py
|-- pipe_diameter/
|   |-- __init__.py
|   |-- diameter_ui.py
|   |-- diameter_logic.py
|   `-- diameter_properties.py
|-- pipe_fillet/
|   |-- __init__.py
|   |-- fillet_apply.py
|   |-- fillet_ui.py
|   `-- fillet_logic.py
|-- pipe_adapter/
|   |-- __init__.py
|   |-- adapter_ui.py
|   `-- adapter_logic.py
|-- pipe_end/
|   |-- __init__.py
|   `-- end_ui.py
|-- pipe_apply/
|   |-- __init__.py
|   |-- apply_operator.py
|   |-- apply_preview.py
|   |-- apply_sockets.py
|   |-- apply_ui.py
|   |-- apply_logic.py
|   `-- apply_properties.py
|-- pipe_node_swap/
|   |-- __init__.py
|   |-- node_swap_ui.py
|   |-- node_swap_logic.py
|   `-- node_swap_properties.py
`-- pipe_warnings/
    |-- __init__.py
    |-- warnings_ui.py
    `-- warnings_logic.py
```
