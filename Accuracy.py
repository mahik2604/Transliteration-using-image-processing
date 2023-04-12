pip install fuzzywuzzy
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from sklearn.metrics import accuracy_score


#Calculating accuracy of Image processing and OCR phase
# Defining true labels and predicted labels as lists or arrays

true_labels = ["प्रश्नकर्ता", "दिल्ली", "दादाश्री", "मनुष्य", "तहलका", "स्वभाव", "कैसा", "रिलेटिव", "यदि", "उसे", "कोई", "थप्पड़", "लेकिन", "समझदार", "सोचेगा", "साक्षी", "हाथ", "ज़िम्मेदारी",
                    "चिंता", "आशीर्वाद", "माध्यम", "अनुभूति", "बंद", "सत्संग", "वहाँ", "ऑफिस", "अंदर", "भटकना", "प्रकार", "विश्वास", "अहंकार", "अग्नि", "संस्कारी", "सौभाग्य", "मनुष्यपना",
                    "जोखिम", "फायदा", "पूछकर", "गालियाँ", "अशांति", "उलझन", "वरीज़", "उपाधी", "समाधि", "वास्तव", "ज्ञानीपुरुष", "शुद्ध", "निरंतर", "परमात्मा", "क्षण", "संसार", "साइड",
                    "नैचुरल", "कुदरत", "ज़बरदस्त", "प्रेम", "मुश्किल", "कारखाना", "दोष", "बंधन", "श्रीकृष्ण", "मात्र", "डाँट", "तलाश", "स्वामी", "कबीर", "साहब", "शरीर", "धीरज", "बुद्धिमान", "रसोई",
                    "बेशकीमती", "प्रकाश", "अहमदाबाद", "भोजन", "सेठानी", "वर्तमान", "एयरकन्डिशन", "एक्सटेन्शन", "प्रतिशत", "ऑब्स्ट्रक्ट", "परिणाम", "मोटर", "बेस्ट", "क्रिएशन", "व्यवसाय",
                    "सरप्लस", "रेग्यूलेशन", "इन्कम", "आत्मज्ञान", "सफोकेशन", "एनर्जी", "वचन", "महिमा", "आयुष", "गौरव", "राहुल", "हर्षित", "विशेष", "मुकेश"]
predicted_labels = ['प्रश्नकर्ता', 'दिल्ली', 'दादाश्री', 'मनुष्य', 'तहलका', 'स्वभाव', 'कैसा', 'रिलेटिव', 'यदि', 'उसे', 'कोई', 'थप्पड़', 'लेकिन', 'समझदार', 'सोचेगा', 'साक्षी',
                    'हाथ', 'ज़िम्मेदारी', 'चिंता', 'आशीर्वाद', 'माध्यम', 'अनुभूति', 'बंद', 'सत्संग', 'वहाँ', 'ऑफिस', 'अंदर', 'भंटकना', 'प्रकार', 'विश्वास', 'अहंकार', 'अग्नि', 'संस्कारी',
                    'सौभाग्य', 'मनुष्यपना', 'जोखिम', 'फायदा', 'पूछकर', 'गालियाँ', 'अशांति', 'उलझन', 'वरीज़', 'उपाधी', 'समाधि', 'वास्तव', 'ज्ञानीपुरुष', 'शुद्ध', 'निरंतर', 'परमात्मा',
                    'क्षण', 'संसार', 'साइड', 'नैचुरल', 'कुदरत', 'ज़बरदस्त', 'प्रेम', 'मुश्किल', 'कारखाना', 'दोष', 'बंधन', 'श्रीकृष्ण', 'मात्र', 'डाँट', 'तलाश', 'स्वामी', 'कबीर', 'साहब',
                    'शरीर', 'धीरज', 'बुद्धिमान', 'रसोई', 'बेशकीमती', 'प्रकाश', 'अहमदाबाद', 'भोजन', 'सेठानी', 'वर्तमान', 'एयरकब्डिशन', 'एक्सटेन्शन', 'प्रतिशत', 'ऑस्ट्रेक्ट', 'परिणाम',
                    'मोटर', 'बेस्ट', 'क्रिएशन', 'व्यवसाय', 'सरप्लस', 'रेग्यूलेशन', 'इनकम', 'आल्मज्ञन', 'सफोकेशन', 'एनर्जी', 'वचन', 'महिमा', 'आयुष', 'गौरव', 'राहुल', 'हर्षित', 'विशेष', 'मुकेश']

