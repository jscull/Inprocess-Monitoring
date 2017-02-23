from O365 import Message

auth = ('mechanic@hieta.biz','Plank65(dons')
m = Message(auth=auth)
m.setRecipients('joescull@hieta.biz')
m.setSubject('Testing script')
m.setBody('This is not a person')
m.sendMessage()\