#!/usr/bin/python

# Dictionary of shortnamed variables for script filenames
script_list = {}

model_info = {}
model_info_settings = {}
model_info_settings["script"] = "com.github.wardsparadox.hello-it.computerdetails.modelinfo.sh"
model_info_settings["title"] = "modelinfo"
model_info["settings"] = model_info_settings
script_list["Model Info"] = model_info

ram_info = {}
ram_info_settings = {}
ram_info_settings["script"] = "com.github.wardsparadox.hello-it.computerdetails.raminfo.sh"
ram_info_settings["title"] = "raminfo"
ram_info["settings"] = ram_info_settings
script_list["RAM Info"] = ram_info

memory_pressure_info = {}
memory_pressure_settings = {}
memory_pressure_settings["script"] = "com.github.paperfixie.hello-it.memorypressure.sh"
memory_pressure_settings["title"] = "memorypressure"
memory_pressure_info["settings"] = memory_pressure_settings
script_list["Memory Pressure Info"] = memory_pressure_info
