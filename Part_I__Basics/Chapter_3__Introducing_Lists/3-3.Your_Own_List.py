mode_transportation = ['bycicle', 'motorcycle', 'car', 'plane', ]

message_byci = f"I don't know how to ride a {mode_transportation[0]}."
message_motor = f"I really hate {mode_transportation[1]}s."
message_car = f"{mode_transportation[2].capitalize()}s are the beast mode of transportation."
message_plane = f"I have only been on a {mode_transportation[-1]} once."

print(message_byci)
print(message_motor)
print(message_car)
print(message_plane)