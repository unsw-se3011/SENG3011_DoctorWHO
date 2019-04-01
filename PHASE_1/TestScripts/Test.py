import requests
from bs4 import BeautifulSoup
import json

# Testing for /article/{article_id}
def test_id(payload):
	r = requests.get('http://127.0.0.1:5000/article/{article_id}', params=payload)
	if r.status_code != 200:
		return str(r.status_code)
	else:
		return r.text

# Testing for /article
def test_article(payload):
	r = requests.get('http://http://127.0.0.1:5000/articles', params=payload)
	if r.status_code != 200:
		return str(r.status_code)
	else:
		return r.text

def count_articles(text):
	dic = json.loads(text)
	num = len(dic["articles"])
	return num

if __name__ == "__main__":	
	# Testing for /article/{article_id}
	# get article 0
	test1 = {'article_id':'0'}
	result1 = test_id(test1)
	num1 = count_articles(result1)
	assert num1 == 1
	print("**** TEST1 PASSED ****")
	
	# get article 1
	test2 = {'article_id':'1'}
	result2 = test_id(test2)
	num2 = count_articles(result2)
	assert num2 == 1
	print("**** TEST2 PASSED ****")

	# test if the api return different results
	assert result1 != result2
	print("**** TEST1.1 PASSED ****")

	# article not found
	test3 = {'article_id':'100'}
	result3 = test_id(test3)
	assert result3 == "404"
	print("**** TEST3 PASSED ****")

	# invalid input
	test4 = {'article_id':'abc'}
	result4 = test_id(test4)
	assert result4 == "400"
	print("**** TEST4 PASSED ****")

	# Testing for /article
	# start_date > end_date
	test5 = {'start_date':'2019-03-29Txx:xx:xx', 'end_date':'2019-03-28Txx:xx:xx'}
	result5 = test_article(test5)
	assert result5 == "400"
	print("**** TEST5 PASSED ****")
	
	# invalid format of the date
	test6 = {'start_date':'19.03.28', 'end_date':'19.03.29'}
	result6 = test_article(test6)
	assert result6 == "400"
	print("**** TEST6 PASSED ****")

	# date range bigger than the stored date range
	test7 = {'start_date':'2019-03-27Txx:xx:xx', 'end_date':'2019-04-01Txx:xx:xx'}
	result7 = test_article(test7)
	num7 = count_articles(result7)
	assert num7 >= 1
	print("**** TEST7 PASSED ****")

	# no articles of the chosen date range
	test8 = {'start_date':'2020-01-01Txx:xx:xx', 'end_date':'2020-01-02Txx:xx:xx'}
	result8 = test_article(test8)
	assert result8 == "404"
	print("**** TEST8 PASSED ****")

	# on just one day
	test9 = {'start_date':'2019-03-29T00:00:00','end_date':'2019-03-29T23:59:59'}
	result9 = test_article(test9)
	num9 = count_articles(result9)
	assert num9 >= 1
	print("**** TEST9 PASSED ****")
	
	# key_term doesn't exit (hospital doesn't exist)
	test10 = {'start_date':'2019-03-28Txx:xx:xx','end_date':'2019-03-29Txx:xx:xx','key_terms':'hopital'}
	result10 = test_article(test10)
	assert result10 == "404"
	print("**** TEST10 PASSED ****")

	# location doesn't exit
	test11 = {'start_date':'2019-03-28Txx:xx:xx','end_date':'2019-03-29Txx:xx:xx','location':'Toko'}
	result11 = test_article(test11)
	assert result11 == "404"
	print("**** TEST11 PASSED ****")

	# location invalid format
	test12 = {'start_date':'2019-03-28Txx:xx:xx','end_date':'2019-03-29Txx:xx:xx','location':'Tokyo, Shanghai'}
	result12 = test_article(test12)
	assert result12 == "404"
	print("**** TEST12 PASSED ****")
	
	# correct dates only
	test13 = {'start_date':'2019-03-28Txx:xx:xx','end_date':'2019-03-29Txx:xx:xx'}
	result13 = test_article(test13)
	num13 = count_articles(result13)
	assert num13 >= 1
	print("**** TEST13 PASSED ****")

	# correct without location1
	test14 = {'start_date':'2019-03-28Txx:xx:xx','end_date':'2019-03-29Txx:xx:xx','key_terms':'Ebola'}
	result14 = test_article(test14)
	num14 = count_articles(result14)
	assert num14 >= 1
	print("**** TEST14 PASSED ****")

	# correct without location2, to compare the results to see if they're different
	test14_1 = {'start_date':'2019-03-28Txx:xx:xx','end_date':'2019-03-29Txx:xx:xx','key_terms':'flu'}
	result14_1 = test_article(test14_1)
	assert result14 != result14_1
	print("**** TEST14.1 PASSED ****")

	# correct without key_term
	test15 = {'start_date':'2019-03-28Txx:xx:xx','end_date':'2019-03-29Txx:xx:xx','location':'America'}
	result15 = test_article(test15)
	num15 = count_articles(result15)
	assert num15 >= 1
	print("**** TEST15 PASSED ****")

	# correct full input1
	test16 = {'start_date':'2019-03-28Txx:xx:xx','end_date':'2019-03-29Txx:xx:xx','key_terms':'flu','location':'the United States'}
	result16 = test_article(test16)
	num16 = count_articles(result16)
	assert num16 >= 1
	print("**** TEST16 PASSED ****")

