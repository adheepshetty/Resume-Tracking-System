import urllib.request
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json
import threading
from random import randint
from time import sleep
import os
from kafka import KafkaProducer
import json

class Resume(object):

	def __init__ (self, idd, jobs, schools):
		self._id = idd
		self.jobs = jobs
		self.schools = schools

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, 
			sort_keys=True, indent=0)


class Job(object):
	def __init__(self, title, company, location, hire_date):
		self.title = title
		self.company = company
		self.location = location
		self.hire_date = hire_date

class School(object):
	def __init__(self, degree, school_name, grad_date):
		self.degree = degree
		self.school_name = school_name
		self.grad_date = grad_date


def gen_idds(url, driver):
	driver.implicitly_wait(50)
	driver.get(url)
	wait = WebDriverWait(driver, 20)
	element = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "rezemp-u-h4")))
	p_element = driver.page_source
	soup = BeautifulSoup(p_element, 'html.parser')
	print(soup)
	links = soup.find_all(class_="icl-TextLink icl-TextLink--primary rezemp-u-h4")
	idds=[]

	for link in links:
		path = link.get("href")
		#print(path[8:path.find("?")]) #8 is to account for "\resume\" at the beginning
		idds.append(path[8:path.find("?")])

	return idds
#print(idds)

def gen_resume(idd, driver):
	URL = '''https://resumes.indeed.com/resume/''' + idd


	driver.get(URL)
	p_element = driver.page_source
	soup = BeautifulSoup(p_element, 'html.parser')

	results = soup.find_all('div', attrs={"class":"rezemp-ResumeDisplaySection"})

	schools = []

	try:
		education = results[1]
		content = education.find(class_="rezemp-ResumeDisplaySection-content")
		for uni in content.children:
			degree = uni.find(class_ = "rezemp-ResumeDisplay-itemTitle").get_text()
			university = uni.find(class_="rezemp-ResumeDisplay-university").contents[0].get_text()
			date = uni.find(class_="rezemp-ResumeDisplay-date").get_text()
			schools.append(School(degree, university, date))
	except:
		pass

	jobs = []
	
	try:
		work_experience = results[0]
		job_titles = work_experience.find_all(class_="rezemp-u-h4")
		job_descriptions = work_experience.find_all(class_="rezemp-u-h5")
		for i in range(len(job_titles)):
			dates = job_descriptions[i].find_next_sibling().get_text()
			date = dates[:dates.find("to")]
			title = job_titles[i].get_text()
			desc = [p.get_text() for p in job_descriptions[i].find_all("span")][1:]
			company = desc[0]
			location = desc[1]
			jobs.append(Job(title, company, location, date))
	except:
		pass

	return Resume(idd, jobs, schools)



def mine(name, URL, override=True, rangee=None):
	driver = webdriver.Chrome('/Users/rajanpatel/Documents/selected_project/resume-scraper/chromedriver')
	driver.implicitly_wait(10)
	#producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
	
	if(override):
		with open('resume_output' + name + '.json', 'w') as outfile:
			outfile.write("")


	if rangee == None:	
		start_index = 700
		target = 10901
	else:
		start_index = rangee[0]
		target = rangee[1]


	print(start_index, target)

	while 1:
		if (start_index >= target):
			break
		
		stri = URL+"&start="+str(start_index)
		print(stri)
		# wait = WebDriverWait(driver, 20)
		# element = wait.until(EC.presence_of_all_elements_located())
		idds = gen_idds(URL+"&start="+str(start_index), driver)
		start_index+=50
		print(start_index)
		print(idds)
		if(len(idds) == 0):
			time.sleep(4)
			continue
		for idd in idds:
			print("sending....")
			print(json.loads(gen_resume(idd, driver).toJSON()))
			#producer.send('test', json.loads(gen_resume(idd, driver).toJSON()))
	driver.close()


def mine_multi(name, url, override=True):

	thread_list = []
	names = []

	target = 8000
	tr = 1
	for i in range(tr):
		# Instantiates the thread
		# (i) does not make a sequence, so (i,)
		t = threading.Thread(target=mine, args=(name+str(i),url,), kwargs={"override" : override, "rangee" : (i*(target//tr), (i+1)*(target//tr)),})
		# Sticks the thread in a list so that it remains accessible
		thread_list.append(t)
		names.append("resume_output" + name + str(i) +".json")

	# Starts threads
	for thread in thread_list:
		thread.start()

	# This blocks the calling thread until the thread whose join() method is called is terminated.
	# From http://docs.python.org/2/library/threading.html#thread-objects
	for thread in thread_list:
		thread.join()


def main():

	URL = "https://resumes.indeed.com/search?l=california&q=software%20engineer&searchFields="

	mine_multi("doctor-california", URL)



main()
