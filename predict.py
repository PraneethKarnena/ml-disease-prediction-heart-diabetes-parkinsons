import pickle  # pre trained model loading
import streamlit as st  # web app
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Prediction of Disease Outbreaks", layout="wide", page_icon="🧑‍⚕️"
)
diabetes_model = pickle.load(open("built-models/diabetes_model.sav", "rb"))
heart_disease_model = pickle.load(open("built-models/heart_model.sav", "rb"))
parkinsons_model = pickle.load(open("built-models/parkinsons_model.sav", "rb"))

with st.sidebar:
    selected = option_menu(
        "Prediction of disease outbreak system",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction"],
        menu_icon="hospital-fill",
        icons=["activity", "heart", "person"],
        default_index=0,
    )

if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction using Ml")
    col1, col2, col3 = st.columns(3)
    with col1:
        pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        glucose_level = st.text_input("Glucose level")
    with col3:
        blood_pressure = st.text_input("Blood Pressure value")
    with col1:
        skin_thickness = st.text_input("Skin Thickness value")
    with col2:
        insulin_level = st.text_input("Insulin level")
    with col3:
        bmi = st.text_input("BMI  value")
    with col1:
        diabetes_pedigree_function_value = st.text_input(
            "Diabetes Pedigree Function value"
        )
    with col2:
        age = st.text_input("Age of the person")

    diab_diagnosis = ""
    if st.button("Diabetes Test Result"):
        try:
            user_input = [
                float(pregnancies),
                float(glucose_level),
                float(blood_pressure),
                float(skin_thickness),
                float(insulin_level),
                float(bmi),
                float(diabetes_pedigree_function_value),
                float(age),
            ]

            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                st.error("The person is diabetic")
            else:
                st.success("The person is not diabetic")

        except ValueError:
            st.warning("Please enter valid numerical values.")


if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction using Ml")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age of the person")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("Cerebral Palsy value")
    with col1:
        trestbps = st.text_input("trestbps value")
    with col2:
        chol = st.text_input("chol value")
    with col3:
        fbs = st.text_input("fbs  value")
    with col1:
        restecg = st.text_input("restecg value")
    with col2:
        thalach = st.text_input("thalach value")
    with col1:
        exang = st.text_input("exang value")
    with col2:
        oldpeak = st.text_input("oldpeak value")
    with col3:
        slope = st.text_input("slope value")
    with col1:
        ca = st.text_input("ca value")
    with col2:
        thal = st.text_input("thal")

    heart_diagnosis = ""
    if st.button("Heart Disease Test Result"):
        try:
            user_input = [
                float(age),
                float(sex),
                float(cp),
                float(trestbps),
                float(chol),
                float(fbs),
                float(restecg),
                float(thalach),
                float(exang),
                float(oldpeak),
                float(slope),
                float(ca),
                float(thal),
            ]

            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                st.error("The person has heart disease")
            else:
                st.success("The person does not have heart disease")

        except ValueError:
            st.warning("Please enter valid numerical values.")


if selected == "Parkinsons Prediction":
    st.title("Parkinsons Prediction using Ml")
    col1, col2, col3 = st.columns(3)

    with col1:
        mdvp_fo = st.text_input("MDVP:Fo(Hz)")
        mdvp_fhi = st.text_input("MDVP:Fhi(Hz)")
        mdvp_flo = st.text_input("MDVP:Flo(Hz)")
        mdvp_jitter_percent = st.text_input("MDVP:Jitter(%)")
        mdvp_jitter_abs = st.text_input("MDVP:Jitter(Abs)")
        mdvp_rap = st.text_input("MDVP:RAP")
        mdvp_ppq = st.text_input("MDVP:PPQ")
        jitter_ddp = st.text_input("Jitter:DDP")

    with col2:
        mdvp_shimmer = st.text_input("MDVP:Shimmer")
        mdvp_shimmer_db = st.text_input("MDVP:Shimmer(dB)")
        shimmer_apq3 = st.text_input("Shimmer:APQ3")
        shimmer_apq5 = st.text_input("Shimmer:APQ5")
        mdvp_apq = st.text_input("MDVP:APQ")
        shimmer_dda = st.text_input("Shimmer:DDA")
        nhr = st.text_input("NHR")
        hnr = st.text_input("HNR")

    with col3:
        rpde = st.text_input("RPDE")
        dfa = st.text_input("DFA")
        spread1 = st.text_input("SPREAD1")
        spread2 = st.text_input("SPREAD2")
        d2 = st.text_input("D2")
        ppe = st.text_input("PPE")

    parkinsons_diagnosis = ""
    if st.button("Parkinsons Test Result"):
        try:
            user_input = [
                float(mdvp_fo),
                float(mdvp_fhi),
                float(mdvp_flo),
                float(mdvp_jitter_percent),
                float(mdvp_jitter_abs),
                float(mdvp_rap),
                float(mdvp_ppq),
                float(jitter_ddp),
                float(mdvp_shimmer),
                float(mdvp_shimmer_db),
                float(shimmer_apq3),
                float(shimmer_apq5),
                float(mdvp_apq),
                float(shimmer_dda),
                float(nhr),
                float(hnr),
                float(rpde),
                float(dfa),
                float(spread1),
                float(spread2),
                float(d2),
                float(ppe),
            ]

            parkinsons_prediction = parkinsons_model.predict([user_input])
            print(
                "###########################################################################"
            )
            print(parkinsons_prediction[0])
            print(
                "###########################################################################"
            )

            if parkinsons_prediction[0] == 1:
                st.error("The person has parkinsons")
            else:
                st.success("The person does not have parkinsons")

        except ValueError:
            st.warning("Please enter valid numerical values.")
