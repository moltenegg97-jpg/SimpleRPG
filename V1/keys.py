list_of_keys = {
    'w': False,
    'a': False, 
    's': False,
    'd': False,
    'm': False, 
    't': False, #для теста
    'y': False, #для теста
    'Return': False
}

def key_pressed(event):
    if event.keysym in list_of_keys:
        list_of_keys[event.keysym] = True


def key_released(event):
    if event.keysym in list_of_keys:
        list_of_keys[event.keysym] = False