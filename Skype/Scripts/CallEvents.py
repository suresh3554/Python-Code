#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Handle call events
# check enums.py fot status meaning
# when call status is changed - OnCallStatus
# other handlers - OnCallSeenStatusChanged, OnCallInputStatusChanged
# OnCallTransferStatusChanged, OnCallDtmfReceived, OnCallVideoStatusChanged
# OnCallVideoSendStatusChanged, OnCallVideoReceiveStatusChanged

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

def CallStatusHandler(callObject, status):
    print 'OnCallStatus - ' , status

def CallSeenStatusChangedHandler(callObject, status):
    print 'OnCallSeenStatusChanged - ' , status

def CallInputStatusChangedHandler(callObject, status):
    print 'OnCallInputStatusChanged - ' , status

def CallTransferStatusChangedHandler(callObject, status):
    print 'OnCallTransferStatusChanged - ' , status

def CallDtmfReceivedHandler(callObject, status):
    print 'OnCallDtmfReceived - ' , status

def CallVideoStatusChangedHandler(callObject, status):
    print 'OnCallVideoStatusChanged - ' , status

def CallVideoSendStatusChangedHandler(callObject, status):
    print 'OnCallVideoSendStatusChanged - ' , status

def CallVideoReceiveStatusHandler(callObject, status):
    print 'OnCallVideoReceiveStatusChanged - ' , status
    
skype.OnAttachmentStatus = OnAttachmentHandler
skype.OnCallStatus = CallStatusHandler 
skype.OnCallSeenStatusChanged = CallSeenStatusChangedHandler
skype.OnCallInputStatusChanged = CallInputStatusChangedHandler
skype.OnCallTransferStatusChanged = CallTransferStatusChangedHandler
skype.OnCallDtmfReceived = CallDtmfReceivedHandler
skype.OnCallVideoStatusChanged = CallVideoStatusChangedHandler
skype.OnCallVideoSendStatusChanged = CallVideoSendStatusChangedHandler
skype.OnCallVideoReceiveStatusChanged = CallVideoReceiveStatusHandler

while True:
    time.sleep(1.0)