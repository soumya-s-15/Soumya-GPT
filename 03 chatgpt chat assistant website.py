import google.generativeai as genai
import gradio as gr

# Configure Google API key
genai.configure(api_key="AIzaSyCCcBxmCQaUnKkCVhkd54YhhpWCVjVjVyA")

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

# Define system message
system_message = "You are a financial expert specializing in real estate investment and negotiation."

def CustomGemini(user_input):
    prompt = f"{system_message}\n\nUser: {user_input}\n\nAssistant:"
    
    # Generate response from Gemini
    response = model.generate_content(prompt)
    
    return response.text

# Create Gradio interface
demo = gr.Interface(fn=CustomGemini, inputs="text", outputs="text", title="SEARCH IN YOUR SITS")

# Launch Gradio app
demo.launch(share=True)
