# -*- coding: utf-8 -*-
"""
Created on Mon May 15 16:27:31 2023

@author: wendy
"""

from waitress import serve
import api
serve(api.app, host='0.0.0.0', port=8888)