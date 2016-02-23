#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Handle voice mail events
# check enums.py fot status meaning
# OnVoicemailStatus

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

def VoicemailStatusHandler(voiceMailObject, status):
    # status - unknown, notdownloaded, downloading, unplayed, buffering, playing,
    # played, blank, recording, recorded, uploading, uploaded, deleting, failed
    # type - unknown, incoming, default_greeting, custom_greeting,  outgoing
    print 'Voice Mail type :', voiceMailObject.Type
    print 'Voice Mail status :', status

skype.OnAttachmentStatus = OnAttachmentHandler
skype.OnVoicemailStatus = VoicemailStatusHandler 

while True:
    time.sleep(1.0)