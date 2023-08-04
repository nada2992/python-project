import random

# Predefined story templates
story_templates = [
    "Once upon a time, there was a {character} who lived in {location}. {character} had {adjective} {noun}.",
    "{character} embarked on a journey to {destination}. Along the way, {character} encountered a {adjective} {noun}.",
    "In a {location} far away, {character} discovered a {adjective} {noun}. This discovery changed {character}'s life forever."
]

# Randomized elements
characters = ["hero", "princess", "wizard", "adventurer"]
locations = ["a magical kingdom", "an enchanted forest", "a distant planet"]
adjectives = ["brave", "mysterious", "courageous", "wise"]
nouns = ["sword", "treasure", "secret", "creature"]
destinations = ["find a hidden treasure", "rescue a captured friend", "uncover a forgotten secret"]

def generate_story():
    # Randomly select elements from the lists
    character = random.choice(characters)
    location = random.choice(locations)
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    destination = random.choice(destinations)

    # Randomly select a story template
    story_template = random.choice(story_templates)

    # Fill in the template with the selected elements
    story = story_template.format(
        character=character,
        location=location,
        adjective=adjective,
        noun=noun,
        destination=destination
    )

    return story

# Generate a story
story = generate_story()
print(story)