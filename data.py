# --- 1. BO'LIMLAR TUZILMASI (YANGI) ---
departments = {
    "1": {"name": "🏢 Rahbariyat (C-Level)", "roles": ["CEO", "CTO", "CFO", "COO", "CMO", "CPO"]},
    "2": {"name": "💻 Dasturlash (Dev Team)", "roles": ["Lead Backend", "Lead Frontend", "UE5 Lead", "AI Engineer", "Blockchain Dev", "DevOps", "QA Engineer"]},
    "3": {"name": "🎨 Kreativ & Dizayn", "roles": ["Art Director", "3D Modeler", "Animator", "Sound Eng", "UI/UX Designer"]},
    "4": {"name": "⚙️ Operatsion & HR", "roles": ["HR Manager", "Sales Lead", "Community Mgr", "Legal Advisor", "Data Analyst", "SysAdmin"]}
}

# --- 2. XODIMLAR PROFILI (TEAM DB) ---
team_db = {
    # C-LEVEL
    "CEO": {"name": "Shohruh", "status": "Strategy", "daily": ["Investor Relations", "Global Strategy"], "roadmap": ["Series A Funding", "IPO 2028"]},
    "CTO": {"name": "Botir (AI)", "status": "Tech Lead", "daily": ["Code Review", "Architecture"], "roadmap": ["Major Tree v2.0", "AI Patent"]},
    "CFO": {"name": "Aziz", "status": "Finance", "daily": ["Cash Flow Analysis", "Audit"], "roadmap": ["Financial Modelling", "Cost Optimization"]},
    "COO": {"name": "Jasur", "status": "Operations", "daily": ["Team Sync", "Legal Checks"], "roadmap": ["Office Expansion", "HR Policy"]},
    "CMO": {"name": "Malika", "status": "Marketing", "daily": ["Ad Campaigns", "PR Strategy"], "roadmap": ["1M Users Growth", "Brand Awareness"]},
    "CPO": {"name": "Davron", "status": "Product", "daily": ["User Feedback", "Feature List"], "roadmap": ["Alpha Launch", "Beta Testing"]},

    # DEV TEAM
    "Lead Backend": {"name": "Rustam", "status": "Coding", "daily": ["API Optimization", "DB Scaling"], "roadmap": ["Server Stability", "Security Patch"]},
    "Lead Frontend": {"name": "Sanjar", "status": "Coding", "daily": ["UI/UX Implementation", "React Logic"], "roadmap": ["Web Dashboard", "Mobile App"]},
    "UE5 Lead": {"name": "Sardor", "status": "Engine", "daily": ["Blueprints", "Physics Engine"], "roadmap": ["Core Mechanics", "Multiplayer Sync"]},
    "AI Engineer": {"name": "Elena", "status": "ML Model", "daily": ["Training Data", "Chatbot Logic"], "roadmap": ["NPC AI Behavior", "Voice Recog"]},
    "Blockchain Dev": {"name": "Timur", "status": "Smart Contract", "daily": ["Solidity Audit", "Tokenomics"], "roadmap": ["Wallet Integration", "NFT Marketplace"]},
    "DevOps": {"name": "Oleg", "status": "Infrastructure", "daily": ["AWS Manage", "CI/CD Pipe"], "roadmap": ["Auto-Scaling", "DDoS Protection"]},
    "QA Engineer": {"name": "Laylo", "status": "Testing", "daily": ["Bug Hunting", "Manual Test"], "roadmap": ["Automated Tests", "Zero-Bug Release"]},

    # CREATIVE
    "Art Director": {"name": "Zarina", "status": "Visuals", "daily": ["Concept Art", "Quality Control"], "roadmap": ["Visual Identity", "Cinematic Trailer"]},
    "3D Modeler": {"name": "Bekzod", "status": "Modelling", "daily": ["Character Design", "Environment"], "roadmap": ["100+ Assets", "City Map"]},
    "Animator": {"name": "Jamshid", "status": "Animation", "daily": ["Rigging", "Motion Capture"], "roadmap": ["Smooth Moves", "Emotes System"]},
    "Sound Eng": {"name": "Dilya", "status": "Audio", "daily": ["SFX Creation", "Ambient Sound"], "roadmap": ["Immersive Audio", "Voice Overs"]},
    "UI/UX Designer": {"name": "Kamola", "status": "Design", "daily": ["Figma Prototyping", "User Flow"], "roadmap": ["Intuitive HUD", "Accessibilty"]},

    # OPERATIONS
    "HR Manager": {"name": "Nargiza", "status": "Hiring", "daily": ["Interviews", "Team Culture"], "roadmap": ["Talent Acquisition", "Retention"]},
    "Sales Lead": {"name": "Farhod", "status": "Sales", "daily": ["B2B Calls", "Partnerships"], "roadmap": ["Corporate Clients", "Sponsorships"]},
    "Community Mgr": {"name": "Ali", "status": "Social", "daily": ["Telegram/Discord", "Events"], "roadmap": ["100k Community", "Ambassadors"]},
    "Legal Advisor": {"name": "Said", "status": "Legal", "daily": ["Contracts", "Compliance"], "roadmap": ["IP Rights", "Global Licenses"]},
    "Data Analyst": {"name": "Murod", "status": "Analytics", "daily": ["KPI Tracking", "Reports"], "roadmap": ["Data Warehouse", "AI Insights"]},
    "SysAdmin": {"name": "Pavel", "status": "Support", "daily": ["Hardware Fix", "Network"], "roadmap": ["IT Security", "Office Tech"]}
}

