import zmq


def main():
    """
    This server function returns kilometers when it receives a valid miles input.

    Example valid inputs include:
    integers (0, 2, 4, etc.),
    floats(0.1, 0.2, 0.3, etc.),
    and strings that can be converted to integers or floats ("1", "0.2", etc.).

    This code is very similar to the code running on the Google Cloud computer.
    """
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    port = 3389

    # Local IP
    ip = "127.0.0.1"

    socket.bind(f"tcp://{ip}:{port}")
    print(f"Listening on port: {port}")

    while True:
        #  Wait for next request from client.
        message = socket.recv().decode()

        try:
            # Attempt to convert the input to a float.
            value = float(message) * 1.609344
            print(f"Conversion requested: {message} miles to kilometers.")
            value = str(value).encode()
            socket.send(value)
            print(f"Conversion sent: {value.decode()} kilometers.")

        except ValueError:
            # Logic for invalid input.
            print(f"Conversion request invalid. Sending error message.")
            socket.send(b"Attempted to send a non-float/integer input.")


if __name__ == "__main__":
    main()
