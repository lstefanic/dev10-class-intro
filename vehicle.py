class Vehicle():
    """Vehicle class"""
    def __init__(self,make,model,year):
        self._make = make
        self._model = model
        self._year = year
    
    def start(self):
        print("Starting")
    
    def stop(self):
        print("Stopping")