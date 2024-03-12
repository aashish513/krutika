import pyttsx3


def parse_request(request):
    if request.method == 'POST':
            # Get the text message from the request data
            message = request.form.get('message')
            # Print the message in the terminal
            print("Received message (POST):", message)
            # Return a response (optional)
            return message
    elif request.method == 'GET':
        # Get the text message from the query parameters
        message = request.args.get('message')
        # Print the message in the terminal
        print("Received message (GET):", message)
        # Return a response (optional)
        return message




     

def text_to_speech(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)

    # Wait for speech to finish
    engine.runAndWait()



def speak(api_request):
     #text to audio
     message= parse_request(api_request)
     text_to_speech(message)
     print(f"Speaking: {message}")
     return f"Speaking: {message}"