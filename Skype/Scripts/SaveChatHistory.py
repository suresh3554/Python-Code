#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Get all chat objects
# separate single chat and multiple chat
# Get its Members
# Each chat has Message objects
# print each sender and time stamp
# print each message body

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

# Obtain some information from the client and print it out.

ChatDetails = {}
GroupChatDetails = {}
buffer = u''

print 'Your full name:', skype.CurrentUser.FullName
print skype.CurrentUser.Handle
print skype.Chats.Count

for chat in skype.Chats:
    buffer = u''
    if chat.Members.Count == 2:
        for member in chat.Members:
            if member.Handle != skype.CurrentUser.Handle:
                if ChatDetails.has_key(member.Handle):
                    buffer = ChatDetails[member.Handle]
                break
        if chat.Messages.Count:
            for msg in chat.Messages:
                buffer = buffer + msg.FromDisplayName + u"  " + str(msg.Datetime) + u"\n  \" " + msg.Body + u" \"\n"
            ChatDetails[member.Handle] = buffer
    else:
        if GroupChatDetails.has_key(chat.Name):
            buffer = GroupChatDetails[chat.Name]
        else:
            buffer = buffer + "Group Members:\n"
            for member in chat.Members:
                buffer = buffer + member.FullName + "\n"
            buffer = buffer + "\n"
        if chat.Messages.Count:
            for msg in chat.Messages:
                buffer = buffer + msg.FromDisplayName + u"  " + str(msg.Datetime) + u"\n  \" " + msg.Body + u" \"\n"
            GroupChatDetails[chat.Name] = buffer
            

for user in ChatDetails.keys():
    chat_dir = os.path.join(working_dir,'Chat_history')
    if os.path.isdir(chat_dir) != True:
        os.makedirs(chat_dir)
    fp = codecs.open(os.path.join(chat_dir, user +'.txt'), encoding='utf-8', mode='w+')
    fp.write(ChatDetails[user])
    fp.close()
    
for i in range(len(GroupChatDetails)):
    chat_dir = os.path.join(working_dir,'Chat_history')
    if os.path.isdir(chat_dir) != True:
        os.makedirs(chat_dir)
    fp = codecs.open(os.path.join(chat_dir, 'Group_%d.txt'%(i+1)), encoding='utf-8', mode='w+')
    fp.write(GroupChatDetails[GroupChatDetails.keys()[i]])
    fp.close()
