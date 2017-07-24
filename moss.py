#!/usr/bin/python
'''
MIT License

 MOSS is a command-line application for generating mobileconfig
 files for use with the Hello IT app by @ygini
 Copyright (C) 2017  Vince Mascoli (@paperfixie) & Zack McCauley (@wardsparadox)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

import pprint
import argparse
from plistlib import writePlist
from uuid import uuid4
from definitions import script_list, keyslist

version = "1.0.0"
_content = []
keyslist.append("Custom Script")

# public.script.item
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
    for key in keyslist:
        print key
    _public_script_item = {}
    _public_script_item["functionIdentifier"] = "public.script.item"
    _public_script_item["settings"] = {}
    while True:
        scriptanswer = raw_input("Which script item would you like to add? "\
        "[Type exactly as seen above!]\n> ")
        try:
            if scriptanswer.lower().startswith("custom"):
                _public_script_item = createCustomScriptItem()
                return _public_script_item
            else:
                _public_script_item["settings"] = script_list[scriptanswer]["settings"]
            break
        except KeyError:
            print "Error: Script choice not found, please enter it again"

    print "Added Script Item: {0}".format(scriptanswer)
    return _public_script_item

# public.submenu
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
    return _public_title

# layout function
def createLayoutItem():
    '''
    Starts the whole layout process.
    '''
    print """What layout item would you like to add?
         [1] Internet Test
         [2] Open Resource
         [3] Script Item
         [4] Separator
         [5] Submenu
         [6] Title Item
         [7] Delete Previous
         """
    layout_input = raw_input("> ")
    if layout_input == '1' or layout_input.lower().startswith('internet'):
        layoutitem = createTestHTTP()
    elif layout_input == '2' or layout_input.lower().startswith('open'):
        layoutitem = createOpenResource()
    elif layout_input == '3' or layout_input.lower().startswith('script'):
        layoutitem = createScriptItem()
    elif layout_input == '4' or layout_input.lower().startswith('seperator'):
        layoutitem = createSeparator()
    elif layout_input == '5' or layout_input.lower().startswith('submenu'):
        layoutitem = createSubmenuItem()
    elif layout_input == '6' or layout_input.lower().startswith("title"):
        layoutitem = createTitleItem()
    elif layout_input == '7' or layout_input.lower().startswith("delete"):
        return "delete previous"
    else:
        print "No item selected"
        return
    return layoutitem

def addToLayout():
    '''
    Main loop for adding content to the current layout
    '''
    userisdone = False
    layout = []
    while userisdone != True:
        print "Current Layout:"
        pprint.pprint(layout, indent=4, depth=3)
        askanswer = raw_input('Add more to the layout? [y/n] : ')
        if askanswer.lower().startswith('y'):
            userisdone = False
            item = createLayoutItem()
            if item == "delete previous":
                print "Deleting previous item"
                try:
                    layout.pop()
                except IndexError:
                    print "No items to delete!"
            else:
                layout.append(item)
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
                   ___
                  |   \__
                  |      \_
            ______|        \__
           _|                 |
           \    -----         |    _----------------_
            \   |    \___   _/    |    Hello IT?     |
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
        files for use with the Hello IT app by Yoann Gini (@ygini)
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
        _mcxcontent["mcx_preference_settings"]["title"] = \
        raw_input("Enter the text for the Menu Bar Title: ")
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
