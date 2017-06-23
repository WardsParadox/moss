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
