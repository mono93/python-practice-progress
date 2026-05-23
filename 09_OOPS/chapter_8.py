# ==========================================
# 1. THE BASE CLASS
# ==========================================
class Device:
    def boot_up(self):
        print("[Device] Powering on core components...")


# ==========================================
# 2. THE MIDDLE PARENT CLASSES (Siblings)
# ==========================================
class Camera(Device):
    def boot_up(self):
        print("[Camera] Calibrating camera lens...")
        super().boot_up()  # Passes control to the next class in MRO line


class Speaker(Device):
    def boot_up(self):
        print("[Speaker] Testing audio frequencies...")
        super().boot_up()  # Passes control to the next class in MRO line


# ==========================================
# 3. THE CHILD CLASS (Multiple Inheritance)
# Look closely at the order: Camera comes BEFORE Speaker
# ==========================================
class SmartDisplay(Camera, Speaker):
    def boot_up(self):
        print("[SmartDisplay] Initializing touchscreen interface...")
        super().boot_up()  # Begins the MRO chain traversal


# ==========================================
# 4. TESTING AND INSPECTING THE MRO
# ==========================================

print("=== 1. Executing the Boot Sequence ===")
hub = SmartDisplay()
hub.boot_up()

print("\n=== 2. Inspecting the True Lookup Path (MRO) ===")
# Two ways to view the execution array order:
for index, class_obj in enumerate(SmartDisplay.__mro__, start=1):
    print(f"Path Step {index}: {class_obj.__name__}")

