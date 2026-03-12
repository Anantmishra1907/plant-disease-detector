"""
Detailed disease information for all 38 PlantVillage classes.
"""

DISEASE_DATABASE = {
    # ── APPLE ──────────────────────────────────────────────────────────────
    "Apple___Apple_scab": {
        "plant": "Apple", "disease_short": "Apple Scab", "is_healthy": False, "severity": "High",
        "description": "Apple scab is a fungal disease caused by Venturia inaequalis that produces dark, scabby lesions on leaves and fruit. It is one of the most economically significant apple diseases worldwide.",
        "symptoms": ["Olive-green to black velvety lesions on leaves", "Scabby, corky spots on fruit", "Premature leaf drop", "Cracked and deformed fruit"],
        "causes": ["Fungus Venturia inaequalis", "Wet, cool spring weather", "Poor air circulation", "Overwintering spores in fallen leaves"],
        "treatment": ["Apply fungicides (captan, myclobutanil) at 7–10 day intervals during wet periods", "Remove and destroy infected leaves", "Prune trees to improve air circulation", "Apply copper-based sprays as protective measure"],
        "prevention": ["Plant scab-resistant apple varieties (e.g., Liberty, Freedom)", "Rake and destroy fallen leaves in autumn", "Maintain good canopy airflow", "Apply preventive fungicide sprays before bud break"],
        "organic_remedies": ["Sulfur-based fungicides", "Neem oil spray", "Bicarbonate solutions", "Compost tea foliar spray"]
    },
    "Apple___Black_rot": {
        "plant": "Apple", "disease_short": "Black Rot", "is_healthy": False, "severity": "High",
        "description": "Black rot is caused by the fungus Botryosphaeria obtusa. It affects fruit, leaves, and bark, causing significant pre- and post-harvest losses.",
        "symptoms": ["Brown, circular leaf spots with purple margins", "Rotting fruit turning black", "Cankers on branches", "Mummified fruit remaining on tree"],
        "causes": ["Fungus Botryosphaeria obtusa", "Warm, humid weather", "Wounds from pruning or insects", "Stressed trees"],
        "treatment": ["Prune out and destroy infected wood", "Apply fungicides (captan, thiophanate-methyl)", "Remove mummified fruit", "Improve drainage to reduce tree stress"],
        "prevention": ["Maintain tree health through proper nutrition", "Avoid wounding trees", "Use resistant rootstocks", "Regular pruning for airflow"],
        "organic_remedies": ["Copper hydroxide spray", "Lime sulfur sprays", "Neem oil applications", "Improve soil drainage"]
    },
    "Apple___Cedar_apple_rust": {
        "plant": "Apple", "disease_short": "Cedar Apple Rust", "is_healthy": False, "severity": "Medium",
        "description": "A fungal disease caused by Gymnosporangium juniperi-virginianae that requires both apple/crabapple and eastern red cedar/juniper hosts to complete its life cycle.",
        "symptoms": ["Bright yellow-orange spots on upper leaf surface", "Tube-like structures on leaf undersides", "Deformed fruit", "Orange gelatinous galls on cedar trees"],
        "causes": ["Fungus Gymnosporangium juniperi-virginianae", "Proximity to juniper/cedar host plants", "Wet spring weather during spore release"],
        "treatment": ["Apply fungicides (myclobutanil, mancozeb) in spring", "Remove nearby juniper galls if possible", "Spray at pink bud stage through petal fall"],
        "prevention": ["Plant resistant apple varieties", "Avoid planting apple and cedar trees near each other", "Apply preventive fungicide program"],
        "organic_remedies": ["Sulfur-based fungicides early season", "Copper sprays", "Remove cedar galls"]
    },
    "Apple___healthy": {
        "plant": "Apple", "disease_short": "Healthy", "is_healthy": True, "severity": "None",
        "description": "The apple plant appears healthy with no signs of disease. Leaves are green and vibrant with no lesions, spots, or abnormalities detected.",
        "symptoms": [], "causes": [],
        "treatment": ["No treatment needed — plant is healthy!"],
        "prevention": ["Continue regular watering and fertilization", "Monitor regularly for early signs of disease", "Maintain good orchard hygiene", "Prune for airflow annually"],
        "organic_remedies": ["Preventive neem oil spray to maintain health", "Compost applications for soil health"]
    },
    # ── BLUEBERRY ──────────────────────────────────────────────────────────
    "Blueberry___healthy": {
        "plant": "Blueberry", "disease_short": "Healthy", "is_healthy": True, "severity": "None",
        "description": "The blueberry plant looks healthy. No disease symptoms detected.",
        "symptoms": [], "causes": [],
        "treatment": ["No treatment needed"],
        "prevention": ["Maintain soil pH between 4.5–5.5", "Apply acidifying fertilizers", "Water consistently and avoid waterlogging"],
        "organic_remedies": ["Sulfur to maintain soil acidity", "Compost mulch"]
    },
    # ── CHERRY ─────────────────────────────────────────────────────────────
    "Cherry_(including_sour)___Powdery_mildew": {
        "plant": "Cherry", "disease_short": "Powdery Mildew", "is_healthy": False, "severity": "Medium",
        "description": "Powdery mildew on cherry is caused by Podosphaera clandestina. It appears as a white powdery coating on leaves, shoots, and fruit, reducing photosynthesis and weakening the tree.",
        "symptoms": ["White powdery coating on leaves and shoots", "Curled or distorted young leaves", "Stunted shoot growth", "Fruit russeting"],
        "causes": ["Fungus Podosphaera clandestina", "High humidity with warm dry weather", "Poor air circulation", "Shaded conditions"],
        "treatment": ["Apply sulfur or potassium bicarbonate fungicides", "Prune affected shoots", "Apply systemic fungicides (myclobutanil)", "Improve canopy airflow"],
        "prevention": ["Choose resistant cherry varieties", "Prune to open canopy", "Avoid excessive nitrogen fertilization", "Good site selection with full sun"],
        "organic_remedies": ["Baking soda spray (1 tsp per litre)", "Neem oil", "Diluted milk spray (40% milk / 60% water)", "Sulfur dust"]
    },
    "Cherry_(including_sour)___healthy": {
        "plant": "Cherry", "disease_short": "Healthy", "is_healthy": True, "severity": "None",
        "description": "The cherry plant appears healthy with no signs of disease.",
        "symptoms": [], "causes": [],
        "treatment": ["No treatment needed"],
        "prevention": ["Regular monitoring", "Good air circulation", "Balanced fertilization"],
        "organic_remedies": ["Preventive neem oil spray"]
    },
    # ── CORN ───────────────────────────────────────────────────────────────
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "plant": "Corn (Maize)", "disease_short": "Gray Leaf Spot", "is_healthy": False, "severity": "High",
        "description": "Gray leaf spot, caused by Cercospora zeae-maydis, is one of the most yield-limiting foliar diseases of corn. It thrives in warm, humid conditions with poor airflow.",
        "symptoms": ["Rectangular tan or gray lesions with parallel margins", "Lesions run parallel to leaf veins", "Yellow halos around spots", "Premature leaf death in severe cases"],
        "causes": ["Fungus Cercospora zeae-maydis", "Warm temperatures (25–30°C)", "High humidity and extended dew periods", "Crop residue from previous season"],
        "treatment": ["Apply foliar fungicides (strobilurins, triazoles)", "Apply at VT/R1 growth stage for best results", "Choose fungicide at early disease onset"],
        "prevention": ["Plant resistant hybrids", "Rotate crops — avoid continuous corn", "Till to bury infected residue", "Improve field drainage"],
        "organic_remedies": ["Copper-based foliar sprays", "Crop rotation", "Residue management"]
    },
    "Corn_(maize)___Common_rust_": {
        "plant": "Corn (Maize)", "disease_short": "Common Rust", "is_healthy": False, "severity": "Medium",
        "description": "Common rust is caused by Puccinia sorghi. Brick-red pustules erupt through the leaf surface. While usually not devastating, severe early infection can reduce yield.",
        "symptoms": ["Small, oval, brick-red to brown powdery pustules on both leaf surfaces", "Pustules scattered randomly on leaves", "Yellowing of severely infected leaves"],
        "causes": ["Fungus Puccinia sorghi", "Cool temperatures (16–23°C)", "High humidity", "Wind-dispersed spores"],
        "treatment": ["Apply fungicides (azoxystrobin, propiconazole) at early infection", "Monitor fields at V8–VT stages", "Economic threshold: >50% plants infected before tasseling"],
        "prevention": ["Plant rust-resistant corn hybrids", "Early planting to avoid peak rust season", "Scout fields regularly"],
        "organic_remedies": ["Neem oil spray", "Copper fungicide", "Early planting to escape peak infection periods"]
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "plant": "Corn (Maize)", "disease_short": "Northern Leaf Blight", "is_healthy": False, "severity": "High",
        "description": "Northern leaf blight (NLB) caused by Exserohilum turcicum produces large cigar-shaped lesions on corn leaves, potentially reducing yields by 30–50% in severe cases.",
        "symptoms": ["Large, cigar-shaped gray-green to tan lesions (2.5–15 cm)", "Lesions appear first on lower leaves", "Dark olive-green spores on lesions in humid weather", "Premature death of severely infected plants"],
        "causes": ["Fungus Exserohilum turcicum", "Moderate temperatures (18–27°C)", "Extended periods of wet, cloudy weather", "Infected crop debris"],
        "treatment": ["Apply fungicides (strobilurins + triazoles) at V8-VT", "Products: azoxystrobin, propiconazole, tebuconazole", "Timely application critical for economic benefit"],
        "prevention": ["Plant NLB-resistant hybrids (Ht1, Ht2, HtN genes)", "Crop rotation with non-host crops", "Tillage to reduce surface residue", "Balanced N fertilization"],
        "organic_remedies": ["Copper hydroxide sprays", "Crop rotation", "Deep plowing of residue"]
    },
    "Corn_(maize)___healthy": {
        "plant": "Corn (Maize)", "disease_short": "Healthy", "is_healthy": True, "severity": "None",
        "description": "The corn plant appears healthy with no signs of foliar disease.",
        "symptoms": [], "causes": [],
        "treatment": ["No treatment needed"],
        "prevention": ["Balanced fertilization", "Adequate plant spacing", "Regular field scouting"],
        "organic_remedies": ["Compost applications", "Cover cropping"]
    },
    # ── GRAPE ──────────────────────────────────────────────────────────────
    "Grape___Black_rot": {
        "plant": "Grape", "disease_short": "Black Rot", "is_healthy": False, "severity": "High",
        "description": "Grape black rot, caused by Guignardia bidwellii, is a devastating fungal disease that can destroy entire crops. It infects leaves, shoots, and berries, turning them into hard, black mummies.",
        "symptoms": ["Tan, circular leaf lesions with dark borders", "Black, shriveled mummified berries", "Lesions on stems and tendrils", "Black pycnidia (fruiting bodies) visible in lesions"],
        "causes": ["Fungus Guignardia bidwellii", "Warm, wet weather during early season", "Overwintering mummified berries", "Poor canopy management"],
        "treatment": ["Apply fungicides (myclobutanil, mancozeb) from bud break", "Remove and destroy mummified berries and infected material", "Spray every 7–14 days during wet periods"],
        "prevention": ["Choose resistant grape varieties", "Remove overwintering inoculum", "Prune for good canopy airflow", "Apply preventive fungicide program"],
        "organic_remedies": ["Copper-based fungicides", "Sulfur sprays", "Improve canopy ventilation by leaf removal"]
    },
    "Grape___Esca_(Black_Measles)": {
        "plant": "Grape", "disease_short": "Esca (Black Measles)", "is_healthy": False, "severity": "High",
        "description": "Esca is a complex wood disease caused by multiple fungi (Phaeomoniella chlamydospora, Phaeoacremonium spp.). It leads to apoplexy (sudden vine death) and chronic decline.",
        "symptoms": ["Tiger-stripe pattern on leaves (interveinal chlorosis)", "Dark spots on berries (measles)", "Sudden vine wilting (apoplexy)", "Brown streaking in cross-section of wood"],
        "causes": ["Complex of wood-infecting fungi", "Pruning wounds as entry points", "Drought stress", "Old vines more susceptible"],
        "treatment": ["No cure available — management only", "Prune out infected wood to healthy tissue", "Protect pruning wounds with fungicidal paste", "Remove severely affected vines"],
        "prevention": ["Use protective wound sealants after pruning", "Double pruning (spur then cane)", "Avoid pruning in wet conditions", "Use disease-free planting material"],
        "organic_remedies": ["Trichoderma-based wound treatments", "Minimize pruning wounds", "Biological control agents on wounds"]
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "plant": "Grape", "disease_short": "Leaf Blight", "is_healthy": False, "severity": "Medium",
        "description": "Grape leaf blight caused by Pseudocercospora vitis produces dark spots on mature leaves, often leading to premature defoliation and reduced photosynthetic capacity.",
        "symptoms": ["Irregular dark brown spots on older leaves", "Yellow halos around lesions", "Premature defoliation", "Petiole lesions causing leaf drop"],
        "causes": ["Fungus Pseudocercospora vitis", "Warm, humid conditions", "Extended wet periods", "Dense canopy"],
        "treatment": ["Apply copper fungicides or mancozeb", "Remove badly affected leaves", "Improve canopy airflow"],
        "prevention": ["Canopy management to improve air circulation", "Avoid overhead irrigation", "Regular preventive fungicide program"],
        "organic_remedies": ["Copper-based sprays", "Sulfur fungicides", "Canopy management"]
    },
    "Grape___healthy": {
        "plant": "Grape", "disease_short": "Healthy", "is_healthy": True, "severity": "None",
        "description": "The grape vine appears healthy with no signs of disease.",
        "symptoms": [], "causes": [],
        "treatment": ["No treatment needed"],
        "prevention": ["Annual pruning for canopy management", "Balanced nutrition", "Monitor for early disease signs"],
        "organic_remedies": ["Preventive copper sprays", "Compost applications"]
    },
    # ── ORANGE ─────────────────────────────────────────────────────────────
    "Orange___Haunglongbing_(Citrus_greening)": {
        "plant": "Orange/Citrus", "disease_short": "Citrus Greening (HLB)", "is_healthy": False, "severity": "Critical",
        "description": "Huanglongbing (HLB) or citrus greening is the most destructive citrus disease worldwide. Caused by the bacterium Candidatus Liberibacter asiaticus, transmitted by the Asian citrus psyllid. There is currently no cure.",
        "symptoms": ["Asymmetric yellowing of leaves (blotchy mottle)", "Yellow shoots (flush)", "Small, lopsided, bitter green fruit", "Premature fruit drop", "General tree decline"],
        "causes": ["Bacterium Candidatus Liberibacter asiaticus", "Asian citrus psyllid (Diaphorina citri) vector", "Grafting with infected material", "Dodder plant parasitism"],
        "treatment": ["No cure exists — management only", "Remove and destroy infected trees promptly", "Control psyllid vector with insecticides", "Nutritional therapy (micro-nutrient injections) may temporarily improve yield"],
        "prevention": ["Use certified disease-free nursery stock", "Control psyllid populations aggressively", "Quarantine regulations compliance", "Regular scouting for psyllid and symptoms"],
        "organic_remedies": ["Sticky yellow traps for psyllid monitoring", "Neem oil for psyllid control", "Kaolin clay particle film", "Beneficial insects to control psyllid"]
    },
    # ── PEACH ──────────────────────────────────────────────────────────────
    "Peach___Bacterial_spot": {
        "plant": "Peach", "disease_short": "Bacterial Spot", "is_healthy": False, "severity": "High",
        "description": "Bacterial spot on peach, caused by Xanthomonas arboricola pv. pruni, is a significant disease causing defoliation, fruit spotting, and economic losses in humid regions.",
        "symptoms": ["Small, water-soaked spots on leaves turning purple-black", "Spots drop out leaving a shot-hole appearance", "Sunken, dark pits on fruit", "Twig cankers and gummosis"],
        "causes": ["Bacterium Xanthomonas arboricola pv. pruni", "Warm, wet weather during spring", "Rain and wind spread bacteria", "Wounds from insects or hail"],
        "treatment": ["Apply copper bactericides preventively and after rains", "Oxytetracycline sprays during early season", "Remove severely infected plant parts"],
        "prevention": ["Plant resistant or tolerant peach varieties", "Avoid overhead irrigation", "Apply copper dormant sprays", "Prune for good airflow"],
        "organic_remedies": ["Copper hydroxide sprays", "Lime sulfur dormant sprays", "Avoid excess nitrogen"]
    },
    "Peach___healthy": {
        "plant": "Peach", "disease_short": "Healthy", "is_healthy": True, "severity": "None",
        "description": "The peach plant looks healthy with no disease symptoms detected.",
        "symptoms": [], "causes": [],
        "treatment": ["No treatment needed"],
        "prevention": ["Regular pruning", "Balanced fertilization", "Monitor for pests and diseases"],
        "organic_remedies": ["Dormant oil sprays", "Neem oil preventive sprays"]
    },
    # ── PEPPER ─────────────────────────────────────────────────────────────
    "Pepper,_bell___Bacterial_spot": {
        "plant": "Bell Pepper", "disease_short": "Bacterial Spot", "is_healthy": False, "severity": "High",
        "description": "Bacterial spot on pepper, caused by Xanthomonas euvesicatoria, is a major disease in warm, wet climates causing severe defoliation and fruit losses.",
        "symptoms": ["Small, water-soaked leaf spots enlarging to brown with yellow halos", "Raised, scabby lesions on fruit", "Defoliation in severe cases", "Stem lesions"],
        "causes": ["Bacterium Xanthomonas euvesicatoria", "Warm temperatures (24–30°C)", "Rain, overhead irrigation", "Infected seed or transplants"],
        "treatment": ["Apply copper bactericides every 5–7 days", "Use fixed copper + mancozeb mixture", "Remove heavily infected plants from field"],
        "prevention": ["Use certified disease-free seed", "Hot-water seed treatment (50°C for 25 min)", "Avoid overhead irrigation", "Crop rotation (2–3 years)"],
        "organic_remedies": ["Copper hydroxide", "Bacillus subtilis biocontrol sprays", "Avoid wetting leaves"]
    },
    "Pepper,_bell___healthy": {
        "plant": "Bell Pepper", "disease_short": "Healthy", "is_healthy": True, "severity": "None",
        "description": "The bell pepper plant appears healthy.",
        "symptoms": [], "causes": [],
        "treatment": ["No treatment needed"],
        "prevention": ["Regular scouting", "Drip irrigation preferred", "Crop rotation"],
        "organic_remedies": ["Neem oil preventive spray", "Compost tea"]
    },
    # ── POTATO ─────────────────────────────────────────────────────────────
    "Potato___Early_blight": {
        "plant": "Potato", "disease_short": "Early Blight", "is_healthy": False, "severity": "Medium",
        "description": "Early blight of potato, caused by Alternaria solani, produces characteristic concentric-ring lesions and causes premature defoliation, reducing tuber yield.",
        "symptoms": ["Dark brown lesions with concentric rings (target-board pattern)", "Yellow halo surrounding lesions", "Lower, older leaves affected first", "Lesions on stems and tubers"],
        "causes": ["Fungus Alternaria solani", "Warm temperatures (24–29°C)", "Extended wet periods alternating with dry", "Nitrogen deficiency"],
        "treatment": ["Apply fungicides (chlorothalonil, mancozeb, azoxystrobin)", "Begin spraying at first symptom appearance", "Ensure adequate nitrogen fertilization"],
        "prevention": ["Use certified disease-free seed potatoes", "Crop rotation (minimum 2 years)", "Ensure adequate plant nutrition", "Avoid water stress"],
        "organic_remedies": ["Copper-based fungicides", "Neem oil sprays", "Compost to improve plant vigor"]
    },
    "Potato___Late_blight": {
        "plant": "Potato", "disease_short": "Late Blight", "is_healthy": False, "severity": "Critical",
        "description": "Late blight, caused by Phytophthora infestans, is the disease responsible for the Irish Potato Famine. It can destroy an entire crop within days under favorable conditions.",
        "symptoms": ["Pale green to dark brown water-soaked lesions expanding rapidly", "White, fluffy sporulation on leaf undersides in humid conditions", "Firm, brown rot in tubers", "Black stems (blackleg) in severe cases"],
        "causes": ["Oomycete Phytophthora infestans", "Cool temperatures (10–20°C) with high humidity", "Rain and fog", "Infected seed potatoes or nearby infected crops"],
        "treatment": ["Apply protectant fungicides (chlorothalonil, mancozeb) preventively", "Apply systemic fungicides (metalaxyl, cymoxanil) at infection", "Destroy infected haulm before harvest", "Harvest in dry conditions"],
        "prevention": ["Plant certified disease-free seed potatoes", "Choose resistant varieties", "Hilling to protect tubers", "Prophylactic spray programs", "Monitor weather forecasts (blight warning systems)"],
        "organic_remedies": ["Copper-based fungicides (Bordeaux mixture)", "Remove infected plants immediately", "Avoid overhead irrigation", "Resistant variety selection"]
    },
    "Potato___healthy": {
        "plant": "Potato", "disease_short": "Healthy", "is_healthy": True, "severity": "None",
        "description": "The potato plant appears healthy with no signs of disease.",
        "symptoms": [], "causes": [],
        "treatment": ["No treatment needed"],
        "prevention": ["Use certified seed potatoes", "Regular hilling", "Monitor weather for blight risk"],
        "organic_remedies": ["Preventive copper sprays in high-risk periods"]
    },
    # ── RASPBERRY ──────────────────────────────────────────────────────────
    "Raspberry___healthy": {
        "plant": "Raspberry", "disease_short": "Healthy", "is_healthy": True, "severity": "None",
        "description": "The raspberry plant appears healthy.",
        "symptoms": [], "causes": [],
        "treatment": ["No treatment needed"],
        "prevention": ["Annual cane pruning", "Good drainage", "Monitor for aphids and disease"],
        "organic_remedies": ["Neem oil", "Compost applications"]
    },
    # ── SOYBEAN ────────────────────────────────────────────────────────────
    "Soybean___healthy": {
        "plant": "Soybean", "disease_short": "Healthy", "is_healthy": True, "severity": "None",
        "description": "The soybean plant appears healthy.",
        "symptoms": [], "causes": [],
        "treatment": ["No treatment needed"],
        "prevention": ["Crop rotation", "Scout regularly for pest and disease", "Balanced fertility program"],
        "organic_remedies": ["Biostimulants", "Compost applications"]
    },
    # ── SQUASH ─────────────────────────────────────────────────────────────
    "Squash___Powdery_mildew": {
        "plant": "Squash", "disease_short": "Powdery Mildew", "is_healthy": False, "severity": "Medium",
        "description": "Powdery mildew on squash, caused by Podosphaera xanthii, is one of the most common and easily recognizable cucurbit diseases, forming white powdery patches on leaves.",
        "symptoms": ["White powdery spots on upper leaf surfaces", "Yellowing and browning of leaves", "Defoliation in severe cases", "Reduced fruit quality and yield"],
        "causes": ["Fungus Podosphaera xanthii", "Warm dry days with cool humid nights", "Poor air circulation", "High plant density"],
        "treatment": ["Apply sulfur or potassium bicarbonate fungicides", "Systemic fungicides (myclobutanil, trifloxystrobin)", "Remove severely infected leaves"],
        "prevention": ["Choose mildew-resistant varieties", "Ensure proper plant spacing", "Avoid excess nitrogen", "Drip irrigation to keep leaves dry"],
        "organic_remedies": ["Baking soda spray", "Neem oil", "Milk spray (1:9 milk:water)", "Potassium bicarbonate"]
    },
    # ── STRAWBERRY ─────────────────────────────────────────────────────────
    "Strawberry___Leaf_scorch": {
        "plant": "Strawberry", "disease_short": "Leaf Scorch", "is_healthy": False, "severity": "Medium",
        "description": "Strawberry leaf scorch, caused by Diplocarpon earlianum, produces small dark purple spots that coalesce, giving leaves a scorched appearance. It weakens plants and reduces yield.",
        "symptoms": ["Small, dark purple to reddish spots on leaves", "Spots merge causing leaf surface to appear 'scorched'", "Leaf undersides show reddish-brown areas", "Severe defoliation in repeated infections"],
        "causes": ["Fungus Diplocarpon earlianum", "Wet, humid weather", "Overhead irrigation", "Overcrowded plantings"],
        "treatment": ["Apply fungicides (captan, myclobutanil) preventively", "Remove and destroy infected leaves", "Improve air circulation"],
        "prevention": ["Use certified disease-free transplants", "Renovate plantings regularly", "Avoid wetting foliage", "Good spacing between plants"],
        "organic_remedies": ["Copper fungicides", "Neem oil", "Remove infected foliage promptly"]
    },
    "Strawberry___healthy": {
        "plant": "Strawberry", "disease_short": "Healthy", "is_healthy": True, "severity": "None",
        "description": "The strawberry plant appears healthy.",
        "symptoms": [], "causes": [],
        "treatment": ["No treatment needed"],
        "prevention": ["Regular renovation of plantings", "Drip irrigation", "Annual renovation"],
        "organic_remedies": ["Neem oil preventive spray", "Compost mulch"]
    },
    # ── TOMATO ─────────────────────────────────────────────────────────────
    "Tomato___Bacterial_spot": {
        "plant": "Tomato", "disease_short": "Bacterial Spot", "is_healthy": False, "severity": "High",
        "description": "Tomato bacterial spot, caused by Xanthomonas species, is a major disease causing dark lesions on leaves, stems, and fruit, leading to significant yield losses.",
        "symptoms": ["Small, water-soaked, circular dark spots on leaves", "Spots with yellow halos (greasy appearance)", "Raised, scab-like spots on fruit", "Defoliation and sunscald of exposed fruit"],
        "causes": ["Xanthomonas vesicatoria / euvesicatoria", "Warm temperatures (24–30°C)", "High humidity and rain", "Infected seed and transplants"],
        "treatment": ["Apply copper bactericide + mancozeb weekly", "Remove infected plant material", "Use drip irrigation to avoid wetting foliage"],
        "prevention": ["Certified disease-free seed", "Hot-water seed treatment", "2–3 year crop rotation", "Resistant varieties"],
        "organic_remedies": ["Fixed copper sprays", "Bacillus subtilis products", "Crop rotation"]
    },
    "Tomato___Early_blight": {
        "plant": "Tomato", "disease_short": "Early Blight", "is_healthy": False, "severity": "Medium",
        "description": "Tomato early blight, caused by Alternaria solani, produces concentric-ring lesions on leaves and fruit, leading to defoliation and yield reduction.",
        "symptoms": ["Dark brown lesions with concentric rings on older leaves", "Yellow halo around lesions", "Stem lesions (collar rot on seedlings)", "Dark, leathery lesions on fruit near stem end"],
        "causes": ["Fungus Alternaria solani", "Warm temperatures with alternating wet/dry periods", "Nitrogen deficiency", "Plant stress"],
        "treatment": ["Apply chlorothalonil, mancozeb, or azoxystrobin fungicides", "Begin at first symptom appearance", "Repeat every 7–10 days in wet weather"],
        "prevention": ["Crop rotation (2–3 years)", "Remove infected crop debris", "Balanced fertilization", "Mulching to prevent soil splash"],
        "organic_remedies": ["Copper-based fungicides", "Neem oil", "Compost to improve plant health"]
    },
    "Tomato___Late_blight": {
        "plant": "Tomato", "disease_short": "Late Blight", "is_healthy": False, "severity": "Critical",
        "description": "Tomato late blight caused by Phytophthora infestans is the most devastating tomato disease worldwide, capable of destroying an entire planting within days.",
        "symptoms": ["Pale green, water-soaked spots on leaves becoming brown", "White mold on undersides of leaves in humid conditions", "Brown, firm lesions on stems", "Dark, greasy lesions on fruit"],
        "causes": ["Oomycete Phytophthora infestans", "Cool, wet weather (10–20°C with high humidity)", "Fog and rain spread spores rapidly", "Infected transplants"],
        "treatment": ["Apply protectant fungicides (chlorothalonil, mancozeb) prophylactically", "Use systemic fungicides (cymoxanil + mancozeb) once infection starts", "Remove infected plants from field immediately"],
        "prevention": ["Plant resistant varieties (e.g., Legend, Defiant)", "Stake plants for airflow", "Avoid overhead watering", "Scout fields during cool wet periods"],
        "organic_remedies": ["Bordeaux mixture (copper sulfate + lime)", "Copper hydroxide sprays", "Destroy infected plants immediately"]
    },
    "Tomato___Leaf_Mold": {
        "plant": "Tomato", "disease_short": "Leaf Mold", "is_healthy": False, "severity": "Medium",
        "description": "Tomato leaf mold, caused by Fulvia fulva (Passalora fulva), is primarily a problem in greenhouse tomatoes. It causes pale patches and a velvety mold on leaf undersides.",
        "symptoms": ["Pale green or yellow patches on upper leaf surfaces", "Olive-green to brown velvety mold on undersides", "Leaf curl and defoliation in severe cases", "Mainly on upper leaves"],
        "causes": ["Fungus Fulvia fulva", "High humidity (>85%) and poor ventilation", "Primarily greenhouse problem", "Dense canopy"],
        "treatment": ["Improve greenhouse ventilation", "Apply fungicides (chlorothalonil, mancozeb)", "Reduce humidity by heating and ventilating"],
        "prevention": ["Choose resistant varieties (Cf genes)", "Space plants properly", "Ventilate greenhouses", "Avoid overhead irrigation"],
        "organic_remedies": ["Improve ventilation first", "Copper-based fungicides", "Reduce plant density"]
    },
    "Tomato___Septoria_leaf_spot": {
        "plant": "Tomato", "disease_short": "Septoria Leaf Spot", "is_healthy": False, "severity": "Medium",
        "description": "Septoria leaf spot, caused by Septoria lycopersici, is one of the most common tomato foliage diseases, causing small circular spots with dark borders and white centers.",
        "symptoms": ["Small (3–6 mm), circular spots with dark brown borders and light tan/white centers", "Tiny black dots (pycnidia) visible in spots", "Lower leaves affected first", "Rapid defoliation reducing fruit quality"],
        "causes": ["Fungus Septoria lycopersici", "Warm, wet conditions", "Infected crop debris", "Splashing water disperses spores"],
        "treatment": ["Apply fungicides (chlorothalonil, mancozeb, copper) every 7–10 days", "Remove infected lower leaves", "Mulch to prevent soil splash"],
        "prevention": ["Crop rotation (2–3 years)", "Stake tomatoes to improve airflow", "Mulch to prevent spore splash", "Remove infected debris"],
        "organic_remedies": ["Copper-based fungicides", "Neem oil", "Remove infected leaves immediately"]
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "plant": "Tomato", "disease_short": "Spider Mites", "is_healthy": False, "severity": "High",
        "description": "Two-spotted spider mites (Tetranychus urticae) are tiny arachnids that cause stippled, bronzed leaves and webbing. They thrive in hot, dry conditions and populations can explode rapidly.",
        "symptoms": ["Tiny yellow or white stippling on leaves", "Bronze or silver sheen on heavily infested leaves", "Fine silky webbing on undersides of leaves", "Leaf drop in severe infestations"],
        "causes": ["Mite Tetranychus urticae", "Hot, dry weather (>27°C)", "Dusty conditions", "Pesticide-induced outbreaks (killing natural enemies)"],
        "treatment": ["Apply miticides (abamectin, spiromesifen, bifenazate)", "Insecticidal soap or neem oil for light infestations", "Increase humidity", "Water-spray plants to knock off mites"],
        "prevention": ["Maintain adequate irrigation", "Avoid dusty conditions", "Preserve natural enemies (predatory mites)", "Monitor plants regularly especially in hot, dry weather"],
        "organic_remedies": ["Neem oil spray", "Insecticidal soap", "Predatory mites (Phytoseiulus persimilis)", "Strong water sprays to dislodge mites"]
    },
    "Tomato___Target_Spot": {
        "plant": "Tomato", "disease_short": "Target Spot", "is_healthy": False, "severity": "Medium",
        "description": "Target spot on tomato, caused by Corynespora cassiicola, produces concentric-ring lesions on leaves, stems, and fruit, particularly problematic in warm tropical climates.",
        "symptoms": ["Brown lesions with concentric rings (target pattern)", "Yellow halo around lesions", "Affects leaves, stems, and fruit", "Defoliation starting from lower leaves"],
        "causes": ["Fungus Corynespora cassiicola", "Warm, humid conditions", "Infected plant debris", "Wounds and other disease lesions"],
        "treatment": ["Apply fungicides (azoxystrobin, fluxapyroxad, mancozeb)", "Begin applications at first sign of disease", "Repeat every 10–14 days"],
        "prevention": ["Use resistant varieties where available", "Crop rotation", "Remove infected debris", "Good canopy management"],
        "organic_remedies": ["Copper-based fungicides", "Neem oil", "Improve plant spacing and airflow"]
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "plant": "Tomato", "disease_short": "Yellow Leaf Curl Virus", "is_healthy": False, "severity": "Critical",
        "description": "Tomato yellow leaf curl virus (TYLCV) is transmitted by whiteflies and is one of the most damaging tomato viruses worldwide, causing severe yield losses in tropical and subtropical regions.",
        "symptoms": ["Upward curling and yellowing of leaf margins", "Small, crinkled leaves", "Severe stunting of plant", "Flower drop and poor fruit set"],
        "causes": ["Tomato yellow leaf curl virus (TYLCV)", "Transmitted by silverleaf whitefly (Bemisia tabaci)", "No cure — virus is systemic"],
        "treatment": ["No cure — remove and destroy infected plants", "Control whitefly populations immediately with insecticides", "Use yellow sticky traps to monitor whitefly levels"],
        "prevention": ["Plant TYLCV-resistant varieties (most modern hybrids)", "Use insect-proof mesh in greenhouse growing", "Apply reflective mulches to repel whiteflies", "Remove infected plants immediately"],
        "organic_remedies": ["Neem oil for whitefly control", "Yellow sticky traps", "Reflective silver mulch", "Kaolin clay spray to repel whiteflies"]
    },
    "Tomato___Tomato_mosaic_virus": {
        "plant": "Tomato", "disease_short": "Tomato Mosaic Virus", "is_healthy": False, "severity": "High",
        "description": "Tomato mosaic virus (ToMV) is a mechanically transmitted virus causing mosaic patterns, distortion, and stunting. It is extremely stable and can persist in soil and on tools.",
        "symptoms": ["Light and dark green mosaic pattern on leaves", "Leaf distortion and curling", "Plant stunting", "Reduced fruit yield and quality"],
        "causes": ["Tomato mosaic virus (ToMV)", "Mechanical transmission (tools, hands, clothing)", "Contact between plants", "Infected seed (rarely)"],
        "treatment": ["No cure — remove infected plants", "Sanitize all tools with bleach solution", "Wash hands thoroughly before handling plants"],
        "prevention": ["Use certified virus-free seed", "Plant resistant varieties (Tm-2 gene)", "Sanitize tools between plants", "Avoid smoking near tomato plants (ToMV related to tobacco)"],
        "organic_remedies": ["Strict sanitation protocols", "Remove infected plants", "Milk spray on tools as sanitizer", "Resistant varieties"]
    },
    "Tomato___healthy": {
        "plant": "Tomato", "disease_short": "Healthy", "is_healthy": True, "severity": "None",
        "description": "The tomato plant appears healthy with no signs of disease or pest damage. Leaves are deep green with normal morphology.",
        "symptoms": [], "causes": [],
        "treatment": ["No treatment needed — plant looks great!"],
        "prevention": ["Regular scouting for early disease detection", "Consistent watering to avoid stress", "Balanced NPK fertilization", "Staking for airflow and fruit support"],
        "organic_remedies": ["Preventive neem oil spray", "Compost tea foliar spray", "Seaweed extract biostimulant"]
    },
}

# Default fallback for any unknown class
DEFAULT_INFO = {
    "plant": "Unknown", "disease_short": "Unknown", "is_healthy": False, "severity": "Unknown",
    "description": "Disease information not available for this class. Please consult an agronomist.",
    "symptoms": ["Consult a plant disease specialist for accurate diagnosis."],
    "causes": ["Unknown"],
    "treatment": ["Consult your local agricultural extension service."],
    "prevention": ["Regular monitoring and good agricultural practices."],
    "organic_remedies": ["Consult a certified organic grower or agronomist."]
}


def get_disease_info(class_name: str) -> dict:
    """
    Returns disease detail dict for a given class label.
    Falls back gracefully if label not in database.
    """
    return DISEASE_DATABASE.get(class_name, {**DEFAULT_INFO, "plant": class_name})
