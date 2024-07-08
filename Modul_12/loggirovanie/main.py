import requests as rq
import logging


format_ = '%(levelname)s: %(message)s '
logging.basicConfig(level=logging.INFO)
formatter = logging.Formatter(format_)

logger_info = logging.getLogger('success')
h_inf = logging.FileHandler(filename='success_responses.log', mode='w')
h_inf.setFormatter(formatter)
logger_info.addHandler(h_inf)

logger_war = logging.getLogger('bad')
h_war = logging.FileHandler(filename='bad_responses.log', mode='w')
h_war.setFormatter(formatter)
logger_war.addHandler(h_war)

logger_err = logging.getLogger('blocked')
h_err = logging.FileHandler(filename='blocked_responses.log', mode='w')
h_err.setFormatter(formatter)
logger_err.addHandler(h_err)


sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        code = response.status_code
        if code == 200:
            logger_info.info(f"'{site}', response - {response.status_code}")
        elif code != 200:
            logger_war.warning(f"'{site}', response - {response.status_code}")
    except Exception:
        logger_err.error(f"'{site}', NO CONNECTION")
