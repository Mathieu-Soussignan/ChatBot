import tkinter as tk
from tkinter import scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Dictionnaire pour les correspondances exactes
exact_qa_pairs = {
    "salut, comment vas-tu ?": "Bonjour ! Je vais bien, merci. Et vous, comment vous sentez-vous aujourd'hui ?",
    "quel est ton nom ?": "Je m'appelle Assistant. Comment puis-je vous aider ?",
    "qui t'a créé ?": "J'ai été conçu par un développeur passionné en IA.",
    "que peux-tu faire ?": "Je peux répondre à des questions sur l'IA, la programmation et même raconter des blagues.",
    "quelles sont tes limites ?": "Je ne peux pas accomplir de tâches physiques ni apprendre en temps réel.",
    "qu'est-ce que l'intelligence artificielle ?": "L'intelligence artificielle imite l'intelligence humaine à travers des algorithmes.",
    "quels sont les différents types d'ia ?": "Il existe l'IA faible pour des tâches spécifiques, et l'IA forte qui rivalise avec l'intelligence humaine.",
    "comment puis-je apprendre la programmation ?": "Apprenez la programmation en pratiquant avec des langages comme Python.",
    "peux-tu m'expliquer les bases de python ?": "Python est un langage simple et polyvalent, parfait pour les débutants.",
    "raconte-moi une blague.": "Pourquoi les mathématiciens aiment-ils les graphes ? Parce qu'ils ont des relations !",
    "au revoir": "Au revoir ! Revenez quand vous voulez.",
    "merci pour ton aide": "Avec plaisir, je suis là pour vous aider."
}

# Charger les questions et réponses à partir d'un fichier (si nécessaire)
def load_conversation():
    questions = []
    answers = []
    try:
        with open('conversation.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i in range(0, len(lines) - 1, 2):
                question = lines[i].strip().lower()
                answer = lines[i + 1].strip()
                questions.append(question)
                answers.append(answer)
    except FileNotFoundError:
        print("Le fichier conversation.txt n'a pas été trouvé.")
    return questions, answers

questions, answers = load_conversation()

# Initialiser le modèle TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(questions)

def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    
    # Vérifier si la question est dans le dictionnaire de correspondances exactes
    if user_input in exact_qa_pairs:
        return exact_qa_pairs[user_input]
    
    # Sinon, utiliser TF-IDF pour la correspondance approximative
    user_input_tfidf = vectorizer.transform([user_input])
    similarity_scores = cosine_similarity(user_input_tfidf, tfidf_matrix)
    closest_match_index = np.argmax(similarity_scores)
    closest_match_score = similarity_scores[0][closest_match_index]

    if closest_match_score >= 0.5:  # Ajuster ce seuil si nécessaire
        return answers[closest_match_index]
    else:
        return "Je suis désolé, je ne comprends pas votre demande."

# Fonction d'envoi de message
def send_message():
    user_input = entry.get().strip()
    if user_input:
        chatbox.config(state=tk.NORMAL)
        chatbox.insert(tk.END, "Vous: " + user_input + "\n", "user")
        response_text = get_bot_response(user_input)
        chatbox.insert(tk.END, "Bot: " + response_text + "\n", "bot")
        chatbox.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        chatbox.see(tk.END)

# Fonction pour gérer le choix dans le menu déroulant
def menu_select(selection):
    entry.delete(0, tk.END)
    entry.insert(0, selection)

# Configuration de l'interface graphique
root = tk.Tk()
root.title("Chatbot amélioré")
root.geometry("500x600")
root.configure(bg="#333333")

chatbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, bg="#1E1E1E", fg="white", font=("Arial", 12))
chatbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chatbox.tag_configure("user", foreground="#4CAF50", justify="left")
chatbox.tag_configure("bot", foreground="#FF5722", justify="right")

# Ajouter une entrée de texte pour l'utilisateur
entry = tk.Entry(root, bg="#444444", fg="white", font=("Arial", 12))
entry.pack(padx=10, pady=10, fill=tk.X)

# Ajouter un bouton d'envoi avec un changement de couleur au clic
# Ajouter un bouton d'envoi avec des couleurs ajustées pour l'état actif
send_button = tk.Button(root, text="Envoyer", bg="#555555", fg="black", activebackground="#444444", activeforeground="#FFFFFF", font=("Arial", 12), command=send_message)
send_button.pack(padx=10, pady=10)

# Menu déroulant pour les questions possibles
questions_list = list(exact_qa_pairs.keys())  # Liste des questions possibles
selected_question = tk.StringVar(root)
selected_question.set("Choisir une question")  # Valeur par défaut

question_menu = tk.OptionMenu(root, selected_question, *questions_list, command=menu_select)
question_menu.config(bg="#555555", fg="white", font=("Arial", 12), activebackground="#777777", activeforeground="white")
question_menu.pack(padx=10, pady=10)

root.mainloop()