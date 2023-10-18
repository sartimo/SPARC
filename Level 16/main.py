import socket
import time


def connect_to_server(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    ip = str(ip)
    port = int(port)
    s.connect((ip, port))
    return s


def send_data_to_server(s, data):
    # s is a connected socket, data is a string
    data = str(data)
    data = data.encode("utf-8")
    s.send(data)


def receive_data_from_server(s):
    # s is a connected socket, if there is no data to receive, this will hang for 5 seconds and then die
    data = s.recv(1024*10).decode("utf-8")
    return data


def close_connection_to_server(s):
    s.close()


def display_level():
    client_socket = connect_to_server("10.0.0.5", 1234)
    # receive message
    print(receive_data_from_server(client_socket))
    # set level
    level = "16"
    # send level
    send_data_to_server(client_socket, level)

    # receive level instructions
    instructions = receive_data_from_server(client_socket)
    print(instructions)

    # receive challenge input from the server
    # (messages from the server have a new-line character at the end, which is why we need to strip it)
    challenge_input = receive_data_from_server(client_socket).strip()
    print(challenge_input + "\n\n")

    attribute = receive_data_from_server(client_socket).strip()
    print("attribute: " + attribute + "\n\n")
    # v start developing your answer here v

    print(type(challenge_input))
    import json

    jsonObject = json.loads(challenge_input)
    print(type(str(jsonObject)))

    jsonAttribute = jsonObject[attribute]
    print(jsonAttribute)

    contains_string = False
    if type(jsonAttribute) is str: 
        for item in jsonAttribute:
            if isinstance(item, str):
                contains_string = True
                print("contains string")
                break

    

    result = jsonAttribute










    # send response to the server (response has to be stored in "result" by your code above)
    send_data_to_server(client_socket, result)

    # receive status message
    time.sleep(0.1)
    print(receive_data_from_server(client_socket))

    close_connection_to_server(client_socket)


# Press the play button in the top right corner to run the script.
if __name__ == '__main__':
    display_level()
