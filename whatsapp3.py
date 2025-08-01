from whatsapp import WhatsAppMessage
from Whatsapp1 import WhatsAppMessageList

message1 = WhatsAppMessage( text= 'hey' , sender = 'person1', receiver =  'person2' , status= 'sent')
message2 = WhatsAppMessage(text= 'hello' , sender = 'person2', receiver =  'person1' , status= 'seen')
message3 = WhatsAppMessage(text= 'how are uh?' , sender = 'person1', receiver =  'person2' , status= 'seen')

chat =  WhatsAppMessageList()
chat.add_message(message1)
chat.add_message(message2)
chat.add_message(message3)

chat.printmessage()