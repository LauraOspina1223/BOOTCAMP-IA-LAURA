import os
os.environ["GROQ_API_KEY"]=""
from groq import Groq
client= Groq(
    api_key = os.environ.get("GROQ_API_KEY")
)
chat_completion = client.chat.completions.create(
    model = "llama-3.3-70b-versatile", 
    messages = [
        {
            "role": "system", # system es el agente
            "content": (
                "Eres un experto en Micrsoft Excel y análisis de datos. "
                "Tu tarea es interpretarinstrucciones en lenguaje natural "
                "y extraer la instrucción del usuario\n\n"
                "Debes identificar:\n"
                "- La acción principal (sumar,filtrar,ordenar,agrupar,etc.)\n"
                "- Las columnas involucradas \n"
                "- Las condiciones si existen \n"
                "Devuelve SIEMPRE la respuesta en formato JSON con esta estructura:\n"
                "{\n"
                '"accion":"",\n'
                '"columnas":[],\n'
                '"condiciones":[],\n'
                '"resultado":""\n'
                "}"

            )
        },
        {
            "role":"user",
            "content":"Quiero sumar las ventas por vendedor solo del año 2024"
        }
    ],

    
)
print(chat_completion.choices[0].message.content)