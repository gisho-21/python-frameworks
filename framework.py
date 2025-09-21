# Part 1: Load & Explore Data (Jupyter Notebook)

# notebooks/analysis.ipynb
import pandas as pd

# Load dataset
df = pd.read_csv("../data/metadata.csv")

# Preview data
print(df.shape)
print(df.info())
print(df.head())

# Missing values
print(df.isnull().sum().sort_values(ascending=False))

# Part 2: Clean & Prepare Data
 
# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract year
df['year'] = df['publish_time'].dt.year

# Add abstract word count
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))

# Part 3: Analysis & Visualization

import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Publications by year
year_counts = df['year'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()

# Top journals
top_journals = df['journal'].value_counts().head(10)
sns.barplot(y=top_journals.index, x=top_journals.values)
plt.title("Top Journals")
plt.show()

# Word cloud from titles
text = " ".join(df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# Part 4: Streamlit Application

# app/streamlit_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("../data/metadata.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

# App layout
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Filters
year_range = st.slider("Select Year Range", 2018, 2022, (2020, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Publications by year
st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
st.pyplot(fig)

# Sample data
st.subheader("Sample Data")
st.write(filtered[['title', 'authors', 'journal', 'year']].head(20))

