class bird:
    def intro(self):
        print("there are different types of bird")
    def flight(self):
        print("most of the birds can fly but some can not")

class parrot(bird):
    def flight(self):
        print("parrots can fly")

class penguin(bird):
    def flight(self):
        print("penguin do not fly")

obj_bird = bird()
obj_parrot = parrot()
obj_penguin = penguin()

obj_bird.intro()
obj_bird.flight()

obj_parrot.intro()
obj_parrot.flight()

obj_penguin.intro()
obj_penguin.flight()
