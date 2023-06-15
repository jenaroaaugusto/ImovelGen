"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "ImovelGen"

_ = MessageFactory("ImovelGen")

logger = logging.getLogger("ImovelGen")
