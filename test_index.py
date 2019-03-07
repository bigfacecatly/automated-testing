

import unittest
import time
import requests
from HTMLTestRunner import HTMLTestRunner
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


class Seckill_Test(unittest.TestCase):
    def H5_seckill(self):
        #秒杀订单页
        #秒杀需要User-Agent跟cookies 其中cookies是手机号通过微信验证过后的cookies
        headers={
            "User-Agent":"MicroMessenger / 6.6.6.1300(0x26060632)",
            "Cookie":"COOKIES_SESSION_ID=9B3EEF7C31EECA3AC5B3023924CB6554; dynamic_code_session=6f62e77b-c630-493c-b750-e36b077fb630; "
                     "access_token=2fd2159f-b7c3-4fe8-9880-ae81cddbb888; gpsd = 500e6bb5067b5dad637474d58e6a0f22; "
                     "JSESSIONID = B35994F3097E3F4069E3E3DFA72AD45D"}


        seckill = requests.get('http://dohko.m.hualala.com/online/store/seckill/seckillPrdouctList?g=1155&groupID=1155&shopID=76067972',headers=headers)
        self.assertEqual(seckill.status_code,200)
        #print(seckill.text)
        self.assertIn("千里山",seckill.text)



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



    def H5_seckillShopping(self):
        #商品购物车,前端写死后，给后端提供
        pass

if __name__ == '__main__':
    print(1)
    suite = unittest.TestSuite()
    suite.addTest(Index_Test("H5_index"))                                 #首页
    suite.addTest(Seckill_Test("H5_seckill"))                             #秒杀订单页
    suite.addTest(Stock_Test("H5_stock"))                                 # 商品分类页-全部商品
    suite.addTest(CategoryProduct_Test("H5_categoryProduct"))             #商品分类页--单一类型商品


    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = now + '_result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='H5微商城接口自动化测试报告',description='Implementation Example with:')
    #runner = unittest.TextTestRunner()
    runner.run(suite)
    fp.close()



