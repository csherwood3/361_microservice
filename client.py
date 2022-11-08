import zmq


def convert_to_kilometers(miles):
    """
    This client function takes miles as a parameter and converts it to kilometers.

    A ZMQ socket is first created. Then, we connect to the server socket and send
    the request from miles to kilometers. We get the response in bytes and decode
    it. The value conversion is returned.
    
    If you want to use the Google socket, un-comment the Google connection line 
    and comment out the local server connection.
    """
    context = zmq.Context()

    # Socket to talk to server
    print("Connecting to miles/kilometer converter…")
    socket = context.socket(zmq.REQ)

    # Local server connection
    socket.connect("tcp://127.0.0.1:3389")

    # Google server connection
    # socket.connect("tcp://34.127.106.38:3389")

    # Send the request
    print(f"Sending request {miles} …")
    request = f"{miles}".encode()
    socket.send(request)

    # Get the reply
    kilometers = socket.recv()
    socket.close()
    return kilometers.decode()


if __name__ == "__main__":
    print(convert_to_kilometers(23.2))
