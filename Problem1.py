import json
import sys
def parsing(inputs, specs, outputs):
    with open(specs, 'r') as f:
        spec = json.load(f)
    column_names = spec["ColumnNames"]
    offsets = list(map(int, spec["Offsets"]))
    encoding = spec["FixedWidthEncoding"]
    include_header = spec.get("IncludeHeader", "False").lower() == "true"
    delimiter_encoding = spec["DelimitedEncoding"]
    with open(inputs, 'r', encoding=encoding) as inf, open(outputs, 'w', encoding=delimiter_encoding) as outf:
        if include_header:
            outf.write(','.join(column_names) + '\n')
        for line in inf:
            start = 0
            row = []
            for offset in offsets:
                field = line[start:start + offset].strip()
                row.append(field)
                start += offset
            outf.write(','.join(row) + '\n')
if __name__ == "__main__":
    args=sys.argv
    parsing(args[1], args[2], args[3])
