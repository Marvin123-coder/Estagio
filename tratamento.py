import csv
with open('ranking.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    vetor = list(csv_reader)
    for row in vetor:
        if "Æ" in row[2]:
            row[2] = row[2].replace("Æ","ã")
        if "£" in row[2]:
            row[2] = row[2].replace("£","ú")
        if "¡" in row[2]:
            row[2] = row[2].replace("¡","í")
        if "¢" in row[2]:
            row[2] = row[2].replace("¢","ó")
        if "‚" in row[2]:
            row[2] = row[2].replace("‚","é")
        if "ˆ" in row[2]:
            row[2] = row[2].replace("ˆ","ê")
        if "\xa0" in row[2]:
            row[2] = row[2].replace("\xa0","á")

with open('ranking_novo.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=';', lineterminator = '\n')
    
    for row in vetor:
        employee_writer.writerow([row[0],row[2],row[1],row[3],row[11]])