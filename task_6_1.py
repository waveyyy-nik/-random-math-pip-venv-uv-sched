pip install uv

uv --version
uv venv .venv
uv venv --python 3.12 .venv312
uv pip install requests --python .venv
uv pip list --python .venv
uv pip freeze --python .venv
uv python list
uv python install 3.13