import random
import pandas as pd
from faker import Faker
import json
from main import main

fake = Faker("tr_TR")  

# Constants
num_entries = 1000
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



names = [
    "Ahmet", "Mehmet", "Mustafa", "Fatma", "Ayşe", "Emine", "Hatice", "Ali", "Hüseyin", "Hasan",
    "Yusuf", "Osman", "Ömer", "İsmail", "İbrahim", "Murat", "Süleyman", "Hakan", "Halil", "İsmet",
    "Nur", "Zeynep", "Derya", "Burak", "Elif", "Gökhan", "Seda", "Cem", "Deniz", "Kemal", "Gül",
    "Serkan", "Sevgi", "Selim", "Cihan", "Ebru", "Erdem", "Can", "Gizem", "Ercan", "Yasemin",
    "Yasin", "Ferhat", "Berkay", "Ceren", "Oğuz", "Tuğçe", "Tolga", "Özge", "Ege", "Davud", "Batuhan",
    "Fatih", "Mert", "Berke", "Yiğit", "Efe", "Miraç", "Atlas", "Eylül", "Derin", "Altin", "Yaren",
    "Emir", "Aleyna", "Berat", "Duygu", "Irem", "Esra", "Azra", "Yakup", "Bahar", "Merve", "Büşra",
    "Cansu", "Eda", "Recep", "Selen", "Cafer", "Tuğba", "Kenan", "Orhan", "Kübra", "Harun", "Levent",
    "Didem", "Koray", "Arzu", "Engin", "Çağla", "Taner", "Nihan", "Şeyma", "Serdar", "Bilge", "Nisa",
    "Doğan", "Rüya", "Volkan", "Pınar", "Erdal", "Burcu", "Dilek", "Esma", "Umut", "Sema", "Hülya",
    "Bülent", "Yavuz", "Onur", "Mediha", "Tufan", "Leyla", "Tanju", "Neşe", "Verda", "Güliz", "Bahadır",
    "Şule", "Doğru", "Aylin", "Kaya", "Semra", "Zeliha", "Erkan", "Nazlı", "Şenay", "Gülden", "Fırat",
    "Figen", "Alper", "Billur", "Lale", "Arda", "Nihal", "Canan", "Ferdi", "Sevinç",
    "Tuncay", "Serpil", "Nurgül", "Gülay", "Fikret", "Reyhan", "Suna", "Hamza", "Berk", "Berkan",
    "Zehra", "Sultan", "Aysel", "Gülsüm", "Sevil", "Şükrü", "Gülşen", "Şeref", "Gönül",
    "Feride", "Şaban", "Sibel", "Adem", "Fadime", "Metin", "Gülten", "Turan", "Nalan", "Serap", "Sedat",
    "Tuncay", "Nurdan", "Mehmet Ali", "Sevim", "Ersin", "Tülay", "Hakkı", "Leyla", "Mehmet Emin", 
    "Handan", "Ethem", "Erhan", "Salih", "Seher", "Fulya", "Perihan", "Özcan", "Bekir", "Hamdi", "Gülizar",
    "Ercüment", "Gülşah", "Ahmet Ali", "Ayşegül", "Zeki", "Ali Rıza", "Filiz", "Özlem", "Şevket", "Asuman",
    "Sinan", "Necati", "Ahu", "Emin", "Nesrin", "Müge", "Yakup", "Şule", "Nurettin", "Ayfer", "Kadir",
    "Yeliz", "Şengül", "Barış", "Fuat", "Selda", "Nihat", "Seval", "Mikail", "Nazan", "Vedat", "Gülay",
    "Mustafa Kemal", "Sevgi", "Mahir", "Hilmi", "Zerrin", "Yılmaz", "Aysun", "Şahin", "Pınar",
    "Abdullah", "Neslihan", "Emel", "Halit", "Nesibe", "Elif", "Bülent", "Sevinç", "Necmettin",
    "Şerif", "Nuray", "Cemal", "Ayla", "Özlem", "Cengiz", "Musa", "Meral", "Şebnem", "Nilgün",
    "Selçuk", "Songül", "Halil İbrahim", "Muhammet", "Ferit", "Hikmet", "Kazım", "Eylem", "İnci",
    "Cüneyt", "Erdoğan", "Feray", "Okan", "Mehtap", "Kamil", "Semiha", "Ayten", "Meryem", "Sami", "Nuriye",
    "Feridun", "Tülin", "Cahit", "Şenay", "Muharrem", "Füsun", "Birsen", "Kerim",
    "Savaş", "Birgül", "Berrin", "İlhan", "Gülsüm", "Adnan", "Yunus", "Şükran",
    "Atilla", "Figen", "Nergis", "Behçet", "Gülcan", "Selahattin", "Dilek", "Kader", "Tevfik",
    "Mazlum", "Merve", "Filiz", "Tarık", "Selami",
    "Gülsen", "Ferhan", "Müjgan", "Orçun", "Asım", "Gülgün", "Veli", "Necip",
    "Feyza", "Haluk", "Gülbahar", "Ekrem", "Rıza", "Rıfat", "Nermin", "Burak", "Güllü",
    "Ergin", "Yıldırım", "Soner", "Önder", "Özgür", "Ümit", "Özlem"
]



