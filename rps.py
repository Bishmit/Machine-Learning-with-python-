import pygame
import sys
import speech_recognition as sr

# Initialize Pygame
pygame.init()

rock_img = pygame.image.load("rock.png")
paper_img = pygame.image.load("paper.png")
scissors_img = pygame.image.load("scissors.png")

# Set up screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Speech Recognition Game")

# Set up recognizer and microphone
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def recognize_speech():
    """Recognize speech from the microphone."""
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return ""

def main():
    # Set up game variables
    running = True
    guess_mode = False  # Flag to indicate whether the user is guessing

    # Initialize current_img
    current_img = None

    # Set up clock
    clock = pygame.time.Clock()

    try:
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        guess_mode = True
        

            # Check recognizer and microphone types
            if not isinstance(recognizer, sr.Recognizer):
                raise TypeError("`recognizer` must be `Recognizer` instance")

            if not isinstance(microphone, sr.Microphone):
                raise TypeError("`microphone` must be `Microphone` instance")

            # Get speech input only when in guess mode
            if guess_mode:
                speech = recognize_speech()
                if speech:
                    if "rock" in speech:
                        current_img = rock_img
                    elif "paper" in speech:
                        current_img = paper_img
                    elif "scissors" in speech:
                        current_img = scissors_img

            # Clear the screen
            screen.fill((0, 0, 0))

            # Blit the current image onto the screen
            if current_img is not None:
                screen.blit(current_img, (0, 0))

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            clock.tick(10)

    except Exception as e:
        print("An error occurred:", e)
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
