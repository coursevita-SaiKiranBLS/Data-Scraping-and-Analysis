# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager
# # from bs4 import BeautifulSoup
# # import time
# # import firebase_admin
# # from firebase_admin import credentials
# # from firebase_admin import firestore
# # import json

# # # Initialize Firebase
# # cred = credentials.Certificate("web-scrape-3dee8-firebase-adminsdk-osug0-8326fa4e7e.json")
# # firebase_admin.initialize_app(cred)
# # db = firestore.client()

# # # Initialize Selenium WebDriver
# # service = Service(ChromeDriverManager().install())
# # driver = webdriver.Chrome(service=service)

# # def get_url():
# #     try:

# #         Jobs,_ref = db.collection('Jobs,').stream()
# #         print("Retrieved job data from Firestore successfully.")
# #         for doc in Jobs,_ref:
# #             job_data = doc.to_dict()
# #             url = job_data.get("url")
# #             print("check")
# #             if url:
# #                 print("Scraping data from URL:", url)
# #                 scrape_job_data(url)
# #     except Exception as e:
# #         print("Error:", e)
        
# # def update_firebase(job_data):
# #     try:
# #         db.collection('analysis').add(job_data)
# #         print("Job data added to Firestore successfully.")
# #     except Exception as e:
# #         print("Error adding job data to Firestore:", e)
  


# # def scrape_job_data(url):
# #     driver.get(url)
# #     time.sleep(10)
# #     soup = BeautifulSoup(driver.page_source, 'html.parser')
    
# #     script_tags = soup.find_all('script')
    
# #     try:
# #         for script_tag in script_tags:
# #             if script_tag.get('type') == "application/ld+json":
# #                 json_data = json.loads(script_tag.text)
# #                 if json_data["@type"] == "JobPosting":
# #                     items = json_data["itemListElement"]
# #                     for item in items:
# #                         job_data = {
# #                             "title": item.get("title", ""),
# #                             "description": item.get("description", ""),
# #                             "identifier": item.get("identifier", {}).get("value", ""),
# #                             "datePosted": item.get("datePosted", ""),
# #                             "validThrough": item.get("validThrough", ""),
# #                             "qualifications": item.get("qualifications", {}).get("educationalLevel", ""),
# #                             "experienceRequirements": item.get("experienceRequirements", {}).get("monthsOfExperience", ""),
# #                             "occupationalCategory": item.get("occupationalCategory", ""),
# #                             "responsibilities": item.get("responsibilities", ""),
# #                             "industry": item.get("industry", ""),
# #                             "skills": item.get("skills", []),
# #                             "specialCommitments": item.get("specialCommitments", ""),
# #                             "workHours": item.get("workHours", ""),
# #                             "employmentType": item.get("employmentType", ""),
# #                             "hiringOrganization": item.get("hiringOrganization", {}).get("name", ""),
# #                             "logo": item.get("hiringOrganization", {}).get("logo", ""),
# #                             "jobLocation": item.get("jobLocation", {}).get("address", {}).get("addressLocality", [""])[0],
# #                             "postalCode": item.get("jobLocation", {}).get("address", {}).get("postalCode", ""),
# #                             "streetAddress": item.get("jobLocation", {}).get("address", {}).get("streetAddress", [""])[0],
# #                             "addressRegion": item.get("jobLocation", {}).get("address", {}).get("addressRegion", [""])[0],
# #                             "addressCountry": item.get("jobLocation", {}).get("address", {}).get("addressCountry", ""),
# #                             "baseSalary": item.get("baseSalary", {}).get("value", {}).get("value", ""),
# #                             "currency": item.get("baseSalary", {}).get("value", {}).get("currency", ""),
# #                             "unitText": item.get("baseSalary", {}).get("value", {}).get("unitText", "")
# #                         }
                      
# #                         update_firebase(job_data)

# #     except Exception as e:
# #         print("Error:", e)


# # driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.api_core.retry import Retry
import json

# Initialize Firebase
cred = credentials.Certificate("web-scrape-3dee8-firebase-adminsdk-osug0-8326fa4e7e.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Initialize Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def update_firebase(job_data):
    try:
        db.collection('analysis').add(job_data)
        print("Job data added to Firestore successfully.")
    except Exception as e:
        print("Error adding job data to Firestore error updating:", e)

def scrape_job_data(url):
    driver.set_page_load_timeout(60) 

    try:
        driver.get(url)
        time.sleep(10)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        script_tags = soup.find_all('script')
        for script_tag in script_tags:
            if script_tag.get('type') == "application/ld+json":
                json_data = json.loads(script_tag.text)
                if json_data.get("@type") == "JobPosting":
                    job_data = {
                        "title": json_data.get("title", ""),
                        "description": json_data.get("description", ""),
                        "identifier": json_data.get("identifier", {}).get("value", ""),
                        "datePosted": json_data.get("datePosted", ""),
                        "validThrough": json_data.get("validThrough", ""),
                        "qualifications": json_data.get("qualifications", {}).get("educationalLevel", ""),
                        "experienceRequirements": json_data.get("experienceRequirements", {}).get("monthsOfExperience", ""),
                        "occupationalCategory": json_data.get("occupationalCategory", ""),
                        "responsibilities": json_data.get("responsibilities", ""),
                        "industry": json_data.get("industry", ""),
                        "skills": json_data.get("skills", []),
                        "specialCommitments": json_data.get("specialCommitments", ""),
                        "workHours": json_data.get("workHours", ""),
                        "employmentType": json_data.get("employmentType", ""),
                        "hiringOrganization": json_data.get("hiringOrganization", {}).get("name", ""),
                        "logo": json_data.get("hiringOrganization", {}).get("logo", ""),
                        "jobLocation": json_data.get("jobLocation", {}).get("address", {}).get("addressLocality", [""])[0],
                        "postalCode": json_data.get("jobLocation", {}).get("address", {}).get("postalCode", ""),
                        "streetAddress": json_data.get("jobLocation", {}).get("address", {}).get("streetAddress", [""])[0],
                        "addressRegion": json_data.get("jobLocation", {}).get("address", {}).get("addressRegion", [""])[0],
                        "addressCountry": json_data.get("jobLocation", {}).get("address", {}).get("addressCountry", ""),
                        "baseSalary": json_data.get("baseSalary", {}).get("value", {}).get("value", ""),
                        "currency": json_data.get("baseSalary", {}).get("value", {}).get("currency", ""),
                        "unitText": json_data.get("baseSalary", {}).get("value", {}).get("unitText", "")
                    }
                    update_firebase(job_data)

    except Exception as e:
        print("Error+data adding:", e)

def get_url():
    try:
        retry = Retry()
        Jobs,_ref = db.collection('Jobs,').stream(retry=retry)
        print("Retrieved job data from Firestore successfully.")
        for doc in Jobs,_ref:
            job_data = doc.to_dict()
            print(job_data)
            url = job_data.get("url")
            print(url)
            if url:
                print("Scraping data from URL:", url)
                try:
                    scrape_job_data(url)
                except TimeoutException:
                    print("Timeout occurred while scraping data from URL:", url)
                    continue
    except Exception as e:
        print("Error fetching URL:", e)

get_url()



print("Sus")
driver.quit()

