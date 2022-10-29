# 361_microservice
Convert miles to kilometers using this microservice!

<h2>Library Requirement</h2>
To both request and receive data from the server, please install one of ZeroMQ's free libraries (https://zeromq.org/).

<h2>Requesting and Receiving Data</h2>

To request data from the server, initialize a ZMQ socket client-side socket. Then, connect the socket to tcp://34.127.106.38:3389:

    import zmq
    context = zmq.Context()

    # Socket to talk to server
    print("Connecting to miles/kilometer converter…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://34.127.106.38:3389")

Then, send a your request encoded in bytes:

    # Send the request
    request = miles
    print(f"Sending request {request} …")
    request = f"{request}".encode()
    socket.send(request)
    
Finally, the response will be stored in the variable that is bound to socket.recv. Decode the response, and you will have the conversion!

    # Get the reply
    message = socket.recv()
    return message.decode()
