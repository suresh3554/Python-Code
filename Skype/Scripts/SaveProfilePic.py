#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Saves each friends profile picture.

import Skype4Py
import os

working_dir = 'E:\\Myfiles\\Scripts\\Skype\\scripts\\' 

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

for user in skype.Friends:
    profile_pic_dir = os.path.join(working_dir + 'Profile_Pics')
    if os.path.isdir(profile_pic_dir) != True:
        os.makedirs(profile_pic_dir)

    try:
        if(user.BuddyStatus == 3): # Only Friends
            profile_pic = os.path.join(profile_pic_dir , user.Handle +'.jpeg')
            #profile_pic = os.path.join(os.path.dirname(os.path.realpath(__file__)), user.Handle +'.jpg')
            user.SaveAvatarToFile(profile_pic)
    except Exception as e:
        print 'No Avatar for user - ', user.Handle, ', Error msg: ', e

    
