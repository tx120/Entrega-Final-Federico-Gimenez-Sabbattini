import streamlit as st
import google.generativeai as genai
import nltk
import requests

genai.configure(api_key="AIzaSyAhOY-dZK1W0gKanz-cfY1W8CfrehPBEes")
model = genai.GenerativeModel("gemini-1.5-flash")

generation_config = genai.GenerationConfig(
    max_output_tokens=1000,
    temperature=0.1,
)

system_instruction = "Eres un experto en servicio técnico de PC. Diagnostica problemas técnicos descritos por los usuarios y proporciona soluciones básicas y concisas, bastante simples. Si el problema no puede ser resuelto por el usuario, indica que se necesita asistencia técnica."

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def gemini_diagnosis(user_input):
    prompt = f"{system_instruction}\n\nUsuario: {user_input}\nDiagnóstico:"
    response = model.generate_content(
        prompt,
        generation_config=generation_config
    )
    diagnosis = response.text.strip()
    return diagnosis

def main():
    st.title("PC Doctor AI - Diagnóstico Técnico")
    st.write("Bienvenido a PC Doctor AI. Esta aplicación proporciona un diagnóstico técnico superficial para problemas de PC. En caso de un problema complejo, se derivará a un técnico especializado.")

    user_input = st.text_input("Describa su problema aquí:")
    if st.button("Iniciar Consulta"):
        if user_input:
            diagnosis = gemini_diagnosis(user_input)
            st.write("Diagnóstico:", diagnosis)

            if "asistencia técnica" in diagnosis:
                st.write("Por favor, contacte a un técnico especializado en el siguiente enlace: -----------------")
                st.write("Información de contacto del técnico: 123456789")
        else:
            st.write("Por favor, describa su problema antes de iniciar la consulta.")

if __name__ == "__main__":
    main()
