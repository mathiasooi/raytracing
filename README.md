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
You can load your own world by passing in a JSON file as a command line argument
```bash
poetry run python ./raytracing.py shapes.json
```

JSON format:
```json
[
	{
    	"type": "sphere",
        "x": 0,
        "y": 0,
        "z": 0,
        "r": 1
    }
]
```
*more shapes to come...*