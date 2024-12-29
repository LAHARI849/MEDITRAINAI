import streamlit as st
import requests


# Set up the Streamlit app
def main():
    st.title("MEDITRAIN AI CHATBOT")
    st.write("Mindful Support, Anytime, Anywhere.")
    st.write("Type your question or request in the chat box below, and let Meditrain guide you to a calmer, more balanced state")

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
        st.write(f"**You:** {chat['user']}")
        st.write(f"**Chatbot:** {chat['bot']}")


if __name__ == "__main__":
    main()


