from random import choice

answer = input("How are you today?")

generic_response = "What else do you want to talk about?"

family_words = ["family",
                "grandparent", "grandmother", "grandfather",
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
            break
        else:
            response = generic_response
    answer = input(response)
