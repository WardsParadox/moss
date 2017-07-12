#!/usr/bin/python
#
#
# MOSS is a command-line application for generating mobileconfig
# files for use with the Hello IT app by @ygini
# Copyright (C) 2017  Vince Mascoli (@paperfixie) & Zack McCauley (@wardsparadox)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

import pprint
#import argparse
from plistlib import writePlist
from uuid import uuid4
profileuuid = str(uuid4())
payloaduuid = str(uuid4())


userisdone = False

# Actual Content (ridiculous number of nested dicts)

_content = []

# MCX Content
_payloadcontent = {}
_forcedcontent = []
_mcxcontent = {}
_contentarray = {}
_contentarray["content"] = _content
_mcxcontent["mcx_preference_settings"] = _contentarray
_forced = {}
_forcedcontent.append(_mcxcontent)
_forced["Forced"] = _forcedcontent
_payloadcontent["com.github.ygini.hello-it"] = _forced


# Payload Content
_payload = {}
_payload["PayloadContent"] = _payloadcontent
_payload["PayloadEnabled"] = True
_payload["PayloadIdentifier"] = "org.github.wardsparadox.nestedid"
_payload["PayloadType"] = "com.apple.ManagedClient.preferences"
_payload["PayloadUUID"] = payloaduuid
_payload["PayloadVersion"] = 1

# Profile info
_profile = {}
_profile["PayloadDisplayName"] = "Hello IT Configuration Profile"
_profile["PayloadIdentifier"] = "com.github.wardsparadox.test"
_profile["PayloadOrganization"] = "test org"
_profile["PayloadRemovalDisallowed"] = False
_profile["PayloadScope"] = "System"
_profile["PayloadType"] = "Configuration"
_profile["PayloadUUID"] = profileuuid
_profile["PayloadVersion"] = 1
_profile["PayloadContent"] = [_payload]





# Dictionaries for public functions
# public.script.item

_script_item = {}
_script_dict = {}
_script_settings = {}
_script_freq = {}
_script_item["functionIdentifier"] = "public.script.item"
_script_item["settings"] = _script_dict
_script_dict["script"] = _script_settings
#_script_settings["script_name"] = script_list
_script_settings["title"] = "$script_list"
_script_settings["script_freq"] = _script_freq
_script_freq["run"] = "periodic_run"
_script_freq["time_int"] = int()

def createScriptItem():
    print "Feature in development..."

# public.submenu

#def createSubmenuItem():
#    titletext = raw_input("Enter the text for the Title Element:")
#    _public_submenu = {}
#    _submenu_settings = {}
#    _submenu_settings["title"] = titletext
#    _public_submenu["functionIdentifier"] = "public.submenu"
#    _public_submenu["settings"] = _submenu_settings
#    print "Added {0} Submenu Title to layout".format(_public_submenu["settings"]["title"])
#    print _content
#    _content.append(_public_submenu)
#    print _content
#oldcontent
#_public_submenu = {}
#_submenu_settings = {}
#_submenu_settings["content"] = [] # Each list item is a dict
#_submenu_settings["title"] = ""
#_public_submenu["functionIdentifier"] = "public.submenu"
#_public_submenu["settings"] = _submenu_settings

def createSubmenuItem():
    print "Feature in development..."

# public.open.resource
def createOpenResource():
    _public_open_resource = {}
    _public_open_resource_settings = {}
    _public_open_resource["functionIdentifier"] = "public.open.resource"
    _public_open_resource["settings"] = _public_open_resource_settings
    _public_open_resource_settings["URL"] = raw_input("Enter URL: ")
    _public_open_resource_settings["title"] = raw_input("Enter Title: ")
    print "Added Open Resource Item"
    _content.append(_public_open_resource)

# public.separator
def createSeparator():
    _public_separator = {}
    _public_separator["functionIdentifier"] = "public.separator"
    print "Added Menu Separator"
    _content.append(_public_separator)

# public.quit

_public_quit = {}
_public_quit["functionIdentifier"] = "public.quit"

def createTestHTTP():
    _public_test_http = {}
    _public_test_http_settings = {}
    _public_test_http["functionIdentifier"] = "public.test.http"
    _public_test_http["settings"] = _public_test_http_settings
    _public_test_http_settings["URL"] = "https://raw.githubusercontent.com/ygini/Hello-IT/master/staticfiles/internet_test.txt"
    _public_test_http_settings["imageBaseName"] = "network"
    _public_test_http_settings["mode"] = "md5"
    _public_test_http_settings["originalString"] = "ccf41dc8262810b99142b5627d27c25e"
    _public_test_http_settings["repeat"] = 60
    _public_test_http_settings["title"] = "Internet"
    print "Added Internet Test item"
    _content.append(_public_test_http)

# public.title
def createTitleItem():
    titletext = raw_input("Enter the text for the Title Element: ")
    _public_title = {}
    _public_title_settings = {}
    _public_title_settings["title"] = titletext
    _public_title["functionIdentifier"] = "public.title"
    _public_title["settings"] = _public_title_settings
    print "Added {0} Title to layout".format(_public_title["settings"]["title"])
    _content.append(_public_title)

# layout function
def createLayoutItem():
    print """What layout item would you like to add?
         [1] internet test
         [2] open resource
         [3] script item
         [4] menu separator
         [5] submenu
         [6] title item"""
    layout_input = raw_input("> ")
    if layout_input == '1' or layout_input.lower().startswith('i'):
        createTestHTTP()
    elif layout_input == '2' or layout_input.lower().startswith('o'):
        createOpenResource()
    elif layout_input == '3' or layout_input.lower().startswith('s'):
        createScriptItem()
    elif layout_input == '4' or layout_input.lower().startswith('m'):
        createSeparator()
    elif layout_input == '5' or layout_input.lower().startswith('t'):
        createTitleItem()
    else:
        createTitleItem()

print """MOSS is a command-line application for generating mobileconfig
files for use with the Hello IT app by @ygini
Copyright (C) 2017  Vince Mascoli (@paperfixie) & Zack McCauley (@wardsparadox)
#####################################################
           "Hello IT?"
               ___
              |   \__
              |      \_
        ______|        \__
       _|                 |
       \    -----         |
        \   |    \___   _/     _----------------_
         ---|________|        |  Have you tried  |
           |[__]-[__]|        |   initiating an  |
            | ______ |        |    unexpected    |
            | |____| |        <      reboot?     |
             \      /          -________________-
              \____/
        _|----|{_}|----|_
        |      [ ]       |
        |      [ ]       |
######################################################
"""
print """Would you prefer a Text based Title instead of an Icon?
https://github.com/ygini/Hello-IT/wiki/Preferences#menu-bar-look"""
answer = raw_input("[y/n] : ")
if answer.lower().startswith('y'):
    createTitleItem()
while userisdone != True:
    print "Current Layout:"
    pprint.pprint(_content, indent=4)
    answer = raw_input('Add more to the layout? [y/n] : ')
    if answer.lower().startswith('y'):
        userisdone = False
        createLayoutItem()
    else:
        userisdone = True
answer = raw_input("Would you like a quit option for your layout? [y/n] : ")
if answer.lower().startswith('y'):
    print "Added Quit Function, Goodbye!"
    _content.append(_public_quit)


writePlist(_profile, "test.mobileconfig")