surnames = [
    "Yılmaz", "Kaya", "Demir", "Şahin", "Çelik", "Öztürk", "Yıldız", "Kılıç", "Arslan", "Koç",
    "Aydın", "Doğan", "Çetin", "Kurt", "Koca", "Aslan", "Aksoy", "Çakır", "Turan", "Taş",
    "Kaplan", "Özdemir", "Ateş", "Güler", "Karadağ", "Güneş", "Çoban", "Bulut", "Polat", "Şimşek",
    "Gündoğdu", "Kurtuluş", "Erdoğan", "Şen", "Yalçın", "Çalışkan", "Akyüz", "Yılmazer", "Korkmaz", "Avcı",
    "Uysal", "Şentürk", "Gür", "Er", "Sarı", "Koçak", "Çetinkaya", "Türk", "Alkan",
    "Serbest", "Bozkurt", "Bayraktar", "Aydemir", "Gül", "Erbay", "Şahiner", "Erdem", "Uzun",
    "Tosun", "Erçetin", "Gürbüz", "Yaman", "Sönmez", "Taşkın", "Koçyiğit", "Kartal",
    "Orhan", "Tunç", "Baş", "Can", "Duman", "Bayram", "Cengiz", "Göçer", "Büyük", "Ay",
    "Özcan", "Pamuk", "Akgül", "Demirel", "Özkan", "Demircan", "Bora", "Batı", 
    "Işık", "Bıçakhan", "Şolta", "Kazanan", "Tatlıtuğ", "Turgal", "Boztaş", "Oran", "Karalı",
    "Kayman", "Algın", "Alim", "Savaş", "Cebeci", "Tanrıverdi", "Altuğ", "Sevecen", "Karaca",
    "Tüfekçi", "Tekin", "Aktaş", "Özbek", "Demirci", "Köse", "Güney", "Acar", "Eroğlu",
    "Gündüz", "Oğuz", "Kayaalp", "Alp", "Öz", "Güngör", "Karademir", "Uçar", "Akın",
    "Sancak", "Arı", "Karataş", "Çınar", "Bilgin", "Aygün", "Karaman", "Karahan", "Bülbül",
    "Aydoğan", "Keleş", "Doğru", "Atalay", "Akbulut", "Küçük", "Karakuş", "Ertaş",
    "Eren", "Akça", "Berk", "Köksal", "Çiçek", "Aksu", "Özmen", "Ay", "Akkuş", "Kocaman",
    "Sarıkaya", "Akgün", "Bilge", "Kurtul", "Karakaş", "Açıkgöz", "Arıkan", "Karagöz", "Akyıldız",
    "Akbaş", "Güçlü", "Güzel", "Genç", "Büyük", "Tuncer", "Güven", "Özen", "Çiçek", "Can",
    "Yüksel", "Atasoy", "Çiftçi", "Duman", "Sönmez", "Göçer", "Yavuz"
]

# Lists of possible values for some columns
# Dictionary that maps universities to their cities
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
    "Physics", "Chemistry", "Biology", "Environmental Science", "Architecture, Industrial Engineering"
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
]

# Cities
cities = [
    "Istanbul", "Ankara", "Izmir", "Antalya", "Bursa", "Adana", "Gaziantep", "Samsun", "Mersin", "Konya",
    "Trabzon", "Kayseri", "Van", "Diyarbakir", "Erzurum", "Denizli", "Kocaeli", "Sakarya", "Eskisehir",
    "Canakkale", "Mugla"
]

