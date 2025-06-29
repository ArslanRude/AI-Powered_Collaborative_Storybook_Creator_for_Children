from diffusers import StableDiffusionPipeline
import torch

class IllustrationGenerator:
    def __init__(self):
        self.model = StableDiffusionPipeline.from_pretrained('CompVis/stable-diffusion-v1-4', torch_dtype=torch.float16)
        self.model.to('cuda')

    def generate_illustration(self, story_elements):
        # Generate illustration based on story elements
        prompt = f'Generate an illustration for a children story about {story_elements}. ' +
                'Make it colorful and whimsical.'
        
        with torch.no_grad():
            image = self.model(prompt).images[0]
        
        image.save('illustration.png')
        
        return 'illustration.png'