class Case:
    def __init__(self):
        self.plage_x = None
        self.plage_y = None
        self.carte_posee = None
        self.rect = None
        self.click = False
    
    def get_card(self):
        return self.carte_posee
    
    def set_click(self,click):
        self.click = click