# Districts
districts = [
    "Kadikoy", "Besiktas", "Bakirkoy", "Sisli", "Sariyer", "Uskudar", "Kizilay", "Cankaya", "Bornova", "Karsiyaka",
    "Maltepe", "Kartal", "Beyoglu", "Fatih", "Beylikduzu", "Atasehir", "Bagcilar", "Bahcelievler", "Zeytinburnu",
    "Mamak", "Altindag", "Etimesgut", "Kecioren", "Yenimahalle", "Gaziemir", "Buca", "Guzelbahce", "Konak",
    "Nilufer", "Yuregir", "Mezitli", "Ilkadim", "Merkezefendi", "Kocasinan"
]

interests = [
    'Native App Development', 'Cross-platform App Development', 'Front End Design', 'Back End Design', 'Java', 'Python', 'Unity Game Development', 
    'Unreal Engine Game Devlopment', 'Mobile Game Development', 'Android', 'IOS', 'JavaScript', 'Machine Learning', 'Data Science', 
    'Artificial Intelligence', 'Web Development', 'Mobile Development', 'Cloud Computing', 'Internet of Things (IoT)', 'Cybersecurity', 
    'Blockchain Technology', 'Augmented Reality', 'Virtual Reality', 'Computer Graphics', 'Robotics', 'Quantum Computing', 'Bioinformatics', 
    'Natural Language Processing', 'Image Generation', 'Graphic Design', 'Entrepreneurship', 'Startup', 'Marketing', 'E-commerce', 
    'Illustration', 'Animation', 'Photography', 'Video Production', 'Music Production', 'Creative Writing', 'Film Making', 'Interior Design', 
    'Fashion Design', 'Typography', 'Fine Arts', 'Digital Art', 'Physics', 'Chemistry', 'Biology', 'Astronomy', 'Geology', 'Ecology', 'Mathematics', 
    'Statistics', 'Neuroscience', 'Genetics', 'Meteorology', 'Oceanography', 'Botany', 'Literature', 'Languages', 'Computer Networking', 
    'Database Management', 'DevOps', 'User Experience (UX) Design', 'User Interface (UI) Design', 'Ethical Hacking', 'Penetration Testing', 
    'Digital Marketing', 'Content Writing', 'Search Engine Optimization (SEO)', 'Quality Assurance (QA)', 'Virtual Assistant Services', 
    'Technical Support', 'Freelancing', 'Generative AI', 'Software Development', 'Flutter development', 'React Native Development', 'Embedded Systems'
]

purposes = [
    "project partner", "startup", "networking", "brain storming", "project assist", "freelance", "other", 'study partner'
]


cities_to_district = {
    "Istanbul": ["Kadikoy", "Besiktas", "Bakirkoy", "Sisli", "Sariyer", "Uskudar","Mecidiyekoy", "Taksim", "Erenkoy", "Tarabya", "Levent", "4. Levent"],
    "Ankara": ["Cankaya", "Kizilay", "Kecioren", "Mamak", "Etimesgut", "Yenimahalle", "Sincan"],
    "Izmir": ["Konak", "Bornova", "Karsiyaka", "Buca", "Guzelyali", "Alsancak", "Bayrakli"],
    "Antalya": ["Muratpasa", "Konyaalti", "Kepez", "Dosemealti", "Lara", "Aksu"],
    "Bursa": ["Osmangazi", "Nilufer", "Yildirim", "Gursu", "Gemlik", "Mudanya", "Inegol"],
    "Adana": ["Seyhan", "Yuregir", "Ceyhan", "Aladag", "Karaisali"],
    "Gaziantep": ["Sehitkamil", "Sahinbey", "Nizip", "Oguzeli", "Karkamis"],
    "Samsun": ["Ilkadim", "Atakum", "Canik", "Tekkeko", "Yakakent"],
    "Mersin": ["Akdeniz", "Yenisehir", "Mezitli", "Toroslar", "Erdemli"],
    "Konya": ["Selcuklu", "Meram", "Karatay", "Ereğli", "Beyşehir"],
    "Trabzon": ["Ortahisar", "Akcaabat", "Yomra", "Arsin", "Arakli"],
    "Kayseri": ["Melikgazi", "Kocasinan", "Talas", "Bünyan", "Felahiye"],
    "Van": ["İpekyolu", "Tusba", "Edremit", "Ercis", "Gurpinar"],
    "Diyarbakir": ["Bağlar", "Yenişehir", "Sur", "Ergani", "Bismil"],
    "Erzurum": ["Yakutiye", "Palandoken", "Aziziye", "Oltu", "Karakocan"],
    "Denizli": ["Merkezefendi", "Pamukkale", "Buldan", "Sarayköy", "Çal"],
    "Kocaeli": ["İzmit", "Gebze", "Körfez", "Darica", "Gölcük"],
    "Sakarya": ["Serdivan", "Adapazari", "Arifiye", "Sapanca", "Ferizli"],
    "Eskisehir": ["Tepebasi", "Odunpazari", "Çankaya", "Sivrihisar", "Mihalgazi"],
    "Canakkale": ["Merkez", "Biga", "Çan", "Eceabat", "Gelibolu"],
    "Mugla": ["Bodrum", "Fethiye", "Marmaris", "Menteşe", "Dalaman"]
}




