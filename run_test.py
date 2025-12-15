import pytest

#Lista de archivos de pruebas
test_files = [
    "tests/test_login.py",
    "tests/test_invetory.py",
    "tests/test_carrito.py",
    "tests/test_menu.py",
    "tests/test_filtro.py",
    "tests/test_login_invalido.py"
]

# Argumentos para ejecutar las pruebas: archivo + reporte html
pytest_args = test_files + ["--html=report.html", "--self-contained-html", "-v"]

pytest.main(pytest_args)
    