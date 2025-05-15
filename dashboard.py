import  pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
import streamlit as st
import plotly.express as px

df = pd.read_csv("Nhóm-7-Women_Clothes_Data.csv")
df['Review_length'] = df['Review'].dropna().apply(len)

# Tạo cột Label (giả sử phân loại review tốt nếu Pos_Feedback_Cnt >= 6, ngược lại là xấu)
df['Label'] = df['Pos_Feedback_Cnt'].apply(lambda x: 'Tốt' if x >= 6 else 'Xấu')

st.set_page_config(layout="wide")
st.title("📊 Dashboard EDA - Women Clothing Reviews")

# Bộ lọc Sidebar
st.sidebar.header("🔍 Bộ lọc")
selected_label = st.sidebar.selectbox("Chọn Label:", options=df['Label'].unique())
length_range = st.sidebar.slider("Chọn độ dài review:", int(df['Review_length'].min()), int(df['Review_length'].max()), (20, 300))

# Lọc dl
df_filtered = df[(df['Label'] == selected_label) & (df['Review_length'].between(*length_range))]

# Tabs layout
tabs = st.tabs(["📈 Tổng quan", "☁️ WordCloud", "🧠 Từ khóa"])

with tabs[0]:
    st.subheader("Tổng quan dữ liệu")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Số lượng review", df_filtered.shape[0])
        fig_len = px.histogram(df_filtered, x='Review_length', nbins=40, title="Phân bố độ dài review")
        st.plotly_chart(fig_len, use_container_width=True)
    with col2:
        label_count = df['Label'].value_counts()
        fig_pie = px.pie(values=label_count.values, names=label_count.index, title="Tỉ lệ các Label")
        st.plotly_chart(fig_pie, use_container_width=True)
        
with tabs[1]:
    st.subheader("WordCloud theo Label đã chọn")
    wc_text = " ".join(df_filtered['Review'].dropna().astype(str).values)
    wc = WordCloud(width=800, height=400, background_color='white').generate(wc_text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)


with tabs[2]:
    st.subheader("Từ khóa phổ biến")
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df_filtered['Review'].dropna().astype(str))
    word_freq = dict(zip(vectorizer.get_feature_names_out(), X.toarray().sum(axis=0)))
    keyword_df = pd.DataFrame(word_freq.items(), columns=['Từ khóa', 'Tần suất']).sort_values(by='Tần suất', ascending=False)
    st.dataframe(keyword_df)
