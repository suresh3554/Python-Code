#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Handle sms message events
# check enums.py fot status meaning
# OnSmsMessageStatusChanged, OnSmsTargetStatusChanged

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

def SmsMessageStatusChangedHandler(smsMessageObject, status):
    # status - unknown, recieved, read, composing, sending to server, sent to server, delivered, some targets failed, failed
    print 'sms body :', smsMessageObject.Body
    print 'sms status :',  status

def SmsTargetStatusChangedHandler(smsTargetObject, status):
    # status - unknown, target_undefined, target_analyzing, target_acceptable, target_not_routable, 
    # target_delivery_pending, target_delivery_successful, target_delivery_failed
    print 'Target Number :', smsTargetObject.Number
    print 'Target sms body :', smsTargetObject.Message.Body
    print 'Target sms status :',  status

skype.OnAttachmentStatus = OnAttachmentHandler
skype.OnSmsMessageStatusChanged = SmsMessageStatusChangedHandler 
skype.OnSmsTargetStatusChanged = SmsTargetStatusChangedHandler

while True:
    time.sleep(1.0)