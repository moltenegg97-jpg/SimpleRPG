import keys
from game_state_control import game_state

def exit_inventory():
    if keys.key_tapped['i']:
        game_state.back_from_inventory()
        keys.reset_input_flags()