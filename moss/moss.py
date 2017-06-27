#!/usr/bin/python

#
#
# Moss is designed to
# to quickly create mobileconfig files from a JSON file
# created by Roy the GUI app.
#
# Authors Vince Mascoli (@paperfixie) and Zack McCauley (@wardsparadox)
#
#
import os
from plistlib import writePlist
from uuid import uuid4
profileuuid = str(uuid4())
payloaduuid = str(uuid4())


# Actual Content (ridiculous number of nested dicts)

_content = {}

# MCX Content
_payloadcontent = {}
_forcedcontent = []
_mcxcontent = {}
_contentarray = {}
_contentarray["content"] = [_content]
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

filename = "test.mobileconfig"
writePlist(_profile, filename)

# Dictionary of shortnamed variables for script filenames

script_list = {}
script_list["model_info"] = "com.github.ygini.hello-it.computerdetails.modelinfo.sh"
script_list["mac_os_version"] = "com.github.ygini.hello-it.computerdetails.macOSversion.sh"
script_list["ram_info"] = "com.github.ygini.hello-it.computerdetails.raminfo.sh"
script_list["smart_status"] = "com.github.ygini.hello-it.computerdetails.smartstatus.sh"
script_list["storage_space"] = "com.github.ygini.hello-it.computerdetails.storagespace.sh"
script_list["email_computer_info"] = "com.github.ygini.hello-it.computerdetails.emailcomputerinfo.sh"
script_list["mac_address"] = "com.github.ygini.hello-it.networkdetails.macaddress.sh"

script_frequency ={}
script_frequency["run"] = "periodic_run"
script_frequency["time_int"] = int()

# Dictionaries for public functions

_script_item = {}
_script_dict = {}
_script_settings = {}
_script_item["functionIdentifier"] = "public.script.item"
_script_item["settings"] = _script_dict
_script_dict["script"] = _script_settings
_script_settings["script_name"] = script_list
_script_settings["script_freq"] = script_frequency
