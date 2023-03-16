import json

AUTHOR = 'Sitala'
SITENAME = 'CV'

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'Russian'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = "resume"
CSS_FILE = 'main-3.css'

# Profile information
NAME = 'Сітала Микола'
TAGLINE = 'Заступник директора'
PIC = 'profile.png'

# sidebar links
EMAIL = 'nsitala@ukr.net'
PHONE = '(+38) 067-569-14-55'
WEBSITE = 'sitala.netlify.app'
LINKEDIN = 'nsitala'
GITHUB = 'sharkevolution'
TWITTER = 'nsitala'

CAREER_SUMMARY_HEAD = 'Профіль'
CAREER_SUMMARY = 'Фахівець у галузі транспортної логістики. Маю хороші аналітичні здібності та досвід створення унікальних рішень у транспортній логістиці.' \
                 'Швидко навчаюсь, прагну стати частиною професійної команди, ' \
                 'в якій я міг би застосувати свої навички та досвід для досягнення командних результатів. '


SOFT_SKILLS_HEAD = 'Ключові навички'

SOFT_SKILLS = [
    {
        'title': 'Командна праця',
        'level': '100'
    },
    {
        'title': 'Креативність',
        'level': '80'
    },
    {
        'title': 'Аналіз даних',
        'level': '100'
    },
    {
        'title': 'Управління персоналом',
        'level': '90'
    },
]

HARD_SKILLS_HEAD = 'Технічні навички'
HARD_SKILLS = json.dumps({"Python": 4.0,
                          "Jupyter": 4.0,
                          "Sql": 3.0,
                          "Lua": 3.0,
                          "HTML": 3.0,
                          "CSS": 2.0,
                          "BPMN": 4.0,
                          "linux": 3.0
                          })

PROJECT_INTRO = 'Частина реалізованих проектів'

PROJECTS_HEAD = 'Проекты'
PROJECTS = [
    {
        'title': 'Оцінка вартості володіння транспортом на періоді до 5 років.<br>',
        'tagline': 'на підставі виконаної оцінки вартості володіння різними типами транспорту, ' \
        'компанія придбала транспорт для доставки та господарських потреб.'
    },
    {
        'title': 'Cистема розрахунку вартості підйомів на поверх<br>',
        'tagline': "на підставі проведеного аналізу проведено розрахунок та впроваджено систему оцінки вартості підйомів на поверх для кур'єрів."
    },
    {
        'title': 'Система обліку та планування транспорту<br>',
        'tagline': 'брав участь у створенні, написанні, розробці системи обліку та планування на підприємстві з нуля.'
    },
    {
        'title': 'Впровадження системи мотивації диспетчерів<br>',
        'tagline': 'з метою підвищення ефективності диспетчерів, запроваджено систему мотивації на підставі показників.'
    },
]

LANGUAGES_HEAD = 'Мови'
LANGUAGES = [
    {
        'name': 'Український',
        'description': 'Native'
    },
    {
        'name': 'English',
        'description': 'Intermediate'
    },
    {
        'name': 'Російська',
        'description': 'Native'
    }
]

INTERESTS_HEAD = 'Інтереси'
INTERESTS = [
    'Алгоритми',
    'Метаевристика',
    'Теорія графів',
    'Задача комівояжера',
    'GIS',
    'BigData',
    'Data Mining',
    ]


EXPERIENCES_HEAD = 'Досвід роботи'
ACHIEVMENTS_HEAD = None  # 'Досягнення'
EXPERIENCES = [
    {
        'job_title': 'Заступник директора з логістики',
        'time': '2019 - 2022',
        'company': 'ТОВ Розетка',
        'details': 'Організація та управління магістральними перевезеннями; <br>'
                   'Планування потреб у транспорті; <br>'
                   'Оцінка та розрахунок вартості володіння транспортром 2т, 5т, 20т; <br>'
                   'Розрахунок рентабельності доставки у регіонах (last mile); <br>'
                   'Розрахунок вартості підйомів на поверх B2C ; <br>'
                   'Формування бізнес-вимог, технічних завдань.',
        'achievments': 'ok'
    },
    {
        'job_title': 'Начальник відділу',
        'time': '2009 - 2019',
        'company': 'ТОВ БаДМ',
        'details': 'Організація роботи відділу 7чол; <br>'
                   'Оптимізація та облік транспортних витрат, KPI; <br>'
                   'Скорочені витрати на 5% за рахунок створення та впровадження системи обліку та планування транспорту, GPS; <br>'
                   'Формування бізнес-вимог, технічних завдань; <br>'
                   'Аналіз, розуміння, розробка систем планування із нуля.',
        'achievments': 'ok'
    },
    {
        'job_title': 'Начальник сектора',
        'time': '2000 - 2009',
        'company': 'ТОВ АТБ-Маркет',
        'details': 'Впровадження системи мотивації диспетчерів; <br>'
                   'Збільшено обсяги завантаження транспорту на 7%; <br>'
                   'Планування та управління диспетчерською службою 27чол; <br>'
                   'Планування потреби рухомого складу >200од; <br>'
                   'Розробка вимог щодо диспетчеризації; <br>'
                   'Автоматизація розрахунків, розробка алгоритму пошуку найкоротших відстаней.',
        'achievments': 'ok'
    },
]

EDUCATIONS_HEAD = 'Освіта'
EDUCATIONS = [
    {
        'degree': 'Товарознавство та комерційна діяльність; Облік і аудит',
        'meta': 'Харківський університет харчування та торгівлі',
        'time': '2001 - 2006'
    },
    {
        'degree': 'Компанія SkillsUp',
        'meta': 'Навчання Бізнес аналіз у дії',
        'time': '2018'
    },
    {
        'degree': 'Бізнес тренер Сергей Жарков',
        'meta': 'Бізнес-тренінг «Розвиток управлінських навичок»',
        'time': '2015'
    }
]

EXTRA_HEAD = 'Додатково'

SITEMAP = {
    "format": "xml"
}

if __name__ == '__main__':
    print(CAREER_SUMMARY)
