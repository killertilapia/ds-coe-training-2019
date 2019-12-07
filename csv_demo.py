import os
import csv

def main():
    src_path = os.path.join(os.getcwd(), 'ds', 'ds_parts_inductors.csv')
    write_path = os.path.join(os.getcwd(), 'ds', 'clean_parts.csv')

    # read csv
    with open(src_path, mode='r') as src_csv:
        with open(write_path, mode='w', encoding='utf-8') as write_file:
            reader = csv.reader(src_csv)
            writer = csv.writer(write_file)

            for idx, line in enumerate(reader):
                if idx == 10:
                    break
                
                print(" ".join(line))
                
                # process line here

                writer.writerows(line)

if __name__ == "__main__":
    main()