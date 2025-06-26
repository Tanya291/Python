import os
import webbrowser
import datetime
import pyjokes
import wikipedia

def greet():
    print("👋 Hello! I am your Command Line Assistant.")
    print("Type 'help' to see what I can do.\n")

def show_help():
    print("""
📋 Available Commands:
  open youtube      → Opens YouTube in browser
  open google       → Opens Google
  search <query>    → Searches Wikipedia
  time              → Shows current time
  date              → Shows today’s date
  joke              → Tells a programming joke
  clear             → Clears the screen
  exit              → Exit the assistant
""")

def assistant():
    greet()
    while True:
        command = input(">> ").lower()

        if 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in command:
            webbrowser.open("https://www.google.com")

        elif command.startswith('search'):
            topic = command.replace('search', '').strip()
            try:
                result = wikipedia.summary(topic, sentences=2)
                print(f"\n🔍 {result}\n")
            except:
                print("❌ Couldn't find the topic.")

        elif 'time' in command:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"🕒 Current time is {now}")

        elif 'date' in command:
            today = datetime.date.today()
            print(f"📅 Today's date is {today}")

        elif 'joke' in command:
            print("😂 " + pyjokes.get_joke())

        elif 'clear' in command:
            os.system('cls' if os.name == 'nt' else 'clear')

        elif 'help' in command:
            show_help()

        elif 'exit' in command:
            print("👋 Goodbye!")
            break

        else:
            print("❓ I don't understand that command. Type 'help'.")

assistant()
