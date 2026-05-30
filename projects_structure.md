pipe-tools-addon/
│
├── __init__.py
├── .gitignore
│
├── preferences/
│   ├── __init__.py
│   ├── pref_properties.py   # ui, properties, id_name
│   └── pref_logic.py
│
├── assets/
│   └── pipe_fillet_nodes.blend
│
├── core/                    # Common addon things
│   ├── __init__.py
│   │── data_loader.py       # Загрузка JSON / библиотек
│   └── utils.py             # Calculation & setups (distance, resolution...)
│
├── pipe_diameter/           # Pipe Auto diameters
│   ├── __init__.py
│   ├── diameter_ui.py
│   ├── diameter_logic.py
│   └── diameter_properties.py
│
├── pipe_fillet/             # АВТОСКРУГЛЕНИЕ
│   ├── __init__.py
│   ├── fillet_apply.py      # Применение скругления к трубе
│   ├── fillet_ui.py
│   └── fillet_logic.py
│
├── pipe_adapter/            # ПЕРЕХОДНИКИ
│   ├── __init__.py
│   ├── adapter_ui.py
│   └── adapter_logic.py
│
├── pipe_end/                # КОНЦЕВИКИ ТРУБ (крышки)
│   ├── __init__.py
│   └── end_ui.py
│
├── pipe_apply/              # Pipe apply, objects separation, convertion from curve to mesh
│   ├── __init__.py
│   ├── apply_operator.py
│   ├── apply_preview.py
│   ├── apply_sockets.py
│   ├── apply_ui.py
│   ├── apply_logic.py
│   └── apply_properties.py
│
├── pipe_node_swap/
│   ├── __init__.py
│   ├── node_swap_ui.py
│   ├── node_swap_logic.py
│   └── node_swap_properties.py
│
└── pipe_warnings/
    ├── __init__.py
    ├── warnings_ui.py
    └── warnings_logic.py