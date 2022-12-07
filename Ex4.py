#file_csv = r'C:\Users\nhanthanhhuynh\Desktop\NhanHuynh\VPF_Training\data.csv'
import csv
def ReadCSV(file_csv):
    with open(file_csv,'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        if header != None:
            i = 0
        for row in reader:
            i += 1
            if(i <= 2):
                print(f'\t{row[0]} {row[1]} {row[2]} {row[3]}')
            else:
                break
def main():
    content = ReadCSV(r'C:\Users\nhanthanhhuynh\Desktop\NhanHuynh\VPF_Training\Python Code\data.csv')
    #print(content)
main()