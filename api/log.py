# -*- coding:utf-8 -*-
import logging
import requests

logging.basicConfig(filename="api.log", level=logging.ERROR)
logger = logging.getLogger(__name__)


def get_status_code(request):
    if request.status_code != 200:
        msg_error = "Une erreur est survenue. La page demandée a retourner le code d'erreur {0} : {1}"
        msg_error = msg_error.format(request.status_code, request.reason)
        logger.error(msg_error)
