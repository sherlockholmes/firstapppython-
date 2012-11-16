# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('app')

from app_lib import Window
from app.AboutAppDialog import AboutAppDialog
from app.PreferencesAppDialog import PreferencesAppDialog
from app_lib import arduino

# See app_lib.Window.py for more details about how this class works
class AppWindow(Window):
    __gtype_name__ = "AppWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(AppWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutAppDialog
        self.PreferencesDialog = PreferencesAppDialog

        

