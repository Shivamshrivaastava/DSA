import random

def generate_caption(description):
    templates = [
        "This image shows {}.",
        "Here we have {}.",
        "Look at this {}.",
        "An example of {}.",
        "A beautiful {}."
    ]
    
    template = random.choice(templates)
    caption = template.format(description)
    return caption

descriptions = [
    "a sunset over the mountains",
    "a cute puppy playing in the yard",
    "a bustling city street",
    "a serene beach at dawn",
    "a delicious plate of pasta"
]

for description in descriptions:
    caption = generate_caption(description)
    print(caption)