import random
import pandas as pd
from faker import Faker
import json
from main import main

fake = Faker("tr_TR")  

# Constants
num_entries = 5000
start_id = 1
start_join_date = pd.Timestamp("2023-01-01")
end_join_date = pd.Timestamp("2024-06-30")

# Lists of possible values for some columns

# Ensure city matches university location if the user attends university
def assign_city(attends_university, university):
    if attends_university and university in university_to_city:
        return university_to_city[university]
    else:
        return random.choice(cities)  # Choose a random city otherwise

male_names = [
    "Abdullah", "Adem", "Adnan", "Ahmet", "Ahmet Ali", "Ali", "Ali Rıza", "Alp", "Alper", "Alperen", "Altın", "Arda",
    "Asım", "Atilla", "Bahadır", "Barış", "Batuhan", "Bekir", "Berk", "Berkay", "Berkan", "Berat",
    "Berke", "Bilge", "Bülent", "Burak", "Cafer", "Cahit", "Can", "Cem", "Cemal", "Cengiz", "Cihan",
    "Cüneyt", "Çağın", "Davud", "Deniz", "Derya", "Doğan", "Ege", "Emin", "Emir", "Ercan", "Ercüment", "Erdal",
    "Erdem", "Ersin", "Erdoğan", "Ergin", "Erhan", "Ethem", "Efe", "Ekrem", "Engin", "Emin",
    "Ercan", "Eren", "Ersin", "Erkan", "Ethem", "Evren", "Fahrettin", "Fatih", "Ferdi", "Ferhat",
    "Ferit", "Fikret", "Fırat", "Fuat", "Gökay", "Gökalp", "Gökhan", "Güven", "Güvenç", "Hakkı", "Halil", "Halil İbrahim", "Hamdi",
    "Hamit", "Harun", "Hasan", "Hikmet", "Hilmi", "Hüseyin", "Hüsnü", "İbrahim", "İhsan", "İlhan",
    "İrfan", "İsmail", "İzzet", "Kadir", "Kemal", "Kenan", "Kerim", "Kubilay", "Koray", "Kıvanç", "Levent",
    "Lütfi", "Mahmut", "Mehmet", "Mehmet Ali", "Mehmet Emin", "Metin", "Mesut", "Mikail", "Muhammet", "Murat",
    "Mustafa", "Mustafa Kemal", "Nihat", "Nuri", "Okan", "Onur", "Orhan", "Osman", "Ömer", "Özcan",
    "Ragıp", "Ramazan", "Recep", "Remzi", "Rıfat", "Rıza", "Rüstem", "Sadık", "Salih", "Sami",
    "Sedat", "Selami", "Selçuk", "Selim", "Serdar", "Süleyman", "Sinan", "Soner", "Suat", "Süleyman",
    "Şaban", "Şahin", "Şerif", "Şevket", "Tanju", "Tarık", "Tayfun", "Tufan", "Tuncay", "Turan",
    "Uğur", "Umut", "Ümit", "Veli", "Yahya", "Yakup", "Yasin", "Yavuz", "Yılmaz", "Yunus", "Yusuf",
    "Zafer", "Zeki", "Zeynel"
]

female_names = [
    "Ahu", "Afet", "Alev", "Ayla", "Aylin", "Ayfer", "Ayşe", "Ayşegül", "Ayten", "Aysel", "Aysun",
    "Azra", "Bahar", "Belma", "Bengi", "Bengisu", "Beren", "Beril", "Berna", "Berrin", "Bilge", "Birgül", "Birsen", "Birsu", "Büşra", "Billur", "Burcu", "Buse", "Busenur", "Ceren", "Cansu",
    "Cemile", "Çağla", "Deniz", "Derya", "Dilek", "Duygu", "Ebru", "Ece", "Eda", "Elif", "Emine", "Esma",
    "Esra", "Eylül", "Fadime", "Fatma", "Feray", "Ferda", "Feyza", "Filiz", "Figen", "Fikriye", "Fulya",
    "Füsun", "Gizem", "Gülay", "Gülbahar", "Gülben", "Gülden", "Gülgün", "Güliz", "Gülizar", "Güllü", "Gülsüm",
    "Gülşen", "Gülsen", "Gülten", "Gülşah", "Hale", "Hande", "Havva", "Hülya", "İclal", "İdil", "İda",
    "İlknur", "İnci", "Işıl", "Işık", "Kadriye", "Kader", "Kübra", "Leyla", "Leman", "Lale",
    "Mazlum", "Mediha", "Mehtap", "Melek", "Meral", "Meryem", "Merve", "Mevlüde", "Mualla",
    "Mukadder", "Mukaddes", "Müge", "Munise", "Müjgan", "Müşerref", "Naciye", "Nalan", "Nazan", "Nergis",
    "Nesibe", "Neslihan", "Nihal", "Nilgün", "Nur", "Nuran", "Nurgül", "Nurhan", "Nuriye",
    "Nursel", "Nurten", "Olcay", "Oya", "Perihan", "Pınar", "Rukiye", "Rüya", "Sadiye", "Saime", "Sema",
    "Samiye", "Seda", "Seden", "Seher", "Selda", "Selen", "Selime", "Selin", "Semiha", "Semra",
    "Seval", "Sevgi", "Sevim", "Sevinç", "Sevtap", "Sibel", "Songül", "Suheyla", "Süheyla", "Sultan", "Suna",
    "Şafak", "Şaziye", "Şebnem", "Şehnaz", "Şehri", "Şehval", "Şemsi", "Şermin", "Şerife", "Şeyma",
    "Şevval", "Şule", "Şükran", "Tansu", "Taybet", "Tülay", "Tülin", "Ülkü", "Ülker", "Ümmü", "Vildan",
    "Yaren", "Yasemin", "Yeşim", "Yeliz", "Yurdagül", "Zehra", "Zeliha", "Zerrin", "Zeynep", "Zinnur","Zuhal"
]

