#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python2
# pyuac==0.0.3
import subprocess
import json
import re
import pyuac
# pip install pyuac
import xml.etree.ElementTree as ET
from ctypes import Structure, pointer, windll, wintypes

# https://learn.microsoft.com/en-us/windows/win32/api/guiddef/ns-guiddef-guid
class GUID(Structure):
    _fields_ = [
        ("Data1", wintypes.DWORD),
        ("Data2", wintypes.WORD),
        ("Data3", wintypes.WORD),
        ("Data4", wintypes.BYTE * 8),
    ]


# https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/ns-wlanapi-wlan_interface_info
class WLAN_INTERFACE_INFO(Structure):
    _fields_ = [
        ("InterfaceGuid", GUID),
        ("strInterfaceDescription", wintypes.WCHAR * 256),
        ("isState", wintypes.DWORD),
        ("isState", wintypes.DWORD),
    ]


# https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/ns-wlanapi-wlan_interface_info_list
class WLAN_INTERFACE_INFO_LIST(Structure):
    _fields_ = [
        ("dwNumberOfItems", wintypes.DWORD),
        ("dwIndex", wintypes.DWORD),
        ("InterfaceInfo", WLAN_INTERFACE_INFO * 256),
    ]


# https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/ns-wlanapi-wlan_profile_info
class WLAN_PROFILE_INFO(Structure):
    _fields_ = [
        # Max length of wifi name is 255 + null termination
        ("strProfileName", wintypes.WCHAR * 256),
        ("dwFlags", wintypes.DWORD),
    ]


# https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/ns-wlanapi-wlan_profile_info_list
class WLAN_PROFILE_INFO_LIST(Structure):
    _fields_ = [
        ("dwNumberOfItems", wintypes.DWORD),
        ("dwIndex", wintypes.DWORD),
        ("ProfileInfo", WLAN_PROFILE_INFO * 256),
    ]


# https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/nf-wlanapi-wlanopenhandle
WlanOpenHandle = windll.wlanapi.WlanOpenHandle
WlanOpenHandle.argtypes = [
    wintypes.DWORD,
    wintypes.LPVOID,
    wintypes.LPDWORD,
    wintypes.PHANDLE,
]
WlanOpenHandle.restype = wintypes.DWORD

# https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/nf-wlanapi-wlanenuminterfaces
WlanEnumInterfaces = windll.wlanapi.WlanEnumInterfaces
WlanEnumInterfaces.argtypes = [
    wintypes.HANDLE,
    wintypes.LPVOID,
    wintypes.LPVOID,
]
WlanEnumInterfaces.restype = wintypes.DWORD

# https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/nf-wlanapi-wlangetprofilelist
WlanGetProfileList = windll.wlanapi.WlanGetProfileList
WlanGetProfileList.argtypes = [
    wintypes.HANDLE,
    GUID,
    wintypes.LPVOID,
    wintypes.LPVOID,
]
WlanGetProfileList.restype = wintypes.DWORD

# https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/nf-wlanapi-wlangetprofile
WlanGetProfile = windll.wlanapi.WlanGetProfile
WlanGetProfile.argtypes = [
    wintypes.HANDLE,
    GUID,
    wintypes.LPCWSTR,
    wintypes.LPCWSTR,
    wintypes.LPVOID,
    wintypes.LPVOID,
    wintypes.LPVOID,
]
WlanGetProfile.restype = wintypes.DWORD

# https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/ne-wlanapi-wlan_securable_object
WLAN_PROFILE_GET_PLAINTEXT_KEY = 0x0C

# Namespaces for XML parsing
WLAN_XML_NAMESPACES = {
    "v1": "http://www.microsoft.com/networking/WLAN/profile/v1",
    "v3": "http://www.microsoft.com/networking/WLAN/profile/v3",
}

# Convert XML to dictionary using ET
def parse_wifi_entry(xml: str) -> dict:
    root = ET.fromstring(xml.strip())

    # We already have the SSID but sure why not
    ssid = root.find("v1:name", WLAN_XML_NAMESPACES).text
    connection_mode = root.find("v1:connectionMode", WLAN_XML_NAMESPACES).text
    authEncryptionET = (
        root.find("v1:MSM", WLAN_XML_NAMESPACES)
        .find("v1:security", WLAN_XML_NAMESPACES)
        .find("v1:authEncryption", WLAN_XML_NAMESPACES)
    )
    authentication = authEncryptionET.find(
        "v1:authentication", WLAN_XML_NAMESPACES
    ).text
    encryption = authEncryptionET.find("v1:encryption", WLAN_XML_NAMESPACES).text

    # Get the key
    try:
        key = (
            root.find("v1:MSM", WLAN_XML_NAMESPACES)
            .find("v1:security", WLAN_XML_NAMESPACES)
            .find("v1:sharedKey", WLAN_XML_NAMESPACES)
            .find("v1:keyMaterial", WLAN_XML_NAMESPACES)
            .text
        )
    except:
        key = None

    return {
        "ssid": ssid,
        "connection_mode": connection_mode,
        "authentication": authentication,
        "encryption": encryption,
        "key": key,
    }


def get_wifi_passwords():

    wifi_entry_list = []

    dwClientVersion = 2
    hClientHandle = wintypes.HANDLE()
    pReserved = None

    # Pointers to pointers!
    ppInterfaceList = pointer(pointer(WLAN_INTERFACE_INFO_LIST()))
    ppProfileList = pointer(pointer(WLAN_PROFILE_INFO_LIST()))

    # Open handle
    open_handle_res = WlanOpenHandle(
        dwClientVersion, pReserved, pointer(wintypes.DWORD()), hClientHandle
    )

    # Enumerate interfaces
    WlanEnumInterfaces(hClientHandle, pReserved, ppInterfaceList)
    num_interfaces = ppInterfaceList.contents.contents.dwNumberOfItems
    for interface in ppInterfaceList.contents.contents.InterfaceInfo[:num_interfaces]:

        # Enumerate profiles
        WlanGetProfileList(
            hClientHandle,
            interface.InterfaceGuid,
            pReserved,
            ppProfileList,
        )

        num_profiles = ppProfileList.contents.contents.dwNumberOfItems
        for profile in ppProfileList.contents.contents.ProfileInfo[:num_profiles]:
            pstrProfileXml = pointer(wintypes.LPWSTR())
            pdwFlags = pointer(wintypes.DWORD(WLAN_PROFILE_GET_PLAINTEXT_KEY))
            pdwGrantedAccess = pointer(pointer(wintypes.DWORD()))

            res = WlanGetProfile(
                hClientHandle,
                interface.InterfaceGuid,
                profile.strProfileName,
                pReserved,
                pstrProfileXml,
                pdwFlags,
                pdwGrantedAccess,
            )
            # print(profile.strProfileName, res)
            # print(pdwGrantedAccess.contents.contents.value)
            if profile := pstrProfileXml.contents.value:
                wifi_entry_list.append(parse_wifi_entry(profile))

    # Close handle
    windll.wlanapi.WlanCloseHandle(hClientHandle, pReserved)
    return wifi_entry_list


def main():
    print(get_wifi_passwords())

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
        main()
    else:        
        main() 
