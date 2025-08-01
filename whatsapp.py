"""

    HW: (Mandatory)
    Class1: WhatsAppMessage: text, sender, receiver, status
    Class2: WhatsAppMessageList: head, tail, size (Doubly LinkedList)
            here, follow the same session11, 11A, 11B
            only head and tail will not refer to each other


"""
class WhatsAppMessage:
    def __init__(self, text, sender, receiver, status ):
        self.text = text
        self.sender  = sender
        self.receiver = receiver
        self.status = status
        self.next = None
        self.prev = None

    def show_message(self):
        print("------------")
        print(f"text:{self.text}")
        print(f"sender:{self.sender}' | 'receiver:{self.receiver}")
        print(f"status:{self.status}")
        print('------------')

        

