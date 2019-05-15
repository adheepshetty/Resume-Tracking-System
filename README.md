# Resume-Tracking-System
The main idea of this project is to keep track large number of resumes, here “large” means not in hundreds or thousands but in millions of resumes. To handle such a large amount of data we will be using new emerging technologies like Mongo and Kafka which will provide an effective and faster way to store and stream data and at the final result of the project, we have provided best data visualization user interface to track and easy search control over information.

# Teammates
<ul>
<li> Rajan Patel
<li> Suraj Nair
</ul>

# Description
Resume analyser is a dashboard consisting of visualizations which have been
made to fulfil the need of recruiters or companies who are looking for right candidate
which are perfectly fit in job description. It helps the recruiters to get exact count of
people who are currently working for a particular company. If the user wants to hire
applicants only from a certain university they can have a look at count of how many
graduated from that university and can decide accordingly what percentage of
students can be picked from that university.
While creating visualizations we have taken into consideration all the possible
cases that could prove helpful to a recruiter. Thus this dashboard proves to be a
great source of information for the recruiters and serves its purpose.
However, while scraping the data it was found to contain certain anomalies
and not uniform. So this scraped data from indeed.com it would not be of any use if it
would not have been manipulated or analysed by us. So we made sure that data is
uniform before we start using it, to get most out of data.

# Technology Used

We have research many different and most latest technologies, and choose right one
which give maximum benefit for this project. Technologies we used to build this
project are.
<ul>
<li>Data collection - Web scraping using python.
<ul>
<li> Beautifulsoup.
<li> Selenium.
<li> Threading.
</ul>
<li> Data Streaming - Apache Kafka.
<li> Data Storage - Mongodb.
<li> Data visualization - Tableau.
</ul>

# Project System Design
![alt text](https://github.com/adheepshetty/Resume-Tracking-System/blob/master/project_images/systdesign.PNG)

# 1st Viz
This sheet showcases a barchart containing information of distinct count
of the resume which has been differentiated on the company work history of all the
applicants.
![alt text](https://github.com/adheepshetty/Resume-Tracking-System/blob/master/project_images/companyvsresume.PNG)

# 2nd Viz
This sheet shows a bubble graph containing information of distinct count of
the resume which has been differentiated on the basis of their university.
![alt text](https://github.com/adheepshetty/Resume-Tracking-System/blob/master/project_images/univvsresume.PNG)

# 3rd Viz
This sheet showcases a barchart containing information of distinct count of
the resume which has been differentiated on the basis of the job title of the
applicants.
![alt text](https://github.com/adheepshetty/Resume-Tracking-System/blob/master/project_images/jobfield_resume.PNG)


# Project Results
A dashboard is a culmination of these sheets and we have created a dashboard of
our sheets and published them on the Tableau Public Server wherein anyone can
view and check out the results.
Dashboard view:
https://public.tableau.com/profile/suraj.nair1535#!/vizhome/Resumeactivitytracker/Da
shboard1?publish=yes



