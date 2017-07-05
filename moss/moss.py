#!/usr/bin/python

#
#
# Moss is designed to
# to quickly create mobileconfig files for use
# with the Hello IT app by Yoann Gini (@ygini) from a JSON file
# created by the Roy GUI app
#
# Authors Vince Mascoli (@paperfixie) and Zack McCauley (@wardsparadox)
#
#
import pprint
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

# Dictionary of shortnamed variables for script filenames

script_list = {}
script_list["model_info"] = "com.github.ygini.hello-it.computerdetails.modelinfo.sh"
script_list["mac_os_version"] = "com.github.ygini.hello-it.computerdetails.macOSversion.sh"
script_list["ram_info"] = "com.github.ygini.hello-it.computerdetails.raminfo.sh"
script_list["smart_status"] = "com.github.ygini.hello-it.computerdetails.smartstatus.sh"
script_list["storage_space"] = "com.github.ygini.hello-it.computerdetails.storagespace.sh"
script_list["email_computer_info"] = "com.github.ygini.hello-it.computerdetails.emailcomputerinfo.sh"
script_list["mac_address"] = "com.github.ygini.hello-it.networkdetails.macaddress.sh"



# Dictionaries for public functions
# public.script.item

_script_item = {}
_script_dict = {}
_script_settings = {}
_script_freq = {}
_script_item["functionIdentifier"] = "public.script.item"
_script_item["settings"] = _script_dict
_script_dict["script"] = _script_settings
_script_settings["script_name"] = script_list
_script_settings["title"] = "$script_list"
_script_settings["script_freq"] = _script_freq
_script_freq["run"] = "periodic_run"
_script_freq["time_int"] = int()

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

# public.open.resource

_public_open_resource = {}
_public_open_resource_settings = {}
_public_open_resource["functionIdentifier"] = "public.open.resource"
_public_open_resource["settings"] = _public_open_resource_settings
_public_open_resource_settings["URL"] = ""
_public_open_resource_settings["title"] = ""

# public.separator

_public_separator = {}
_public_separator["functionIdentifier"] = "public.separator"

# public.quit

_public_quit = {}
_public_quit["functionIdentifier"] = "public.quit"

# public.test.http

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

# public.title
def createTitleItem():
    titletext = raw_input("Enter the text for the Title Element:")
    _public_title = {}
    _public_title_settings = {}
    _public_title_settings["title"] = titletext
    _public_title["functionIdentifier"] = "public.title"
    _public_title["settings"] = _public_title_settings
    print "Added {0} Title to layout".format(_public_title["settings"]["title"])
    _content.append(_public_title)


while userisdone != True:
    print "Current Layout:"
    pprint.pprint(_content, indent=4)
    answer = raw_input('Add more to the layout? [y/n] ')
    if answer.lower().startswith('y'):
        userisdone = False
        createTitleItem()
    else:
        userisdone = True

writePlist(_profile, "test.mobileconfig")
