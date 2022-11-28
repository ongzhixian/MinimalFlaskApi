from minimal_app import app
from minimal_app.features.logging import log

@app.route('/')
def root_get():
    """Path: / (Application root)"""
    return "OK", 200