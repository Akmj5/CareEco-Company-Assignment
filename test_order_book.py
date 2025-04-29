# test_order_book.py

from order_book import ConsolidatedBook

def test_basic_operations():
    book = ConsolidatedBook()

    book.new_order("o1", "AAPL", 100.0, "BUY", 10)
    book.new_order("o2", "AAPL", 101.0, "BUY", 5)
    book.new_order("o3", "AAPL", 102.0, "SELL", 7)
    book.new_order("o4", "AAPL", 103.0, "SELL", 8)

    print("\nTop 5 Levels After New Orders:")
    top_levels = book.get_top_levels("AAPL")
    for level in top_levels:
        print(level)

    book.cancel_order("o2")
    print("\nTop 5 Levels After Cancel Order o2:")
    top_levels = book.get_top_levels("AAPL")
    for level in top_levels:
        print(level)

    book.modify_order("o1", 20)
    print("\nTop 5 Levels After Modify Order o1:")
    top_levels = book.get_top_levels("AAPL")
    for level in top_levels:
        print(level)

def test_top_of_book_update():
    book = ConsolidatedBook()

    book.top_of_book_update("GOOG", 1500.0, 10, 1501.0, 12)
    book.top_of_book_update("GOOG", 1500.0, 15, 1502.0, 8)

    print("\nTop 5 Levels After Top of Book Updates:")
    top_levels = book.get_top_levels("GOOG")
    for level in top_levels:
        print(level)

if __name__ == "__main__":
    print("Running Basic Operations Test:")
    test_basic_operations()

    print("\nRunning Top of Book Test:")
    test_top_of_book_update()
