#!/usr/bin/python
'''
 MOSS is a command-line application for generating mobileconfig
 files for use with the Hello IT app by @ygini
 Copyright (C) 2017  Vince Mascoli (@paperfixie) & Zack McCauley (@wardsparadox)

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
'''

import pprint
import argparse
from plistlib import writePlist
from uuid import uuid4
from definitions import script_list

version = "1.0.0"
_content = []

def createCustomScriptItem():
    '''
        Creates a script item with custom info.
    '''
    print "Please review the settings mentioned here before continuing:\
     https://github.com/ygini/Hello-IT/wiki/public.script.item"
    _custom_script_item = {}
    _custom_script_item["functionIdentifier"] = "public.script.item"
    _custom_script_item["settings"] = {}
    _custom_script_item["settings"]["title"] = raw_input("Title: ")
    scriptpath_answer = raw_input("Is the script located in the CustomScript's folder? [y/n] : ")
    if scriptpath_answer.lower().startswith('y'):
        _custom_script_item["settings"]["script"] = \
        raw_input("Full name of Script (extension included): ")
    else:
        _custom_script_item["settings"]["path"] = raw_input("Full Path to Script: ")
    scriptrepeat_answer = raw_input("Add a repeat setting?\n[y/n] : ")
    if scriptrepeat_answer.lower().startswith('y'):
        while True:
            try:
                _custom_script_item["settings"]["repeat"] = \
                int(raw_input("How often should it repeat in seconds?: "))
                break
            except TypeError:
                pass
    scriptperiodic_answer = raw_input("Add a periodic-run setting?\n[y/n] : ")
    if scriptperiodic_answer.lower().startswith('y'):
        while True:
            try:
                _custom_script_item["settings"]["periodic-run"] = \
                int(raw_input("How often should it periodically run in seconds?: "))
                break
            except TypeError:
                pass
    print "Added Custom Script Item."
    return _custom_script_item

def createScriptItem():
    '''
    Creates a script item based on selection in definitions.py
    '''
    for key in sorted(script_list.keys()):
        print key
    print "Custom Script"
    scriptanswer = raw_input("Which script item would you like to add?"\
    "Type exactly as seen above!\n")
    if scriptanswer.lower().startswith("custom"):
        _public_script_item = createCustomScriptItem()
        return _public_script_item
    _public_script_item = {}
    _public_script_item["functionIdentifier"] = "public.script.item"
    _public_script_item["settings"] = {}
    _public_script_item["settings"] = script_list[scriptanswer]["settings"]
    print "Added Script Item: {0}".format(scriptanswer)
    return _public_script_item

def createSubmenuItem():
    '''
    Creates a submenu and loops through addToLayout
    '''
    _public_submenu = {}
    _public_submenu["functionIdentifier"] = "public.submenu"
    _public_submenu["settings"] = {}
    _public_submenu["settings"]["title"] = raw_input("Enter Title for Submenu: ")
    _public_submenu["settings"]["content"] = addToLayout()
    print "Added submenu with title {0}".format(_public_submenu["settings"]["title"])
    return _public_submenu

# public.open.resource
def createOpenResource():
    '''
    Creates a Open Resource item dict.
    '''
    _public_open_resource = {}
    _public_open_resource["functionIdentifier"] = "public.open.resource"
    _public_open_resource["settings"] = {}
    _public_open_resource["settings"]["URL"] = raw_input("Enter URL: ")
    _public_open_resource["settings"]["title"] = raw_input("Enter Title: ")
    print "Added \"Open Resource\" Item: {0}".format(_public_open_resource["settings"]["title"])
    return _public_open_resource

# public.separator
def createSeparator():
    '''
    Add's the seperator function to config
    '''
    _public_separator = {}
    _public_separator["functionIdentifier"] = "public.separator"
    print "Added Menu Separator"
    return _public_separator

# public.quit
def createQuit():
    '''
    Add's the quit function to config
    '''
    _public_quit = {}
    _public_quit["functionIdentifier"] = "public.quit"
    return _public_quit

def createTestHTTP():
    '''
    Creates the internet test built in fuction
    '''
    _public_test_http = {}
    _public_test_http_settings = {}
    _public_test_http["functionIdentifier"] = "public.test.http"
    _public_test_http["settings"] = _public_test_http_settings
    _public_test_http_settings["URL"] = \
    "https://raw.githubusercontent.com/ygini/Hello-IT/master/staticfiles/internet_test.txt"
    _public_test_http_settings["imageBaseName"] = "network"
    _public_test_http_settings["mode"] = "md5"
    _public_test_http_settings["originalString"] = "ccf41dc8262810b99142b5627d27c25e"
    _public_test_http_settings["repeat"] = 60
    _public_test_http_settings["title"] = "Internet"
    print "Added Internet Test item"
    return _public_test_http

