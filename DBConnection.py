import pyodbc

class DbConnection:
    def __init__(self, DSN=''):
        self.dsn=DSN

    def getCursor(self):
        return self.cnxn

    def addProdReviewData(self,proddata):
        self.cnxn = pyodbc.connect(self.dsn)
        cursor = self.cnxn.cursor()
        #sqlnew="INSERT INTO customers (asin, product_title,rating,review_title,variation,review_text,review-links) VALUES (%s, %s)"
        for rows in proddata:
            #for col in rows:
            sql = "INSERT INTO amazon.product_reviews(asin,product_title)" \
                      "VALUES ('"+rows[0]+"','"+rows[1]+"');"
            number_of_rows = cursor.execute(sql)
        self.cnxn.commit()  # you need to call commit() method to save
        self.cnxn.close()
        print('Record has been added successfully')

if __name__ == '__main__':
    con=DbConnection('dsn=testDSN')
    l = [
        ['B075T1YTR9', "Lenovo Tab4 10 Tablet (10.1 inch,16GB,Wi-Fi + 4G LTE) Slate Black", 1.0, 'N/A',
         "Got the delivery on 26th August 2018 and since yesterday i.e; 16th September the tab stopped charging..very disappointed as this was a gift to my son and he is very very upset as the product cannot not be properly used for even a month. The return product window got closed on 5th September else would have returned it. Felt cheated"],
        ['B075T1YTR9', "Lenovo Tab4 10 Tablet (10.1 inch,16GB,Wi-Fi + 4G LTE) Slate Black", 1.0, 'N/A',
         "Got the delivery on 26th August 2018 and since yesterday i.e; 16th September the tab stopped charging..very disappointed as this was a gift to my son and he is very very upset as the product cannot not be properly used for even a month. The return product window got closed on 5th September else would have returned it. Felt cheated"],
        ]
    con.addProdReviewData(l)