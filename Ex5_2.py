import csv

new = []
newfile = []
csv_file = r"C:\Users\nhanthanhhuynh\Desktop\NhanHuynh\VPF_Training\Python Code\data.csv"
class Data():
    def __init__(self):
        self.open = csv_file

    def prepare_data(self, data):
        with open(data, newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                if row[1] == '0x200':
                    continue
                else:
                    new.append(row)
        return new
    #def write_csv(self):
        #with open('new_file.csv','w') as newfile:
        #    writer = csv.writer(newfile)
        #    writer.writerow(newfile)
        #return newfile
file = Data()
print(file.prepare_data(csv_file))
#print(file.write_csv())