surnames = [
    "Açıkgöz", "Ağca", "Akbaş", "Akbulut", "Akgül", "Akgün", "Akyıldız", "Akın", "Akkuş", "Aksoy",
    "Alim", "Alkan", "Altuğ", "Algın", "Arslan", "Arı", "Arıkan", "Arıtan", "Arısoy", "Arıtaş",
    "Aslan", "Atalay", "Atasoy", "Ateş", "Ay", "Aydemir", "Aygün", "Ayhan", "Aytaç", "Aytaş",
    "Aydoğan", "Ayhan", "Aytaç", "Aytaş", "Bora", "Baş", "Bayram", "Bayraktar", "Berk", "Bilgin",
    "Boz", "Bozkurt", "Boztaş", "Bülbül", "Büyük", "Can", "Cebeci", "Cengiz", "Çalışkan", "Çamurcu", "Çamuroğlu", "Çakır", "Çakıroğlu", "Çelik",
    "Çetin", "Çetinkaya", "Çiftçi", "Çiçek", "Çınar", "Demir", "Demircan", "Demirci", "Demirel", "Doğan",
    "Doğru", "Duman", "Erbay", "Erdem", "Eren", "Eren", "Eroğlu", "Ertaş", "Erçetin", "Eryılmaz",
    "Güler", "Göçer", "Göçmen", "Güçlü", "Gül", "Gülen", "Güler", "Güngör", "Güneş", "Güven", "Güz", "Gür",
    "Karaca", "Karademir", "Karagöz", "Karahan", "Karakaş", "Karalı", "Karataş", "Karakuş", "Karaman", "Karaoğlu",
    "Kayman", "Kazanan", "Keleş", "Kılıç", "Kılıçoğlu", "Kocaman", "Koç", "Koçak", "Koçyiğit", "Koşar",
    "Kurt", "Kurtul", "Kurtuluş", "Kurtul", "Kurtul", "Küçük", "Köksal", "Köse", "Öz", "Özen",
    "Özbek", "Özcan", "Özdemir", "Özkan", "Özmen", "Öztürk", "Polat", "Sarı", "Sarıkaya", "Savaş",
    "Sevecen", "Serbest", "Sönmez", "Sönmez", "Sözer", "Şahin", "Şahiner", "Şahin", "Şahin", "Şimşek",
    "Şolta", "Şen", "Şentürk", "Tanrıverdi", "Taş", "Taşkın", "Tatlıtuğ", "Tekin", "Tekinoğlu", "Temiz", "Temizer", "Tosun", "Tuncer",
    "Turan", "Turgal", "Tunç", "Tüfekçi", "Uçar", "Uysal", "Uzun", "Yalçın", "Yaman", "Yavuz",
    "Yıldız", "Yılmaz", "Yılmazer", "Yüksel", "Zengin", "Zarif"
]

