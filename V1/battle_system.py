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
    def active_battle(self):
        if not game_state.state['battle']:
            return
        if (game_objects.pc.hp <= 0 or game_state.enemy_id.hp <= 0): #and self.turn_is_finished:
            return
        
        if self.turn_is_finished:
            print(game_objects.pc.conditions)
            self.start_player_turn()
            self.player_action()
            
        """
        self.start_player_turn()
        print(self.isPlayerturn)
        print('новый ход')
        print(f'состояния до обновления: {game_objects.pc.conditions}')
        self.refresh_conditions_counters(game_objects.pc)
        print(f'состояния после обновления: {game_objects.pc.conditions}')
        self.player_action()                
        print(f'состояния до обновления: {game_state.enemy_id.conditions}')
        self.refresh_conditions_counters(game_state.enemy_id)
        print(f'состояния после обновления: {game_state.enemy_id.conditions}')
        if self.isPlayerturn == False:
            self.ai_action()
                    
            self.repite_active_battle = main_window.main_window.after(30, self.active_battle)
        else:
            main_window.main_window.after_cancel(self.repite_active_battle)
        """
    def register_choice_callback(self, callback):
        self.on_player_choice_callback = callback
    
    def on_player_choice(self, action):
        self.isPlayerturn = False
        game_objects.pc.apply_condition_end_turn()
        print('я тут')
        print(game_objects.pc.conditions['defending'])
        print(game_objects.pc.phy_res)

        if hasattr(self, 'ref_cursor'):
            main_window.main_window.after_cancel(self.ref_cursor)
        self.ai_action()

    def refresh_conditions_counters(self, target):
        for i in target.conditions:
            if target.conditions[i] != 0:
                target.conditions[i] = target.conditions[i] - 1
    
    def start_player_turn(self):
        self.isPlayerturn = True
        self.turn_is_finished = False



    def player_action(self):
        self.isPlayerturn = True
        game_objects.pc.apply_condition_start_turn()
        print('применил состояние в начале хода')

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
        game_state.enemy_id.apply_condition_start_turn()
        ai_choice = random.choice(game_state.enemy_id.list_of_actions)
        if ai_choice == 'attack':
            game_state.enemy_id.make_attack(game_objects.pc)
            print(game_state.enemy_id.name, f'attacks')
        if ai_choice == 'heal':
            game_state.enemy_id.heal(game_objects.pc)
            print(game_state.enemy_id.name, f'heal')
        game_state.enemy_id.apply_condition_end_turn()
        print('here')
        self.turn_is_finished = True

battle_system = BattleSystem()
battle.cursor.set_choice_callback(battle_system.on_player_choice)