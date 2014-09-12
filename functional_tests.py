# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitortest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #用户打开网站，localhost:8000
        self.browser.get('http://localhost:8000')
        #用户发现网站的title以及header上面写着To-Do
        self.assertIn('To-Do',self.browser.title)
    
        #用户被要求在文本框中输入一个to-do项目
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        #用户输入"buy peacock feathers"
        inputbox.send_keys('buy peacock feathers')

        #用户输入enter后，页面跳转，页面显示"1: buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: buy peacock feathers' for row in rows),
                "New to-do item did not appear in the table -- its text was:\n%s" % (table.text,)
        )

        #这里仍然有个文本框用于第二个to-do项目的输入，用户继续输入"use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        #用户输入enter后页面跳转，页面显示两个之前用户输入的to-do项目
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: buy peacock feathers', [ row.text for row in rows ])
        self.assertIn('2: use peacock feathers to make a fly',
                [row.text for row in rows]
        )
        #用户需要单独的list url

        #用户输入独立的url，能够看到自己之前的to-do项目list


if __name__ == '__main__':
    unittest.main(warnings='ignore')
