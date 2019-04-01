import requests
from bs4 import BeautifulSoup

# Testing for /article/{article_id}
def test_id(payload):
	r = requests.get('http://doctorwhoseng.tk/swagger.json/article/{article_id}', params=payload)
	if r.status_code != 200
		return r.status_code
	else:
		return r.text

# Testing for /article
def test_article(payload):
	r = requests.get('http://doctorwhoseng.tk/swagger.json/articles', params=payload)
	if r.status_code != 200
		return r.status_code
	else:
		return r.text

def count_articles(text)：
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
	test5 = {'start_date':'2019-03-29', 'end_date':'2019-03-28'}
	result5 = test_article(test5)
	assert result5 == "400"
	print("**** TEST5 PASSED ****")
	
	# invalid format of the date
	test6 = {'start_date':'19.03.28', 'end_date':'19.03.29'}
	result6 = test_article(test6)
	assert result6 == "400"
	print("**** TEST6 PASSED ****")

	# date range bigger than the stored date range
	test7 = {'start_date':'2019-03-27', 'end_date':'2019-04-01'}

	# no articles of the chosen date range
	test8 = {'start_date':'2020-01-01', 'end_date':'2020-01-02'}

	# on just one day
	test9 = {'start_date':'2019-03-29','end_date':'2019-03-29'}
	
	# key_term doesn't exit (hospital doesn't exist)
	test10 = {}
	# location doesn't exit
	
	# correct dates only
	# correct without location
	# correct without key_term
	# correct input1
	# correct input2
	# correst input3
