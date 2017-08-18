from handlers.rewards_handler import RewardsHandler
from handlers.purchase_handler import PurchasesHandler
from handlers.account_handler import AccountHandler 
url_patterns = [
    (r'/rewards', RewardsHandler),
    (r'/purchases', PurchasesHandler),
    (r'/accounts/[0-9]+', AccountHandler),
]
