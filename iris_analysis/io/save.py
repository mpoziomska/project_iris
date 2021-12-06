import csv

def save(save_path, data):
	with open(save_path, 'w', newline='') as f:
	    writer = csv.writer(f)
	    writer.writerows(data)