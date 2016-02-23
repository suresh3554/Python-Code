import Skype4Py
import os, sys

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

# Obtain some information and print it out.
print 'Your Profile Information\n'


print 'Skype-Id:', skype.CurrentUser.Handle
print 'Full name:', skype.CurrentUser.FullName
print 'Display name:', skype.CurrentUser.DisplayName
print 'Gender:', skype.CurrentUser.Sex
print 'Birthday:', skype.CurrentUser.Birthday

print 'Number Of Contacts:', skype.CurrentUser.NumberOfAuthBuddies
print 'Online Status:', skype.CurrentUser.OnlineStatus
print 'Last Online:', skype.CurrentUser.LastOnlineDatetime
print 'Buddy Status:', skype.CurrentUser.BuddyStatus
print 'Language:', skype.CurrentUser.Language
print 'Language Code:', skype.CurrentUser.LanguageCode

print 'Mood:', skype.CurrentUser.MoodText
print 'Rich Mood Text:', skype.CurrentUser.RichMoodText
print 'About:', skype.CurrentUser.About

print 'Phone Home:', skype.CurrentUser.PhoneHome
print 'Phone Mobile:', skype.CurrentUser.PhoneMobile
print 'Phone Office:', skype.CurrentUser.PhoneOffice
print 'Speed Dial:', skype.CurrentUser.SpeedDial
print 'State/Province:', skype.CurrentUser.Province
print 'City:', skype.CurrentUser.City
print 'Country:', skype.CurrentUser.Country
print 'Country Code:', skype.CurrentUser.CountryCode

print 'Home Page:', skype.CurrentUser.Homepage
print 'Time zone:', skype.CurrentUser.Timezone

print 'Has Call Equipment:', skype.CurrentUser.HasCallEquipment
print 'Can Leave Voicemail:', skype.CurrentUser.CanLeaveVoicemail
print 'Received Auth Request:', skype.CurrentUser.ReceivedAuthRequest

print 'Is Authorized:', skype.CurrentUser.IsAuthorized
print 'Is Blocked:', skype.CurrentUser.IsBlocked
print 'Is Call Forward Active:', skype.CurrentUser.IsCallForwardActive
print 'Is Skype Out Contact:', skype.CurrentUser.IsSkypeOutContact
print 'Is Video Capable:', skype.CurrentUser.IsVideoCapable
print 'Is Voicemail Capable:', skype.CurrentUser.IsVoicemailCapable

# change directory 
profile_pic = 'E:\\Myfiles\\Scripts\\Skype\\scripts\\' + skype.CurrentUser.Handle +'.jpg'
#profile_pic = os.path.join(os.path.dirname(os.path.realpath(__file__)), skype.CurrentUser.Handle +'.jpg')
skype.CurrentUser.SaveAvatarToFile(profile_pic)
print 'Save Avatar To File:', 'Saved at ' + profile_pic

