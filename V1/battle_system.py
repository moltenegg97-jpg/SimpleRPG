import battle
import game_objects
from game_state_control import game_state
import random
from game_window import main_window

class BattleSystem():
    def __init__(self):
        self.isPlayerturn = False #для боя
        self.turn_is_finished = True
        self.on_player_choice_callback = None
        self.corrent_state = None
        self.previous_state = None
        self.states = {
            'begin_of_new_turn': None,
            'player_turn_start': self.player_start_turn,
            'player_turn_choice': self.player_action,
            'player_turn_end': self.player_end_turn,
            'enemy_turn': self.ai_action
        }

    def change_state(self, new_state):
        self.previous_state = self.corrent_state
        self.corrent_state = new_state
        self.states[new_state]()

    def active_battle(self):
        if not game_state.state['battle']:
            return
        if (game_objects.pc.hp <= 0 or game_state.enemy_id.hp <= 0): #and self.turn_is_finished:
            return
        
        if self.turn_is_finished:
            self.change_state('player_turn_start')
            print(game_objects.pc.conditions)
            #self.start_player_turn()
            self.player_action()
    
    def player_start_turn(self):
        self.isPlayerturn = True
        self.turn_is_finished = False
        self.refresh_conditions_counters(game_objects.pc)
        game_objects.pc.apply_condition_start_turn()
        self.change_state('player_turn_choice')

    def register_choice_callback(self, callback):
        self.on_player_choice_callback = callback
    
    def on_player_choice(self, action):
        if hasattr(self, 'ref_cursor'):
            main_window.main_window.after_cancel(self.ref_cursor)
        
        self.change_state('player_turn_end')
    
    def player_end_turn(self):
        self.isPlayerturn = False
        game_objects.pc.apply_condition_end_turn()
        print('я тут')
        print(game_objects.pc.conditions['defending'])
        print(game_objects.pc.phy_res)
        self.change_state('enemy_turn')

    def refresh_conditions_counters(self, target):
        for i in target.conditions:
            if target.conditions[i] != 0:
                target.conditions[i] = target.conditions[i] - 1


    def player_action(self):

        def refresh_cursor():
            battle.cursor.move_cursor()
            battle.cursor.pick_battle_option()
            self.ref_cursor = main_window.main_window.after(16, refresh_cursor)    

        if battle.cursor.pick_battle_option():
            self.isPlayerturn = False
            game_objects.pc.apply_condition_end_turn()
            main_window.main_window.after_cancel(self.ref_cursor)
            
        
        refresh_cursor()

    def ai_action(self):
        self.refresh_conditions_counters(game_state.enemy_id)
        game_state.enemy_id.apply_condition_start_turn()
        ai_choice = random.choice(game_state.enemy_id.list_of_actions)
        if ai_choice == 'attack':
            game_state.enemy_id.make_attack(game_objects.pc)
            print(game_state.enemy_id.name, f'attacks')
            
            #main_window.add_battle_log(f'{game_state.enemy_id.name,} attacks')
            #main_window.battle_log.insert('end',f'{game_state.enemy_id.name,} attacks')
        if ai_choice == 'heal':
            game_state.enemy_id.heal(game_objects.pc)
            print(game_state.enemy_id.name, f'heal')
            #main_window.add_battle_log(f'{game_state.enemy_id.name,} heals')
        game_state.enemy_id.apply_condition_end_turn()
        print('here')
        self.turn_is_finished = True
        self.active_battle()

battle_system = BattleSystem()
battle.cursor.set_choice_callback(battle_system.on_player_choice)