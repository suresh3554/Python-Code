#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Lists groups type and its user count

import Skype4Py

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Starting Skype if it's not running already..
if not skype.Client.IsRunning:
    print 'Starting Skype..'
    skype.Client.Start()
    
# Connect the Skype object to the Skype client.
skype.Attach()

# Set up an event handler.
def new_skype_status(status):
    # If Skype is closed and reopened, it informs us about it
    # so we can reattach.
    if status == Skype4Py.apiAttachAvailable:
        skype.Attach()

skype.OnAttachmentStatus = new_skype_status

# Obtain some information from the client and print it out.
names = []
print 'Your full name:', skype.CurrentUser.FullName

for group in skype.Groups:
    print skype.Convert.GroupTypeToText(group.Type), group.Users.Count
    
