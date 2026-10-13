# 🎓 Smart Student Placement Prediction System

An end-to-end Machine Learning project that estimates whether a student is likely to be placed based on academic performance and student skill-related inputs. The project includes data preparation, exploratory data analysis, model selection, and an interactive Streamlit web application.

> **Note:** Predictions are estimates from a trained model and are not a guarantee of employment.

## 🌐 Live Demo

**[Launch the Streamlit App](https://student-placement-prediction-01.streamlit.app/)**

Enter student details and click **Predict Placement** to view the predicted placement outcome and, when supported by the model, its prediction probabilities.

## ✨ Features

- Interactive placement prediction form
- Academic and skill-related input fields
- Placement outcome with prediction probabilities
- Data cleaning and preprocessing notebooks
- Exploratory Data Analysis (EDA) and visualizations
- Feature engineering and model selection workflow
- Trained model saved with Joblib
- Online deployment using Streamlit Community Cloud

## 🧰 Tech Stack

- **Language:** Python
- **Data handling:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Model persistence:** Joblib
- **Web app:** Streamlit
- **Analysis & visualization:** Jupyter Notebook, Matplotlib, Seaborn

## 📊 Input Features

The application accepts these inputs:

- IQ
- Previous Semester Result
- CGPA
- Academic Performance
- Internship Experience
- Extra-Curricular Score
- Communication Skills
- Projects Completed

## 🔄 Project Workflow

1. Data cleaning and preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature engineering
4. Model training and comparison
5. Model evaluation
6. Saving the trained model
7. Building and deploying the Streamlit application

## 📁 Repository Structure

```text
.
├── app.py                                  # Streamlit prediction app
├── placement_model.pkl                     # Saved trained model
├── requirements.txt                        # Python dependencies
├── college_student_placement_dataset.csv   # Dataset
├── data_cleaning.ipynb                     # Data cleaning workflow
├── EDA.ipynb                               # Exploratory data analysis
├── feature_Engenering.ipynb                # Feature engineering workflow
├── model_selection.ipynb                   # Model comparison and selection
└── README.md                               # Project documentation
```

## 💻 Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/artimore614/collage-student-Placement-.git
   cd collage-student-Placement-
   ```

2. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Start the Streamlit app:

   ```bash
   python -m streamlit run app.py
   ```

Make sure `app.py`, `placement_model.pkl`, and `requirements.txt` are in the project root folder.

## ⚠️ Limitations

- Results depend on the dataset and training process used for the model.
- Prediction probabilities should not be interpreted as guaranteed real-world placement chances.
- Model performance should be assessed using appropriate evaluation metrics, especially precision, recall, F1-score, and the confusion matrix, rather than accuracy alone.

## 👩‍💻 Author

**Arti More**  
Aspiring Data Scientist | Machine Learning Enthusiast

- **GitHub:** [artimore614](https://github.com/artimore614)
- **Live App:** [Student Placement Prediction](https://student-placement-prediction-01.streamlit.app/)

---

If you find this project useful, feel free to explore the repository and share feedback.
