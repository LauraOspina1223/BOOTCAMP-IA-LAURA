# MODELO SUPERVISADO PARA CHATBOT EN ESPAÑOL

#scikit-learn
from sklearn.feature_extraction.text import CountVectorizer # Esta línea extrae el texto y lo convierte en números (en un vector)
from sklearn.naive_bayes import MultinomialNB # Naive Bayes para clasificación de texto
# MutlinomialNB relacionaes entre el texto y las respuestas posibles. 
# "sklearn" Esta de las pocas librerías que el nombre no coincide con función

# Función para entrenamiento preguntas y respuestas

def build_and_train_model(train_pairs):
    # train_pairs lista de tuplas (pares) (pregunta, respuesta) la tupla es inmutable
    # Ejemplo [("Hola", "¡Hola!"),("Adiós","¡Hasta luego!")]
    # Separamos las preguntas y respuestas en dos listas
    questions = [q for q, _ in train_pairs] # Lista de preguntas
    answers = [a for _, a in train_pairs] # Lista de respuestas
    # a y q son variables temporales para recorrer las tuplas
    # Convertimos las preguntas en una matriz de características
    vectorizer = CountVectorizer() # Crear el vectorizador
    # Entrenamiento del vectorizador con las preguntas
    x = vectorizer.fit_transform(questions)
    # Obtenemos una lista de respuestas únicas 
    unique_answers = sorted(set(answers)) #Sorted ordena la lista y el set elimina duplicados
    # Crear el diccionario con las etiquetas (labels) para las respuestas
    answer_to_label = {a: i for i, a in enumerate(unique_answers)}
    # Creamos una lista
    y = [answer_to_label[a] for a in answers] # Convertimos respuestas a etiquetas numéricas
    # Modelo clasificación de texto Naive bayes
    model = MultinomialNB() # Crear el modelo
    # Entrenar el modelo 
    model.fit(x, y)
    return model, vectorizer, unique_answers
# Función predict_answer
def predict_answer(model,vectorizer,unique_answers,user_text):
    # Convertir la pregunta en una matriz de características, osea a números
    x = vectorizer.transform([user_text])
    # Predecir la etiqueta (label) de la respuesta
    label = model.predict(x)[0]
    return unique_answers[label] # Devolver la respuesta correspondiente a la etiqueta

# Programa principal

if __name__ == "__main__":
   training_data = [
    ("hola", "¡Hola! ¿En qué podemos ayudarte hoy?"),
    ("buenos días", "Buenos días, gracias por contactarnos. ¿Cómo podemos asistirte?"),
    ("buenas tardes", "Buenas tardes, es un gusto atenderte. ¿Qué consulta tienes?"),
  # ("buenas noches", "Buenas noches, estamos a tu disposición. ¿En qué podemos ayudarte?"),
    ("información", "Con gusto te brindamos la información que necesitas. ¿Sobre qué tema?"),
    ("soporte", "Nuestro equipo de soporte está listo para ayudarte. Cuéntanos tu inconveniente."),
    ("precio", "Con gusto te compartimos nuestros precios. ¿Qué servicio te interesa?"),
    ("gracias", "Gracias a ti por comunicarte con nosotros. ¡Que tengas un excelente día!")
   ]

   model, vectorizer, unique_answers = build_and_train_model(training_data) # Ella recibe la lista y devuelve el modelo entrenado, el vectorizador y las respuestas únicas
   # En esta línea puedes decir unique_answers o unique_answer, ambas funcionan igual porque es una variable local
   print("Chatbot supervisado listo. Escribre 'Salir' para terminar.'\n")
   while True:
         # Pedimos una frase al usuario
         user = input("Tú: ").strip() # strip elimina espacios en blanco al inicio y al final
         # Si el usuario escribe "salir", terminamos el programa
         if user.lower() in {"salir","exit","quit"}: # lower convierte a minúsculas
              print("Chatbot: ¡Hasta luego!")
              break
         response=predict_answer(model,vectorizer,unique_answers,user) # Predecimos la respuesta
         print("Chatbot:", response) # Mostramos la respuesta