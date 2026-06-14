import streamlit as st
import pandas as pd

df = pd.read_csv("data/cleaned_data.csv")

st.set_page_config(page_title="Budget Food Finder", layout="wide")

st.title("🍽 Budget Food Finder")

# ---------------- Sidebar ----------------
st.sidebar.header("Filters")

keyword = st.sidebar.text_input("Search food (e.g. chicken, bowl, salad)")
budget = st.sidebar.number_input("Max Budget (₹)", min_value=0, value=500)

category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["Category"].unique().tolist())
)

# ---------------- Filtering ----------------
filtered = df.copy()

if keyword:
    filtered = filtered[
        filtered["Menu_Item"].str.lower().str.contains(keyword.lower(), na=False)
    ]

if category != "All":
    filtered = filtered[filtered["Category"] == category]

filtered = filtered[filtered["Price"] <= budget]

# ---------------- Main UI ----------------
st.subheader("Results")

if filtered.empty:
    st.warning("No items found. Try increasing budget or changing filters.")
else:
    filtered = filtered.sort_values(by="Price")

    # BEST ITEM HIGHLIGHT
    best = filtered.iloc[0]

    st.success("🔥 Top Recommendation")
    st.markdown(f"""
    ### {best['Menu_Item']}
    **Category:** {best['Category']}  
    **Price:** ₹{best['Price']}
    """)

    st.divider()

    # CARD STYLE DISPLAY
    st.subheader("All Matches")

    for _, row in filtered.iterrows():
        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(f"""
            **{row['Menu_Item']}**  
            Category: {row['Category']}
            """)

        with col2:
            st.markdown(f"### ₹{row['Price']}")

        st.divider()

# ---------------- Analytics ----------------
st.subheader("Insights")

col1, col2 = st.columns(2)

with col1:
    st.write("Category Distribution")
    st.bar_chart(df["Category"].value_counts())

with col2:
    st.write("Average Price by Category")
    st.bar_chart(df.groupby("Category")["Price"].mean())