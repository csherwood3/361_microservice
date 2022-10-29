import zmq


def convert_to_kilometers(miles):
    context = zmq.Context()

    # Socket to talk to server
    print("Connecting to miles/kilometer converter…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://34.127.106.38:3389")

    # Send the request
    request = miles
    print(f"Sending request {request} …")
    request = f"{request}".encode()
    socket.send(request)

    # Get the reply
    message = socket.recv()
    return message.decode()


print(convert_to_kilometers(300))
