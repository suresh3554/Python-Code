#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# List all Friends Detailed info.

import Skype4Py
import os, codecs

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

# Obtain some information and print it out.

fp = codecs.open(working_dir + 'FriendsInfo.txt', encoding='utf-8', mode='w+')

print 'Your Name', skype.CurrentUser.FullName
fp.write( r'Your Name:'+ skype.CurrentUser.FullName + "\n")
fp.write( r'Your Friends Information' + "\n" )

count = 1

for user in skype.Friends:
    fp.write( str(count))
    fp.write( r' - Skype-Id:'+ user.Handle + "\n")
    fp.write( r'Full name:'+ user.FullName + "\n")
    fp.write( r'Display name:'+ user.DisplayName + "\n")
    fp.write( r'Gender:'+ user.Sex + "\n")
    fp.write( r'Birthday:'+ str(user.Birthday) + "\n")
    
    fp.write( r'Number Of Contacts:'+ str(user.NumberOfAuthBuddies) + "\n")
    fp.write( r'Online Status:'+ skype.Convert.OnlineStatusToText(user.OnlineStatus) + "\n")
    fp.write( r'Last Online:'+ str(user.LastOnlineDatetime) + "\n")
    fp.write( r'Buddy Status:'+ skype.Convert.BuddyStatusToText(user.BuddyStatus) + "\n")
    fp.write( r'Language:'+ user.Language + "\n")
    fp.write( r'Language Code:'+ user.LanguageCode + "\n")
    
    fp.write( r'Mood:'+ user.MoodText + "\n")
    fp.write( r'Rich Mood Text:'+ user.RichMoodText + "\n")
    fp.write( r'About:'+ user.About + "\n")
    
    fp.write( r'Phone Home:'+ str(user.PhoneHome) + "\n")
    fp.write( r'Phone Mobile:'+ str(user.PhoneMobile) + "\n")
    fp.write( r'Phone Office:'+ str(user.PhoneOffice) + "\n")
    fp.write( r'Speed Dial:'+ str(user.SpeedDial) + "\n")
    fp.write( r'State/Province:'+ user.Province + "\n")
    fp.write( r'City:'+ user.City + "\n")
    fp.write( r'Country:'+ user.Country + "\n")
    fp.write( r'Country Code:'+ user.CountryCode + "\n")
    
    fp.write( r'Home Page:'+ user.Homepage + "\n")
    fp.write( r'Time zone:'+ str(user.Timezone) + "\n")
    
    fp.write( r'Has Call Equipment:'+ str(user.HasCallEquipment) + "\n")
    fp.write( r'Can Leave Voicemail:'+ str(user.CanLeaveVoicemail) + "\n")
    fp.write( r'Received Auth Request:'+ str(user.ReceivedAuthRequest) + "\n")
    
    fp.write( r'Is Authorized:'+ str(user.IsAuthorized) + "\n")
    fp.write( r'Is Blocked:'+ str(user.IsBlocked) + "\n")
    fp.write( r'Is Call Forward Active:'+ str(user.IsCallForwardActive) + "\n")
    fp.write( r'Is Skype Out Contact:'+ str(user.IsSkypeOutContact) + "\n")
    fp.write( r'Is Video Capable:'+ str(user.IsVideoCapable) + "\n")
    fp.write( r'Is Voicemail Capable:'+ str(user.IsVoicemailCapable) + "\n")
    fp.write( "\n" )
    count = count + 1
    
    
fp.close()

print 'Your Friends Information is saved at :' + working_dir
