
import binascii
import json
import logging
import traceback
from urllib.parse import urlencode

from robobrowser import RoboBrowser


from cga2121.modal import get_device_modal

_LOGGER = logging.getLogger(__name__)

__version__ = "1.0"


class Cga2121:
    def __init__(self, host, port, user, password) -> None:
        self._host = host
        self._port = port
        self._uri = f'http://{host}:{port}'
        self._user = user
        self._password = password
        self._br = RoboBrowser(history=True, parser="html.parser")

    def authenticate(self):
        try:
            self._br.open(self._uri)




            self._br.open(f'{self._uri}/goform/logon', method='POST',
                              data = {"username_login": self._user, "password_login": self._password,"languaje_selector": "en"})
            _LOGGER.debug("br.response %s", self._br.response)
            

            
            

            return True

        except Exception as execption:
            _LOGGER.error("Authentication failed. Exception: %s", execption)
            traceback.print_exc()
            raise

    def get_device_modal(self):
        data = self.get_device_modals(f"{self._uri}/st_wireless.html")
        return data

    def get_device_modals(self, device_modal):
        req = self._br.session.get(device_modal)
        self._br._update_state(req)
        content = req.content.decode()
        return get_device_modal(content)


