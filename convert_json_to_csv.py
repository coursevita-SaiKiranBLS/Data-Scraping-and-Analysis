import pandas as pd
import json
from bs4 import BeautifulSoup

df = pd.read_csv("merged_1.csv")

#JSON TO CSV

def extract_json_fields(row):
    try:
        field_value = row['Field2']
        
        # Check if the value is a valid JSON string
        if isinstance(field_value, str):
            json_data = json.loads(field_value)
            
            # Extract attributes from JSON data
            attributes = {
                'Title': json_data.get('title', ''),
                'Description': clean_html(json_data.get('description', '')),
                'Identifier': json_data.get('identifier', {}).get('value', ''),
                'DatePosted': json_data.get('datePosted', ''),
                'ValidThrough': json_data.get('validThrough', ''),
                'Qualifications': json_data.get('qualifications', {}).get('@type', ''),
                'ExperienceMonths': json_data.get('experienceRequirements', {}).get('monthsOfExperience', ''),
                'OccupationalCategory': json_data.get('occupationalCategory', ''),
                'Responsibilities': json_data.get('responsibilities', ''),
                'Industry': json_data.get('industry', ''),
                'Skills': ', '.join(json_data.get('skills', [])),
                'SpecialCommitments': json_data.get('specialCommitments', ''),
                'WorkHours': json_data.get('workHours', ''),
                'EmploymentType': json_data.get('employmentType', ''),
                'OrganizationName': json_data.get('hiringOrganization', {}).get('name', ''),
                'OrganizationType': json_data.get('hiringOrganization', {}).get('@type', ''),
                'OrganizationSameAs': json_data.get('hiringOrganization', {}).get('sameAs', ''),
                'OrganizationLogo': json_data.get('hiringOrganization', {}).get('logo', ''),
                'LocationLocality': ', '.join(json_data.get('jobLocation', {}).get('address', {}).get('addressLocality', [])),
                'LocationRegion': ', '.join(json_data.get('jobLocation', {}).get('address', {}).get('addressRegion', [])),
                'LocationPostalCode': json_data.get('jobLocation', {}).get('address', {}).get('postalCode', ''),
                'LocationStreetAddress': ', '.join(json_data.get('jobLocation', {}).get('address', {}).get('streetAddress', [])),
                'LocationCountry': json_data.get('jobLocation', {}).get('address', {}).get('addressCountry', ''),
                'BaseSalary': json_data.get('baseSalary', {}).get('value', {}).get('value', '') if 'baseSalary' in json_data else ''

            }
            
            return attributes
        else:
            print(f"Ignoring row {row.name} - Field2 is not a valid JSON string: {field_value}")
            return {
                'Title': '',
                'Description': '',
                'Identifier': '',
                'DatePosted': '',
                'ValidThrough': '',
                'Qualifications': '',
                'ExperienceMonths': '',
                'OccupationalCategory': '',
                'Responsibilities': '',
                'Industry': '',
                'Skills': '',
                'SpecialCommitments': '',
                'WorkHours': '',
                'EmploymentType': '',
                'OrganizationName': '',
                'OrganizationType': '',
                'OrganizationSameAs': '',
                'OrganizationLogo': '',
                'LocationLocality': '',
                'LocationRegion': '',
                'LocationPostalCode': '',
                'LocationStreetAddress': '',
                'LocationCountry': ''
            }
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error processing row {row.name}: {e}")
        return {
            'Title': '',
            'Description': '',
            'Identifier': '',
            'DatePosted': '',
            'ValidThrough': '',
            'Qualifications': '',
            'ExperienceMonths': '',
            'OccupationalCategory': '',
            'Responsibilities': '',
            'Industry': '',
            'Skills': '',
            'SpecialCommitments': '',
            'WorkHours': '',
            'EmploymentType': '',
            'OrganizationName': '',
            'OrganizationType': '',
            'OrganizationSameAs': '',
            'OrganizationLogo': '',
            'LocationLocality': '',
            'LocationRegion': '',
            'LocationPostalCode': '',
            'LocationStreetAddress': '',
            'LocationCountry': ''
        }



def clean_html(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    clean_text = soup.get_text(separator=' ')
    return clean_text

json_data_df = pd.DataFrame(df.apply(extract_json_fields, axis=1).tolist())

json_data_df.to_csv('output_1.csv', index=False)

print("Conversion complete.")
