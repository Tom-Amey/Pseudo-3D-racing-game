#menu checker

def check_button_menu(button_pressed_list):

    if button_pressed_list[0]:
        return "leaderboard"
    if button_pressed_list[1]:
        return "garage" 
    if button_pressed_list[2]:
        return "levels"
    if button_pressed_list[3]:
        return "login" 
    
    
# simply iterates through list that is returned by menu (list containing true and false levels)
# returns string indicating which function/pathway of game to progress to
    
