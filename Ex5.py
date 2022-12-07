import csv

csv_file = r"C:\Users\nhanthanhhuynh\Desktop\NhanHuynh\VPF_Training\Python Code\data.csv"
new_file = "new.csv"

class Data():
    def __init__(self):
        self.file = []

    def prepare_data(self, data):
        with open(data, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == '0x200':
                    continue
                else:
                    self.file.append(row)
        
    def write_csv(self):
        with open(new_file,'w',newline='') as file:
            new = csv.writer(file)
            new.writerows(self.file)           
def main():   
    file = Data()
    file.prepare_data(csv_file)
    file.write_csv()
main()