# ==========================================
# 1. THE BASE CLASS
# ==========================================
class Vehicle:
    def __init__(self, motor_type, power_output):
        self.motor_type = motor_type              # e.g., "V8 Engine", "Dual Electric"
        self.power_output = power_output          # e.g., "300 HP", "500 HP"

    def standard_diagnostic(self):
        return f"System check: {self.motor_type} running at {self.power_output}."


# ==========================================
# APPROACH 1: Manual Assignment (No Core Code Reuse)
# Disadvantaged because it duplicates parent constructor logic manually.
# ==========================================
# class ElectricVehicle(Vehicle):
#     def __init__(self, motor_type, power_output, battery_capacity):
#         self.motor_type = motor_type
#         self.power_output = power_output
#         self.battery_capacity = battery_capacity


# ==========================================
# APPROACH 2: Explicit Parent Class Calling
# Functional, but brittle because it hardcodes the parent class name.
# ==========================================
# class ElectricVehicle(Vehicle):
#     def __init__(self, motor_type, power_output, battery_capacity):
#         Vehicle.__init__(self, motor_type, power_output)
#         self.battery_capacity = battery_capacity


# ==========================================
# APPROACH 3: Industry Best Practice Using super()
# Dynamic, clean, and optimally handles complex inheritance trees.
# ==========================================
class ElectricVehicle(Vehicle):
    def __init__(self, motor_type, power_output, battery_capacity):
        # Explicitly forwards required parameters to the parent constructor
        super().__init__(motor_type, power_output)
        self.battery_capacity = battery_capacity   # e.g., "85 kWh"

    def run_full_diagnostic(self):
        # Combines base class functionality with child class metrics
        base_log = super().standard_diagnostic()
        return f"{base_log} Battery charge status at {self.battery_capacity}."


# ==========================================
# EXECUTION & DEMONSTRATION
# ==========================================

print("--- Initializing Electric Vehicle Class ---")
my_ev = ElectricVehicle(motor_type="Dual Electric", power_output="450 HP", battery_capacity="100 kWh")
print(my_ev.run_full_diagnostic())
