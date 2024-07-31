# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time
# import requests
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore
# import json

# # Initialize Firebase
# cred = credentials.Certificate("Create and delete db collections\\naukri-jobs-coursevita-firebase-adminsdk-nd813-75f1ea85df.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()
# # Initialize Selenium WebDriver
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# job_counter = 0



# def update_firebase(job_data):
#     global job_counter
#     try:
        
#         db.collection('textiles-jobs').add(job_data)
#         print("Job data added to Firestore successfully.")
#         job_counter = job_counter + 1
#         print(f"Job data added to Firestore successfully. Total jobs added: {job_counter}")
#     except Exception as e:
#         print("Error adding job data to Firestore:", e)
        
        
# def scrape_naukri(category_url):
   
#     driver.get(category_url)

#     time.sleep(10)  

#     soup = BeautifulSoup(driver.page_source, 'html.parser')
        
#     script_tags = soup.find_all('script')

#     try:
#         for script_tag in script_tags:
#             if script_tag.get('type') == "application/ld+json":
#                 json_data = json.loads(script_tag.text)
#                 print(json_data)  

#                 if json_data["@type"] == "ItemList":
#                     items = json_data["itemListElement"]
#                     for item in items:
#                         print("Name:", item.get("name", ""))
#                         print("URL:", item.get("url", ""))
#                         print("Image:", item.get("image", ""))
#                         print("------")
                      
#                         job_data = {
#                             "name": item.get("name", ""),
#                             "url": item.get("url", ""),
#                             "image": item.get("image", "")
#                         }
#                         update_firebase(job_data)
#     except Exception as e:
#         print("Error:", e)
        

# array = [
#     "textiles-jobs"
# ]

# for category in array:
#     for i in range(1,10000):
#         if i == 1:
#             category_url = f"https://www.naukri.com/{category}"
#             print("Category:", category)  
#             scrape_naukri(category_url) 
#         else:
#             category_url = f"https://www.naukri.com/{category}-{i}"
#             if category_url != "null":
#                 print("Category:", category)  
#                 scrape_naukri(category_url)                  
                
# driver.quit()



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time
# import json
# from firebase_admin import credentials, firestore, initialize_app
# import os


# current_file_path = __file__


# current_file_name = os.path.basename(current_file_path)


# trimmed_file_name = current_file_name[:-3]




# cred = credentials.Certificate("naukri-jobs-e83f6-firebase-adminsdk-9efux-1c2bf587e8.json")
# initialize_app(cred)
# db = firestore.client()

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)


# job_counter = 0

# def batch_data(iterable, batch_size=500):

#     for idx in range(0, len(iterable), batch_size):
#         yield iterable[idx:idx + batch_size]


# def update_firestore(job_data_list):
#     global job_counter
#     batch = db.batch()
    
#     for job_data in job_data_list:
#         try:
#             job_url = job_data.get("url")
#             if job_url:
#                 existing_docs = db.collection(str(trimmed_file_name)).where("url", "==", job_url).limit(1).get()
#                 if not existing_docs:
#                     doc_ref = db.collection(trimmed_file_name).document()
#                     batch.set(doc_ref, job_data)
#                     job_counter += 1
#                     print("Added job data to Firestore successfully. Total jobs added:", job_counter)
#                 else:
#                     print(f"Job with URL '{job_url}' already exists in Firestore.")  
#         except Exception as e:
#             print(f"Error adding job data to Firestore: {e}")

#     batch.commit()


# def scrape_naukri(category_url):
#     driver.get(category_url)
#     time.sleep(5) 

#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     script_tags = soup.find_all('script', type="application/ld+json")

#     job_data_list = []
#     for script_tag in script_tags:
#         try:
#             json_data = json.loads(script_tag.text)
#             if json_data.get("@type") == "ItemList":
#                 items = json_data.get("itemListElement", [])
#                 for item in items:
#                     job_data = {
#                         "name": item.get("name", ""),
#                         "url": item.get("url", ""),
#                         "image": item.get("image", "")
#                     }
#                     job_data_list.append(job_data)
#         except Exception as e:
#             print(f"Error processing script tag: {e}")

#     # Batch update Firestore with job data
#     update_firestore(job_data_list)
    
    

# # Main function
# def main():
#     base_url = "https://www.naukri.com/"
#     categories = [str(trimmed_file_name)]
    

#     for category in categories:
#         for i in range(1, 3000):
#             category_url = f"{base_url}{category}-{i}" if i > 1 else f"{base_url}{category}"
#             print(f"Scraping category: {category}, Page: {i}")

#             try:
#                 scrape_naukri(category_url)
#             except Exception as e:
#                 print(f"Error scraping {category_url}: {e}")
#                 continue

#     driver.quit()
#     print("Scraping completed.")
#     print("Total jobs scraped:", job_counter)
    
    

# if __name__ == "__main__":
#     main()




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import json
import firebase_admin
from firebase_admin import credentials, firestore

