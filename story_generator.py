from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

class StoryGenerator:
    def __init__(self):
        self.model = T5ForConditionalGeneration.from_pretrained('t5-base')
        self.tokenizer = T5Tokenizer.from_pretrained('t5-base')
        
    def generate_story(self, theme, age):
        # Generate story based on theme and age
        prompt = f'Generate a story about {theme} for a {age} year old child. ' +
                'Make it adventurous and educational.'
        
        input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
        output = self.model.generate(input_ids)
        
        return self.tokenizer.decode(output[0], skip_padding=True)

    def generate_characters(self, theme, age):
        # Generate characters based on theme and age
        prompt = f'Generate characters for a story about {theme} for a {age} year old child. ' +
                'Make them friendly and relatable.'
        
        input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
        output = self.model.generate(input_ids)
        
        return self.tokenizer.decode(output[0], skip_padding=True)

    def generate_plot(self, theme, age):
        # Generate plot based on theme and age
        prompt = f'Generate a plot for a story about {theme} for a {age} year old child. ' +
                'Make it engaging and with a moral lesson.'
        
        input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
        output = self.model.generate(input_ids)
        
        return self.tokenizer.decode(output[0], skip_padding=True)