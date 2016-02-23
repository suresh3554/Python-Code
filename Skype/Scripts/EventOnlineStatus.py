#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# when a user changes status - OnOnlineStatus event occurs. 
# It is handled to print user and his status
# output: it prints 'skypename ONLINE/OFFLINE/....'

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

def onlinestatus(user, status):
    print user.Handle, status
    
skype.OnOnlineStatus = onlinestatus
skype.OnAttachmentStatus = OnAttachment

while True:
    time.sleep(1.0)