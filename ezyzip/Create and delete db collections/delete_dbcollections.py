import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('naukri-jobs-e83f6-firebase-adminsdk-9efux-1c2bf587e8.json') 
firebase_admin.initialize_app(cred)


db = firestore.client()

def delete_collection(collection_path, batch_size=20):
    """
    Delete all documents in a collection recursively.
    """
    collection_ref = db.collection(collection_path)
    docs = collection_ref.limit(batch_size).stream()

    deleted = 0

    for doc in docs:
        doc.reference.delete()
        deleted += 1

    if deleted >= batch_size:
        return delete_collection(collection_path, batch_size)

def delete_collections(collection_names):
    """
    Delete multiple collections.
    """
    for collection_name in collection_names:
        delete_collection(collection_name)
        
        
job_categories_to_delete = [
    
    "accounting-jobs", "advertising-jobs", "agriculture-jobs", "air-conditioning-jobs", "airline-jobs", "analytics-jobs", "animation-jobs", "application-programming-jobs", "architecture-jobs", "automation-jobs", "automobile-jobs", "aviation-jobs", "bpo-jobs", "bank-jobs", "brewery-jobs", "business-intelligence-jobs", "chemical-jobs", "client-server-jobs", "consultant-jobs", "consumer-durables-jobs", "content-writing-jobs", "corporate-planning-jobs", "courier-jobs", "dba-jobs", "defence-jobs", "dotcom-jobs", "edp-jobs", "erp-jobs", "ecommerce-jobs", "electrical-jobs", "electronics-jobs", "engineering-jobs", "entertainment-jobs", "export-import-jobs", "fmcg-jobs", "facility-management-jobs", "fertilizers-jobs", "film-jobs", "fitness-trainer-jobs", "food-processing-jobs", "fresher-jobs", "gems-jewellery-jobs", "glass-jobs", "graphic-designer-jobs", "hr-jobs", "hotel-jobs", "information-technology-jobs", "industrial-jobs", "insurance-jobs", "interior-design-jobs", "internet-jobs", "kpo-jobs", "legal-jobs", "logistics-jobs", "mainframe-jobs", "maintenance-jobs", "marketing-jobs", "media-jobs", "medical-jobs", "merchandiser-jobs", "middleware-jobs", "mining-jobs", "mobile-jobs", "ngo-jobs", "network-administrator-jobs", "networking-jobs", "oil-and-gas-jobs", "packaging-jobs", "paper-jobs", "pharma-jobs", "printing-jobs", "publishing-jobs", "real-estate-jobs", "recruitment-jobs", "retail-jobs", "sales-jobs", "sanitary-jobs", "secretary-jobs", "security-jobs", "shipping-jobs", "site-engineering-jobs", "steel-jobs", "system-programming-jobs", "teacher-jobs", "telecom-jobs", "telecom-software-jobs", "testing-jobs", "textiles-jobs", "tyres-jobs", "vlsi-jobs", "water-treatment-jobs"
]


delete_collections(job_categories_to_delete)

print("Sucessfull deleted all collections")
