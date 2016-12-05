# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:03:03 2016

@author: ERS'S
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 05 14:21:27 2016

@author: ERS'S
"""


from selenium import webdriver
import xlsxwriter

workbook = xlsxwriter.Workbook('excelfile.xlsx')
worksheet1 = workbook.add_worksheet()
worksheet1.set_column(0, 0, 400)
worksheet1.set_column(0, 1, 800)
worksheet1.set_column(0, 2, 20)
worksheet1.set_column(0, 3, 20)


bold = workbook.add_format({'bold': True})
cell_format = workbook.add_format({'bold': False, 'italic': True})

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.nur.kz/1276590-rypakova-stala-pervoy-v-istorii-kazakh.html")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

authors = driver.find_elements_by_xpath('/html/body/section[2]/div[2]/section/div[7]/div[2]/ul/li/div[1]/span[1]')
comments = driver.find_elements_by_xpath('/html/body/section[2]/div[2]/section/div[7]/div[2]/ul/li/div[2]/div[1]')
likes = driver.find_elements_by_xpath('/html/body/section[2]/div[2]/section/div[7]/div[2]/ul/li/div[1]/span[3]/div[1]/span[1]')



for i in range(0, 20):
	for j in range(0, 20):
		if i==0:
			if j==0:
				worksheet1.write(i, j, "Авторы", bold)
			if j==1:
				worksheet1.write(i, j, "Комментарий", bold)
			if j==2:
				worksheet1.write(i, j, "Нравится", bold)
		else:
			if   j==0:
				worksheet1.write(i, j, authors[i].text, cell_format)
			elif j==1:
				worksheet1.write(i, j, comments[i].text, cell_format)
			elif j==2:
				worksheet1.write(i, j, likes[i].text, cell_format)


workbook.close()
