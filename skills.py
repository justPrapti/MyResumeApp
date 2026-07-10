skills_database=({

"HR":[
"recruitment","payroll","employee relations","onboarding",
"hr policies","performance management","communication",
"training","compliance","ms excel"
],

"INFORMATION-TECHNOLOGY":[
"python","java","sql","html","css","javascript",
"git","flask","machine learning","linux"
],

"FINANCE":[
"accounting","financial analysis","excel","budgeting",
"taxation","forecasting","auditing","quickbooks"
],

"ACCOUNTANT":[
"tally","gst","accounting","excel",
"bookkeeping","auditing","financial reporting"
],

"ENGINEERING":[
"autocad","solidworks","python","matlab",
"problem solving","cad","simulation"
],

"HEALTHCARE":[
"patient care","medical records","clinical",
"diagnosis","communication","healthcare"
],

"TEACHER":[
"lesson planning","communication",
"classroom management","curriculum",
"presentation","assessment"
],

"SALES":[
"sales","crm","negotiation",
"customer service","lead generation",
"communication"
],

"CONSULTANT":[
"excel","powerpoint","analysis",
"stakeholder management","communication",
"problem solving"
],

"BANKING":[
"loan","banking","finance",
"customer service","risk analysis",
"excel"
],

"CHEF":[
"food preparation","menu planning",
"hygiene","cooking","kitchen management"
],

"AVIATION":[
"aircraft","faa","aviation",
"safety","flight","maintenance"
],

"PUBLIC-RELATIONS":[
"media","branding","communication",
"marketing","social media"
],

"BUSINESS-DEVELOPMENT":[
"sales","marketing","lead generation",
"crm","negotiation","business strategy"
],

"DIGITAL-MEDIA":[
"seo","social media","content",
"photoshop","marketing","analytics"
],

"FITNESS":[
"nutrition","fitness","exercise",
"coaching","strength training"
],

"AGRICULTURE":[
"farming","soil","crop",
"irrigation","agriculture"
],

"APPAREL":[
"fashion","textile","garment",
"merchandising","design"
],

"BPO":[
"customer support","communication",
"voice process","crm","typing"
],

"ARTS":[
"drawing","painting","illustration",
"creative","design"
]

})
#######################
def extract_skills(resume, category):

    detected=[]

    if category in skills_database:

        for skill in skills_database[category]:

            if skill.lower() in resume.lower():

                detected.append(skill)

    return detected


def calculate_ats(category, detected_skills):

    if category not in skills_database:
        return 50

    expected = len(skills_database[category])

    found = len(detected_skills)

    ats = 45 + round((found / expected) * 55)

    return min(ats, 100)


def missing_skills(category, detected_skills):

    if category not in skills_database:
        return []

    missing = []

    for skill in skills_database[category]:
        if skill not in detected_skills:
            missing.append(skill)

    return missing


def get_suggestions(cleaned_resume, detected_skills, ats_score):

    suggestions = []

    if ats_score < 60:
        suggestions.append("Add more relevant technical skills.")

    if len(detected_skills) < 5:
        suggestions.append("Include more relevant skills.")

    if "github" not in cleaned_resume:
        suggestions.append("Mention your GitHub profile.")

    if "project" not in cleaned_resume:
        suggestions.append("Add project experience.")

    if "certification" not in cleaned_resume:
        suggestions.append("Mention certifications.")

    return suggestions

DEFAULT_SKILLS = [
    "communication",
    "problem solving",
    "teamwork",
    "leadership",
    "time management",
    "excel",
    "documentation",
    "project management"
]

ALL_CATEGORIES = [
    "ADVOCATE",
    "ARTS",
    "AVIATION",
    "BANKING",
    "BPO",
    "BUSINESS-DEVELOPMENT",
    "CHEF",
    "CONSTRUCTION",
    "CONSULTANT",
    "DESIGNER",
    "DIGITAL-MEDIA",
    "ENGINEERING",
    "FINANCE",
    "FITNESS",
    "HEALTHCARE",
    "HR",
    "INFORMATION-TECHNOLOGY",
    "PUBLIC-RELATIONS",
    "SALES",
    "TEACHER",
    "ACCOUNTANT",
    "APPAREL",
    "AGRICULTURE",
    "DATA SCIENCE"
]

for cat in ALL_CATEGORIES:
    if cat not in skills_database:
        skills_database[cat] = DEFAULT_SKILLS