#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Sets Mood text

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

while True:
    input_var = raw_input("Do you want to change Mood text?(Y/N) : ")
    if(input_var == 'Y'):
        input_var = raw_input("Enter Mood Text: ")
        skype.CurrentUserProfile._SetMoodText(input_var)
        print skype.CurrentUser.MoodText
    else:
        print "exiting"
        break