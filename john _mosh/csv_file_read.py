import csv

ticket_dict = {}

with open("/home/loki/Downloads/Hyperlocal Support Master Sheet - Ticket_work_sheet.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)  # Reads with column names
    
    for row in reader:
        ticket_id = row["Ticket ID"]   # adjust name exactly as in CSV header
        subject = row["Subject"]       # adjust name exactly as in CSV header
        ticket_dict[ticket_id] = subject
    print(ticket_dict)    

# Print the dictionary
# for k in ticket_dict:
#     print(k, ":", ticket_dict[k])
