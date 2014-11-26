# -*- coding:utf-8 -*-
import logging

logging.basicConfig(filename="api.log", level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt="%d-%m-%Y %H:%M:%s")
logger = logging.getLogger(__name__)


def get_status_code(request):
    if request.status_code != 200:
        msg_error = "Une erreur est survenue. La page demandée à retourné le code d'erreur {0} : {1}"
        msg_error = msg_error.format(request.status_code, request.reason)
        logger.error(msg_error)
        return False
    return True
