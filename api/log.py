# -*- coding:utf-8 -*-
import logging
import requests

logging.basicConfig(filename="api.log", level=logging.ERROR)


def get_status_code(request):
    if request.status_code != 200:
        msg_error = "Une erreur est survenue. La page demandée a retourner le code d'erreur {0} : {1}"
        msg_error = msg_error.format(request.status_code, request.reason)
        logging.error(msg_error)


r = requests.get("http://google.fr/grlkjhonfrj")
get_status_code(r)