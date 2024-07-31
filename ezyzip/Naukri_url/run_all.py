import concurrent.futures
import subprocess
import multiprocessing

file_names = [
    "Naukri_url/accounting-jobs.py",
    "Naukri_url/advertising-jobs.py",
    "Naukri_url/agriculture-jobs.py",
    "Naukri_url/air-conditioning-jobs.py",
    "Naukri_url/airline-jobs.py",
    "Naukri_url/analytics-jobs.py",
    "Naukri_url/animation-jobs.py",
    "Naukri_url/application-programming-jobs.py",
    "Naukri_url/architecture-jobs.py",
    "Naukri_url/automation-jobs.py",
    "Naukri_url/automobile-jobs.py",
    "Naukri_url/aviation-jobs.py",
    "Naukri_url/bpo-jobs.py",
    "Naukri_url/bank-jobs.py",
    "Naukri_url/brewery-jobs.py",
    "Naukri_url/business-intelligence-jobs.py",
    "Naukri_url/chemical-jobs.py",
    "Naukri_url/client-server-jobs.py",
    "Naukri_url/consultant-jobs.py",
    "Naukri_url/consumer-durables-jobs.py",
    "Naukri_url/content-writing-jobs.py",
    "Naukri_url/corporate-planning-jobs.py",
    "Naukri_url/courier-jobs.py",
    "Naukri_url/dba-jobs.py",
    "Naukri_url/defence-jobs.py",
    "Naukri_url/dotcom-jobs.py",
    "Naukri_url/edp-jobs.py",
    "Naukri_url/erp-jobs.py",
    "Naukri_url/ecommerce-jobs.py",
    "Naukri_url/electrical-jobs.py",
    "Naukri_url/electronics-jobs.py",
    "Naukri_url/engineering-jobs.py",
    "Naukri_url/entertainment-jobs.py",
    "Naukri_url/export-import-jobs.py",
    "Naukri_url/fmcg-jobs.py",
    "Naukri_url/facility-management-jobs.py",
    "Naukri_url/fertilizers-jobs.py",
    "Naukri_url/film-jobs.py",
    "Naukri_url/fitness-trainer-jobs.py",
    "Naukri_url/food-processing-jobs.py",
    "Naukri_url/fresher-jobs.py",
    "Naukri_url/gems-jewellery-jobs.py",
    "Naukri_url/glass-jobs.py",
    "Naukri_url/graphic-designer-jobs.py",   
]

def run_script(script):
    subprocess.run(["python", script])

if __name__ == '__main__':
    multiprocessing.freeze_support()  # Required for Windows
    max_processes = min(15, len(file_names))  # You can adjust the number of processes

    with concurrent.futures.ProcessPoolExecutor(max_workers=max_processes) as executor:
        executor.map(run_script, file_names)
