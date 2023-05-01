from selenium.webdriver.common.by import By

# descriere selectori din site

HOME = (By.XPATH, '//*[@id="logo"]/a')
REZERVA_ACUM = (By.XPATH, '//*[@id="header"]/div/nav/a[1]')
HOME_REZERVA = (By.XPATH, '//*[@id="myTopnav"]/a[2]/span')
MENIU_RESTAURANT = (By.CSS_SELECTOR, '#header > div > nav > a:nth-child(2)')
LOGO = (By.CSS_SELECTOR, '#logo > a')
GALERIE_FOTO = (By.CSS_SELECTOR, '#header > div > nav > a:nth-child(3)')
DESPRE_NOI = (By.CSS_SELECTOR, '#header > div > nav > a:nth-child(4)')
CONTACT = (By.CSS_SELECTOR, '#header > div > nav > a:nth-child(5)')
IMAGINI = (By.CLASS_NAME, 'booking-item-img-num')
REZERVAREA_MEA = (By.CLASS_NAME, "mb0")
NOTA_REVIEW = (By.CLASS_NAME, 'review-number')
COD_PROMOTIONAL_BTN = (By.CSS_SELECTOR, '#voucherCodeForm > div.col-xs-4.pln > input')
COD_PROMO_ERROR = (By.CSS_SELECTOR, "#voucherCodeError")
AUTENTIFICARE = (By.CSS_SELECTOR,
                 '#main-header > div.header-top.bg-color > div > div > div.col-md-4 > div > ul >'
                 ' li.top-user-area-avatar.hidden-sm.hidden-xs')
NR_REZERVARE = (By.CSS_SELECTOR,
                'body > main > div.global-wrap > div.container > div > div.col-md-4.mb30 > form >'
                ' div:nth-child(1) > input')
PAROLA = (By.CSS_SELECTOR,
          'body > main > div.global-wrap > div.container > div > div.col-md-4.mb30 > form > div:nth-child(2) > input')
IDENTIFICA = (By.CSS_SELECTOR, 'body > main > div.global-wrap > div.container > div > div.col-md-4.mb30 > form > input')
TEXT_AUTENT = (By.CLASS_NAME, 'text-small')
TERMENI_COND = (By.PARTIAL_LINK_TEXT, 'Termeni')
AM_CITIT = (By.CSS_SELECTOR, '#privacyPolicy > div > div > div > div > button')
LIMBI_DISPONIBILE = (By.CLASS_NAME, 'fa fa-angle-up')