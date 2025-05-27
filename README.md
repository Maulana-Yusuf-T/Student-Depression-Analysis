# Student Depression Analysis
Developed a Gradient Boosting model to predict student depression from academic, psychological, and social features. Achieved ROC-AUC > 90% with focus on Recall and F1-Score to ensure early detection. Insights support targeted mental health interventions in schools.

## Repository Outline
├── deployment/
│   ├── app.py
│   ├── best_model.pkl
│   ├── eda.py
│   ├── prediction.py
│   ├── requirements.txt
│   ├── student_depression_dataset.csv
│   └── student-depression.jpg
├── description.md
├── P1M2_Maulana_Yusuf_inf.ipynb
├── P1M2_Maulana_Yusuf.ipynb
├── url.txt
└── README.md

Content of this project:
1. README.md - General description about the project.
2. student_depression_dataset.csv - The chosen dataset for this project.
3. P1M2_Maulana_Yusuf.ipynb - Notebook containing data processing with Python using Machine Learning methods.
4. mod_inf_M2.ipynb - Notebook containing the predicition test that already made in the first notebook.
5. app.py - The main Python file containing the EDA and Inference to show the main display of both.
6. eda.py - A Python file containing the visualization of this project
7. predictin.py - A Python file containing the inference (prediction) of this project. It can be said the test section.
8. url.txt - A text containing the library packages.
9. best_model.pkl - The best model for this project with Pickle.

## Problem Background
Student mental health is a serious issue worldwide, particularly in Indonesia. Students are more vulnerable to depression, anxiety, and stress due to social circumstances, lack of sleep, financial difficulties, and academic pressure. In order for pupils to receive the proper assistance before their health worsens, early diagnosis of these disorders is crucial.

Early identification is difficult, nevertheless, due to the scarcity of mental health professionals and students' poor self-awareness of their symptoms. Therefore, in order to identify children who may be suffering from severe depression, a data-driven approach is required.

The objective of this research is to develop a classification model based on Machine Learning that can determine if a student is at high risk of developing depression. This prediction is based on health conditions (e.g., sleep duration and chronic diseases), lifestyle and psychological characteristics (e.g., history of psychological issues and physical activity), and demographic information (e.g., age, gender, and relationship status).

It is anticipated that this methodology will assist campuses or mental health service providers in early screening students who require additional support.

## Project Output
1. **`Machine Learning Model`**: A classification model that is able to predict the level of depression in students based on factors such as academic pressure, sleep duration, study satisfaction, work pressure, and others. The best model is saved in the form of a .pkl (pickle) file for inference/prediction purposes.
2. **`Interactive Dashboard (Streamlit App)`**: A Streamlit-based application that allows users to:
- Perform data exploration (EDA) visually.
- Input new data manually.
- Get a prediction of whether or not a student is depressed based on the input.<p>

This output can be used to help campuses or mental health organizations identify potential risks of depression in students more quickly and measurably.

## Data
The dataset used in this project is the Student Depression Dataset obtained from [Kaggle](https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset/data). This dataset contains student respondent data related to academic stress, sleep habits, work stress, and study satisfaction.
General data characteristics:
- Number of rows: **`27901`** rows of data.
- Number of columns: **`18`** features.<p>

The features consist of a combination of numeric and categorical data and no missing values ​​and duplicated data.

## Method
This project uses a Supervised Learning approach with the target of classifying the level of depression in students. Several models tested include:
- K-Nearest Neighbors **(KNN)**.
- Support Vector Machine **(SVM)**.
- Decision Tree.
- Random Forest.
- Gradient Boosting.<p>

The model selected as the best model based on the evaluation score **(ROC-AUC)** is the **`Boosting Classifier`**.
In addition to training and evaluating the model, the following stages were also carried out:
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Cross Validation
- Hyperparameter Tuning
- Model Deployment via **`Streamlit`**

## Stacks
Stack and tools used in this project include:
- **`Programming Language`**: Python 3

**`Libraries`**:
1. pandas and numpy – For data manipulation
2. matplotlib, seaborn – For data visualization
3. scikit-learn – For modeling and evaluation
4. joblib – For storing models
5. streamlit – For interactive web application deployment

**`Tools`**:
1. Jupyter Notebook – for exploration and early development
2. Visual Studio Code – for writing .py files
3. GitHub – for version control and collaboration

## Reference
Deployment link: https://huggingface.co/spaces/Maulanayt/Milestone_2

---

**Additional References:**
- [Depression, Anxiety, and Stress among Students in Newly Established Remote University Campus in Indonesia](https://www.researchgate.net/publication/341566348_Depression_Anxiety_and_Stress_among_Students_in_Newly_Established_Remote_University_Campus_in_Indonesia)
- [Burden of Adolescent Mental Disorders in Indonesia: Results from Indonesia’s First National Mental Health Survey](https://ugm.ac.id/en/news/23169-burden-of-adolescent-mental-disorders-in-indonesia-results-from-indonesia-s-first-national-mental-health-survey/?utm_source=chatgpt.com)
- [Mental Wellbeing of Indonesian Students: Mean Comparison with UK Students and Relationships with Self-Compassion and Academic Engagement](https://pmc.ncbi.nlm.nih.gov/articles/PMC9407787/?utm_source=chatgpt.com)