#accuracy
accuracy = accuracy_score(true_labels, predicted_labels)
print("Accuracy:", accuracy)

ratio1 = fuzz.ratio(true_labels, predicted_labels)
print('Similarity score 1: {}'.format(ratio1))

ratio2 = fuzz.partial_ratio(true_labels, predicted_labels)
print('Similarity score 2: {}'.format(ratio2))



#calculating accuracy score for different transliteration models

# English
true_labels =   ['prashankarta', 'dilli', 'dadashree', 'manushya', 'tahalka', 'swabhav', 'vidyapeeth', 'chatravas', 'yadi', 'use', 'koi', 'thappad', 'lekin', 'samajhdaar', 'sochega', 'sakshi', 'hath', 'zimmedari', 'chinta', 'ashirvad', 'madhyam', 'anubhooti', 'band', 'satsang', 'wahan', 'udas', 'andar', 'bhatkana', 'prakar', 'vishvas', 'ahankar', 'agni', 'sanskari', 'saubhagya', 'manushyapana', 'jokhim', 'fida', 'puchkar', 'galiyan', 'ashanti', 'uljhan', 'azadi', 'upadhi', 'samadhi', 'vastav', 'pagal', 'shuddh', 'nirantar', 'paramatma', 'kshan', 'sansar', 'side', 'natural', 'kudarat', 'zabardast', 'prem', 'mushkil', 'karkhana', 'dosh', 'bandhan', 'shrikrishna', 'matra', 'upyog', 'talash', 'swami', 'kabir', 'sahab', 'sharir', 'dhiraj', 'buddhiman', 'rasoi', 'beshkimati', 'prakash', 'ahamdabad', 'bhojan', 'sethani', 'vartaman', 'mazak', 'mahila', 'pratishat', 'sundar', 'parinam', 'aadmi', 'sanket', 'dost', 'vyavsay', 'taapmaan', 'namaste', 'khush', 'dopahar', 'ajeeb', 'kahani', 'wachan', 'mahima', 'ayush', 'gaurav', 'rahul', 'harshit', 'vishesh', 'mukesh']
indicate =      ['prashnkarta', 'dilli', 'dadashree', 'manushya', 'tahalka', 'swabhav', 'vidyapeeth', 'chhatravas', 'yadi', 'use', 'koi', 'thappad', 'lekin', 'samajhdaar', 'sochega', 'sakshi', 'hath', 'zimmedari', 'chinta', 'ashirvad', 'madhyam', 'anubhooti', 'band', 'satsang', 'wahha', 'udas', 'andar', 'bhatkana', 'prakar', 'vishvas', 'ahankar', 'agni', 'sanskari', 'saubhagya', 'manushyapana', 'jokhim', 'fida', 'puchcar', 'galiyan', 'ashanti', 'uljhan', 'azadi', 'upadhi', 'samadhi', 'vastav', 'pagal', 'shuddh', 'nirantar', 'paramatma', 'kshan', 'sansara', 'side', 'natural', 'kudarat', 'zabardast', 'prem', 'mushkil', 'karkhana', 'dosh', 'band', 'shrikrishna', 'matra', 'upyog', 'talash', 'swami', 'kabir', 'sahab', 'sharir', 'dhiraj', 'buddhiman', 'rasoi', 'beshkimati', 'prakash', 'ahamdabad', 'bhojan', 'sethani', 'varthaman', 'mazak', 'mahila', 'pratishat', 'sundar', 'parinam', 'adami', 'sanket', 'dost', 'vyavsay', 'tapman', 'namaste', 'khush', 'dophar', 'ajib', 'kahani', 'wachan', 'mahima', 'ayush', 'gaurava', 'rahul', 'harshit', 'vishesh', 'mukesh']
indic_trans =   ['prasnakarta', 'dilli', 'dadasri', 'manusya', 'tahlaka', 'svabhav', 'vidyapitha', 'chatravasa', 'yadi', 'use', 'koi', 'thappar', 'lekin', 'samajhdar', 'sochega', 'saksī', 'hath', 'zimmēdari', 'chinta', 'asirvada', 'madhyama', 'anubhuti', 'band', 'satsanga', 'vaham', 'udasa', 'andar', 'bhataknā', 'prakara', 'visvasa', 'ahamkara', 'agni', 'samskari', 'saubhagya', 'manusyapana', 'jokhim', 'phayada', 'puchakara', 'galiyam', 'asanti', 'ulajhana', 'azadi', 'upadhi', 'samadhi', 'vastava', 'pagal', 'suddha', 'nirantara', 'paramatmā', 'ksana', 'samsara', 'saida', 'naicurala', 'kudarata', 'zabardasta', 'prema', 'muskil', 'karkhana', 'dosa', 'bandhana', 'srikrsna', 'matra', 'upayoga', 'talasa', 'svami', 'kabira', 'sahaba', 'sarira', 'dhiraja', 'buddhimana', 'rasoi', 'besakimati', 'prakasa', 'ahamadabada', 'bhojana', 'sethani', 'vartamana', 'mazaka', 'mahila', 'pratisata', 'sundara', 'parinama', 'adami', 'samketa', 'dosta', 'vyavasaya', 'tapamana', 'namaste', 'khusa', 'dopahara', 'ajiba', 'kahani', 'vachana', 'mahima', 'ayusa', 'gaurava', 'rahula', 'harsita', 'visesa', 'mukesa']
quillpad =      ['prashnakarta','dilli', 'dadashri', 'manushy', 'tahlaka', 'svabhav', 'vidyapeeth', 'chatravas', 'yadi', 'use', 'koi', 'thappar', 'lekin', 'samajhdar', 'sochega', 'sakshi', 'hath', 'zimmedari', 'chinta', 'ashirwad', 'madhyam', 'anubhooti', 'band', 'satsang', 'vahan','udas','andar','bhatkana','prakar','vishwas','ahankar','agni','sanskaari','saubhagy','manushyapana','jokhim','fayda','puchhkar','galiyan','ashanti','uljhan','aazadi','upaadhi','samadhi','vaastav','pagal','shuddh','nirantar','paramatma','kshan','sansar','said','natural','kudrat','zabardast','prem','mushkil','karkhana','dosh','bandhan','shrikrishn','matr','upayog','talash','swami','kabir','sahab','shareer','dheeraj','buddhimaan','rasoi','beshakimti','prakash','ahmadabad','bhojan', 'sethani', 'vartamaan', 'mazaak', 'mahila', 'pratishat', 'sundar', 'parinaam', 'aadmi', 'sanket', 'dost', 'vyavasaay', 'taapamaan', 'namaste', 'khush', 'dopahar', 'ajeeb', 'kahaani', 'vachan', 'mahima', 'ayush', 'gaourav', 'rahul', 'harshit', 'vishesh', 'mukesh']
itrans =        ["prashnakarta", "dilli", "dadashri", "manushya", "tahalaka", "svabhava", "vidyapitha", "chatravasa", "yadi", "use", "koi", "thappada", "lekina", "samajhadara", "sochega", "sakshi", "hatha", "zimmedari", "chimta", "ashirvada", "madhyama", "anubhuti", "bamda", "satsamga", "vahan", "udasa", "amdara", "bhamtakana", "prakara", "vishvasa", "ahamkara", "agni", "samskari", "saubhagya", "manushyapana", "jokhima", "phayada", "puchakara", "galiya.n", "ashamti", "ulajhana", "azadi", "upadhi", "samadhi", "vastava", "pagala", "shuddha", "niramtara", "paramatma", "kshana", "samsara", "saida", "naichurala", "kudarata", "zabaradasta", "prema", "mushkila", "karakhana", "dosha", "bamdhana", "shrikrrishna", "matra", "upayoga", "talasha", "svami", "kabira", "sahaba", "sharira", "dhiraja", "buddhimana", "rasoi", "beshakimati", "prakasha", "ahamadabada", "bhojana", "sethani", "vartamana", "mazaka", "mahila", "pratishata", "sumdara", "parinama", "adami", "samketa", "dosta", "vyavasaya", "tapamana", "namaste", "khusha", "dopahara", "ajiba", "kahani", "vachana", "mahima", "ayusha", "gaurava", "rahula", "harshita", "vishesha", "mukesha"]
google =        ["prashnkar‍tā", "dilli", "dadasri", "manusya", "tahlka", "svabhav", "vidyapith", "chhatravas", "yadi", "use", "koi", "thappar", "lekin", "samajhdar", "sochega", "sakshi", "hath", "zimmedari", "chinta", "asirvad", "madhyam", "anubhuti", "band", "satsang", "vahan", "udas", "andar", "bhatakna", "prakar", "visvas", "ahankar", "agni", "sanskari", "saubhagya", "manusyapna", "jokhim", "phayda", "puchk‍ar", "galiyam", "ashanti", "uljhan", "azadi", "upadhi", "samadhi", "vastav", "pagal", "suddh", "nirantar", "paramsama", "ksan", "sansar", "said", "naichural", "kudrat", "zabardast", "prem", "mushkil", "karkhana", "dos", "bandhan", "srikrshn", "matr", "upyog", "talash", "svami", "kabeer", "sahab", "sarir", "dhiraj", "buddhiman", "rasoi", "beshakimti", "prakash", "ahmadabad", "bhojan", "sethani", "vartaman", "mazak", "mahila", "pratishat", "sundar", "parinam", "admi", "sanket", "dost", "vyavasay", "tapman", "namaste", "khush", "dopahar", "ajib", "kahani", "vachan", "mahima", "ayush", "gaurav", "rahul", "harshit", "vises", "mukesh"]
microsoft =     [ 'prashnkarata','dilli','dadashri','manushya','tahalaka','svabhav','vidyapeeth','chatravas','yadi','use','koi','thappad','lekin','samajhdaar','sochega','sakshi','haath','zimmedari','chinta','ashirvaad','madhyam','anubhuti','band','satsang','wahan','udas','andar','bhatkana','prakar','vishwas','ahankaar','agni','sanskari','saubaagya','manushyapana','jokhim','fayda','poochhkar','galiyan','ashanti','ulajhan','azaadi','upadhi','samaadhi','vaastav','pagal','shuddh','nirantar','paramaatma','kshan','sansaar','side','natural','kudrat','zabardast','prem','mushkil','kaarkhaana','dosh','bandhan','shrikrishna','matra','upyog','talash','swami','kabir','saahab','shareer','dheeraj','buddhimaan','rasoi','beshakeemati','prakash','ahmadabad','bhojan','sethani','vartamaan','mazaak','mahila','pratishat','sundar','parinaam','adami','sanket','dost','vyavasaay','tapamaan','namaste','khush','dopahar','ajeet','kahaani','vachan','mahima','ayush','gaurav','rahul','harshit','vishesh','mukesh']




