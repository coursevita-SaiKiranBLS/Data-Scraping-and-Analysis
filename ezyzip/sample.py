arr = [
    "Accounting Jobs", "Interior Design Jobs", "Bank Jobs", "Content Writing Jobs", 
    "Consultant Jobs", "Engineering Jobs", "Export Import Jobs", "Merchandiser Jobs", 
    "Security Jobs", "HR Jobs", "Hotel Jobs", "Application Programming Jobs", 
    "Client Server Jobs", "DBA Jobs", "Ecommerce Jobs", "ERP Jobs", "VLSI Jobs", 
    "Mainframe Jobs", "Middleware Jobs", "Mobile Jobs", "Network administrator Jobs", 
    "IT Jobs", "Testing Jobs", "System Programming Jobs", "EDP Jobs", "Telecom Software Jobs", 
    "Telecom Jobs", "BPO Jobs", "Legal Jobs", "Marketing Jobs", "Packaging Jobs", 
    "Pharma Jobs", "Maintenance Jobs", "Logistics Jobs", "Sales Jobs", "Secretary Jobs", 
    "Corporate Planning Jobs", "Site Engineering Jobs", "Film Jobs", "Teacher Jobs", 
    "Airline Jobs", "Graphic Designer Jobs", "Shipping Jobs", "Analytics Jobs", 
    "Business Intelligence Jobs", "Accounting Jobs", "Advertising Jobs", "Agriculture Jobs", 
    "Animation Jobs", "Architecture Jobs", "Automobile Jobs", "Aviation Jobs", "BPO Jobs", 
    "Bank Jobs", "Brewery Jobs", "Sanitary Jobs", "Chemical Jobs", "Engineering Jobs", 
    "Consumer Durables Jobs", "Courier Jobs", "Defence Jobs", "Teacher Jobs", "Electrical Jobs", 
    "Export Import Jobs", "FMCG Jobs", "Facility Management Jobs", "Fertilizers Jobs", 
    "Food Processing Jobs", "Fresher Jobs", "Gems Jewellery Jobs", "Glass Jobs", 
    "Air Conditioning Jobs", "Airline Jobs", "Networking Jobs", "IT Jobs", "Industrial Jobs", 
    "Insurance Jobs", "KPO Jobs", "Legal Jobs", "Media Jobs", "Dotcom Jobs", 
    "Entertainment Jobs", "Medical Jobs", "Mining Jobs", "NGO Jobs", "Automation Jobs", 
    "Oil and Gas Jobs", "Paper Jobs", "Pharma Jobs", "Printing Jobs", "Publishing Jobs", 
    "Real Estate Jobs", "Recruitment Jobs", "Retail Jobs", "Security Jobs", 
    "Electronics Jobs", "Shipping Jobs", "Steel Jobs", "Consultant Jobs", "Telecom Jobs", 
    "Textiles Jobs", "Tyres Jobs", "Water Treatment Jobs", "Fitness Trainer Jobs", 
    "Ecommerce Jobs", "Internet Jobs"
]


list_set=list(set(arr))
list_set.sort()
a=""
for i in list_set:
   
    a = "\""+i.replace(" ", "-")
    a = a.lower()
    a += "\""
    a +=","
    
    print(a,end=" ")
    a=""
# print(len(set(arr)))