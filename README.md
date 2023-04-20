# Ray Tracing

Installing:\
Ray Tracing requires `poetry`
```bash
git clone https://github.com/mathiasooi/raytracing
cd raytracing
poetry install
```

Testing:
```bash
poetry run pytest
```

Running:
```bash
poetry run python ./raytracing.py
```
You can load your own scene by passing in a JSON file as a command line argument
```bash
poetry run python ./raytracing.py scene.json
```
