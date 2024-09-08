import csv
import hashlib
import sys
def anonymize1(inputs, outputs):
    def anonymize(value):
        return hashlib.sha256(value.encode('utf-8')).hexdigest()
    with open(inputs, 'r', encoding='utf-8') as infile, open(outputs, 'w', newline='', encoding='utf-8') as outfile:
        data = csv.DictReader(infile)
        cols = data.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=cols)
        writer.writeheader()
        for row in data:
            row['first_name'] = anonymize(row['first_name'])
            row['last_name'] = anonymize(row['last_name'])
            row['address'] = anonymize(row['address'])
            writer.writerow(row)
if __name__ == "__main__":
    args=sys.argv
    anonymize1(args[1], args[2])
