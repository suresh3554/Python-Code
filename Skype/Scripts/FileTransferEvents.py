#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Handle file transfer events
# check enums.py fot status meaning
# OnFileTransferStatusChanged

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

def FileTransferStatusChangedHandler(fileTransferObject, status):
    # status - new, connecting, waiting_for_accept, composing, transferring, transferring_over_relay,
    # paused, remotely_paused, cancelled, completed, failed
    print 'File Name :', fileTransferObject.FileName
    print 'File Path :', fileTransferObject.FilePath
    print 'File size :', fileTransferObject.FileSize
    print 'File Transfer type :', fileTransferObject.Type
    print 'File Transfer status :', status

skype.OnAttachmentStatus = OnAttachmentHandler
skype.OnFileTransferStatusChanged = FileTransferStatusChangedHandler 

while True:
    time.sleep(1.0)