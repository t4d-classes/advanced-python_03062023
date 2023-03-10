# Calc App

1. Change into the outer `calc_app` folder.

```bash
cd calc_app
```

2. Run the `setup.py` file to generate the wheel.

```bash
python setup.py sdist bdist_wheel
```

3. Install the wheel.

```bash
python -m pip install --user ./dist/calc_app-0.1.0-py3-none-any.whl
```

4. Create a single file executable.

```bash
pyinstaller calc_app/__main__.py --onefile -n calc_app
```
