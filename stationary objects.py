class Stationary_objects:
    def __init__(self):
        self.x = x
        self.y = y
        self.max_durability = durability
        self.durability = durability
        self.max_capasity = capability
        self.capasity = 0
        self.update_path = update_path
        self.update_state = 0
        self.current_state
        self.isbroken = False

    def updating(self):
        if not self.isbroken:
            self.update_path += 1
            for i in range(len(self.update_path)):
                if self.update_state < self.update_path[i][1]:
                    self.current_state = self.update_path[i][0]
                    break
