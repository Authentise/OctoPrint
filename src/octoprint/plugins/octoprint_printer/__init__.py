# coding=utf-8
from .printer import OctoPrintPrinter

__plugin_name__ = "OctoPrint Printer"
__plugin_author__ = "Scott Lemmon, based on work by Gina Häußge"
__plugin_homepage__ = "https://github.com/authentise/OctoPrint/"
__plugin_license__ = "AGPLv3"
__plugin_description__ = "Provides the default printer for OctoPrint to use for printing"
__plugin_implementation__ = OctoPrintPrinter()
