class animal():
    name="tom"
    color="black"
    size="small"
    hairs="furry"
    
    def get_color(self,abc):
      print(self.color +""+ abc)
    @property
    def get_size(self):
      print(self.size)
    


class dog(animal):
    name="jon"
    color="brown"
    def eyes(self):
        print('black')
jon=dog()
jon.get_color("grey")
jon.hairs
jon.get_size
jon.eyes()

class puppy(dog):
    name="snoopy"
snoopy=puppy()
snoopy.color

    
class cat(animal):
    name="pussy"
    def eat(self):
        print('food')
        
pussy=cat()
pussy.get_color("red")
pussy.eat()

    
