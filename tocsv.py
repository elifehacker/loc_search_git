import csv
with open('emails_batch4_filtered.txt', 'r') as opened_file:
	arr = opened_file.readline().split(';')
	with open('b1.csv', 'a', newline='') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(["Email"])
		for email in arr:
			writer.writerow([email])
			