import logging
import coreapi
from django.core.handlers.wsgi import WSGIHandler
from werkzeug.wrappers import Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def vc_handler(environ, start_response):
    try:
        response = Response.from_app(WSGIHandler(), environ)
        return response(environ, start_response)
    except Exception as e:
        logger.error("Unhandled exception in Lambda function", exc_info=True)
        raise e