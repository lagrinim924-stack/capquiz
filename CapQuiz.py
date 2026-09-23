import random

print("🌍 Welcome to CapQuiz")
print("Test your knowledge. Conquer the world.")
score = 0
questions = [
    {
        "question": "What is the capital of Switzerland?",
        "options": ["Zurich", "Geneva", "Lausanne", "Bern"],
        "answer": "Bern"
    },
    {
        "question": "What is the capital of Morocco?",
        "options": ["Casablanca", "Marrakesh", "Rabat", "Tangier"],
        "answer": "Rabat"
    },
    {
        "question": "What is the capital of Argentina?",
        "options": ["Buenos Aires", "Córdoba", "Rosario", "Mendoza"],
        "answer": "Buenos Aires"
    },
    {
        "question": "What is the capital of Canada?",
        "options": ["Toronto", "Ottawa", "Montreal", "Vancouver"],
        "answer": "Ottawa"
    },
    {
        "question": "What is the capital of Spain?",
        "options": ["Barcelona", "Madrid", "Valencia", "Seville"],
        "answer": "Madrid"
    },
    {
        "question": "What is the capital of Italy?",
        "options": ["Milan", "Naples", "Rome", "Turin"],
        "answer": "Rome"
    },
    {
        "question": "What is the capital of Belgium?",
        "options": ["Antwerp", "Bruges", "Brussels", "Ghent"],
        "answer": "Brussels"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["Osaka", "Kyoto", "Tokyo", "Nagoya"],
        "answer": "Tokyo"
    },
    {
        "question": "What is the capital of Brazil?",
        "options": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
        "answer": "Brasília"
    },
    {
        "question": "What is the capital of Norway?",
        "options": ["Bergen", "Oslo", "Trondheim", "Stavanger"],
        "answer": "Oslo"
    },
    {
        "question": "What is the capital of Egypt?",
        "options": ["Alexandria", "Giza", "Cairo", "Luxor"],
        "answer": "Cairo"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        "answer": "Canberra"
    },
    {
        "question": "What is the capital of South Korea?",
        "options": ["Busan", "Incheon", "Seoul", "Daegu"],
        "answer": "Seoul"
    },
    {
        "question": "What is the capital of Portugal?",
        "options": ["Porto", "Lisbon", "Braga", "Coimbra"],
        "answer": "Lisbon"
    },
    {
        "question": "What is the capital of Kenya?",
        "options": ["Mombasa", "Nairobi", "Kisumu", "Nakuru"],
        "answer": "Nairobi"
    },
    {
        "question": "What is the capital of Thailand?",
        "options": ["Phuket", "Chiang Mai", "Bangkok", "Pattaya"],
        "answer": "Bangkok"
    },
    {
        "question": "What is the capital of Greece?",
        "options": ["Thessaloniki", "Patras", "Athens", "Larissa"],
        "answer": "Athens"
    },
    {
        "question": "What is the capital of Austria?",
        "options": ["Salzburg", "Graz", "Vienna", "Innsbruck"],
        "answer": "Vienna"
    },
    {
        "question": "What is the capital of Poland?",
        "options": ["Kraków", "Warsaw", "Gdańsk", "Wrocław"],
        "answer": "Warsaw"
    },
    {
        "question": "What is the capital of Ireland?",
        "options": ["Cork", "Galway", "Dublin", "Limerick"],
        "answer": "Dublin"
    },
    {
        "question": "What is the capital of Denmark?",
        "options": ["Aarhus", "Odense", "Copenhagen", "Aalborg"],
        "answer": "Copenhagen"
    },
    {
        "question": "What is the capital of Finland?",
        "options": ["Espoo", "Tampere", "Helsinki", "Turku"],
        "answer": "Helsinki"
    },
    {
        "question": "What is the capital of Sweden?",
        "options": ["Gothenburg", "Malmö", "Stockholm", "Uppsala"],
        "answer": "Stockholm"
    },
    {
        "question": "What is the capital of Czech Republic?",
        "options": ["Brno", "Ostrava", "Prague", "Plzeň"],
        "answer": "Prague"
    },
    {
        "question": "What is the capital of Hungary?",
        "options": ["Debrecen", "Szeged", "Budapest", "Pécs"],
        "answer": "Budapest"
    },
    {
        "question": "What is the capital of Romania?",
        "options": ["Cluj-Napoca", "Timișoara", "Bucharest", "Iași"],
        "answer": "Bucharest"
    },
    {
        "question": "What is the capital of Croatia?",
        "options": ["Split", "Dubrovnik", "Zagreb", "Rijeka"],
        "answer": "Zagreb"
    },
    {
        "question": "What is the capital of Serbia?",
        "options": ["Novi Sad", "Niš", "Belgrade", "Kragujevac"],
        "answer": "Belgrade"
    },
    {
        "question": "What is the capital of Ukraine?",
        "options": ["Lviv", "Odesa", "Kyiv", "Kharkiv"],
        "answer": "Kyiv"
    },
    {
        "question": "What is the capital of Iceland?",
        "options": ["Akureyri", "Reykjavik", "Keflavík", "Hafnarfjörður"],
        "answer": "Reykjavik"
    },
    {
        "question": "What is the capital of Chile?",
        "options": ["Valparaíso", "Concepción", "Santiago", "Antofagasta"],
        "answer": "Santiago"
    },
    {
        "question": "What is the capital of Peru?",
        "options": ["Cusco", "Arequipa", "Lima", "Trujillo"],
        "answer": "Lima"
    },
    {
        "question": "What is the capital of Colombia?",
        "options": ["Medellín", "Cali", "Bogotá", "Cartagena"],
        "answer": "Bogotá"
    },
    {
        "question": "What is the capital of Vietnam?",
        "options": ["Ho Chi Minh City", "Da Nang", "Hanoi", "Hue"],
        "answer": "Hanoi"
    },
    {
        "question": "What is the capital of Malaysia?",
        "options": ["George Town", "Johor Bahru", "Kuala Lumpur", "Malacca"],
        "answer": "Kuala Lumpur"
    },
    {
        "question": "What is the capital of Kazakhstan?",
        "options": ["Almaty", "Shymkent", "Astana", "Aktobe"],
        "answer": "Astana"
    },
    {
        "question": "What is the capital of Uzbekistan?",
        "options": ["Samarkand", "Bukhara", "Tashkent", "Khiva"],
        "answer": "Tashkent"
    },
    {
        "question": "What is the capital of Azerbaijan?",
        "options": ["Ganja", "Baku", "Sumqayit", "Shaki"],
        "answer": "Baku"
    },
    {
        "question": "What is the capital of Jordan?",
        "options": ["Aqaba", "Irbid", "Amman", "Zarqa"],
        "answer": "Amman"
    },
    {
        "question": "What is the capital of Lebanon?",
        "options": ["Tripoli", "Sidon", "Beirut", "Tyre"],
        "answer": "Beirut"
    },
    {
        "question": "What is the capital of Oman?",
        "options": ["Salalah", "Sohar", "Muscat", "Nizwa"],
        "answer": "Muscat"
    },
    {
        "question": "What is the capital of Qatar?",
        "options": ["Al Rayyan", "Doha", "Al Wakrah", "Lusail"],
        "answer": "Doha"
    },
    {
        "question": "What is the capital of Bahrain?",
        "options": ["Riffa", "Muharraq", "Manama", "Hamad Town"],
        "answer": "Manama"
    },
    {
        "question": "What is the capital of Kuwait?",
        "options": ["Hawally", "Salmiya", "Kuwait City", "Jahra"],
        "answer": "Kuwait City"
    },
    {
        "question": "What is the capital of Tunisia?",
        "options": ["Sfax", "Sousse", "Tunis", "Bizerte"],
        "answer": "Tunis"
    },
    {
        "question": "What is the capital of Algeria?",
        "options": ["Oran", "Constantine", "Algiers", "Annaba"],
        "answer": "Algiers"
    },
    {
        "question": "What is the capital of Senegal?",
        "options": ["Saint-Louis", "Dakar", "Thiès", "Touba"],
        "answer": "Dakar"
    },
    {
        "question": "What is the capital of Ethiopia?",
        "options": ["Gondar", "Dire Dawa", "Addis Ababa", "Mekelle"],
        "answer": "Addis Ababa"
    },
    {
        "question": "What is the capital of Rwanda?",
        "options": ["Butare", "Gisenyi", "Kigali", "Ruhengeri"],
        "answer": "Kigali"
    },
    {
        "question": "What is the capital of Uganda?",
        "options": ["Entebbe", "Jinja", "Kampala", "Mbale"],
        "answer": "Kampala"
    },
    {
        "question": "What is the capital of Zimbabwe?",
        "options": ["Bulawayo", "Mutare", "Harare", "Gweru"],
        "answer": "Harare"
    },
    {
        "question": "What is the capital of Zambia?",
        "options": ["Kitwe", "Ndola", "Lusaka", "Livingstone"],
        "answer": "Lusaka"
    },
    {
        "question": "What is the capital of Botswana?",
        "options": ["Francistown", "Maun", "Gaborone", "Kasane"],
        "answer": "Gaborone"
    },
    {
        "question": "What is the capital of Namibia?",
        "options": ["Swakopmund", "Walvis Bay", "Windhoek", "Oshakati"],
        "answer": "Windhoek"
    },
    {
        "question": "What is the capital of Mauritius?",
        "options": ["Curepipe", "Quatre Bornes", "Port Louis", "Vacoas"],
        "answer": "Port Louis"
    },
    {
        "question": "What is the capital of Moldova?",
        "options": ["Bălți", "Tiraspol", "Chișinău", "Cahul"],
        "answer": "Chișinău"
    },
    {
        "question": "What is the capital of North Macedonia?",
        "options": ["Bitola", "Ohrid", "Skopje", "Kumanovo"],
        "answer": "Skopje"
    },
    {
        "question": "What is the capital of Montenegro?",
        "options": ["Budva", "Kotor", "Podgorica", "Bar"],
        "answer": "Podgorica"
    },
    {
        "question": "What is the capital of Cyprus?",
        "options": ["Limassol", "Larnaca", "Nicosia", "Paphos"],
        "answer": "Nicosia"
    },
    {
        "question": "What is the capital of Malta?",
        "options": ["Birkirkara", "Sliema", "Valletta", "Mosta"],
        "answer": "Valletta"
    },
    {
        "question": "What is the capital of Belarus?",
        "options": ["Brest", "Gomel", "Minsk", "Vitebsk"],
        "answer": "Minsk"
    },
    {
        "question": "What is the capital of Tajikistan?",
        "options": ["Khujand", "Kulob", "Dushanbe", "Qurghonteppa"],
        "answer": "Dushanbe"
    },
    {
        "question": "What is the capital of Kyrgyzstan?",
        "options": ["Osh", "Jalal-Abad", "Bishkek", "Karakol"],
        "answer": "Bishkek"
    },
    {
        "question": "What is the capital of Turkmenistan?",
        "options": ["Turkmenabat", "Mary", "Ashgabat", "Dashoguz"],
        "answer": "Ashgabat"
    },
    {
        "question": "What is the capital of Mongolia?",
        "options": ["Erdenet", "Darkhan", "Ulaanbaatar", "Choibalsan"],
        "answer": "Ulaanbaatar"
    },
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "answer": "Islamabad"
    },
    {
        "question": "What is the capital of Nepal?",
        "options": ["Pokhara", "Lalitpur", "Kathmandu", "Bharatpur"],
        "answer": "Kathmandu"
    },
    {
        "question": "What is the capital of Bhutan?",
        "options": ["Paro", "Punakha", "Thimphu", "Phuentsholing"],
        "answer": "Thimphu"
    },
    {
        "question": "What is the capital of Bangladesh?",
        "options": ["Chittagong", "Khulna", "Dhaka", "Rajshahi"],
        "answer": "Dhaka"
    },
    {
        "question": "What is the capital of Myanmar?",
        "options": ["Yangon", "Mandalay", "Naypyidaw", "Bago"],
        "answer": "Naypyidaw"
    },
    {
        "question": "What is the capital of Laos?",
        "options": ["Luang Prabang", "Pakse", "Vientiane", "Savannakhet"],
        "answer": "Vientiane"
    },
    {
        "question": "What is the capital of Cambodia?",
        "options": ["Siem Reap", "Battambang", "Phnom Penh", "Kampot"],
        "answer": "Phnom Penh"
    },
    {
        "question": "What is the capital of Brunei?",
        "options": ["Seria", "Tutong", "Bandar Seri Begawan", "Kuala Belait"],
        "answer": "Bandar Seri Begawan"
    },
    {
        "question": "What is the capital of Timor-Leste?",
        "options": ["Baucau", "Maliana", "Dili", "Suai"],
        "answer": "Dili"
    },
    {
        "question": "What is the capital of Papua New Guinea?",
        "options": ["Lae", "Madang", "Port Moresby", "Mount Hagen"],
        "answer": "Port Moresby"
    },
    {
        "question": "What is the capital of Slovenia?",
        "options": ["Maribor", "Ljubljana", "Koper", "Celje"],
        "answer": "Ljubljana"
    },
    {
        "question": "What is the capital of Slovakia?",
        "options": ["Košice", "Prešov", "Bratislava", "Žilina"],
        "answer": "Bratislava"
    },
    {
        "question": "What is the capital of Bulgaria?",
        "options": ["Plovdiv", "Varna", "Sofia", "Burgas"],
        "answer": "Sofia"
    },
    {
        "question": "What is the capital of Estonia?",
        "options": ["Tartu", "Narva", "Tallinn", "Pärnu"],
        "answer": "Tallinn"
    },
    {
        "question": "What is the capital of Latvia?",
        "options": ["Daugavpils", "Jelgava", "Riga", "Liepāja"],
        "answer": "Riga"
    },
    {
        "question": "What is the capital of Lithuania?",
        "options": ["Kaunas", "Klaipėda", "Vilnius", "Šiauliai"],
        "answer": "Vilnius"
    },
    {
        "question": "What is the capital of Albania?",
        "options": ["Durrës", "Vlorë", "Tirana", "Shkodër"],
        "answer": "Tirana"
    },
    {
        "question": "What is the capital of Bosnia and Herzegovina?",
        "options": ["Mostar", "Banja Luka", "Sarajevo", "Tuzla"],
        "answer": "Sarajevo"
    },
    {
        "question": "What is the capital of Georgia?",
        "options": ["Batumi", "Kutaisi", "Tbilisi", "Rustavi"],
        "answer": "Tbilisi"
    },
    {
        "question": "What is the capital of Armenia?",
        "options": ["Gyumri", "Vanadzor", "Yerevan", "Hrazdan"],
        "answer": "Yerevan"
    },
    {
        "question": "What is the capital of Afghanistan?",
        "options": ["Herat", "Kandahar", "Kabul", "Mazar-i-Sharif"],
        "answer": "Kabul"
    },
    {
        "question": "What is the capital of Andorra?",
        "options": ["Encamp", "Canillo", "Andorra la Vella", "La Massana"],
        "answer": "Andorra la Vella"
    },
    {
        "question": "What is the capital of Angola?",
        "options": ["Huambo", "Lobito", "Luanda", "Benguela"],
        "answer": "Luanda"
    },
    {
        "question": "What is the capital of Antigua and Barbuda?",
        "options": ["Codrington", "Saint John's", "All Saints", "Liberta"],
        "answer": "Saint John's"
    },
    {
        "question": "What is the capital of Bahamas?",
        "options": ["Freeport", "Nassau", "Marsh Harbour", "George Town"],
        "answer": "Nassau"
    },
    {
        "question": "What is the capital of Barbados?",
        "options": ["Bridgetown", "Oistins", "Speightstown", "Holetown"],
        "answer": "Bridgetown"
    },
    {
        "question": "What is the capital of Belize?",
        "options": ["Belmopan", "Belize City", "San Ignacio", "Orange Walk"],
        "answer": "Belmopan"
    },
    {
        "question": "What is the capital of Benin?",
        "options": ["Cotonou", "Porto-Novo", "Abomey", "Parakou"],
        "answer": "Porto-Novo"
    },
    {
        "question": "What is the capital of Bolivia?",
        "options": ["La Paz", "Santa Cruz", "Sucre", "Cochabamba"],
        "answer": "Sucre"
    },
    {
        "question": "What is the capital of Burkina Faso?",
        "options": ["Bobo-Dioulasso", "Ouagadougou", "Koudougou", "Banfora"],
        "answer": "Ouagadougou"
    },
    {
        "question": "What is the capital of Burundi?",
        "options": ["Gitega", "Bujumbura", "Ngozi", "Muyinga"],
        "answer": "Gitega"
    },
    {
        "question": "What is the capital of Cabo Verde?",
        "options": ["Mindelo", "Praia", "Santa Maria", "Assomada"],
        "answer": "Praia"
    },
    {
        "question": "What is the capital of Cameroon?",
        "options": ["Douala", "Yaoundé", "Garoua", "Bamenda"],
        "answer": "Yaoundé"
    },
    {
        "question": "What is the capital of Central African Republic?",
        "options": ["Bimbo", "Bangui", "Berbérati", "Bambari"],
        "answer": "Bangui"
    },
    {
        "question": "What is the capital of Chad?",
        "options": ["Moundou", "Abéché", "N'Djamena", "Sarh"],
        "answer": "N'Djamena"
    },
    {
        "question": "What is the capital of China?",
        "options": ["Shanghai", "Beijing", "Guangzhou", "Shenzhen"],
        "answer": "Beijing"
    },
    {
        "question": "What is the capital of Comoros?",
        "options": ["Fomboni", "Moroni", "Mutsamudu", "Domoni"],
        "answer": "Moroni"
    },
    {
        "question": "What is the capital of Democratic Republic of the Congo?",
        "options": ["Lubumbashi", "Goma", "Kinshasa", "Kisangani"],
        "answer": "Kinshasa"
    },
    {
        "question": "What is the capital of Republic of the Congo?",
        "options": ["Pointe-Noire", "Brazzaville", "Dolisie", "Nkayi"],
        "answer": "Brazzaville"
    },
    {
        "question": "What is the capital of Costa Rica?",
        "options": ["Alajuela", "Cartago", "San José", "Heredia"],
        "answer": "San José"
    },
    {
        "question": "What is the capital of Cuba?",
        "options": ["Santiago de Cuba", "Camagüey", "Havana", "Holguín"],
        "answer": "Havana"
    },
    {
        "question": "What is the capital of Djibouti?",
        "options": ["Ali Sabieh", "Tadjoura", "Djibouti City", "Obock"],
        "answer": "Djibouti City"
    },
    {
        "question": "What is the capital of Dominica?",
        "options": ["Portsmouth", "Roseau", "Marigot", "Mahaut"],
        "answer": "Roseau"
    },
    {
        "question": "What is the capital of Dominican Republic?",
        "options": ["Santiago de los Caballeros", "La Romana", "Santo Domingo", "Puerto Plata"],
        "answer": "Santo Domingo"
    },
    {
        "question": "What is the capital of Ecuador?",
        "options": ["Guayaquil", "Cuenca", "Quito", "Loja"],
        "answer": "Quito"
    },
    {
        "question": "What is the capital of El Salvador?",
        "options": ["Santa Ana", "San Miguel", "San Salvador", "Sonsonate"],
        "answer": "San Salvador"
    },
    {
        "question": "What is the capital of Equatorial Guinea?",
        "options": ["Bata", "Malabo", "Ciudad de la Paz", "Ebebiyín"],
        "answer": "Ciudad de la Paz"
    },
    {
        "question": "What is the capital of Eritrea?",
        "options": ["Massawa", "Keren", "Asmara", "Assab"],
        "answer": "Asmara"
    },
    {
        "question": "What is the capital of Eswatini?",
        "options": ["Manzini", "Mbabane", "Lobamba", "Siteki"],
        "answer": "Mbabane"
    },
    {
        "question": "What is the capital of Fiji?",
        "options": ["Nadi", "Lautoka", "Suva", "Labasa"],
        "answer": "Suva"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Lyon", "Marseille", "Paris", "Nice"],
        "answer": "Paris"
    },
    {
        "question": "What is the capital of Gabon?",
        "options": ["Port-Gentil", "Franceville", "Libreville", "Oyem"],
        "answer": "Libreville"
    },
    {
        "question": "What is the capital of Gambia?",
        "options": ["Brikama", "Bakau", "Banjul", "Serrekunda"],
        "answer": "Banjul"
    },
    {
        "question": "What is the capital of Germany?",
        "options": ["Munich", "Hamburg", "Berlin", "Frankfurt"],
        "answer": "Berlin"
    },
    {
        "question": "What is the capital of Ghana?",
        "options": ["Kumasi", "Tamale", "Accra", "Takoradi"],
        "answer": "Accra"
    },
    {
        "question": "What is the capital of Grenada?",
        "options": ["Gouyave", "Grenville", "St. George's", "Sauteurs"],
        "answer": "St. George's"
    },
    {
        "question": "What is the capital of Guatemala?",
        "options": ["Antigua Guatemala", "Quetzaltenango", "Guatemala City", "Escuintla"],
        "answer": "Guatemala City"
    },
    {
        "question": "What is the capital of Guinea?",
        "options": ["Kankan", "Kindia", "Conakry", "Labé"],
        "answer": "Conakry"
    },
    {
        "question": "What is the capital of Guinea-Bissau?",
        "options": ["Bafatá", "Bissau", "Gabú", "Cacheu"],
        "answer": "Bissau"
    },
    {
        "question": "What is the capital of Guyana?",
        "options": ["Linden", "New Amsterdam", "Georgetown", "Bartica"],
        "answer": "Georgetown"
    },
    {
        "question": "What is the capital of Haiti?",
        "options": ["Cap-Haïtien", "Gonaïves", "Port-au-Prince", "Jacmel"],
        "answer": "Port-au-Prince"
    },
    {
        "question": "What is the capital of Honduras?",
        "options": ["San Pedro Sula", "La Ceiba", "Tegucigalpa", "Comayagua"],
        "answer": "Tegucigalpa"
    },
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Bengaluru", "Kolkata"],
        "answer": "New Delhi"
    },
    {
        "question": "What is the capital of Indonesia?",
        "options": ["Jakarta", "Surabaya", "Bandung", "Medan"],
        "answer": "Jakarta"
    },
    {
        "question": "What is the capital of Iran?",
        "options": ["Mashhad", "Isfahan", "Tehran", "Shiraz"],
        "answer": "Tehran"
    },
    {
        "question": "What is the capital of Iraq?",
        "options": ["Basra", "Mosul", "Baghdad", "Erbil"],
        "answer": "Baghdad"
    },
    {
        "question": "What is the capital of Israel?",
        "options": ["Tel Aviv", "Haifa", "Jerusalem", "Eilat"],
        "answer": "Jerusalem"
    },
    {
        "question": "What is the capital of Jamaica?",
        "options": ["Montego Bay", "Kingston", "Spanish Town", "Portmore"],
        "answer": "Kingston"
    },
    {
        "question": "What is the capital of Kiribati?",
        "options": ["Betio", "Bairiki", "South Tarawa", "Banraeaba"],
        "answer": "South Tarawa"
    },
    {
        "question": "What is the capital of Lesotho?",
        "options": ["Maseru", "Mafeteng", "Hlotse", "Teyateyaneng"],
        "answer": "Maseru"
    },
    {
        "question": "What is the capital of Liberia?",
        "options": ["Buchanan", "Gbarnga", "Monrovia", "Kakata"],
        "answer": "Monrovia"
    },
    {
        "question": "What is the capital of Libya?",
        "options": ["Benghazi", "Misrata", "Tripoli", "Sabha"],
        "answer": "Tripoli"
    },
    {
        "question": "What is the capital of Liechtenstein?",
        "options": ["Balzers", "Vaduz", "Schaan", "Triesen"],
        "answer": "Vaduz"
    },
    {
        "question": "What is the capital of Luxembourg?",
        "options": ["Esch-sur-Alzette", "Differdange", "Luxembourg City", "Dudelange"],
        "answer": "Luxembourg City"
    },
    {
        "question": "What is the capital of Madagascar?",
        "options": ["Toamasina", "Antsirabe", "Antananarivo", "Mahajanga"],
        "answer": "Antananarivo"
    },
    {
        "question": "What is the capital of Malawi?",
        "options": ["Blantyre", "Mzuzu", "Lilongwe", "Zomba"],
        "answer": "Lilongwe"
    },
    {
        "question": "What is the capital of Maldives?",
        "options": ["Addu City", "Malé", "Fuvahmulah", "Kulhudhuffushi"],
        "answer": "Malé"
    },
    {
        "question": "What is the capital of Mali?",
        "options": ["Sikasso", "Mopti", "Bamako", "Ségou"],
        "answer": "Bamako"
    },
    {
        "question": "What is the capital of Marshall Islands?",
        "options": ["Ebeye", "Majuro", "Jaluit", "Wotje"],
        "answer": "Majuro"
    },
    {
        "question": "What is the capital of Mauritania?",
        "options": ["Nouadhibou", "Atar", "Nouakchott", "Rosso"],
        "answer": "Nouakchott"
    },
    {
        "question": "What is the capital of Mexico?",
        "options": ["Guadalajara", "Monterrey", "Mexico City", "Puebla"],
        "answer": "Mexico City"
    },
    {
        "question": "What is the capital of Micronesia?",
        "options": ["Kolonia", "Palikir", "Weno", "Colonia"],
        "answer": "Palikir"
    },
    {
        "question": "What is the capital of Monaco?",
        "options": ["Monte Carlo", "La Condamine", "Monaco", "Fontvieille"],
        "answer": "Monaco"
    },
    {
        "question": "What is the capital of Mozambique?",
        "options": ["Beira", "Nampula", "Maputo", "Matola"],
        "answer": "Maputo"
    },
    {
        "question": "What is the capital of Nauru?",
        "options": ["Yaren", "Aiwo", "Meneng", "Anibare"],
        "answer": "Yaren"
    },
    {
        "question": "What is the capital of Netherlands?",
        "options": ["Rotterdam", "Amsterdam", "The Hague", "Utrecht"],
        "answer": "Amsterdam"
    },
    {
        "question": "What is the capital of New Zealand?",
        "options": ["Auckland", "Christchurch", "Wellington", "Hamilton"],
        "answer": "Wellington"
    },
    {
        "question": "What is the capital of Nicaragua?",
        "options": ["León", "Granada", "Managua", "Masaya"],
        "answer": "Managua"
    },
    {
        "question": "What is the capital of Niger?",
        "options": ["Zinder", "Maradi", "Niamey", "Agadez"],
        "answer": "Niamey"
    },
    {
        "question": "What is the capital of Nigeria?",
        "options": ["Lagos", "Kano", "Abuja", "Ibadan"],
        "answer": "Abuja"
    },
    {
        "question": "What is the capital of North Korea?",
        "options": ["Hamhung", "Wonsan", "Pyongyang", "Kaesong"],
        "answer": "Pyongyang"
    },
    {
        "question": "What is the capital of Palau?",
        "options": ["Koror", "Melekeok", "Airai", "Ngerulmud"],
        "answer": "Ngerulmud"
    },
    {
        "question": "What is the capital of Panama?",
        "options": ["Colón", "David", "Panama City", "Chitré"],
        "answer": "Panama City"
    },
    {
        "question": "What is the capital of Paraguay?",
        "options": ["Ciudad del Este", "Encarnación", "Asunción", "Luque"],
        "answer": "Asunción"
    },
    {
        "question": "What is the capital of Philippines?",
        "options": ["Cebu City", "Davao City", "Manila", "Quezon City"],
        "answer": "Manila"
    },
    {
        "question": "What is the capital of Russia?",
        "options": ["Saint Petersburg", "Novosibirsk", "Moscow", "Kazan"],
        "answer": "Moscow"
    },
    {
        "question": "What is the capital of Saint Kitts and Nevis?",
        "options": ["Basseterre", "Charlestown", "Sandy Point", "Cayon"],
        "answer": "Basseterre"
    },
    {
        "question": "What is the capital of Saint Lucia?",
        "options": ["Castries", "Vieux Fort", "Soufrière", "Gros Islet"],
        "answer": "Castries"
    },
    {
        "question": "What is the capital of Saint Vincent and the Grenadines?",
        "options": ["Kingstown", "Georgetown", "Barrouallie", "Chateaubelair"],
        "answer": "Kingstown"
    },
    {
        "question": "What is the capital of Samoa?",
        "options": ["Apia", "Salelologa", "Vaitele", "Safotu"],
        "answer": "Apia"
    },
    {
        "question": "What is the capital of San Marino?",
        "options": ["Borgo Maggiore", "Serravalle", "San Marino", "Domagnano"],
        "answer": "San Marino"
    },
    {
        "question": "What is the capital of São Tomé and Príncipe?",
        "options": ["Santo António", "São Tomé", "Neves", "Trindade"],
        "answer": "São Tomé"
    },
    {
        "question": "What is the capital of Saudi Arabia?",
        "options": ["Jeddah", "Mecca", "Riyadh", "Medina"],
        "answer": "Riyadh"
    },
    {
        "question": "What is the capital of Seychelles?",
        "options": ["Victoria", "Anse Boileau", "Beau Vallon", "Takamaka"],
        "answer": "Victoria"
    },
    {
        "question": "What is the capital of Sierra Leone?",
        "options": ["Bo", "Kenema", "Freetown", "Makeni"],
        "answer": "Freetown"
    },
    {
        "question": "What is the capital of Singapore?",
        "options": ["Jurong", "Woodlands", "Singapore", "Tampines"],
        "answer": "Singapore"
    },
    {
        "question": "What is the capital of Solomon Islands?",
        "options": ["Gizo", "Honiara", "Auki", "Munda"],
        "answer": "Honiara"
    },
    {
        "question": "What is the capital of Somalia?",
        "options": ["Hargeisa", "Kismayo", "Mogadishu", "Bosaso"],
        "answer": "Mogadishu"
    },
    {
        "question": "What is the capital of South Africa?",
        "options": ["Cape Town", "Johannesburg", "Pretoria", "Durban"],
        "answer": "Pretoria"
    },
    {
        "question": "What is the capital of South Sudan?",
        "options": ["Wau", "Malakal", "Juba", "Yei"],
        "answer": "Juba"
    },
    {
        "question": "What is the capital of Sri Lanka?",
        "options": ["Colombo", "Kandy", "Sri Jayawardenepura Kotte", "Galle"],
        "answer": "Sri Jayawardenepura Kotte"
    },
    {
        "question": "What is the capital of Sudan?",
        "options": ["Omdurman", "Port Sudan", "Khartoum", "Kassala"],
        "answer": "Khartoum"
    },
    {
        "question": "What is the capital of Suriname?",
        "options": ["Lelydorp", "Nieuw Nickerie", "Paramaribo", "Moengo"],
        "answer": "Paramaribo"
    },
    {
        "question": "What is the capital of Syria?",
        "options": ["Aleppo", "Homs", "Damascus", "Latakia"],
        "answer": "Damascus"
    },
    {
        "question": "What is the capital of Tanzania?",
        "options": ["Dar es Salaam", "Arusha", "Dodoma", "Mwanza"],
        "answer": "Dodoma"
    },
    {
        "question": "What is the capital of Togo?",
        "options": ["Sokodé", "Kara", "Lomé", "Atakpamé"],
        "answer": "Lomé"
    },
    {
        "question": "What is the capital of Tonga?",
        "options": ["Neiafu", "Nuku'alofa", "Haveluloto", "Pangai"],
        "answer": "Nuku'alofa"
    },
    {
        "question": "What is the capital of Trinidad and Tobago?",
        "options": ["San Fernando", "Chaguanas", "Port of Spain", "Arima"],
        "answer": "Port of Spain"
    },
    {
        "question": "What is the capital of Turkey?",
        "options": ["Istanbul", "Izmir", "Ankara", "Bursa"],
        "answer": "Ankara"
    },
    {
        "question": "What is the capital of Tuvalu?",
        "options": ["Funafuti", "Vaiaku", "Asau", "Savave"],
        "answer": "Funafuti"
    },
    {
        "question": "What is the capital of United Arab Emirates?",
        "options": ["Dubai", "Sharjah", "Abu Dhabi", "Ajman"],
        "answer": "Abu Dhabi"
    },
    {
        "question": "What is the capital of United Kingdom?",
        "options": ["Manchester", "Birmingham", "London", "Liverpool"],
        "answer": "London"
    },
    {
        "question": "What is the capital of United States?",
        "options": ["New York City", "Los Angeles", "Washington, D.C.", "Chicago"],
        "answer": "Washington, D.C."
    },
    {
        "question": "What is the capital of Uruguay?",
        "options": ["Salto", "Punta del Este", "Montevideo", "Paysandú"],
        "answer": "Montevideo"
    },
    {
        "question": "What is the capital of Vanuatu?",
        "options": ["Luganville", "Port Vila", "Isangel", "Sola"],
        "answer": "Port Vila"
    },
    {
        "question": "What is the capital of Vatican City?",
        "options": ["Vatican City", "Rome", "Castel Gandolfo", "Fiumicino"],
        "answer": "Vatican City"
    },
    {
        "question": "What is the capital of Venezuela?",
        "options": ["Maracaibo", "Valencia", "Caracas", "Barquisimeto"],
        "answer": "Caracas"
    },
    {
        "question": "What is the capital of Yemen?",
        "options": ["Aden", "Taiz", "Sana'a", "Hodeidah"],
        "answer": "Sana'a"
    },
    {
        "question": "What is the capital of Palestine?",
        "options": ["Gaza City", "Hebron", "Ramallah", "East Jerusalem"],
        "answer": "East Jerusalem"
    }
]

total = len(questions)
print(f"\nTotal number of questions : {total}")

while True:
    try:
        num = int(input(f"How many questions do you want in this round: "))
        if 1<= num <= total:
            break
        print(f"Please enter a number between 1 and {total} : ")
    except ValueError:
        print("Please enter a valid number!")    


random.shuffle(questions)

for question in questions[:num]:
    print("\n" + question["question"])
    random.shuffle(question["options"])
    for i, option in enumerate(question["options"]):
        print(f"{i + 1}. {option}")
    user_answer = input("\nPlease enter your answer : ")
    if user_answer.strip().lower() == question["answer"].strip().lower():
        print("Good job! You got it right.")
        score += 1
    else:
        print("Sorry, that's incorrect. The correct answer is : " + question["answer"])
       
print(f"\nYour final score is : {score}/{num}")