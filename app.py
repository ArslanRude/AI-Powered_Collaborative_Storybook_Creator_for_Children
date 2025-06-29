from flask import Flask, render_template
from story_generator import StoryGenerator
from illustration_generator import IllustrationGenerator
from user_manager import UserManager

app = Flask(__name__)

# Initialize AI components
story_gen = StoryGenerator()
il_gen = IllustrationGenerator()
user_mgr = UserManager()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate-story', methods=['POST'])
def generate_story():
    # Get user input
    theme = request.form['theme']
    age = request.form['age']
    
    # Generate story elements
    story = story_gen.generate_story(theme, age)
    characters = story_gen.generate_characters(theme, age)
    plot = story_gen.generate_plot(theme, age)
    
    return render_template('story.html', story=story, characters=characters, plot=plot)

@app.route('/generate-illustration')
def generate_illustration():
    # Get story elements
    story_elements = request.args.get('story_elements')
    
    # Generate illustration
    illustration = il_gen.generate_illustration(story_elements)
    
    return send_file(illustration)

@app.route('/save-story')
def save_story():
    # Get story data
    story_data = request.form['story_data']
    
    # Save story to database
    user_mgr.save_story(story_data)
    
    return 'Story saved successfully'

@app.route('/profile')
def profile():
    # Get user preferences
    user_id = request.args.get('user_id')
    preferences = user_mgr.get_user_preferences(user_id)
    
    return render_template('profile.html', preferences=preferences)

if __name__ == '__main__':
    app.run(debug=True)