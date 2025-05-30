p1 = "make money"
p2 = "buy now"
p3 = "subscribe now"
p4 = "limited time offer"

message = input("Enter a message: ")

if( (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This message is a spam")
else:
    print("This message is not a spam")