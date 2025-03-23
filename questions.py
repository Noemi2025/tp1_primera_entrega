import random

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Inicialización del puntaje
puntaje = 0

'''# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)

    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")'''
        
 # Se combina las preguntas, respuestas y respuestas correctas en una lista
combined_questions = list(zip(questions, answers, correct_answers_index))

# Se seleccionan 3 preguntas aleatorias de la lista de preguntas sin repeticiones
questions_to_ask = random.sample(combined_questions, 3)

# El usuario deberá contestar 3 preguntas
for question, possible_answers, correct_index in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(possible_answers): 
        print(f"{i + 1}. {answer}")
        
    # Variable para rastrear si el usuario acertó
    acierto = False

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        # Se solicita la respuesta del usuario
        user_input = input("Respuesta: ")

       # Verificar si la entrada es un número dentro del rango válido
        if not user_input.isdigit() or not (1 <= int(user_input) <= 4):
            print("Respuesta no válida. Debe ser un número entre 1 y 4.")
            print("Fin del juego.")
            exit(1)
        
        # Convertir la respuesta a un número entero entre 0 y 3
        user_answer = int(user_input) - 1

        # Se verifica si la respuesta es correcta
        if user_answer == correct_index:
           print("¡Correcto!")
           puntaje = puntaje + 1
           acierto = True  
           break  
        elif   intento < 1: # Mostrar "Intenta de nuevo" solo si no es el último intento
               print("Incorrecto. Intenta de nuevo.")
               puntaje = puntaje - 0.5
    
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
    if not acierto:
        print("Incorrecto. La respuesta correcta es:")
        print(possible_answers[correct_index])
        puntaje = puntaje - 0.5
    # Se imprime un blanco al final de la pregunta
    print()
    
    # El puntaje no puede ser negativo
puntaje = max(0, puntaje)  
    
# Se muestra el puntaje final
print(f"Tu puntaje es: {puntaje}")