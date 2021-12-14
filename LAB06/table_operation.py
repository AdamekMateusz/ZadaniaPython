import pandas as pd
import os

class CarSeler():
    def __init__(self,filename):
        self.columns_name = ['Brand', 'Model', 'Engine Size', 'Fuel','Drive Train']
        print("Welcome in Car Selers Record")
        self.filename = filename
        self.df = self.open_csv(self.filename)
        self.main_menu()


    def open_csv(self,filename):
        if os.path.isfile(filename):
            df = pd.read_csv(filename,index_col=0)
            return df
        else:
            df = pd.DataFrame(columns=self.columns_name)
            return df

    def save_to_file(self,df):
        df.to_csv(r'seller_car.csv', index = True, header = True)

    def insert_into(self,df):
        record = []
        columns_name = self.columns_name
        for item in columns_name:
            data = input(f'Get {item}: ')
            record.append(data)

        df = df.append({columns_name[0]: record[0], columns_name[1]: record[1],columns_name[2]: record[2],columns_name[3]: record[3], columns_name[4]: record[4] }, ignore_index=True)
        print(df)
        self.save_to_file(df)
        return df

    def delete_record(self,df,index):
        max_index = self.df.index[-1]
        if index > max_index:
            print("Index out of range")
            self.main_menu()
        else:
            df = df.drop(index)
            self.save_to_file(df)
            print(df)
            return df

    def main_menu(self):
        print('\n*********************')
        print('1. Print Records')
        print('2. Add Records')
        print('3. Delete Records')
        print('4. Save Records')
        print('5. Exit')
        value = int(input("Get number from 1 - 5 :"))
        if value < 1 or value > 5:
            self.main_menu()
        else:
            if value == 1:
                print(self.df)
                self.main_menu()
            elif value == 2:
                self.df = self.insert_into(self.df)
                self.main_menu()
            elif value == 3:
                index_record = int(input('Which record delte: '))
                self.df = self.delete_record(self.df, index_record)
                self.main_menu()
            elif value == 4:
                self.save_to_file(self.df)
                self.main_menu()
            elif value == 5:
                exit(0)
        

if __name__ == '__main__':

    car = CarSeler('seller_car.csv')

