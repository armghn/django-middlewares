import time
import logging

logger = logging.getLogger(__name__)


class LoggingMiddleware:
    """Calculate execution time of views"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()

        execution_time = end_time - start_time

        logger.info(
            f"View: {request.path}, Method: {request.method}, Execution time: {execution_time}  "
        )

        return response


from django.utils.deprecation import MiddlewareMixin


class LogMiddleware(MiddlewareMixin):
    """Log before calling requests"""
    def process_request(self, request):
        print(f"Path: {request.path}, User: {request.user}")
