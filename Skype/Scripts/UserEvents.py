#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# handle User events
# when online status is changed - OnOnlineStatus
# when user mood text is changed - OnUserMood
# when user sends you a request - OnUserAuthorizationRequestReceived

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

def OnlinestatusHandler(user, status):
    print user.Handle,' is ', status

def UserMoodHandler(user, txt):
    print user.Handle, '- Mood text is ', txt

def UserAuthorizationRequestReceivedHandler(user):
    print user.Handle, ' sent you a request'
    
skype.OnAttachmentStatus = OnAttachmentHandler
skype.OnOnlineStatus = OnlinestatusHandler
skype.OnUserMood = UserMoodHandler
skype.OnUserAuthorizationRequestReceived = UserAuthorizationRequestReceivedHandler

while True:
    time.sleep(1.0)