university_to_city = {
    "Koc University": "Istanbul",
    "Beykent University": "Istanbul",
    "Bogazici University": "Istanbul",
    "Sabanci University": "Istanbul",
    "MEF University": "Istanbul",
    "Istanbul Technical University": "Istanbul",
    "Ankara University": "Ankara",
    "Hacettepe University": "Ankara",
    "Middle East Technical University": "Ankara",
    "Yildiz Technical University": "Istanbul",
    "Marmara University": "Istanbul",
    "Istanbul University": "Istanbul",
    "Istanbul Bilgi University": "Istanbul",
    "Istanbul Aydin University": "Istanbul",
    "Istanbul Medipol University": "Istanbul",
    "Istanbul Sehir University": "Istanbul",
    "Gazi University": "Ankara",
    "Bilkent University": "Ankara",
    "Yildirim Beyazit University": "Ankara",
    "Atilim University": "Ankara",
    "Ufuk University": "Ankara",
    "TOBB University of Economics and Technology": "Ankara",
    "Ege University": "Izmir",
    "Dokuz Eylul University": "Izmir",
    "Izmir University of Economics": "Izmir",
    "Yasar University": "Izmir",
    "Uludag University": "Bursa",
    "Cukurova University": "Adana",
    "Mersin University": "Mersin",
    "Samsun University": "Samsun",
    "Akdeniz University": "Antalya",
    "Karadeniz Technical University": "Trabzon",
    "Van Yuzuncu Yil University": "Van",
    "Selcuk University": "Konya",
    "Erciyes University": "Kayseri"
}

# Fields
fields = [
    "Law", "Education", "Economics", "Business", "Computer Engineering", "Civil Engineering", 
    "Mechanical Engineering", "Electrical Engineering", "Chemical Engineering", "Aerospace Engineering",
    "Physics", "Chemistry", "Biology", "Environmental Science", "Architecture", "Industrial Engineering"
]

# Universities
universities = [
    "Koc University", "Beykent University", "Bogazici University", "Sabanci University", "MEF University",
    "Istanbul Technical University", "Ankara University", "Hacettepe University", "Middle East Technical University",
    "Yildiz Technical University", "Marmara University", "Istanbul University", "Istanbul Bilgi University",
    "Istanbul Aydin University", "Istanbul Medipol University", "Istanbul Sehir University",
    "Gazi University", "Bilkent University", "Yildirim Beyazit University", "Atilim University", "Ufuk University",
    "TOBB University of Economics and Technology", "Ege University", "Dokuz Eylul University", "Izmir University of Economics",
    "Yasar University", "Uludag University", "Cukurova University", "Mersin University", "Samsun University",
    "Akdeniz University", "Karadeniz Technical University", "Van Yuzuncu Yil University", "Selcuk University",
    "Erciyes University"
]

# Workplaces
workplaces = [
    "Turk Telekom", "Koc Holding", "Arcelik", "Turkish Airlines", "Sabanci Holding", "A101", "Letgo",
    "Vestel", "Zorlu Holding", "Ford Otosan", "Developia", "Yapi Kredi Bank", "Garanti Bank", "Beko", "Eti",
    "Havelsan", "Roketsan", "Siemens Turkey", "Microsoft Turkey", "Google Turkey", "IBM Turkey", "Huawei Turkey" ,
    "Dogus Holding", "Alarko Holding", "TAV Airports", "Dogan Holding", "Okan Holding", "Amazon Turkey", "Trendyol",
    "YemekSepeti", "Getir", "HepsiBuarda", "Netflix Turkey", "Turkcell", "Vodafone", "Tueknet", "Sahibinden", "Cisco"
    "GlassHouse", "Not Employed"
]

# Cities
cities = [
    "Istanbul", "Ankara", "Izmir", "Antalya", "Bursa", "Adana", "Gaziantep", "Samsun", "Mersin", "Konya",
    "Trabzon", "Kayseri", "Van", "Diyarbakir", "Erzurum", "Denizli", "Kocaeli", "Sakarya", "Eskisehir",
    "Canakkale", "Mugla", "Tekirdağ", "Edirne"
]

interests = [
    'Native App Development', 'Cross-platform App Development', 'Front End Design', 'Back End Design', 'Java', 'Python', 'Unity Game Development', 
    'Unreal Engine Game Devlopment', 'Mobile Game Development', 'Android', 'IOS', 'JavaScript', 'Machine Learning', 'Data Science', 
    'Artificial Intelligence', 'Web Development', 'Mobile Development', 'Cloud Computing', 'Internet of Things (IoT)', 'Cybersecurity', 
    'Blockchain Technology', 'Augmented Reality', 'Virtual Reality', 'Computer Graphics', 'Robotics', 'Quantum Computing', 'Computer Networking', 
    'Natural Language Processing', 'Image Generation', 'Graphic Design', 'Entrepreneurship', 'Startup', 'Marketing', 'E-commerce', 
    'Illustration', 'Animation', 'Photography', 'Video Production', 'Music Production', 'Creative Writing', 'Film Making', 'Interior Design', 
    'Digital Art', 'Physics', 'Chemistry', 'Biology', 'Astronomy', 'Geology', 'Mathematics', 'Statistics', 'Neuroscience', 'Literature', 'Languages', 
    'Database Management', 'DevOps', 'User Experience (UX) Design', 'User Interface (UI) Design', 'Ethical Hacking', 'Penetration Testing', 
    'Digital Marketing', 'Content Writing', 'Search Engine Optimization (SEO)', 'Quality Assurance (QA)', 'Virtual Assistant Services', 
    'Freelancing', 'Generative AI', 'Software Development', 'Flutter development', 'React Native Development', 'Embedded Systems'
]

