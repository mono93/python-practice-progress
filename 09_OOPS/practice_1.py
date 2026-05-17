class SmartDevice:
    brand = "HomeTech"
    def __init__(self, device_name, power_status):
        self.device_name = device_name
        self.power_status = power_status
        self.brand = "CustomBrand"

    def get_status(self):
        return f"{self.device_name} is {'ON' if self.power_status else 'OFF'} - {self.brand}"