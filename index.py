# with open('vps_data.txt', 'r') as file:
#     lines = file.readlines()

# # Skipping the first line as it contains the headers
# for index, line in enumerate(lines[1:]):
#     values = line.strip().split()
#     if len(values) >= 3:
#         hostname, ip, due_date, month, day, year = values[:6]
#         print("index:", index + 1)
#         print("Hostname:", hostname)
#         print("IP:", ip)
#         dayMonthYear = day.replace(',', '') + "-" + month + "-" + year
#         print("day-month-Year:", dayMonthYear)
#         print()



# from datetime import datetime
# from dateutil import parser

# with open('vps_data.txt', 'r') as file:
#     lines = file.readlines()

# # Skipping the first line as it contains the headers
# for index, line in enumerate(lines[1:]):
#     values = line.strip().split()
#     if len(values) >= 3:
#         hostname, ip, due_date, month, day, year = values[:6]
#         print("index:", index + 1)
#         print("Hostname:", hostname)
#         print("IP:", ip)
#         dayMonthYear = day.replace(',', '') + " " + month + " " + year
#         print("dayMonthYear:", dayMonthYear)
#         date_obj = parser.parse(dayMonthYear)
#         numeric_date = date_obj.strftime("%m/%d/%Y")
#         print("Numeric date:", numeric_date)
#         print()


from datetime import datetime, date
from dateutil import parser, relativedelta

with open('vps_data.txt', 'r') as file:
    lines = file.readlines()

# Skipping the first line as it contains the headers
for index, line in enumerate(lines[1:]):
    values = line.strip().split()
    if len(values) >= 3:
        hostname, ip, due_date, month, day, year = values[:6]
        print("index:", index + 1)
        print("Hostname:", hostname)
        print("IP:", ip)
        dayMonthYear = day.replace(',', '') + " " + month + " " + year
        print("dayMonthYear:", dayMonthYear)
        date_obj = parser.parse(dayMonthYear)

        # Format the date as desired (e.g., day-month-Year)
        formatted_date = date_obj.strftime("%d-%m-%Y")
        print("Formatted date:", formatted_date)


        print()
