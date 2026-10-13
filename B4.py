#B4
#continous discharge analysis
voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8,
            11.6, 11.5, 11.5, 11.2]

longest_length = 1
current_length = 1
longest_start = voltages[0]
longest_end = voltages[0]
current_start = voltages[0]

for index in range(1, len(voltages)):
    if voltages[index] < voltages[index - 1]:
        current_length += 1
    else:
        current_length = 1
        current_start = voltages[index]

    if current_length > longest_length:
        longest_length = current_length
        longest_start = current_start
        longest_end = voltages[index]

print("Longest continuous drop:", longest_length, "readings")
print("Started at:", longest_start, "V")
print("Ended at:", longest_end, "V")
