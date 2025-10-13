class ClimateController:
    def __init__(self, comfort_level):
        self.comfort_level = comfort_level
        self.previous_state = None

    def get_temperature(self, current_reading):
        self.current_reading = current_reading

    def control_logic(self):
        if self.current_reading < self.comfort_level:
            state = "Heating Enabled"
        else:
            state = "Heating Disabled"
        if state == self.previous_state:
            state = "No Change (Maintain Status)"
        else:
            self.previous_state = state

        return state

    def operate_heater(self):
        decision = self.control_logic()
        print(f"{self.current_reading}°C => {decision}")
house_temperatures = {
    "Living Area": 20,
    "Guest Suite": 22,
    "Cooking Zone": 25,
    "Master Bedroom": 19,
    "Washroom": 22,
}
climate_system = ClimateController(comfort_level=22)
for area, temperature in house_temperatures.items():
    print(f"{area}:\t", end="")
    climate_system.get_temperature(temperature)
    climate_system.operate_heater()
