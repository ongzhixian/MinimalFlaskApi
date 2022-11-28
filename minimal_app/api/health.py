# 
################################################################################
# Modules and functions import statements
################################################################################

import logging
from flask import request, make_response, abort
from minimal_app import app, app_secrets

@app.route('/api/health', methods=['GET', 'POST'])
def api_health():
    try:
        response_message = "OK"
        logging.info("response_message")
        return response_message
    except Exception as e:
        logging.info("ERROR----------ERROR----------")
        logging.error(e)
