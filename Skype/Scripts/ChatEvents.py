#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Handle chat events
# check enums.py fot status meaning
# OnChatMembersChanged, OnChatWindowState

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

def ChatMembersChangedHandler(chatObject, members):
    print 'Chat Name - ', chatObject.Name
    print 'Chat members :'
    for mem in members:
        print mem.Handle

def ChatWindowStateHandler(chatObject, windowState):
    # window state 1 = OPENED, 0 - CLOSED
    print 'Chat Name - ', chatObject.Name
    print 'Chat members :'
    for mem in members:
        print mem.Handle
    print 'ChatWindowState - ' , windowState

skype.OnAttachmentStatus = OnAttachmentHandler
skype.OnChatMembersChanged = ChatMembersChangedHandler 
skype.OnChatWindowState = ChatWindowStateHandler

while True:
    time.sleep(1.0)