purposes = [
    "project partner", "startup", "networking", "brain storming", "project assist", "freelance", "other", 'study partner'
]

cities_to_district = {
    "Istanbul": ["Eyüp", "Tarabya", "Sarıyer", "4. Levent", "Levent", "Kağıthane", "Beşiktaş", "Şişli", "Mecidiyeköy", "Üsküdar", "Kadıköy", "Taksim", "Kartal", "Tuzla"],
    "Ankara": ["Etimesgut", "Yenimahalle", "Çankaya", "Keçiören", "Altındağ" "Akyurt","Kalecik"],
    "Izmir": ["Foça","Menemen","Karşıyaka","Bornova","Buca","Narlıdere","Güzelbahçe","Urla","Çeşme"],
    "Antalya": ["Kaş","Kale","Finike","Kumluca","Kemer","Konyaaltı","Muratpaşa","Manavgat","Alanya"],
    "Bursa": ["Karacabey","Mudanya","Gemlik","Orhangazi","İznik","Yenişehir","İnegöl"],
    "Adana": ["Karataş","Yumurtalık","Ceyhan","İmamoğlu","Kozan","Aladağ","Feke","Saimbeyli"],
    "Gaziantep": ["Nurdağı","Şehitkamil","Yavuzeli","Nizip","Karkamış","Oğuzeli"],
    "Samsun": ["Alaçam","Bafra","Havza","Ladik","Asarcik","Ayvacık","Salıpazarı"],
    "Konya": ["Beyşehir", "Seydişehir", "Bozkır", "Akören", "Çumra", "Karatay"],
    "Trabzon": ["Çarşıbaşı", "Akcaabat", "Ortahisar", "Yomra", "Arsin", "Araklı", "Sürmene", "Of"],
    "Tekirdağ": ["Süleymanpaşa", "Çorlu", "Malkara", "Çerkezköy", "Şarköy"],
    "Edirne": ["Havsa", "Uzunköprü", "Keşan", "İpsala", "Enez"],
    "Mugla": ["Bodrum", "Milas", "Yatağan", "Ula", "Marmaris", "Köyceğiz", "Dalaman", "Fethiye"],
    "Canakkale": ["Yenice", "Biga", "Lapseki", "Çanakkale Merkez","Ezine", "Ayvacık"],
    "Eskisehir": ["Tepebasi", "Odunpazari", "Seyitgazi", "Çifteler", "Mahmudiye","Sivrihisar"],
    "Mersin": ["Anamur", "Bozyazı", "Gülnar", "Silifke","Erdemli", "Tarsus"],
    "Sakarya": ["Serdivan", "Adapazari", "Sapanca", "Arifiye", "Erenler", "Karapürçek", "Akyazı"],
    "Van": ["Erciş", "Muradiye", "Çaldıran", "Özalp","Saray","Başkale"],
    "Kocaeli": ["Darıca", "Gebze", "Dilovası", "Körfez", "Derince", "İzmit", "Kartepe"],
    "Diyarbakir": ["Kulp", "Lice", "Hani", "Dicle","Ergani", "Çüngüş"],
    "Denizli": ["Çameli","Acıpayam","Tavas","Serinhisar","Bozkurt","Çivril"],
    "Erzurum": ["Aşkale", "Çat", "Palandöken", "Tekman", "Hınıs", "Karayazı", "Horasan"],
    "Kayseri": ["Pınarbaşı", "Sarız", "Tomarza", "Develi","Yahyâlı", "Yeşilhisar"]
}

# Initialize an empty list to store the dataset
data = []
data.append(f"id/name/surname/email/birthDate/allowOppositeGender/gender/field/interest1/interest2/interest3/interest4/interest5/attendsUni/university/workplace/purpose/online/f2f/country/city/district/joinDate/rating/uniOnly/priority\n")
json_data = []

# MEF University students counter
mef_count = 0