# Har bir lavozimning aniq oylik maoshi (USD)
salary_map = {
    # C-LEVEL
    "CEO": 2000, "CTO": 2000, "CFO": 1800, "COO": 1800, "CMO": 1800, "CPO": 1800,
    # DEV TEAM
    "Lead Backend": 3500, "Lead Frontend": 3000, "UE5 Lead": 4000, "AI Engineer": 3500,
    "Blockchain Dev": 3500, "DevOps": 3000, "QA Engineer": 1500,
    # CREATIVE
    "Art Director": 2500, "3D Modeler": 2000, "Animator": 2000, "Sound Eng": 1500, "UI/UX Designer": 2000,
    # OPERATIONS
    "HR Manager": 1500, "Sales Lead": 1500, "Community Mgr": 1200, "Legal Advisor": 2500,
    "Data Analyst": 2000, "SysAdmin": 1500
}
# --- 4. MUAMMOLAR (MAJOR TREE) ---
problems_db = {
    1: {
        "name": "Server & Infratuzilma",
        "problems": {
            101: {
                "title": "Serverda yuklama 99% (Overload)",
                "solutions": {
                    1: {"desc": "Auto-Scalingni yoqish (AWS)", "scripts": ["Script: AWS EC2 instancelarni 2x oshirish.", "Script: Load Balancer qayta sozlash."]},
                    2: {"desc": "Keraksiz jarayonlarni o'chirish", "scripts": ["Script: Background tasklarni to'xtatish.", "Script: Log yozishni kamaytirish."]},
                    3: {"desc": "DDoS himoyani kuchaytirish", "scripts": ["Script: Cloudflare 'Under Attack' rejimini yoqish.", "Script: IP ban listni yangilash."]},
                    4: {"desc": "Database optimizatsiyasi", "scripts": ["Script: SQL so'rovlarni indekslash.", "Script: Read-Replica serverni ulash."]},
                    5: {"desc": "Tizimni vaqtincha yopish", "scripts": ["Script: Maintenance Mode yoqish.", "Script: Userlarga xabar yuborish."]}
                }
            },
            102: {
                "title": "Unreal Engine 5 Render qotib qoldi",
                "solutions": {
                    1: {"desc": "LOD (Level of Detail) kamaytirish", "scripts": ["Script: Uzoq obyektlar sifatini tushirish.", "Script: Poligonlarni optimizatsiya qilish."]},
                    2: {"desc": "Nanite texnologiyasini tekshirish", "scripts": ["Script: Nanite ishlamayotgan meshlar ro'yxatini olish."]},
                    3: {"desc": "Texture Streaming Pool oshirish", "scripts": ["Script: `r.Streaming.PoolSize 4000` buyrug'ini berish."]},
                    4: {"desc": "Ray Tracingni o'chirish", "scripts": ["Script: Global Illumination sozlamalarini pasaytirish."]},
                    5: {"desc": "Drayverlarni yangilash", "scripts": ["Script: NVIDIA Studio drayverini o'rnatish."]}
                }
            }
        }
    },
    2: {
        "name": "Moliya & Investitsiya",
        "problems": {
            201: {
                "title": "Kassada pul tugadi (Cash Gap)",
                "solutions": {
                    1: {"desc": "Xodimlarni 'Equity' (Ulush) ga o'tkazish", "scripts": ["Script: Maoshni 50% kesib, 0.5% ulush taklif qilish.", "Script: Shartnomalarni yangilash."]},
                    2: {"desc": "Favqulodda investitsiya (Bridge Round)", "scripts": ["Script: Mavjud investorlardan $100k so'rash.", "Script: Convertible Note rasmiylashtirish."]},
                    3: {"desc": "Marketingni to'xtatish", "scripts": ["Script: Google Ads va FB reklamalarini pauza qilish ($10k tejaladi)."]},
                    4: {"desc": "Ofisdan voz kechish", "scripts": ["Script: Remote ishlash rejimiga o'tish.", "Script: Ijara shartnomasini bekor qilish."]},
                    5: {"desc": "Bankrotlik e'lon qilish", "scripts": ["Script: Yuridik jarayonni boshlash (Eng yomon ssenariy)."]}
                }
            },
            202: {
                "title": "IT-Coin inflyatsiyasi",
                "solutions": {
                    1: {"desc": "Tokenlarni yoqish (Burn)", "scripts": ["Script: Bozordan 1M tokenni sotib olib yoqib yuborish."]},
                    2: {"desc": "Staking foizini oshirish", "scripts": ["Script: APR ni 12% dan 20% ga ko'tarish."]},
                    3: {"desc": "Yangi In-Game xaridlar qo'shish", "scripts": ["Script: Eksklyuziv Skinlar sotuvini ochish."]},
                    4: {"desc": "Market Maker bilan ishlash", "scripts": ["Script: Likvidlikni sun'iy ushlab turish."]},
                    5: {"desc": "Exchange Listing e'lon qilish", "scripts": ["Script: Yangi birja bilan kelishuvni e'lon qilish."]}
                }
            }
        }
    },
    3: {
        "name": "Marketing & PR",
        "problems": {
            301: {
                "title": "Reklama ROI juda past",
                "solutions": {
                    1: {"desc": "Auditoriyani o'zgartirish", "scripts": ["Script: Yosh chegarasini 18-24 ga tushirish."]},
                    2: {"desc": "Kreativlarni almashtirish", "scripts": ["Script: Gameplay videolarni 3D renderlar o'rniga qo'yish."]},
                    3: {"desc": "Influencer Marketingga o'tish", "scripts": ["Script: TikTok bloggerlarga to'lash."]},
                    4: {"desc": "Referral dasturni kuchaytirish", "scripts": ["Script: Har bir do'st uchun $5 bonus."]},
                    5: {"desc": "Free-to-Play modelini reklama qilish", "scripts": ["Script: 'Bepul boshlash' tugmasini kattalashtirish."]}
                }
            }
        }
    },
    4: {
        "name": "Yuridik & Xavfsizlik",
        "problems": {
            401: {
                "title": "SEC tekshiruvi",
                "solutions": {
                    1: {"desc": "Utility Token ekanligini isbotlash", "scripts": ["Script: Howey Test hujjatlarini taqdim etish."]},
                    2: {"desc": "US bozorini yopish", "scripts": ["Script: Geo-blocking yoqish."]},
                    3: {"desc": "Jarimani to'lash", "scripts": ["Script: Settlement shartnomasini imzolash."]},
                    4: {"desc": "DAO strukturasiga o'tish", "scripts": ["Script: Boshqaruvni communityga topshirish."]},
                    5: {"desc": "Token savdosini to'xtatish", "scripts": ["Script: Delisting so'rovini yuborish."]}
                }
            }
        }
    },
    5: {
        "name": "HR & Jamoa",
        "problems": {
            501: {
                "title": "Lead Developer ishdan ketmoqchi",
                "solutions": {
                    1: {"desc": "Maoshni oshirish (+20%)", "scripts": ["Script: Oylik maoshni oshirish buyrug'i."]},
                    2: {"desc": "Vesting (Ulush) taklif qilish", "scripts": ["Script: 1% kompaniya ulushini bloklab berish."]},
                    3: {"desc": "Yangi Lead qidirish", "scripts": ["Script: LinkedIn vakansiya e'lon qilish."]},
                    4: {"desc": "Outsource jamoa yollash", "scripts": ["Script: Studiyaga murojaat qilish."]},
                    5: {"desc": "CEO o'zi kod yozishi", "scripts": ["Script: CEO -> Coding Mode."]}
                }
            }
        }
    }
}
problems_extra = {
    6: {
        "name": "📱 Mahsulot & UX (Product)",
        "problems": {
            601: {
                "title": "Apple App Store rad etdi",
                "solutions": {
                    1: {"desc": "NFT funksiyasini yashirish", "scripts": ["Script: iOS versiyada 'Marketplace' tugmasini o'chirish.", "Script: Web-versiyaga yo'naltirish."]},
                    2: {"desc": "30% Komissiyaga rozi bo'lish", "scripts": ["Script: In-App Purchase narxlarini 30% ga oshirish."]},
                    3: {"desc": "Yangi ilova sifatida topshirish", "scripts": ["Script: UI dizaynni o'zgartirib qayta deploy qilish."]},
                    4: {"desc": "Faqat Android (APK) qoldirish", "scripts": ["Script: Marketingni Google Play ga yo'naltirish."]},
                    5: {"desc": "Tim Cook ga xat yozish", "scripts": ["Script: PR kampaniya boshlash."]}
                }
            },
            602: {
                "title": "Foydalanuvchilar o'yindan chiqib ketyapti (Churn)",
                "solutions": {
                    1: {"desc": "Push-xabarlarni yoqish", "scripts": ["Script: 'Sizni sovg'a kutyapti' xabarini yuborish."]},
                    2: {"desc": "Login Bonus joriy qilish", "scripts": ["Script: Har kunlik kirish uchun IT-Coin berish."]},
                    3: {"desc": "Tutorialni osonlashtirish", "scripts": ["Script: Birinchi missiya vaqtini 10 daqiqadan 3 daqiqaga tushirish."]},
                    4: {"desc": "Turnir e'lon qilish", "scripts": ["Script: $10,000 mukofotli chempionat boshlash."]},
                    5: {"desc": "Serverni tekshirish", "scripts": ["Script: Ping balandligi sababini aniqlash."]}
                }
            }
        }
    },
    7: {
        "name": "⚔️ Raqobat (Competitors)",
        "problems": {
            701: {
                "title": "Raqobatchi bizning g'oyani o'g'irladi",
                "solutions": {
                    1: {"desc": "Sudga berish (IP Claim)", "scripts": ["Script: Patent hujjatlarini yuborish.", "Script: DMCA Strike berish."]},
                    2: {"desc": "Tezroq release qilish", "scripts": ["Script: Jamoani 'Crunch' (24/7 ishlash) rejimiga o'tkazish."]},
                    3: {"desc": "Narxlarni tushirish", "scripts": ["Script: Barcha xizmatlarga 50% chegirma e'lon qilish."]},
                    4: {"desc": "Feature qo'shish", "scripts": ["Script: Raqobatchida yo'q VR rejimini ishga tushirish."]},
                    5: {"desc": "Ularni sotib olish", "scripts": ["Script: M&A (Mergers and Acquisitions) taklifini yuborish."]}
                }
            }
        }
    },
    8: {
        "name": "⛓️ Blockchain & Security",
        "problems": {
            801: {
                "title": "Smart Kontraktda 'Bug' topildi",
                "solutions": {
                    1: {"desc": "Kontraktni pauza qilish", "scripts": ["Script: Emergency Stop funksiyasini chaqirish."]},
                    2: {"desc": "White Hat haker yollash", "scripts": ["Script: Bug Bounty ($50k) e'lon qilish."]},
                    3: {"desc": "Hard Fork qilish", "scripts": ["Script: Eski tokenlarni yangisiga 1:1 almashtirish."]},
                    4: {"desc": "Likvidlikni chiqarib olish", "scripts": ["Script: DEX dagi pullarni sovuq hamyonga o'tkazish."]},
                    5: {"desc": "Audit o'tkazish", "scripts": ["Script: Certik kompaniyasiga shoshilinch audit buyurtma qilish."]}
                }
            }
        }
    }
}

