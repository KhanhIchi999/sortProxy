import re
from datetime import datetime, date
from dateutil import parser, relativedelta

with open('vps_data.txt', 'r') as file:
    lines = file.readlines()

# Skipping the first line as it contains the headers
data = []
unsorted_data = []

for index, line in enumerate(lines[1:]):
    print("index: ", index + 1)
    values = line.strip().split()
    if len(values) >= 3:
        hostname, ip, due_date, month, day, year = values[:6]

        dayMonthYear = day.replace(',', '') + " " + month + " " + year
        date_obj = parser.parse(dayMonthYear)
        formatted_date = date_obj.strftime("%d-%m-%Y")
        print("dayMonthYear:", formatted_date)

        match = re.search(r'(?:V|v)ilas(\d+)', hostname)
        if match:
            number = int(match.group(1))
            data.append((hostname, ip, formatted_date, number))
        else:
            unsorted_data.append((hostname, ip, formatted_date))

# Sort the data by the numbers after "Vilas" or "vilas" in ascending order
sorted_data = sorted(data, key=lambda x: x[3])

print("The unsorted_data is: ", unsorted_data)
with open('resultSort.txt', 'w') as output_file:
    output_file.write("Hostname                 IP                 Next Due Date\n")
    for result in sorted_data:
        hostname, ip, formatted_date, _ = result
        output_file.write("{:<24} {:<19} {:<13}\n".format(hostname, ip, formatted_date))
    for result in unsorted_data:
        hostname, ip, formatted_date = result[:3]  # Unpack three values
        
        output_file.write("{:<24} {:<19} {:<13}\n".format(hostname, ip, formatted_date))

# Print the sorted data
# for item in sorted_data:
#     hostname, ip, due_date, number = item
#     print("index: ", index + 1)
#     print("Hostname:", hostname)
#     print("IP:", ip)
#     print("Next Due Date:", due_date)
#     print()
