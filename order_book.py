# order_book.py

from collections import defaultdict

class ConsolidatedBook:
    def __init__(self):
        self.books = defaultdict(lambda: {"BUY": {}, "SELL": {}})
        self.order_id_map = {}

    def new_order(self, order_id, symbol, limit_price, side, quantity):
        book = self.books[symbol]
        price_level = book[side].setdefault(limit_price, 0)
        book[side][limit_price] = price_level + quantity
        self.order_id_map[order_id] = (symbol, limit_price, side, quantity)

    def cancel_order(self, order_id):
        if order_id not in self.order_id_map:
            return
        symbol, limit_price, side, quantity = self.order_id_map.pop(order_id)
        book = self.books[symbol]
        if limit_price in book[side]:
            book[side][limit_price] -= quantity
            if book[side][limit_price] <= 0:
                del book[side][limit_price]

    def modify_order(self, order_id, new_quantity):
        if order_id not in self.order_id_map:
            return
        symbol, limit_price, side, old_quantity = self.order_id_map[order_id]
        diff = new_quantity - old_quantity
        book = self.books[symbol]
        book[side][limit_price] += diff
        self.order_id_map[order_id] = (symbol, limit_price, side, new_quantity)
        if book[side][limit_price] <= 0:
            del book[side][limit_price]

    def top_of_book_update(self, symbol, best_bid_price, best_bid_size, best_offer_price, best_offer_size):
        book = self.books[symbol]
        book["BUY"][best_bid_price] = best_bid_size
        book["SELL"][best_offer_price] = best_offer_size

    def get_top_levels(self, symbol, levels=5):
        book = self.books[symbol]
        bids = sorted(book["BUY"].items(), key=lambda x: -x[0])
        asks = sorted(book["SELL"].items(), key=lambda x: x[0])

        consolidated = []
        for i in range(levels):
            bid_price, bid_size = bids[i] if i < len(bids) else ("-", "-")
            ask_price, ask_size = asks[i] if i < len(asks) else ("-", "-")
            consolidated.append({
                "Level": i,
                "Bid Size": bid_size,
                "Bid Price": bid_price,
                "Ask Price": ask_price,
                "Ask Size": ask_size
            })
        return consolidated