import os
current_file_path = __file__
current_file_name = os.path.basename(current_file_path)
trimmed_file_name = current_file_name[:-3]

cred = credentials.Certificate("naukri-jobs-e83f6-firebase-adminsdk-9efux-1c2bf587e8.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

job_counts = {
    "accounting-jobs": 150217,
    "advertising-jobs": 36433,
    "agriculture-jobs": 173582,
    "air-conditioning-jobs": 8039,
    "airline-jobs": 5106,
    "analytics-jobs": 6776,
    "animation-jobs": 4892,
    "application-programming-jobs": 109677,
    "architecture-jobs": 68299,
    "automation-jobs": 35656,
    "automobile-jobs": 166967,
    "aviation-jobs": 5604,
    "bpo-jobs": 112451,
    "bank-jobs": 63272,
    "brewery-jobs": 9690,
    "business-intelligence-jobs": 39979,
    "chemical-jobs": 10143,
    "client-server-jobs": 84755,
    "consultant-jobs": 45958,
    "consumer-durables-jobs": 39269,
    "content-writing-jobs": 6656,
    "corporate-planning-jobs": 89844,
    "courier-jobs": 25983,
    "dba-jobs": 13646,
    "defence-jobs": 12865,
    "dotcom-jobs": 10195,
    "edp-jobs": 1781,
    "erp-jobs": 34515,
    "ecommerce-jobs": 23909,
    "electrical-jobs": 19594,
    "electronics-jobs": 29428,
    "engineering-jobs": 4426,
    "entertainment-jobs": 26033,
    "export-import-jobs": 1210,
    "fmcg-jobs": 43495,
    "facility-management-jobs": 6863,
    "fertilizers-jobs": 25648,
    "film-jobs": 18393,
    "fitness-trainer-jobs": 436,
    "food-processing-jobs": 14535,
    "fresher-jobs": 54837,
    "gems-jewellery-jobs": 26074,
    "glass-jobs": 9260,
    "graphic-designer-jobs": 7861,
    "hr-jobs": 13839,
    "hotel-jobs": 83927,
    "information-technology-jobs": 234251,
    "industrial-jobs": 71594,
    "insurance-jobs": 47761,
    "interior-design-jobs": 4121,
    "internet-jobs": 62086,
    "kpo-jobs": 30042,
    "legal-jobs": 142496,
    "logistics-jobs": 129321,
    "mainframe-jobs": 1349,
    "maintenance-jobs": 107441,
    "marketing-jobs": 17873,
    "media-jobs": 44763,
    "medical-jobs": 34779,
    "merchandiser-jobs": 787,
    "middleware-jobs": 15650,
    "mining-jobs": 57778,
    "mobile-jobs": 34998,
    "ngo-jobs": 87531,
    "network-administrator-jobs": 11689,
    "networking-jobs": 56848,
    "oil-and-gas-jobs": 3933,
    "packaging-jobs": 134841,
    "paper-jobs": 33529,
    "pharma-jobs": 154978,
    "printing-jobs": 14855,
    "publishing-jobs": 22381,
    "real-estate-jobs": 38307,
    "recruitment-jobs": 72331,
    "retail-jobs": 62821,
    "sales-jobs": 10486,
    "sanitary-jobs": 23628,
    "secretary-jobs": 21778,
    "security-jobs": 50363,
    "shipping-jobs": 28800,
    "site-engineering-jobs": 8284,
    "steel-jobs": 26100,
    "system-programming-jobs": 75678,
    "teacher-jobs": 12854,
    "telecom-jobs": 21653,
    "telecom-software-jobs": 47389,
    "testing-jobs": 93872,
    "textiles-jobs": 15117,
    "tyres-jobs": 6240,
    "vlsi-jobs": 1428,
    "water-treatment-jobs": 23226
}

def extract_job_data(url):
    driver.get(url)
    time.sleep(2) 

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    script_tags = soup.find_all('script')

    job_data = {}
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
                break
    if 'description' in job_data:
       job_data['description'] = BeautifulSoup(job_data['description'], 'html.parser').get_text()

    return job_data

def update_firestore_with_job(url, job_data):
    try:
        existing_docs = db.collection(str(trimmed_file_name)).where("url", "==", url).limit(1).get()
        if not existing_docs:
            job_data["url"] = url
            db.collection(str(trimmed_file_name)).add(job_data)
            print(f"Added job '{job_data['title']}' to Firestore successfully.")
        else:
            print(f"Job with URL already exists in Firestore.")
    except Exception as e:
        print(f"Error adding job data to Firestore: {e}")

def scrape_naukri(base_url, category):
    job_counter = 0
    n=int(job_counts[category]/20)+30
    for i in range(21, 23):
        category_url = f"{base_url}{category}-{i}" if i > 1 else f"{base_url}{category}"
        print(f"Scraping category: {category}, Page: {i}")

        try:
            driver.get(category_url)
            time.sleep(5) 

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            script_tags = soup.find_all('script', type="application/ld+json")

            for script_tag in script_tags:
                try:
                    json_data = json.loads(script_tag.text)
                    if json_data.get("@type") == "ItemList":
                        items = json_data.get("itemListElement", [])
                        for item in items:
                            job_url = item.get("url", "")
                            if job_url:
                                job_data = extract_job_data(job_url)
                                update_firestore_with_job(job_url, job_data)
                                job_counter += 1
                except Exception as e:
                    print(f"Error processing script tag: {e}")

        except Exception as e:
            print(f"Error scraping {category_url}: {e}")
            continue

    print("Scraping completed.")
    print("Total jobs added to Firestore:", job_counter)

if __name__ == "__main__":
    base_url = "https://www.naukri.com/"
    categories = [str(trimmed_file_name)]  

    for category in categories:
        scrape_naukri(base_url, category)

    driver.quit()



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import json
# import firebase_admin
# from firebase_admin import credentials, firestore
# import concurrent.futures


# # Initialize Firebase
# cred = credentials.Certificate("naukri-jobs-e83f6-firebase-adminsdk-9efux-1c2bf587e8.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# # Initialize Selenium WebDriver in headless mode
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run Chrome in headless mode

# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# def extract_job_data(url):
#     driver.get(url)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')

#     for script_tag in soup.find_all('script', type="application/ld+json"):
#         json_data = json.loads(script_tag.text)
#         if json_data.get("@type") == "JobPosting":
#             return {
#                "title": json_data.get("title", ""),
#                     "description": json_data.get("description", ""),
#                     "identifier": json_data.get("identifier", {}).get("value", ""),
#                     "datePosted": json_data.get("datePosted", ""),
#                     "validThrough": json_data.get("validThrough", ""),
#                     "qualifications": json_data.get("qualifications", {}).get("educationalLevel", ""),
#                     "experienceRequirements": json_data.get("experienceRequirements", {}).get("monthsOfExperience", ""),
#                     "occupationalCategory": json_data.get("occupationalCategory", ""),
#                     "responsibilities": json_data.get("responsibilities", ""),
#                     "industry": json_data.get("industry", ""),
#                     "skills": json_data.get("skills", []),
#                     "specialCommitments": json_data.get("specialCommitments", ""),
#                     "workHours": json_data.get("workHours", ""),
#                     "employmentType": json_data.get("employmentType", ""),
#                     "hiringOrganization": json_data.get("hiringOrganization", {}).get("name", ""),
#                     "logo": json_data.get("hiringOrganization", {}).get("logo", ""),
#                     "jobLocation": json_data.get("jobLocation", {}).get("address", {}).get("addressLocality", [""])[0],
#                     "postalCode": json_data.get("jobLocation", {}).get("address", {}).get("postalCode", ""),
#                     "streetAddress": json_data.get("jobLocation", {}).get("address", {}).get("streetAddress", [""])[0],
#                     "addressRegion": json_data.get("jobLocation", {}).get("address", {}).get("addressRegion", [""])[0],
#                     "addressCountry": json_data.get("jobLocation", {}).get("address", {}).get("addressCountry", ""),
#                     "baseSalary": json_data.get("baseSalary", {}).get("value", {}).get("value", ""),
#                     "currency": json_data.get("baseSalary", {}).get("value", {}).get("currency", ""),
#                     "unitText": json_data.get("baseSalary", {}).get("value", {}).get("unitText", "")
#             }
#     return None

# def update_firestore_with_job(url, job_data):
#     if job_data:
#         try:
#             db.collection('accounting-jobs').document(url).set(job_data)
#             print(f"Added job '{job_data['title']}' to Firestore successfully.")
#         except Exception as e:
#             print(f"Error adding job data to Firestore: {e}")

# def scrape_category(category_url):
#     try:
#         driver.get(category_url)
#         soup = BeautifulSoup(driver.page_source, 'html.parser')

#         for script_tag in soup.find_all('script', type="application/ld+json"):
#             json_data = json.loads(script_tag.text)
#             if json_data.get("@type") == "ItemList":
#                 items = json_data.get("itemListElement", [])
#                 with concurrent.futures.ThreadPoolExecutor() as executor:
#                     futures = [executor.submit(process_job_item, item) for item in items]
#                     for future in concurrent.futures.as_completed(futures):
#                         job_url, job_data = future.result()
#                         if job_url and job_data:
#                             update_firestore_with_job(job_url, job_data)

#     except Exception as e:
#         print(f"Error scraping {category_url}: {e}")

# def process_job_item(item):
#     job_url = item.get("url", "")
#     if job_url:
#         job_data = extract_job_data(job_url)
#         return job_url, job_data
#     return None, None

# if __name__ == "__main__":
#     base_url = "https://www.naukri.com/"
#     categories = ["accounting-jobs"]  # Add your desired categories

#     for category in categories:
#         for i in range(1, 5):
#             category_url = f"{base_url}{category}-{i}" if i > 1 else f"{base_url}{category}"
#             print(f"Scraping category: {category}, Page: {i}")
#             scrape_category(category_url)

#     driver.quit()
