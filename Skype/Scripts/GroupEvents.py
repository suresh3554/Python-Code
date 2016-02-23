#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Handle group events
# check enums.py fot status meaning
# OnGroupVisible, OnGroupExpanded, OnGroupUsers, OnGroupDeleted

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

def GroupVisibleHandler(groupObject, visible):
    # visible - 1 0r 0 
    print skype.Convert.GroupTypeToText(groupObject.Type), ' Group is visible : ',  visible

def GroupExpandedHandler(groupObject, expanded):
    # expanded - 1 0r 0 
    print skype.Convert.GroupTypeToText(groupObject.Type), ' Group is visible : ',  expanded

def GroupUsersHandler(groupObject, userCount):
    print  skype.Convert.GroupTypeToText(groupObject.Type), ' Group user count is : ', userCount

def GroupDeletedHandler(value):
    print  'Group deleted :', value
    
skype.OnAttachmentStatus = OnAttachmentHandler
skype.OnGroupVisible = GroupVisibleHandler 
skype.OnGroupExpanded = GroupExpandedHandler 
skype.OnGroupUsers = GroupUsersHandler 
skype.OnGroupDeleted = GroupDeletedHandler

while True:
    time.sleep(1.0)