# Generate the data
for idx in range(num_entries):
    # Create user data
    user_id = start_id + idx

     # Gender: 'male', 'female', or 'other' (15% must be 'other')
    gender_distribution = ["male", "female", "other"]
    gender_weights = [0.425, 0.425, 0.150]
    gender = random.choices(gender_distribution, weights=gender_weights, k=1)[0]

    if gender=="male":
        name = random.choice(male_names)
    elif gender=="female":
        name = random.choice(female_names)
    elif gender=="other":
        pool = random.choice([male_names, female_names])
        name = random.choice(pool)
    
    surname = random.choice(surnames)
    
    # Email based on name and surname
    email = f"{name.lower()}_{surname.lower()}{random.choice(['', str(random.randint(1, 99))])}@{random.choice(['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com'])}"
    
    # Random birth date, mostly from the '90s, '80s, and early 2000s
    birth_year = random.choice(range(1980, 2007))
    birth_date = f"{birth_year}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    
    # Allow opposite gender (1 or 0)
    allow_opposite_gender = random.choice([0, 1])
    
    # Field
    field = random.choice(fields)

    interest1 = random.choice(interests)
    interest2 = random.choice([inter for inter in interests if inter != interest1])
    interest3 = random.choice([inter for inter in interests if inter != interest1 and inter != interest2])
    interest4 = random.choice([inter for inter in interests if inter != interest1 and inter != interest2 and inter != interest3])
    interest5 = random.choice([inter for inter in interests if inter != interest1 and inter != interest2 and inter != interest3 and inter != interest4])

    purpose = random.choice(purposes)

    # Attends university (1 or 0)
    attends_university = 1 if birth_year > 1994 else random.choice([0, 1])
    uniOnly = 0
    
    # University
    university = ""
    if attends_university:
        uniOnly = random.choices([0, 1], weights=[0.15,0.85])[0]

        # Choose a university from the list
        if mef_count < 75:
            university = "MEF University"
            mef_count += 1
        else:
            university = random.choice([uni for uni in universities if uni != "MEF University"])
    
    # Workplace
    workplace = ""
    if birth_year <= 1994 or (attends_university and random.choice([True, False])):
        workplace = random.choice(workplaces)
    
    # Online meetings (1 or 0)
    online = random.choice([0, 1])
    f2f = random.choice([0, 1])
    while online == 0 and f2f == 0:
        online = random.choice([0, 1])
        f2f = random.choice([0, 1])

    if f2f == 1:
        priority = random.choices([0,1,2,3,4,5], weights=[0.165,0.165,0.165,0.165,0.175,0.165])[0]
    else:
        priority = random.choice([0,1,2,3,5])
    
    # Country, city, and district
    country = "Turkiye"
    city = assign_city(attends_university,university)
    dist_data=cities_to_district[city]
    district = random.choice(dist_data)
    
    # Join date between January 2023 and June 2024
    join_date = str(fake.date_between_dates(start_join_date, end_join_date))
    
    # Rating from 1 to 5 (mostly over 3.5)
    rating = round(random.uniform(3.5, 5.0), 2) if random.random() > 0.3 else round(random.uniform(2.5, 4.5), 2)
    

    obj = {
        "user_id": user_id,
        "name": name,
        "surname": surname,
        "email": email,
        "birth_date": birth_date,
        "allow_opposite_gender": allow_opposite_gender,
        "gender": gender,
        "field": field,
        "interest1": interest1,
        "interest2": interest2,
        "interest3": interest3,
        "interest4": interest4,
        "interest5": interest5,
        "attends_university": attends_university,
        "university": university,
        "workplace": workplace,
        "purpose": purpose,
        "online": online,
        "f2f": f2f,
        "country": country,
        "city": city,
        "district": district,
        "join_date": join_date,
        "rating": rating,
        "uniOnly": uniOnly,
        "priority": priority
    }
    
    # Format the data entry
    entry = f"{user_id}/{name}/{surname}/{email}/{birth_date}/{allow_opposite_gender}/{gender}/{field}/{interest1}/{interest2}/{interest3}/{interest4}/{interest5}/{attends_university}/{university}/{workplace}/{purpose}/{online}/{f2f}/{country}/{city}/{district}/{join_date}/{rating}/{uniOnly}/{priority}\n"
    
    # Add the entry to the data list
    data.append(entry)
    json_data.append(obj)


# Save the data to a .txt file with UTF-8 encoding
file_path = "./WnM_datatset.txt"
with open(file_path, "w", encoding="utf-8") as file:
    file.writelines(data)

file_path_json = "./users.json"
with open(file_path_json, "w", encoding="utf-8") as file:
    file.write(json.dumps(json_data, ensure_ascii=False))

# Provide the file path as the output
file_path

# Provide the file path as the output
print(f"Data saved to {file_path}")

main()

