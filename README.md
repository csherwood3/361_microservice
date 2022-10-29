# 361_microservice
Convert miles to kilometers using this microservice!

<h2>Library Requirement</h2>
To both request and receive data from the server, please install the ZeroMQ's library of your development environment (https://zeromq.org/).

<h2>Requesting and Receiving Data</h2>

This example will follow the Python start code written for this repo.

To request data from the server, first initialize a ZMQ client-side socket. Then, connect the socket to tcp://34.127.106.38:3389:

    import zmq
    context = zmq.Context()

    # Socket to talk to server
    print("Connecting to miles/kilometer converter…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://34.127.106.38:3389")

Then, send a your request encoded in bytes. As an example, let's request 300 miles to be converted:

    # Send the request
    request = 300
    print(f"Sending request {request} …")
    request = f"{request}".encode()
    socket.send(request)
    
Finally, the response will be stored in the variable that is bound to socket.recv. Decode the response, and you will have the conversion!

    # Get the reply
    message = socket.recv()
    return message.decode()

<h2>UML Diagram</h2>
![image](https://user-images.githubusercontent.com/71786657/198851864-fcfb1d51-5d21-4dcc-b162-6564f25e1b98.png)

![UML Diagram](https://github.com/csherwood3/361_microservice/blob/main/UML%20Diagram.PNG "Employee Data title")