# Initialize an empty list to store the dataset
data = []
data.append(f"id/name/surname/email/birthDate/allowOppositeGender/gender/field/interest1/interest2/interest3/interest4/interest5/attendsUni/university/workplace/purpose/online/f2f/country/city/district/joinDate/rating\n")
json_data = []

# MEF University students counter
mef_count = 0

# Generate the data
for idx in range(num_entries):
    # Create user data
    user_id = start_id + idx
    name = random.choice(names)
    surname = random.choice(surnames)
    
    # Email based on name and surname
    email = f"{name.lower()}_{surname.lower()}{random.choice(['', str(random.randint(1, 99))])}@{random.choice(['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com'])}"
    
    # Random birth date, mostly from the '90s, '80s, and early 2000s
    birth_year = random.choice(range(1975, 2007))
    birth_date = f"{birth_year}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    
    # Allow opposite gender (1 or 0)
    allow_opposite_gender = random.choice([0, 1])
    
    # Gender: 'male', 'female', or 'other' (15% must be 'other')
    gender_distribution = ["male", "female", "other"]
    gender_weights = [0.425, 0.425, 0.150]
    gender = random.choices(gender_distribution, weights=gender_weights, k=1)[0]
    
    # Field
    field = random.choice(fields)

    interest1 = random.choice(interests)
    interest2 = random.choice([inter for inter in interests if inter != interest1])
    interest3 = random.choice([inter for inter in interests if inter != interest1 and inter != interest2])
    interest4 = ""
    interest5 = ""

    if random.choice([True, False]):
        interest4 = random.choice([inter for inter in interests if inter != interest1 and inter != interest2 and inter != interest3])
        if random.choice([True, False]):
            interest5 = random.choice([inter for inter in interests if inter != interest1 and inter != interest2 and inter != interest3 and inter != interest4])


    purpose = random.choice(purposes)

    # Attends university (1 or 0)
    attends_university = 1 if birth_year > 1994 else random.choice([0, 1])
    
    # University
    university = ""
    if attends_university:
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
    
    # F2F meetings (1 or 0)
    # Ensure that online and f2f are not both 0
    f2f = random.choice([0, 1])
    if online == 0 and f2f == 0:
        f2f = 1
    
    # Country, city, and district
    country = "Turkiye"
    city = assign_city(attends_university,university)
    dist_data=cities_to_district[city]
    district = random.choice(dist_data)
    
    # Join date between January 2023 and June 2024
    join_date = str(fake.date_between_dates(start_join_date, end_join_date))
    
    # Rating from 1 to 5 (mostly over 3.5)
    rating = round(random.uniform(3.5, 5.0), 2) if random.random() > 0.3 else round(random.uniform(2, 4.0), 2)

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
        "rating": rating
    }
    
    # Format the data entry
    entry = f"{user_id}/{name}/{surname}/{email}/{birth_date}/{allow_opposite_gender}/{gender}/{field}/{interest1}/{interest2}/{interest3}/{interest4}/{interest5}/{attends_university}/{university}/{workplace}/{purpose}/{online}/{f2f}/{country}/{city}/{district}/{join_date}/{rating}\n"
    
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

