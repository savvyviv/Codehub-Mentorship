#functions of some parts of a car stored as a dictionary
carfunctions={
    "engine":"The engine is the heart of the vehicle and is specially designed to convert oxygen and fuel into mechanical energy that propels you forward",
     "Transmission":"The transmission is an extension of the engine and essentially makes sure that the right amount of power is channeled to the wheels.",   
     "Battery":"The battery is a rechargeable unit that ensures your engine starts properly.", 
     "Radiator":"The radiator helps to regulate the temperature of the engine by transferring heat from the fluid inside to the air outside.",
      "Alternator":"The alternator is essentially an electric generator that charges the battery while the vehicle is running.",
       "Brakes":" a brake is a mechanical device that inhibits motion by absorbing energy from a moving system."    
        }
print(type(carfunctions))
print(" ")
print(carfunctions.keys())
print(" ")
print(carfunctions.values())
print(" ")
print(carfunctions.get("engine"))
