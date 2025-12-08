list_of_keys = {
    'w': False,
    'a': False, 
    's': False,
    'd': False,
    'm': False, 
    't': False, #для теста
    'y': False, #для теста
    'u': False, #для теста
    'Return': False
}

#должен повторять list_of_keys
key_tapped = {
    'w': False,
    'a': False, 
    's': False,
    'd': False,
    'm': False, 
    't': False, #для теста
    'y': False, #для теста
    'u': False, #для теста
    'Return': False
}

def reset_input_flags():
    for key in key_tapped:
        key_tapped[key] = False 

def key_pressed(event):
    if event.keysym in list_of_keys:   
        if list_of_keys[event.keysym] == True:
            key_tapped[event.keysym] = False
            return
        list_of_keys[event.keysym] = True
        key_tapped[event.keysym] = True
        

def key_released(event):
    if event.keysym in list_of_keys:
        list_of_keys[event.keysym] = False
        key_tapped[event.keysym] = False
