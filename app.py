# app.py

import streamlit as st
import pandas as pd
import random
import time
from order_book import ConsolidatedBook

# IMPORTANT: This must be the first Streamlit command
st.set_page_config(page_title="One Big Exchange", layout="wide")

@st.cache_resource
def get_book():
    return ConsolidatedBook()

book = get_book()

st.title("📈 One Big Exchange: Live Consolidated Order Book")

symbols = ["AAPL", "GOOG", "MSFT", "TSLA", "AMZN"]

# Sidebar controls
symbol_selected = st.sidebar.selectbox("Select Symbol", symbols)
feed_type = st.sidebar.radio("Feed Type", ("Top of Book Update", "Order Based Feed"))

# Manual update section
with st.sidebar.expander("Manual Order Feed"):
    order_id = st.text_input("Order ID", value=f"ORD{random.randint(1000,9999)}")
    limit_price = st.number_input("Limit Price", value=100.0)
    quantity = st.number_input("Quantity", value=10, step=1)
    side = st.radio("Side", ("BUY", "SELL"))
    if st.button("New Order"):
        book.new_order(order_id, symbol_selected, limit_price, side, quantity)
        st.success("Order Added.")

with st.sidebar.expander("Manual Top of Book Update"):
    bid_price = st.number_input("Best Bid Price", value=99.5)
    bid_size = st.number_input("Best Bid Size", value=20)
    offer_price = st.number_input("Best Offer Price", value=100.5)
    offer_size = st.number_input("Best Offer Size", value=15)
    if st.button("Top Book Update"):
        book.top_of_book_update(symbol_selected, bid_price, bid_size, offer_price, offer_size)
        st.success("Top Book Updated.")

# Auto-simulator of random feeds
if st.button("Simulate Random Feed"):
    for _ in range(10):
        symbol = random.choice(symbols)
        if feed_type == "Order Based Feed":
            order_id = f"SIM{random.randint(1000,9999)}"
            limit_price = round(random.uniform(95, 105), 2)
            quantity = random.randint(1, 20)
            side = random.choice(["BUY", "SELL"])
            book.new_order(order_id, symbol, limit_price, side, quantity)
        else:
            best_bid = round(random.uniform(95, 100), 2)
            best_offer = round(random.uniform(100, 105), 2)
            book.top_of_book_update(symbol, best_bid, random.randint(5,20), best_offer, random.randint(5,20))
        time.sleep(0.1)
    st.success("Simulation Complete.")

st.subheader(f"Top 5 Levels for {symbol_selected}")

data = book.get_top_levels(symbol_selected)
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
