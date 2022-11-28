# 
################################################################################
# Modules and functions import statements
################################################################################

from minimal_app.features.logging import log
from flask import request, make_response, abort
from minimal_app import app, app_secrets

@app.route('/api/health', methods=['GET', 'POST'])
def api_health():
    try:
        response_message = "OK"
        log.info("response_message")
        return response_message
    except Exception as e:
        log.info("ERROR----------ERROR----------")
        log.error(e)