# Calculate the accuracy
accuracy_indicate = accuracy_score(true_labels, indicate)
print("Accuracy indicate:", accuracy_indicate)

accuracy_indic_trans = accuracy_score(true_labels, indic_trans)
print("Accuracy Indic_trans:", accuracy_indic_trans)

accuracy_quillpad = accuracy_score(true_labels, quillpad)
print("Accuracy quillpad:", accuracy_quillpad)

accuracy_itrans = accuracy_score(true_labels, itrans)
print("Accuracy itrans:", accuracy_itrans)

accuracy_google = accuracy_score(true_labels, google)
print("Accuracy google:", accuracy_google)

accuracy_ms = accuracy_score(true_labels, microsoft)
print("Accuracy microsoft:", accuracy_ms)



#Similarity score of different transliteration models

ratio1 = fuzz.ratio(true_labels, indicate)
print('Similarity score indicate: {}'.format(ratio1))

ratio2 = fuzz.ratio(true_labels, indic_trans)
print('Similarity score Indic_trans: {}'.format(ratio2))

ratio3 = fuzz.ratio(true_labels, quillpad)
print('Similarity score quillpad: {}'.format(ratio3))

ratio4 = fuzz.ratio(true_labels, itrans)
print('Similarity score itrans: {}'.format(ratio4))

ratio5 = fuzz.ratio(true_labels, google)
print('Similarity score google: {}'.format(ratio5))

ratio6 = fuzz.ratio(true_labels, microsoft)
print('Similarity score microsoft: {}'.format(ratio6))



