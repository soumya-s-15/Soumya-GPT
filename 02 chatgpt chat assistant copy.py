import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyCCcBxmCQaUnKkCVhkd54YhhpWCVjVjVyA")

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

# Collect system message
system_msg = input("What type of chatbot would you like to create?\n")
messages = [{"role": "system", "content": system_msg}]

print("Your new assistant is ready!")

while True:
    user_input = input()
    
    if user_input.lower() == "quit()":
        print("Exiting chat...")
        break

    messages.append({"role": "user", "content": user_input})
    
    # Generate response
    response = model.generate_content(user_input)
    reply = response.text

    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
