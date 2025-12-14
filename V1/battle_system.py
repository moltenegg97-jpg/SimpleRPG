import battle
import game_objects
from game_state_control import game_state
import random
from game_window import main_window

class BattleSystem():
    def __init__(self):
        self.isPlayerturn = False #для боя
        self.turn_is_finished = True
    def active_battle(self):
        if game_state.state['battle']:
            if (game_objects.pc.hp > 0 and game_state.enemy_id.hp > 0) and self.turn_is_finished:
                self.turn_is_finished = False
                print(self.isPlayerturn)
                print('новый ход')
                self.player_action()
                if self.isPlayerturn == False:
                    self.ai_action()
                    
                self.repite_active_battle = main_window.main_window.after(30, self.active_battle)
        else:
            main_window.main_window.after_cancel(self.repite_active_battle)
                
            
            
            pass

    def player_action(self):
        self.isPlayerturn = True
        

        def refresh_cursor():
            battle.cursor.move_cursor()
            battle.cursor.pick_battle_option()
            self.ref_cursor = main_window.main_window.after(16, refresh_cursor)    

        if battle.cursor.pick_battle_option():
            self.isPlayerturn = False
            main_window.main_window.after_cancel(self.ref_cursor)
        
        refresh_cursor()

    def ai_action(self):
        ai_choice = random.choice(game_state.enemy_id.list_of_actions)
        if ai_choice == 'attack':
            game_state.enemy_id.make_attack(game_objects.pc)
            print(game_state.enemy_id.name, f'attacks')
        if ai_choice == 'heal':
            game_state.enemy_id.heal(game_objects.pc)
            print(game_state.enemy_id.name, f'heal')
        self.turn_is_finished = True
battle_system = BattleSystem()