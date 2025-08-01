from whatsapp import WhatsAppMessage


class WhatsAppMessageList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def add_message(self, message):
        self.size += 1
        if self.head == None:
            self.head = message
            self.tail = message

            message.next = None
            message.prev = None

        else :
            self.tail.next = message
            message.next = None
            message.prev = self.tail
            self.tail = message
        
    def display_messages(self):
        if self.head is None:
            print("no messages to show")
            return
        
        current = self.head 
        while current is not None:
            current.show_message()
            current = current.next

m1 = message( "hey", "alice",  "john" ,  "sent")
m2 = message("hello",  "john", " alice" ,"seen")
m3 = message("how are uh?", "alice", "john", "seen")

msg_list =  WhatsAppMessageList()
msg_list.add_message(m1)
msg_list.add_message(m2)
msg_list.add_message(m3)
msg_list.display_messages()