# ESKI PROBLEMS_DB GA YANGILARINI QO'SHIB QO'YAMIZ
problems_db.update(problems_extra)

# --- XODIMLAR SHAXSIY HISOBI (Eng pastga qo'shing) ---
employee_finance = {
    "Shohruh": {"role": "CEO", "salary": 2000, "last_month": 2000},
    "Botir": {"role": "CTO", "salary": 2000, "last_month": 2000},
    "Sardor": {"role": "UE5 Lead", "salary": 4000, "last_month": 4000},
    "Rustam": {"role": "Lead Backend", "salary": 3500, "last_month": 3500},
    "Aziz": {"role": "CFO", "salary": 1800, "last_month": 1800}
}

# --- INVESTOR FAQ (TOP 50 SAVOL) ---
# --- INVESTOR FAQ KATEGORIYALARI ---
investor_faq_categories = {
    1: "💰 Moliya va Biznes Model",
    2: "📱 Mahsulot va Texnologiya",
    3: "📈 Marketing va O'sish",
    4: "🛡 Xatarlar va Qonunchilik",
    5: "🚀 Strategiya va Exit"
}

# --- INVESTOR FAQ (TO'LIQ 50 TA) ---
investor_faq = {
    # ---------------------------------------------------------
    # 1. MOLIYA (YANGILANGAN: $900M LOGIKASI BILAN)
    # ---------------------------------------------------------
    1: {
        "cat": 1,
        "q": "Nega kompaniyani $20M ga baholadingiz? (Juda qimmat emasmi?)",
        "a": "Biz bu raqamni osmondan olmadik. Baholash 3 ta fundamental metodga asoslangan:\n\n"
             "1. Cost-to-Duplicate (Qayta yaratish narxi): Hozir bizdagi 'Major Tree' tizimi va 1050 ta ssenariyni noldan yaratish uchun raqobatchiga 24 oy va 20 ta Senior AI-dasturchi kerak bo'ladi. O'rtacha Senior maoshi ($10k/oy) bilan hisoblaganda, faqat ish haqining o'zi $4.8 Million ga tushadi. Bu faqat xom-ashyo narxi.\n\n"
             "2. Comparable Method (Bozor taqqoslami): So'nggi 6 oyda AI va Gaming sohasidagi o'xshash startaplar (Pre-Revenue bosqichida) o'rtacha $18M - $22M bahoda investitsiya jalb qildi. Biz bozor standartining o'rtasini oldik.\n\n"
             "3. Texnologik Yakka-hukmronlik (Unfair Advantage): Bizning algoritmlarimiz server xarajatlarini raqobatchilarga qaraganda 10 barobar arzonlashtiradi. Bu bizning marjamiz (foyda ulushi) boshqalardan 2x yuqori bo'lishini ta'minlaydi. $20M — bu yuqori marjali biznes uchun standart baho."
    },
    2: {"cat": 1, "q": "Bozor salohiyati (Market Size) qanday?", "a": "Matematika aniq:\n• **TAM (Jami):** 3 mlrd geymer.\n• **SAM (Bizning bozor):** 300 mln (RPG/Metaverse).\n• **SOM (Maqsad):** 30 mln (Bozorning 1% i).\n• **Natija:** 30 mln x $30 ARPU = **$900M/yil** daromad potensiali."},
    3: {"cat": 1, "q": "Daromad modeli (Business Model) qanaqa?", "a": "Bizda 5 ta daromad oqimi bor:\n1. **In-App Skinlar:** Kosmetik buyumlar.\n2. **VIP Obuna ($9.99):** Tezkor rivojlanish.\n3. **Creator Land:** Yerni kengaytirish uchun to'lov.\n4. **In-World Ads:** Brendlar uchun reklama (B2B).\n5. **Tranzaksiya (5%):** P2P savdodan komissiya."},
    4: {"cat": 1, "q": "Burn Rate (Oylik xarajat) qancha?", "a": "Hozirgi operatsion xarajatlarimiz: oyiga $55,000. $3M investitsiya bilan biz 18-24 oy bemalol ishlay olamiz (Runway). Bu vaqt ichida biz Break-even (Foyda) nuqtasiga chiqamiz."},
    5: {"cat": 1, "q": "Unit Economics: LTV va CAC qanday?", "a": "Mijoz jalb qilish (CAC): **$1.50**.\nMijozdan olinadigan foyda (LTV): **$45**.\nFoydalilik koeffitsiyenti (LTV/CAC): **30x**. (Har $1 reklama $30 foyda keltiradi)."},
    6: {"cat": 1, "q": "Qachon foydaga kirasiz (Break-even)?", "a": "Biz 100,000 faol foydalanuvchiga (MAU) yetganimizda o'zimizni to'liq qoplaymiz. Hozirgi o'sish sur'ati bilan bu 14-oyga to'g'ri keladi."},
    7: {"cat": 1, "q": "Pullarni aynan nimalarga sarflaysiz?", "a": "40% R&D (Dasturlash va AI), 30% Marketing (User Acquisition), 20% Infratuzilma (Serverlar), 10% Zaxira fondi."},
    8: {"cat": 1, "q": "Oldingi raundlarda kimlar pul tikkan?", "a": "Loyiha shu paytgacha 'Bootstrapping' (o'z mablag'imiz) va kichik 'Angel' investorlar ($200k) hisobiga rivojlandi. Bu birinchi institutsional raund."},
    9: {"cat": 1, "q": "Daromadning necha foizi reklamadan keladi?", "a": "Bizning prognozimiz bo'yicha daromadning 30% i B2B hamkorlik va o'yin ichidagi bannerlardan keladi. Brendlar Metaverse auditoriyasiga qiziqmoqda."},
    10: {"cat": 1, "q": "Agar rejaning faqat 10% i o'xshasa-chi?", "a": "Hatto eng yomon ssenariyda, bozorning 1% emas, **0.1%** (3 mln user) olsak ham, yillik daromad **$90 Million** bo'ladi. Bu hozirgi bahodan 5 barobar yuqori. Xavf minimal."},

    # ---------------------------------------------------------
    # 2. MAHSULOT VA TEXNOLOGIYA
    # ---------------------------------------------------------
    11: {"cat": 2, "q": "Raqobatchilardan (Roblox) farqingiz nima?", "a": "Roblox - bu eski grafika. Biz Unreal Engine 5 da ishlaymiz. Asosiy farq: Bizda AI-Agentlar bor, iqtisodiyot tirik va boshqariladigan. Dunyo 'bo'sh' emas."},
    12: {"cat": 2, "q": "AI (Major Tree) nima qiladi?", "a": "U o'yin muvozanatini saqlaydi. Agar o'yinchilar ko'payib ketsa, resurslarni kamaytiradi. Agar zerikishsa, yangi voqealar (Event) yaratadi."},
    13: {"cat": 2, "q": "Serverlar 30 mln odamni ko'taradimi?", "a": "Ha. Biz AWS ning 'Elastic Scaling' va 'Sharding' arxitekturasidan foydalanamiz. Tizim odam soniga qarab avtomatik kengayadi."},
    14: {"cat": 2, "q": "O'yin qaysi platformalarda bor?", "a": "Dastlab PC va Web (Cloud Gaming). 2026-yil oxirida Mobile (iOS/Android) versiya to'liq ishga tushadi."},
    15: {"cat": 2, "q": "Free-to-Play foydalanuvchini qanday ushlab qolasiz?", "a": "O'yin mexanikasi shunday tuzilganki, bepul o'ynab ham yutuqlarga erishish mumkin, lekin vaqt talab etiladi. Bu 'Retention'ni ushlab turadi."},
    16: {"cat": 2, "q": "Barcha grafikani o'zingiz chizasizmi?", "a": "Asosiy aktivlar o'zimizniki, lekin biz 'Procedural Generation' (AI orqali yaratish) dan foydalanib, dunyoni tez kengaytiramiz."},
    17: {"cat": 2, "q": "Ovozli chat bormi?", "a": "Ha, 'Proximity Voice Chat' (Yaqinlashganda eshitish) mavjud. Bu ijtimoiy aloqani kuchaytiradi va Communityni mustahkamlaydi."},
    18: {"cat": 2, "q": "Cheater (G'irrom)larga qarshi tizim bormi?", "a": "Biz AI asosidagi Anti-Cheat tizimini ishlatamiz. U g'ayritabiiy harakatlarni real vaqtda aniqlaydi va bloklaydi."},
    19: {"cat": 2, "q": "Web 3.0 elementlari majburiymi?", "a": "Yo'q, o'yinchi hamyon ulashga majbur emas. Blockchain orqada ishlaydi (Invisible Tech). O'yinchi buni sezmaydi ham."},
    20: {"cat": 2, "q": "Creator Mode imkoniyatlari qanday?", "a": "O'yinchilar o'z uylari, do'konlari va mini-o'yinlarini yaratishi mumkin. Buning uchun kod yozish shart emas (No-code tools)."},

    # ---------------------------------------------------------
    # 3. MARKETING VA O'SISH
    # ---------------------------------------------------------
    21: {"cat": 3, "q": "Auditoriyani qayerdan topasiz?", "a": "Biz Geymerlar va Kripto-entuziastlarni nishonga olganmiz. Influencer marketing va Referral tizim asosiy qurolimiz."},
    22: {"cat": 3, "q": "Viral effekt (Viral Loop) qanday ishlaydi?", "a": "Do'stini taklif qilgan har bir o'yinchiga bepul 'Starter Pack' beriladi. Jamoaviy o'ynash yakkaxon o'ynashdan 2x foydaliroq."},
    23: {"cat": 3, "q": "Reklama byudjeti qancha?", "a": "Dastlabki 6 oyda $500,000 ajratilgan. Asosiy e'tibor TikTok va YouTube Shorts kontentiga qaratiladi."},
    24: {"cat": 3, "q": "Hamkor brendlar bormi?", "a": "Hozirda 3 ta mahalliy brend va 1 ta xalqaro to'lov tizimi bilan 'Letter of Intent' (Kelishuv niyati) imzolangan."},
    25: {"cat": 3, "q": "Global bozorga qachon chiqasiz?", "a": "2026-yil Q3 da Janubiy-Sharqiy Osiyo va Turkiya bozoriga kirish rejada bor. U yerda P2E va o'yinlar juda mashhur."},
    26: {"cat": 3, "q": "Community bilan qanday ishlaysiz?", "a": "Discord va Telegramda 24/7 moderatorlarimiz ishlaydi. Eng faol a'zolar 'Ambassador' maqomini oladi va mukofotlanadi."},
    27: {"cat": 3, "q": "Retention Rate (Qaytish ko'rsatkichi) maqsadi?", "a": "Bizning maqsad: D30 (30-kunlik qaytish) ko'rsatkichini 25% da ushlab turish. Sanoat standarti 15%."},
    28: {"cat": 3, "q": "ASO (App Store Optimization) strategiyasi?", "a": "Biz kalit so'zlar va skrinshotlarni A/B test qilib, organik yuklab olishlarni oshiramiz."},
    29: {"cat": 3, "q": "PR (Jamoatchilik) strategiyasi?", "a": "Biz o'yin ichidagi voqealar orqali OAV e'tiborini tortamiz. Masalan: Virtual konsertlar va Kiber-sport musobaqalari."},
    30: {"cat": 3, "q": "Email Marketing ishlatasizmi?", "a": "Ha, foydalanuvchilarni o'yinga qaytarish uchun 'Haftalik dayjest' va maxsus chegirmalar yuboramiz."},

    # ---------------------------------------------------------
    # 4. XATARLAR VA QONUNCHILIK
    # ---------------------------------------------------------
    31: {"cat": 4, "q": "Agar Apple o'yinni bloklasa?", "a": "Bizda WebGL (Brauzer) versiyasi bor. Asosiy daromad Apple tizimidan tashqarida, Web-do'kon orqali o'tadi. 30% komissiyani ham tejab qolamiz."},
    32: {"cat": 4, "q": "Katta kompaniyalar (Meta) nusxa ko'chirsachi?", "a": "Texnologiyani ko'chirish oson, lekin Jamiyatni (Community) ko'chirish qiyin. Bizning ustunligimiz — sodiq auditoriya va o'ziga xos iqtisodiyot."},
    33: {"cat": 4, "q": "Kripto bozori qulasa (Crypto Winter)?", "a": "Biz token narxiga bog'lanmaganmiz. Daromadimiz Fiat (Dollar) da, reklama va obunalardan keladi. Biz gibrid modeldamiz."},
    34: {"cat": 4, "q": "Xakerlik hujumiga tayyormisiz?", "a": "Biz muntazam 'Penetration Testing' (buzib kirish testi) o'tkazamiz va Cloudflare himoyasidan foydalanamiz."},
    35: {"cat": 4, "q": "Jamoa tarqalib ketsa nima bo'ladi?", "a": "Asosiy xodimlar uchun 'Vesting' (Ulushni vaqtga bog'lash) tizimi bor. Ular 4 yil davomida ketolmaydi, aks holda ulushidan mahrum bo'ladi."},
    36: {"cat": 4, "q": "Server xarajatlari oshib ketsa?", "a": "Bizda 'Unit Economics' ijobiy. Har bir yangi user xarajatdan ko'ra 30 barobar ko'proq daromad keltiradi. O'sish xarajatni qoplaydi."},
    37: {"cat": 4, "q": "Bolalar xavfsizligi (COPPA) qanday?", "a": "Bizda so'kinishlarni bloklovchi AI-filtr va ota-ona nazorati funksiyalari mavjud. Xavfsizlik birinchi o'rinda."},
    38: {"cat": 4, "q": "Yuridik muammolar bormi?", "a": "Bizning yurisdiksiyamiz (Dubay/Singapur) virtual aktivlar uchun eng qulay hudud hisoblanadi. Litsenziyalar olingan."},
    39: {"cat": 4, "q": "Agar o'yin zerikarli bo'lib qolsa?", "a": "Major Tree AI har hafta yangi 'Kvestlar' va ssenariylarni avtomatik yaratadi. O'yin hech qachon bir xil bo'lib qolmaydi."},
    40: {"cat": 4, "q": "Valyuta kursi o'zgarishi ta'siri?", "a": "Bizning barcha narxlarimiz USD ga bog'langan (Stablecoin), bu devalvatsiyadan himoya qiladi."},

    # ---------------------------------------------------------
    # 5. STRATEGIYA VA EXIT
    # ---------------------------------------------------------
    41: {"cat": 5, "q": "Investor qanday chiqib ketadi (Exit)?", "a": "2027 yilda Strategik sotuv (M&A) yoki 2029 yilda IPO orqali. $20M baholash o'shanda $500M+ bo'lishi kutilmoqda."},
    42: {"cat": 5, "q": "Keyingi investitsiya raundi qachon?", "a": "18 oydan keyin Series A ($10M-$15M) jalb qilishni rejalashtirganmiz. Baholash $50M+ bo'ladi."},
    43: {"cat": 5, "q": "Kompaniya missiyasi nima?", "a": "Raqamli dunyoda odamlarga ishlash, yaratish va yashash uchun eng mukammal va adolatli platformani berish."},
    44: {"cat": 5, "q": "Eng katta orzuyingiz (Vision)?", "a": "100 million aholisi bor, yalpi ichki mahsuloti (GDP) real davlatlarnikiga teng bo'lgan virtual davlatni yaratish."},
    45: {"cat": 5, "q": "Hozir eng katta muammo nima?", "a": "Tezkor o'sish uchun yetarli marketing byudjeti va top-darajali AI mutaxassislar yetishmasligi. Investitsiya buni hal qiladi."},
    46: {"cat": 5, "q": "Boshqaruv kengashi (Board) bormi?", "a": "Biz 2 nafar xalqaro maslahatchini (Advisors) jalb qilganmiz. Ular Blizzard va Tencent sobiq xodimlari."},
    47: {"cat": 5, "q": "Mahsulotni rivojlantirish rejasi (Roadmap)?", "a": "Q1: MVP (Alpha) -> Q2: Marketing Campaign -> Q3: Global Launch (PC/Web) -> Q4: Mobile App Release."},
    48: {"cat": 5, "q": "Nega hozir? (Why Now?)", "a": "Texnologiya (UE5, AI) yetildi va bozor 'Zerikarli Metaverse'dan charchadi. Odamlar yangilik kutmoqda. Timing (Vaqt) ideal."},
    49: {"cat": 5, "q": "Bizdan boshqa nima so'raysiz?", "a": "Bizga nafaqat pul, balki sizning 'Networking' (Aloqalar) va strategik maslahatlaringiz kerak. Smart Money qidiryapmiz."},
    50: {"cat": 5, "q": "Agar $3M bermasak nima bo'ladi?", "a": "Biz baribir o'samiz, faqat sekinroq (Bootstrapping). Lekin bozor bo'sh turmaydi, tezlik hozir eng muhim omil. Birga tezroq egallaymiz."}
}