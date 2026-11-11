from flask import Flask, render_template_string, request

app = Flask(__name__)

# Portfolio Data with 4 Languages (Arabic, Darija, French, English)
translations = {
    'ar': {
        'title': 'عمران فتحي - مبرمج ومقاتل MMA',
        'subtitle': 'مطور برمجيات، باحث أمني، ومقاتل محترف',
        'cv_title': 'السيرة الذاتية (CV)',
        'cv_name': 'الاسم الكامل: عمران فتحي',
        'cv_dob': 'تاريخ الازدياد: 10/5/2013',
        'cv_goal': 'المطالب والهدف الحالي: أبحت عن منافسة في الفنون القتالية المختلطة (MMA) وأنا مستعد تماماً!',
        'cv_contact': 'التواصل: 0600333573 | انستغرام: supernova_3x',
        'about_title': 'من أنا؟',
        'about_text': 'أنا عمران، عمري 13 سنة. أجمع بين قوة الانضباط في الـ MMA ودقة البرمجة والأمن السيبراني.',
        'skills_title': 'المهارات التقنية',
        'mma_title': 'مسار الفنون القتالية (MMA)',
        'mma_text': 'التدريب المستمر، الانضباط الذهني، والقتال بروح التحدي.',
        'quiz_title': '🎮 ميني جيم: تحدى معلوماتك مع عمران!',
        'submit': 'إرسال الأجوبة',
        'score_text': 'نتيجة الكويز الخاصة بك:',
        'footer': 'جميع الحقوق محفوظة © 2026 عمران فتحي'
    },
    'ary': {
        'title': 'Imrane Fathi - Pro Coder & MMA Fighter',
        'subtitle': 'ديفلوبر، باحث في السيرفرات، ومقاتل MMA',
        'cv_title': 'السيرة الذاتية (CV)',
        'cv_name': 'السمية الكاملة: عمران فتحي',
        'cv_dob': 'تاريخ الازدياد: 10/5/2013',
        'cv_goal': 'المطالب: كانقلب على شي competition دالـ MMA وأنا واجد ديما!',
        'cv_contact': 'النيمرو: 0600333573 | انستغرام: supernova_3x',
        'about_title': 'شكون أنا؟',
        'about_text': 'أنا عمران، عندي 13 عام. جامع بين القوة والتركيز فـ MMA وبين التخربيق فـ Python وكودات.',
        'skills_title': 'المهارات ديالي',
        'mma_title': 'الكونديسيون والـ MMA',
        'mma_text': 'التدريب الصح، الصبر، والقتال حتى آخر لحظة.',
        'quiz_title': '🎮 ميني جيم: تيصي راسك واش فنان ولا والو!',
        'submit': 'شوف النتيجة',
        'score_text': 'السكور ديالك:',
        'footer': 'جميع الحقوق محفوظة © 2026 عمران فتحي'
    },
    'fr': {
        'title': 'Imrane Fathi - Développeur & Combattant MMA',
        'subtitle': 'Développeur logiciel & passionné de cybersécurité',
        'cv_title': 'CV & Profil',
        'cv_name': 'Nom complet : Imrane Fathi',
        'cv_dob': 'Date de naissance : 10/5/2013',
        'cv_goal': 'Objectif : Je cherche une compétition de MMA et je suis prêt !',
        'cv_contact': 'Tél : 0600333573 | Instagram : supernova_3x',
        'about_title': 'À propos de moi',
        'about_text': 'Je m\'appelle Imrane, 13 ans. Je combine la discipline du MMA et la logique du code.',
        'skills_title': 'Compétences',
        'mma_title': 'Parcours MMA',
        'mma_text': 'Entraînement rigoureux et mentalité de gagnant.',
        'quiz_title': '🎮 Mini-Jeu : Testez vos connaissances !',
        'submit': 'Soumettre',
        'score_text': 'Votre score :',
        'footer': 'Tous droits réservés © 2026 Imrane Fathi'
    },
    'en': {
        'title': 'Imrane Fathi - Coder & MMA Fighter',
        'subtitle': 'Software Developer, Cybersecurity Enthusiast & MMA Fighter',
        'cv_title': 'Curriculum Vitae (CV)',
        'cv_name': 'Full Name: Imrane Fathi',
        'cv_dob': 'Date of Birth: 10/5/2013',
        'cv_goal': 'Goal: Looking for an MMA competition and I am fully ready!',
        'cv_contact': 'Phone: 0600333573 | Instagram: supernova_3x',
        'about_title': 'About Me',
        'about_text': 'I am Imrane, 13 years old. Combining the physical discipline of MMA with programming logic.',
        'skills_title': 'Skills',
        'mma_title': 'MMA Journey',
        'mma_text': 'Relentless training, mental discipline, and fighting spirit.',
        'quiz_title': '🎮 Mini-Game: Test Your Knowledge!',
        'submit': 'Submit Answers',
        'score_text': 'Your Quiz Score:',
        'footer': 'All rights reserved © 2026 Imrane Fathi'
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="{{ lang }}" dir="{{ 'rtl' if lang in ['ar', 'ary'] else 'ltr' }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ t.title }}</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: rgba(30, 41, 59, 0.8);
            --accent: #38bdf8;
            --accent-hover: #0ea5e9;
            --text-color: #f8fafc;
            --text-muted: #94a3b8;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            width: 90%;
            max-width: 850px;
            margin: 40px auto;
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        }
        .lang-switch {
            text-align: center;
            margin-bottom: 20px;
        }
        .lang-switch a {
            color: var(--accent);
            text-decoration: none;
            margin: 0 6px;
            font-weight: bold;
            padding: 6px 12px;
            border: 1px solid var(--accent);
            border-radius: 8px;
            transition: 0.3s;
        }
        .lang-switch a:hover, .lang-switch a.active {
            background-color: var(--accent);
            color: var(--bg-color);
        }
        h1 { color: var(--accent); text-align: center; margin-bottom: 5px; }
        p.subtitle { text-align: center; color: var(--text-muted); margin-top: 0; margin-bottom: 30px; }
        .section {
            background: rgba(15, 23, 42, 0.6);
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            border-left: 4px solid var(--accent);
        }
        .cv-section {
            border-left-color: #4ade80;
            background: rgba(74, 222, 128, 0.05);
        }
        .cv-section h2 { color: #4ade80; margin-top: 0; }
        /* Quiz Styling */
        .quiz-box {
            background: rgba(56, 189, 248, 0.05);
            border: 2px dashed var(--accent);
            padding: 20px;
            border-radius: 12px;
            margin-top: 20px;
        }
        .question-card {
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        .quiz-box label {
            display: block;
            margin: 6px 0;
            cursor: pointer;
        }
        button.btn {
            background-color: var(--accent);
            color: var(--bg-color);
            border: none;
            padding: 10px 20px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 10px;
            transition: 0.2s;
        }
        button.btn:hover { background-color: var(--accent-hover); }
        .score-result {
            margin-top: 15px;
            padding: 12px;
            background: rgba(56, 189, 248, 0.2);
            border-radius: 8px;
            font-weight: bold;
            text-align: center;
            font-size: 1.1rem;
        }
        footer { text-align: center; color: var(--text-muted); margin-top: 20px; font-size: 0.9rem; }
    </style>
</head>
<body>

    <div class="container">
        <!-- Language Switcher -->
        <div class="lang-switch">
            <a href="/?lang=ar" class="{{ 'active' if lang == 'ar' else '' }}">العربية</a>
            <a href="/?lang=ary" class="{{ 'active' if lang == 'ary' else '' }}">الدارجة</a>
            <a href="/?lang=fr" class="{{ 'active' if lang == 'fr' else '' }}">Français</a>
            <a href="/?lang=en" class="{{ 'active' if lang == 'en' else '' }}">English</a>
        </div>

        <h1>{{ t.title }}</h1>
        <p class="subtitle">{{ t.subtitle }}</p>

        <!-- CV Section -->
        <div class="section cv-section">
            <h2>📄 {{ t.cv_title }}</h2>
            <p><strong>{{ t.cv_name }}</strong></p>
            <p>📅 {{ t.cv_dob }}</p>
            <p>🥊 {{ t.cv_goal }}</p>
            <p>📞 🌐 {{ t.cv_contact }}</p>
        </div>

        <!-- About Section -->
        <div class="section">
            <h2>{{ t.about_title }}</h2>
            <p>{{ t.about_text }}</p>
        </div>

        <!-- Skills Section -->
        <div class="section">
            <h2>{{ t.skills_title }}</h2>
            <ul>
                <li>Python, Flask & Web Development</li>
                <li>Network Security & Kali Linux (Basics)</li>
                <li>Git & GitHub Deployment</li>
            </ul>
        </div>

        <!-- MMA Section -->
        <div class="section">
            <h2>{{ t.mma_title }}</h2>
            <p>{{ t.mma_text }}</p>
        </div>

        <!-- Multi-Question Quiz Mini-Game -->
        <div class="quiz-box">
            <h3>{{ t.quiz_title }}</h3>
            <form method="POST">
                <!-- Q1 -->
                <div class="question-card">
                    <p><strong>1. شنوه هي لغة البرمجة باش مصاوب هاد الويبسايت؟ / Which language powers this site?</strong></p>
                    <label><input type="radio" name="q1" value="python" required> Python</label>
                    <label><input type="radio" name="q1" value="html"> HTML only</label>
                </div>

                <!-- Q2 -->
                <div class="question-card">
                    <p><strong>2. شحال فالعمر ديال عمران؟ / How old is Imrane?</strong></p>
                    <label><input type="radio" name="q2" value="13" required> 13 years old</label>
                    <label><input type="radio" name="q2" value="20"> 20 years old</label>
                </div>

                <!-- Q3 -->
                <div class="question-card">
                    <p><strong>3. شنو هو الرياضة اللي كيمارسها عمران بجانب البرمجة؟ / Imrane's combat sport?</strong></p>
                    <label><input type="radio" name="q3" value="mma" required> MMA (Mixed Martial Arts)</label>
                    <label><input type="radio" name="q3" value="tennis"> Tennis</label>
                </div>

                <button type="submit" class="btn">{{ t.submit }}</button>
            </form>

            {% if score is not none %}
                <div class="score-result">
                    🏆 {{ t.score_text }} {{ score }} / 3
                </div>
            {% endif %}
        </div>

        <footer>
            <p>{{ t.footer }}</p>
        </footer>
    </div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    lang = request.args.get('lang', 'ary')  # Default to Darija
    if lang not in translations:
        lang = 'ary'
    
    t = translations[lang]
    score = None

    if request.method == 'POST':
        score = 0
        if request.form.get('q1') == 'python':
            score += 1
        if request.form.get('q2') == '13':
            score += 1
        if request.form.get('q3') == 'mma':
            score += 1

    return render_template_string(HTML_TEMPLATE, t=t, lang=lang, score=score)

if __name__ == '__main__':
    app.run(debug=True)