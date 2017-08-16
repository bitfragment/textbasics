from random import choice

answer = input("How are you today?")

family_words = ["grandparent", "grandmother", "grandfather",
                "parent", "mother", "father", "mom", "dad",
                "uncle", "aunt", 
                "sibling", "sister", "brother", "cousin",
                "daughter", "son",
                "niece", "nephew"]

family_responses = ["Tell me more about your family.",
                    "Are you close to your family?",
                    "Did you have a pleasant childhood?"]

while answer:
    for word in family_words:
        if word in answer:
            response = choice(family_responses)
            answer = input(response)
    answer = input("What else do you want to talk about?")
