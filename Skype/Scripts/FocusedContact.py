#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Print selected Contact skype Name

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
def OnAttachment(status):
    # If Skype is closed and reopened, it informs us about it
    # so we can reattach.
    if status == Skype4Py.apiAttachAvailable:
        skype.Attach()

def contactfocus(name):
    print name
    
skype.OnContactsFocused = contactfocus
skype.OnAttachmentStatus = OnAttachment

while True:
    time.sleep(1.0)
