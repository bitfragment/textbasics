answer = input("How are you today?")

family_words = ["grandparent", "grandmother", "grandfather",
                "parent", "mother", "father", "mom", "dad",
                "uncle", "aunt", 
                "sibling", "sister", "brother", "cousin",
                "daughter", "son",
                "niece", "nephew"]

family_response = "Tell me more about your family."

while answer:
    for word in family_words:
        if word in answer:
            answer = input(family_response)
    answer = input("What else do you want to talk about?")
