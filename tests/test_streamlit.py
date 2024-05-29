from streamlit.testing.v1 import AppTest


def test_app_run():
    app = AppTest.from_file('../main.py')
    app.run(timeout=10)
    assert not app.exception
