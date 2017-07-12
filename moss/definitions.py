#!/usr/bin/python

# Dictionary of shortnamed variables for script filenames
script_list = {}

# Model Info: MacbookPro11,2
model_info = {}
model_info["settings"] = {}
model_info["settings"]["script"] = "com.github.wardsparadox.hello-it.computerdetails.modelinfo.sh"
model_info["settings"]["title"] = "modelinfo"
script_list["Model Info"] = model_info

ram_info = {}
ram_info["settings"] = {}
ram_info["settings"]["script"] = "com.github.wardsparadox.hello-it.computerdetails.raminfo.sh"
ram_info["settings"]["title"] = "raminfo"
script_list["RAM Info"] = ram_info

memory_pressure_info = {}
memory_pressure_info["settings"] = {}
memory_pressure_info["settings"]["script"] = "com.github.paperfixie.hello-it.memorypressure.sh"
memory_pressure_info["settings"]["title"] = "memorypressure"
memory_pressure_info["settings"]["periodic-run"] = 60
script_list["Memory Pressure Info"] = memory_pressure_info

uptime_info = {}
uptime_info["settings"] = {}
uptime_info["settings"]["script"] = "com.github.wardsparadox.hello-it.computerdetails.uptime.sh"
uptime_info["settings"]["title"] = "uptimeinfo"
uptime_info["settings"]["periodic-run"] = 10800
script_list["Uptime Info"] = uptime_info

email_details_info = {}
email_details_info["settings"] = {}
email_details_info["settings"]["script"] = "com.github.wardsparadox.hello-it.computerdetails.emailcomputerinfo.sh"
email_details_info["settings"]["title"] = "emailcomputerdetails"
script_list["Email Computer Details"] = email_details_info

filevault_status_info = {}
filevault_status_info["settings"] = {}
filevault_status_info["settings"]["script"] = "com.github.paperfixie.hello-it.filevaultstasus.sh"
filevault_status_info["settings"]["title"] = "filevaultstatus"
script_list["Filevault Status"] = filevault_status_info

macos_info = {}
macos_info["settings"] = {}
macos_info["settings"]["script"] = "com.github.wardsparadox.hello-it.computerdetails.macOSversion.sh"
macos_info["settings"]["title"] = "macOSversion"
script_list["MacOS Version Info"] = macos_info

serialnumber_info = {}
serialnumber_info["settings"] = {}
serialnumber_info["settings"]["script"] = "com.github.wardsparadox.hello-it.computerdetails.serialnumber.sh"
serialnumber_info["settings"]["title"] = "serialnumber"
script_list["Serial Number Info"] = serialnumber_info

smart_status_info = {}
smart_status_info["settings"] = {}
smart_status_info["settings"]["script"] = "com.github.wardsparadox.hello-it.computerdetails.smartstatus.sh"
smart_status_info["settings"]["title"] = "smartstatus"
smart_status_info["settings"]["periodic-run"] = 360
script_list["SMART Status Info"] = smart_status_info

storage_space_info = {}
storage_space_info["settings"] = {}
storage_space_info["settings"]["script"] = "com.github.wardsparadox.hello-it.computerdetails.storagespace.sh"
storage_space_info["settings"]["title"] = "storagespace"
storage_space_info["settings"]["periodic-run"] = 1080
script_list["Storage Space Info"] = storage_space_info

munki_manifest_info = {}
munki_manifest_info["settings"] = {}
munki_manifest_info["settings"]["script"] = "com.github.wardsparadox.hello-it.munki.manifestname.sh"
munki_manifest_info["settings"]["title"] = "munkimanifest"
script_list["Munki Manifest Info"] = munki_manifest_info

pending_munki_updates = {}
pending_munki_updates["settings"] = {}
pending_munki_updates["settings"]["script"] = "com.github.wardsparadox.hello-it.munki.pendingmscupdates.sh"
pending_munki_updates["settings"]["title"] = "pendingmscupdates"
pending_munki_updates["settings"]["periodic-run"] = 720
script_list["Pending Munki Update Info"] = pending_munki_updates

firewall_status_info = {}
firewall_status_info["settings"] = {}
firewall_status_info["settings"]["script"] = "com.github.paperfixie.hello-it.firewallstatus.sh"
firewall_status_info["settings"]["title"] = "firewallstatus"
firewall_status_info["settings"]["periodic-run"] = 180
script_list["Firewall Status Info"] = firewall_status_info

mac_address_info = {}
mac_address_info["settings"] = {}
mac_address_info["settings"]["script"] = "com.github.wardsparadox.hello-it.networkdetails.macaddress.sh"
mac_address_info["settings"]["title"] = "macaddress"
mac_address_info["settings"]["periodic-run"] = 180
script_list["MAC Address Info"] = mac_address_info

keyslist = sorted(script_list.keys())