# public.title
def createTitleItem():
    '''
    Creates a title item to allow for text mode in title bar
    '''
    titletext = raw_input("Enter the text for the Title Element: ")
    _public_title = {}
    _public_title_settings = {}
    _public_title_settings["title"] = titletext
    _public_title["functionIdentifier"] = "public.title"
    _public_title["settings"] = _public_title_settings
    print "Added {0} Title to layout".format(_public_title["settings"]["title"])
    _content.insert(0, _public_title)

# layout function
def createLayoutItem():
    '''
    Starts the whole layout process.
    '''
    print """What layout item would you like to add?
         [1] internet test
         [2] open resource
         [3] script item
         [4] separator
         [5] submenu
         """
    layout_input = raw_input("> ")
    if layout_input == '1' or layout_input.lower().startswith('internet'):
        return createTestHTTP()
    elif layout_input == '2' or layout_input.lower().startswith('open'):
        return createOpenResource()
    elif layout_input == '3' or layout_input.lower().startswith('script'):
        return createScriptItem()
    elif layout_input == '4' or layout_input.lower().startswith('seperator'):
        return createSeparator()
    elif layout_input == '5' or layout_input.lower().startswith('submenu'):
        return createSubmenuItem()
    else:
        print "No item selected"
        return

def addToLayout():
    '''
    Main loop for adding content to the current layout
    '''
    userisdone = False
    layout = []
    while userisdone != True:
        print "Current Layout:"
        pprint.pprint(layout, indent=4)
        askanswer = raw_input('Add more to the layout? [y/n] : ')
        if askanswer.lower().startswith('y'):
            userisdone = False
            layout.append(createLayoutItem())
        else:
            userisdone = True
    return layout

def printVersion():
    '''
    Prints version and License
    '''
    print "MOSS Version: {0}".format(version)
    print """
    MOSS is a command-line application for generating mobileconfig
    files for use with the Hello IT app by @ygini
    Copyright (C) 2017  Vince Mascoli (@paperfixie) & Zack McCauley (@wardsparadox)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
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
    ######################################################"""

def main():
    '''
    Run this foo!
    '''
    parser = argparse.ArgumentParser(
        description="""MOSS is a command-line application for generating mobileconfig
        files for use with the Hello IT app by @ygini
        Copyright (C) 2017  Vince Mascoli (@paperfixie) & Zack McCauley (@wardsparadox)""")
    parser.add_argument(
        '--profileuuid',
        help='Former profile uuid. Use this if you are updating a layout.',
        default=str(uuid4()))
    parser.add_argument(
        '--version',
        help='Prints Version of MOSS',
        action="store_true")
    parser.add_argument(
        '--organization',
        help='Change Organization of Profile. Defaults to GitHub',
        default="GitHub")
    parser.add_argument(
        '--identifier',
        help='Change Profile Identifier before uuid. '
        'Payload UUID is appended to ensure it is unique. '
        'Defaults to com.github.paperfixie.mossroy.',
        default="com.github.paperfixie.mossroy.hello-it")

    args = parser.parse_args()
    if args.version:
        printVersion()
        exit(0)
    payloaduuid = str(uuid4())
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
    _payload["PayloadIdentifier"] = "{0}.configuration.{1}".format(args.identifier, payloaduuid)
    _payload["PayloadType"] = "com.apple.ManagedClient.preferences"
    _payload["PayloadUUID"] = payloaduuid
    _payload["PayloadVersion"] = 1
    # Profile info
    _profile = {}
    _profile["PayloadDisplayName"] = "Hello IT Configuration Profile"
    _profile["PayloadIdentifier"] = args.identifier
    _profile["PayloadOrganization"] = args.organization
    _profile["PayloadRemovalDisallowed"] = False
    _profile["PayloadScope"] = "System"
    _profile["PayloadType"] = "Configuration"
    _profile["PayloadUUID"] = args.profileuuid
    _profile["PayloadVersion"] = 1
    _profile["PayloadContent"] = [_payload]

    print """Would you prefer a Text based Title instead of an Icon?
    https://github.com/ygini/Hello-IT/wiki/Preferences#menu-bar-look"""
    answer = raw_input("[y/n] : ")
    if answer.lower().startswith('y'):
        createTitleItem()
    additionalContent = addToLayout()
    for layoutItem in additionalContent:
        _content.append(layoutItem)
    answer = raw_input("Would you like a quit option for your layout? [y/n] : ")
    if answer.lower().startswith('y'):
        print "Added Quit Function, Goodbye!"
        _content.append(createQuit())
    print "Writing out configuration as"\
    "HelloITConfiguration.mobileconfig in current working directory."
    writePlist(_profile, "HelloITConfiguration.mobileconfig")

if __name__ == '__main__':
    main()
