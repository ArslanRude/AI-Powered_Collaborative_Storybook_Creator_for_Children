# AI-Powered Collaborative Storybook Creator for Children

This application enables parents and children to collaboratively create personalized storybooks through an AI-powered interface. The AI suggests plotlines, characters, and moral lessons based on the child's interests and learning level. It incorporates real-time illustration generation and adaptive educational elements tailored to the child's developmental stage.

## Features
- AI-powered story generation
- Real-time illustration generation
- User profile management
- Story saving and retrieval
- Educational elements tailored to the child's age

## Installation
1. Clone the repository
2. Install the required packages:
   ```pip install -r requirements.txt```
3. Run the application:
   ```python app.py```

## Usage
1. Open the application in your web browser
2. Select a theme and age group
3. Generate and customize your story
4. Create illustrations for your story
5. Save your story for future access

## Files
- app.py: Main application file that sets up the Flask/Django app and handles routes
- story_generator.py: Contains AI logic for generating stories, characters, and plotlines
- illustration_generator.py: Handles real-time image generation based on story elements
- user_manager.py: Manages user profiles and preferences
- database.db: Stores user data and created stories
- requirements.txt: Lists all Python dependencies for the project
- README.md: Project documentation and setup instructions