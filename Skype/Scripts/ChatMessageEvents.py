#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Handle chat message events
# check enums.py fot status meaning
# OnMessageStatus

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

def MessageStatusHandler(chatMessageObject, status):
    # status - unknown, sending, sent, recieved, read 
    print 'Sender :', chatMessageObject.FromHandle
    print 'Message :', chatMessageObject.Body
    print 'Status :',  status

skype.OnAttachmentStatus = OnAttachmentHandler
skype.OnMessageStatus = MessageStatusHandler 

while True:
    time.sleep(1.0)