#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Search users in skype directory

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

skype.OnAttachmentStatus = OnAttachmentHandler

usrcoll = skype.SearchForUsers('mahadev')
print "Number of users : " , usrcoll.Count
for usr in usrcoll:
    print 'Skype-Id:', usr.Handle, 'Full name:', usr.FullName, 'City:', usr.City
