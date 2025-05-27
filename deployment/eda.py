# Import library packages
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Visualization packages
import matplotlib.pyplot as plt
import seaborn as sns

# Create def function
def app():
    # Add title
    st.title('Exploratory Data Analysis (EDA) of Student Depression')

    # Read the image file
    image = Image.open('student-depression.jpg')
    st.image(image, caption = 'A student need HELP!')

    # Read the csv file
    st.subheader('Student Depression Dataset')
    df = pd.read_csv('student_depression_dataset.csv', delimiter=';')

    # Using Magic Command (Abrakadabra)
    """
    ### The dataset of Student Depression:
    """

    # Show dataframe
    st.write(df)

    # Add subheader
    st.subheader('Visualizations of Student Depression')
    # Create Bar chart among students
    fig1, ax1 = plt.subplots()
    sns.countplot(data = df, x = 'Depression', hue = 'Depression', ax = ax1)
    ax1.set_title("Distribution of Depression among Students")
    st.pyplot(fig1)

    # Create Bar chart by Gender
    fig2, ax2 = plt.subplots()
    sns.countplot(x = 'Gender', hue = 'Depression', data = df, ax = ax2)
    ax2.set_title('Distribution of Depression by Gender')
    st.pyplot(fig2)

    # Create Histogram by Age
    fig3, ax3 = plt.subplots(figsize = (10, 5))
    sns.histplot(df['Age'], kde = True, bins = 30, color='blue', ax = ax3)
    ax3.set_title('Distribution of Depression by Age')
    ax3.set_xlabel('Age')
    ax3.set_ylabel('Amount')
    st.pyplot(fig3)

    # Create Histogram by CPGA
    fig4, ax4 = plt.subplots(figsize=(10, 5))
    sns.histplot(df['CGPA'], kde = True, bins = 30, ax = ax4)
    ax4.set_title('Distribution of Depression by CGPA')
    ax4.set_xlabel('CGPA')
    ax4.set_ylabel('Amount')
    st.pyplot(fig4)

    # Create Boxplot: Academic vs Work Pressure
    fig5, ax5 = plt.subplots(figsize = (8, 5))
    sns.boxplot(data =df[['Academic Pressure', 'Work Pressure']], ax = ax5)
    ax5.set_title('Academic vs. Work Pressure')
    st.pyplot(fig5)

    # Create Scatterplot: Sleep Duration vs Depression by Gender
    fig6, ax6 = plt.subplots(figsize = (8, 5))
    sns.countplot(x = 'Sleep Duration', hue='Gender', data = df, ax = ax6)
    ax6.set_title('Sleep Duration vs. Depression')
    ax6.set_xlabel('Sleep Duration (hours)')
    ax6.set_ylabel('Depression Level')
    st.pyplot(fig6)

    # Make the numerical column lists
    num_cols_ch = ['Age', 'Academic Pressure', 'Work Pressure', 'CGPA', 
                   'Study Satisfaction', 'Job Satisfaction', 'Work/Study Hours']
    
    # Correlation between numerical columns
    corr_matrix = df[num_cols_ch].corr()

    # Create the Heatmap
    fig7, ax7 = plt.subplots(figsize = (10, 6))
    sns.heatmap(corr_matrix, annot = True, cmap = 'coolwarm', fmt = ".2f", ax = ax7)
    ax7.set_title('Correlation Heatmap of Depression-Related Variables')
    st.pyplot(fig7)

# Create an idiom
if __name__ == "__main__":
    app()