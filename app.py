import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Chemos Sales", layout="wide")
st.title("💰 Chemos Sales Transaction System")
st.success("✅ Clean Deployment - Working!")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Go to", ["POS", "Products", "Dashboard"])
    
# Sample data
products = pd.DataFrame({
    'ID': ['P001', 'P002', 'P003'],
    'Name': ['Laptop', 'Mouse', 'Keyboard'],
    'Price': [999.99, 24.99, 79.99],
    'Stock': [25, 100, 50]
})

if page == "POS":
    st.header("🛍️ Point of Sale")
    
    col1, col2 = st.columns(2)
    
    with col1:
        selected = st.selectbox("Select Product", products['Name'].tolist())
        qty = st.number_input("Quantity", 1, 100, 1)
        
        if st.button("Add to Cart", type="primary"):
            st.success(f"Added {qty} x {selected}")
    
    with col2:
        st.subheader("Cart")
        st.write("Cart items will appear here")
        
elif page == "Products":
    st.header("📦 Products")
    st.dataframe(products, use_container_width=True)
    
else:
    st.header("📊 Dashboard")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Sales", ",259.94")
    with col2:
        st.metric("Products", len(products))
    with col3:
        st.metric("Today", datetime.now().strftime("%Y-%m-%d"))

st.markdown("---")
st.info("This is a clean, working deployment of the sales system.")