import dojo_ninja

class Pet:
    def __init__ (self, name, type, tricks, health, energy, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound
    
    def sleep (self):
        self.energy += 25
        print (f"{self.name} is sleeping. When it wakes up, its energy will be {self.energy}!")
        return self

    def eat (self):
        self.energy += 5
        self.health += 10
        return self
    
    def play (self):
        self.energy += 5
        (f"Playing with {self.name}. His energy is now {self.energy}!")
        return self
    
    def noise (self):
        print (f"{self.sound}")
        return self

class Cat(Pet):
    def __init__ (self, name, type, tricks, health, energy, sound):
        super().__init__ (name, type, tricks, health, energy, sound)
    
    def sleep (self):
        self.energy += 15
        print (f"{self.name} is taking a cat nap. When it wakes up, its energy will be {self.energy}!")
        return self
    
    def bathe (self):
        self.energy -= 10
        print (f"Cats hate water. {self.name} has lost 10 energy points from trying to stay out of the bathtub.")
        self.noise() 
        return self

class Snake(Pet):
    def __init__ (self, name, type, tricks, health, energy, sound):
        super().__init__ (name, type, tricks, health, energy, sound)
    
    def sleep (self):
        print(f"Rumors suggest that {self.name} never sleeps.")
        return self
    
    def walk (self):
        print(f"Taking {self.name} for a slither!")
    
    def bathe (self):
        print (f"{self.name} does not need a bath. In fact, she will attack you if you try to give her one. Best to avoid this.")
        self.noise()
        return self


laurence = dojo_ninja.Ninja("Laurence", "Fishburne", "Pup-Peroni Training Treats", "Pedigree", Pet("Fido", "Jack Russell terrior", ["sit", "shake hands", "roll over"], 50, 20, "Woof!"))

laurence.feed()
laurence.walk()
laurence.bathe()

jimmy = dojo_ninja.Ninja("Jimmy", "Fallon", "Friskies Party Mix", "Meow Mix", Cat("Captain Whiskers", "British Shorthair", ["hissing on command", "stealth", "catching mice"], 50, 20, "Meow!"))

jimmy.feed()
jimmy.walk()
jimmy.pet.sleep()
jimmy.pet.bathe()

tom = dojo_ninja.Ninja("Tom", "Riddle", "Bertha Jorkins", "Frank Bryce", Snake("Nagini", "Reticulated Python", ["speaking Parseltongue", "telepathy", "speaking French"], 200, 100, "Sssssss!"))

tom.feed()
tom.pet.walk()
tom.pet.sleep()
tom.pet.bathe()