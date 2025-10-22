# This program will use a dinosaur class to creat a dinosaur.

class Dinosaur:

  def __init__(self, name, species, diet, age):

   self_name = name
   self_species = species
   self_diet = diet
   self_age = age

 
 # Dinosaur 1
  dino_1_name = "Rex"
  dino_1_species = "Tyranosaurus Rex"
  dino_1_diet = "meat"
  self_dino_1_age = 12

  # Dinosaur 2
  dino_2_name = "Bumpy"
  dino_2_species = "Ankylosaurus"
  dino_2_diet = "plants"
  self_dino_2_age = 9

  # Dinosaur 3
  dino_3_name = "Spike"
  dino_3_species = "Spinosaurus"
  dino_3_diet = "fish"
  self_dino_3_age = 15

print(f"{dino_2_name} lets out a mighty ROAR!")

print(f"{dino_1_name} is eating {dino_1_diet}.")


class FlyingDinosaur(Dinosaur):
 def __init__(self, name, species, diet, age, wing_span):
  super().__init__(name, species, diet, age)
  self.wing_span = wing_span

  FlyingDinosaur_dino_name = "Rick"
  FlyingDinosaur_species = "Quetzalcoatlus"
  FlyingDinosaur_diet = "fish"
  self_FlyingDinosaur_age = 29
  FlyingDinosaur_wing_span = "34 ft"

print(f"{FlyingDinosaur_dino_name} lets out a mighty screech!")

class WaterDinosaur(Dinosaur):
  def __init__(self, name, species, diet, age, swim_speed):
   super().__init__(name, species, diet, age)
   self.swim_speed = swim_speed
   
  WaterDinosaur_dino_name = "Will"
  WaterDinosaur_species = "Mosasours"
  WaterDinosaur_diet = "fish"
  self_WaterDinosaur_age = 13
  WaterDinosaur_swim_speed = "30 mph" 


  print(f"{WaterDinosaur_dino_name} lets out a mighty rumble!")


  dino_1 = print("Name: Rex", " Species: Tyrannosaurus Rex", " Diet: meat", "Age: 12")
  dino_2 = print("Name: Bumpy", "Species: Ankylosaurus", "Diet: plants", "Age 9")
  dino_3 = print("Name: Spike", " Species: Spinosaurus", "Diet: fish", "Age 15")
  FlyingDinosaur = print("Name: Rick", "Species: Quetzalcoatlus", "Diet: fish", "Age: 29", "Wing Span: 34ft" )
  WaterDinosaur = print("Name: Will", "Species: Mosasours","Diet: fish", "Age: 13", "Swim Speed: 30mph")




    
  

  
