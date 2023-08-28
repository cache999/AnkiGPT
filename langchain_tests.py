from langchain.llms import AzureOpenAI
from langchain import PromptTemplate
import openai

# Environment Variables
import os


# openai_api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
# openai_api_key = os.getenv("AZURE_OPENAI_KEY_1")
ENGINE_NAME = "EricChatGPT"
# openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")



llm = AzureOpenAI(
    temperature=0,
    deployment_name=ENGINE_NAME,
    model_name=ENGINE_NAME,
)

tone_descriptors = """
1. Pace: The speed at which the story unfolds and events occur.
2. Mood: The overall emotional atmosphere or feeling of the piece.
3. Tone: The author's attitude towards the subject matter or characters.
4. Voice: The unique style and personality of the author as it comes through in the writing.
5. Diction: The choice of words and phrases used by the author.
6. Syntax: The arrangement of words and phrases to create well-formed sentences.
7. Imagery: The use of vivid and descriptive language to create mental images for the reader.
8. Theme: The central idea or message of the piece.
9. Point of View: The perspective from which the story is told (first person, third person, etc.).
10. Structure: The organization and arrangement of the piece, including its chapters, sections, or stanzas.
11. Dialogue: The conversations between characters in the piece.
12. Characterization: The way the author presents and develops characters in the story.
13. Setting: The time and place in which the story takes place.
14. Foreshadowing: The use of hints or clues to suggest future events in the story.
15. Irony: The use of words or situations to convey a meaning that is opposite of its literal meaning.
16. Symbolism: The use of objects, characters, or events to represent abstract ideas or concepts.
17. Allusion: A reference to another work of literature, person, or event within the piece.
18. Conflict: The struggle between opposing forces or characters in the story.
19. Suspense: The tension or excitement created by uncertainty about what will happen next in the story.
20. Climax: The turning point or most intense moment in the story.
21. Resolution: The conclusion of the story, where conflicts are resolved and loose ends are tied up.
"""

prompt_template = """
You are an AI Bot that analyses the tone of writing of examples given to you.
Be opinionated and have an active voice.
Take a strong stance with your response.

% HOW TO DESCRIBE TONE
{tone_descriptors}

% START OF EXAMPLES
{example_text}
% END OF EXAMPLES

List out the tone qualities of the examples above, based on the factors outlined in % HOW TO DESCRIBE TONE.
"""

example_text = """
Ever since I was a small child, I have yearned to make a difference. In primary school I wrote a detail illustrated manual for operating a spaceship.  Complete with hatch opening and airlock  closing procedures, this piece impressed both my teachers and parents a great deal.  Another essay I wrote traced the wars and skirmishes between neighboring enemy planets...  From everything I read about and heard on the news since, getting into an average college and getting an average job just didn’t seem very appealing. If I get the chance, I wanted to be at the frontier of innovation, pushing humanity forward.    Becoming a scholarship holder would surely bring me closer to my dream, and I will feel inspired to give back to the school in many ways. 
Firstly, I believe that my skills in subjects such as  english,  math, science, music and computer programming will give me a chance to make a difference in academics. For example, I’ve done a bit of self learning online in these subjects. In math, I’ve read up on things above my grade level and so far I have learnt about things such as matrices and differentiation. For computer science, I know Scratch, Javascript, Java and Python. Once I saw a Youtube clip about a college class homework competition which was about designing the best AI (Artificial Intelligence) for your Pacman so that it does not get eaten.  And so I tried and have successfully imitated this game last year using Scratch, even using the default AI from the original games.    I have been studying piano since I was five and have reached 8th grade last year.  This year I continue  to develop  my musical side more fully by pursuing the performance diploma.  I feel my senses are just starting to be awakened by the rich interaction with the piano and music.   I am always reminded by my parents that people need to be good in more than one thing to succeed in life.    If I get the scholarship, I will use some of the money to enroll myself in more lessons, online classes or even summer schools to further improve myself to be admitted into a good college. If I’m successful, this would bolster the school’s reputation. 
"""

prompt = PromptTemplate(
    input_variables=["tone_descriptors", "example_text"],
    template=prompt_template,
)

prompt_formatted = prompt.format(tone_descriptors=tone_descriptors, example_text=example_text)

print(prompt_formatted)
tone = llm.predict(prompt_formatted)

print(tone)