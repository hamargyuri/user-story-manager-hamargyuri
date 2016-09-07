# write connection data to local file
def write_connect_data():
    with open('local_connect_data.txt', 'w') as connect_file:
        connect_file.write("{}\n\
{}".format(input("Please enter your dbname (an existing database): "), input("Please enter your username: ")))


# reading connection data from local file
def read_connect_data():
    with open('local_connect_data.txt', 'r') as connect_file:
        return connect_file.readlines()


# try whether local connection file exists
def connect_list():
    try:
        connect_data = read_connect_data()
    except Exception:
        write_connect_data()
        connect_data = read_connect_data()
    return connect_data
