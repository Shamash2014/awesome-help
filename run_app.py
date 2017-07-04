from flask import Flask
from flask import jsonify
from flask import request
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler


app = Flask("HelpAPI")

HTTP_ERROR_CLIENT = 403
HTTP_ERROR_SERVER = 500

def notify_error(err, code):
    resp = jsonify(error=err)
    resp.status_code = code
    return resp


@app.route('/help/get', methods=['GET'])
def help_get_api():
    log = logging.getLogger('werkzeug')
    log.info("API CALL")
    log.info("%s | API CALL: %s " % (str(datetime.now()), request.headers))
    try:
        return jsonify(response="I help you")
    except Exception as ex:
        return notify_error(ex, HTTP_ERROR_SERVER)

if __name__ == '__main__':
    app.run()
