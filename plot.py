import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import scipy

st.title('Titanic Dataset Analysis- Streamlit ')

df= sns.load_dataset('titanic')
#st.dataframe(df)

st.sidebar.header('User Input Parameters')
#c= st.sidebar.selectbox('Select the class',df['class'].unique())
#g= st.sidebar.selectbox('select the class',df['sex'].unique())

plot_type = st.sidebar.radio('Select the plot type',('bar','line','hist','box','kde'))

if plot_type == 'bar':
    st.write('Bar plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='bar',ax=ax)
    st.pyplot(fig)


elif plot_type == 'line':
    st.write('line plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='line',ax=ax)
    st.pyplot(fig)

elif plot_type == 'hist':
    st.write('hist plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='hist',ax=ax)
    st.pyplot(fig)

elif plot_type == 'box':
    st.write('Box plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='box',ax=ax)
    st.pyplot(fig)

else:
    st.write('kde plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='kde',ax=ax)
    st.pyplot(fig)