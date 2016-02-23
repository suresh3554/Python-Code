#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Handle general events
# check enums.py fot status meaning
# OnMute, OnConnectionStatus, OnUserStatus, OnAutoAway
# OnClientWindowState, OnSilentModeStatusChanged, OnWallpaperChanged

import Skype4Py
import time

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Starting Skype if it's not running already..
if not skype.Client.IsRunning:
    print 'Starting Skype..'
    skype.Client.Start()
    
# Connect the Skype object to the Skype client.
skype.Attach()

# Set up an event handler.
def OnAttachmentHandler(status):
    # If Skype is closed and reopened, it informs us about it
    # so we can reattach.
    if status == Skype4Py.apiAttachAvailable:
        skype.Attach()

def MuteHandler(value):
    # value 1 or 0
    print 'Is Mute :', value

def ConnectionStatusHandler(status):
    # status - unknown, offline, connecting, pausing, online
    print 'Connection status :', status

def UserStatusHandler(status):
    # status - unknown, offline, online, away, NA, DND, invisible, loggedout, skypeme
    print 'User status :', status

def AutoAwayHandler(value):
    # value 1 or 0
    print 'Auto away :', value

def ClientWindowStateHandler(state):
    # state - unknown, normal, minimized, maximized, hidden
    print 'Client Window State :', state

def SilentModeStatusChangedHandler(value):
    # value 1 or 0
    print 'Silent Mode :', value

def WallpaperChangedHandler(path):
    print 'wall paper:', path
    
skype.OnAttachmentStatus = OnAttachmentHandler
skype.OnMute = MuteHandler
skype.OnConnectionStatus = ConnectionStatusHandler
skype.OnUserStatus = UserStatusHandler
skype.OnAutoAway = AutoAwayHandler
skype.OnClientWindowState = ClientWindowStateHandler
skype.OnSilentModeStatusChanged = SilentModeStatusChangedHandler
skype.OnWallpaperChanged = WallpaperChangedHandler

while True:
    time.sleep(1.0)