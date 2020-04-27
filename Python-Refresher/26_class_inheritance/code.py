class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        # !r will give single quotes around the variable it's attached to
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print(f"{self.name!r} is disconnected.")


# printer = Device("Printer", "USB")
# print(printer)
# printer.disconnect()

# This is how to show inheritance in python
# In this case: Object Class(default) -> Device(ours) -> Printer(ours)
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # You can manually set the variables as normal, or call the parent class
        # self.name = name
        # self.connected_by = connected_by
        # self.connected = True
        # This calls init method on super(parent) class
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)

print(printer)

printer.disconnect()
printer.print(30)