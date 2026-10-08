import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generar_redaccion_legal(cuerpo_plantilla: str, datos_variables: dict) -> str:
    client = Groq(api_key=GROQ_API_KEY)

    prompt_unico = f"""
    Eres un abogado especialista en la redacción formal de notificaciones, oficios y cartas institucionales.
    
    PLANTILLA BASE:
    "{cuerpo_plantilla}"
    
    DATOS A INCORPORAR:
    {datos_variables}
    
    INSTRUCCIONES:
    - Redacta una carta o notificación formal completa, respetando la estructura base.
    - Integra los datos proporcionados de forma fluida y con lenguaje jurídico impecable.
    - Devuelve únicamente el texto final del documento listo para entregar, sin introducciones ni comentarios adicionales.
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt_unico}
        ],
        model="openai/gpt-oss-20b",
        temperature=0.2
    )

    return chat_completion.choices[0].message.content