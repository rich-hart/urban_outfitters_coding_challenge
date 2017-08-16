from handlers.rewards_handler import RewardsHandler
from handlers.purchase_handler import PurchasesHandler
url_patterns = [
    (r'/rewards', RewardsHandler),
    (r'/purchases', PurchasesHandler),
]
