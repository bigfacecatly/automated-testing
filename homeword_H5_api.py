import unittest
import requests
#共用cookies
cookies = {
    'gpsd': '58c77f60f399c27489339ca17badbddd',
    'JSESSIONID': 'C522CF7F8A791984ACBA5E5FEEC4E94C'}
class Index_Test(unittest.TestCase):
    def H5_index(self):
        #首页
        index = requests.get('http://dohko.m.hualala.com/online/store/stock/inventory?g=1155&groupID=1155&shopID=76067972')
        #print(index.text)
        self.assertEqual(index.status_code,200)
        self.assertIn('精气神',index.text)

class Stock_Test(unittest.TestCase):
    def H5_stock(self):
        # 商品分类页-全部商品
        stock = requests.get("http://dohko.m.hualala.com/online/store/stock/inventory?g=1155&shopID=76067972&groupID=1155",cookies=cookies)
        self.assertEqual(stock.status_code,200)
        self.assertIn("zj蔬菜1",stock.text)


class CategoryProduct_Test(unittest.TestCase):
    def H5_categoryProduct(self):
        #商品分类页--单一类型商品--水果
        categoryProduct = requests.get("http://dohko.m.hualala.com/online/store/shop/categoryProduct?g=1155&groupID=1155&shopID=76067972&pageNo=1&pageSize=10&orderBy=1&categoryID=10197493")
        #print(categoryProduct.text)
        self.assertEqual(categoryProduct.status_code,200)
        self.assertIn('高原红富士苹果',categoryProduct.text)

if __name__ == '__main__':
    print(1)
    suite = unittest.TestSuite()
    suite.addTest(Index_Test("H5_index"))                                 #首页
    suite.addTest(Stock_Test("H5_stock"))                                 # 商品分类页-全部商品
    suite.addTest(CategoryProduct_Test("H5_categoryProduct"))             #商品分类页--单一类型商品
    runner = unittest.TextTestRunner()
    runner.run(suite)
