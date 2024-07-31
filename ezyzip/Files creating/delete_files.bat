@echo off
setlocal enabledelayedexpansion

set "folder_path=C:\Users\bayya\OneDrive\Desktop\web scraper\Naukri_url"

set "file_names=(accounting-jobs.py advertising-jobs.py agriculture-jobs.py air-conditioning-jobs.py airline-jobs.py analytics-jobs.py animation-jobs.py application-programming-jobs.py architecture-jobs.py automation-jobs.py automobile-jobs.py aviation-jobs.py bpo-jobs.py bank-jobs.py brewery-jobs.py business-intelligence-jobs.py chemical-jobs.py client-server-jobs.py consultant-jobs.py consumer-durables-jobs.py content-writing-jobs.py corporate-planning-jobs.py courier-jobs.py dba-jobs.py defence-jobs.py dotcom-jobs.py edp-jobs.py erp-jobs.py ecommerce-jobs.py electrical-jobs.py electronics-jobs.py engineering-jobs.py entertainment-jobs.py export-import-jobs.py fmcg-jobs.py facility-management-jobs.py fertilizers-jobs.py film-jobs.py fitness-trainer-jobs.py food-processing-jobs.py fresher-jobs.py gems-jewellery-jobs.py glass-jobs.py graphic-designer-jobs.py hr-jobs.py hotel-jobs.py jobs.py industrial-jobs.py insurance-jobs.py interior-design-jobs.py internet-jobs.py information-technology.py kpo-jobs.py legal-jobs.py logistics-jobs.py mainframe-jobs.py maintenance-jobs.py marketing-jobs.py media-jobs.py medical-jobs.py merchandiser-jobs.py middleware-jobs.py mining-jobs.py mobile-jobs.py ngo-jobs.py network-administrator-jobs.py networking-jobs.py oil-and-gas-jobs.py packaging-jobs.py paper-jobs.py pharma-jobs.py printing-jobs.py publishing-jobs.py real-estate-jobs.py recruitment-jobs.py retail-jobs.py sales-jobs.py sanitary-jobs.py secretary-jobs.py security-jobs.py shipping-jobs.py site-engineering-jobs.py steel-jobs.py system-programming-jobs.py teacher-jobs.py telecom-jobs.py telecom-software-jobs.py testing-jobs.py textiles-jobs.py tyres-jobs.py vlsi-jobs.py water-treatment-jobs.py)"

cd /d "%folder_path%"


for %%F in %file_names% do (
    del "%%F"
    echo Deleted file: %%F
)

echo All files deleted from "%folder_path%".
pause
