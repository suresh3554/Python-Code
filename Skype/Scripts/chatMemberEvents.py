#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Handle chat member events
# check enums.py fot status meaning
# OnChatMemberRoleChanged

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

def ChatMemberRoleChangedHandler(chatMemberObject, role):
    # role - applicant, creator, helper, listener, master, unknown, user 
    print chatMemberObject.Handle, role

skype.OnAttachmentStatus = OnAttachmentHandler
skype.OnChatMemberRoleChanged = ChatMemberRoleChangedHandler 

while True:
    time.sleep(1.0)