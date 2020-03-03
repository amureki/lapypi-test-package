# lapypi-test-package

Dummy package to test lapypi

Upload package:

```bash
twine upload --repository-url http://127.0.0.1:8000/ dist/*
```

Install package:

1. Add requirements.txt:

```
--index-url http://127.0.0.1:8000/

test-package
```

2. Run usual pip install
```bash
pip install -r requirements.txt
```
