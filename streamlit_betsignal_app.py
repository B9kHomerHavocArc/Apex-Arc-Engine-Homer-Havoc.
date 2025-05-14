
import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="BetSignal DeltaScope", layout="wide")

# Load data
with open("BetSignal_Dashboard_Data.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Title
st.title("BetSignal DeltaScope - HR Prop Value Detector")

# Filters
teams = st.multiselect("Filter by Team", sorted(df["Team"].unique()), default=sorted(df["Team"].unique()))
tiers = st.multiselect("Filter by Value Tier", df["Value Tier"].unique(), default=df["Value Tier"].unique())

filtered_df = df[(df["Team"].isin(teams)) & (df["Value Tier"].isin(tiers))]

# Display table
st.dataframe(filtered_df.style.background_gradient(cmap='coolwarm', subset=["Edge (%)"]))

# Downloadable version
st.download_button("Download CSV", filtered_df.to_csv(index=False), "Filtered_BetSignal_Props.csv", "text/csv")
