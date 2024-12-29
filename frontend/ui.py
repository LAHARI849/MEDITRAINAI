import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Function to dynamically resize images
def resize_image(url, width, height):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            resized_image = image.resize((width, height))
            return resized_image
        else:
            st.error(f"Error loading image from {url}")
            return None
    except Exception as e:
        st.error(f"An error occurred while loading the image: {e}")
        return None

# URLs for the logo, user avatar, and bot avatar
logo_url = "https://github.com/LAHARI849/MEDITRAINAI/blob/main/frontend/logo.jpeg?raw=true"
user_avatar_url = "https://github.com/LAHARI849/MEDITRAINAI/blob/7896e7c36a186c7de455a2b5ec33aaec956f2108/frontend/user.webp"
bot_avatar_url = ""

# Set up the Streamlit app
def main():
    # Resize and display the logo
    logo = resize_image(logo_url, 200, 100)  # Adjust logo size
    if logo:
        st.image(logo)

    # Add title and description
    st.title("Meditrain AI")
    st.markdown("**Mindful Support, Anytime, Anywhere.**")

    # Initialize session state for storing conversation history
    if "conversation" not in st.session_state:
        st.session_state["conversation"] = []

    # Input text box for the user
    user_query = st.text_input("Your Query:", placeholder="Ask something...")

    # Submit button
    if st.button("Ask Meditrain"):
        if user_query:
            # Prepare the payload for the POST request
            payload = {"query": user_query}

            try:
                # Make the POST request to the API endpoint
                response = requests.post("https://meditrainai-10.onrender.com/response", json=payload)
                if response.status_code == 200:
                    # Parse the JSON response
                    data = response.json()

                    # Extract and display the chatbot response
                    bot_response = data.get("response", "No response found.")

                    # Save the conversation to session state
                    st.session_state["conversation"].append(
                        {"user": user_query, "bot": bot_response}
                    )
                else:
                    st.error(
                        f"Error {response.status_code}: Unable to get a response from the API."
                    )
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a query before sending.")

    # Display the conversation history
    st.write("### Conversation History")
    for chat in st.session_state["conversation"]:
        cols = st.columns([1, 9])  # Create two columns for avatars and text

        # User query with avatar
        with cols[0]:
            user_avatar = resize_image(user_avatar_url, 50, 50)  # Resize user avatar
            if user_avatar:
                st.image(user_avatar, use_column_width=False)
        with cols[1]:
            st.markdown(f"**User:** {chat['user']}")

        # Bot response with avatar
        cols = st.columns([1, 9])  # Adjust layout for bot
        with cols[0]:
            bot_avatar = resize_image(bot_avatar_url, 50, 50)  # Resize bot avatar
            if bot_avatar:
                st.image(bot_avatar, use_column_width=False)
        with cols[1]:
            st.markdown(f"**Bot:** {chat['bot']}")

if __name__ == "__main__":
    main()
