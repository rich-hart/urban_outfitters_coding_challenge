from handlers.rewards_handler import RewardsHandler
from handlers.purchase_handler import PurchasesHandler
from handlers.account_handler import AccountsHandler 


url_patterns = [
    (r'/rewards', RewardsHandler),
    (r'/purchases/?'\
      '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)?'\
      '/?', PurchasesHandler),
    (r'/accounts/?'\
      '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)?'\
      '/?', AccountsHandler),
]
