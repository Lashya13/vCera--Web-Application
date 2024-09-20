# chatbot/chatbot_logic.py

conversation = {
    1: {"bot": "Hi, what would you like to talk about today?", "expected_responses": ["yes", "no"]},
    2: {"bot": "Are you sure?", "expected_responses": ["yes", "no"]},
    3: {"bot": "Would you like me to tell you some stories?", "expected_responses": ["yes", "no"]},
    4: {"bot": "Computer, did we bring batteries? - Eileen Gunn", "expected_responses": []},
}

def get_bot_response(user_input, step):
    user_input = user_input.lower()

    # Move to the next step based on the user's input and the current step
    if user_input in conversation[step]["expected_responses"]:
        step += 1

    # Return bot response and the current step
    bot_message = conversation.get(step, {"bot": "Sorry, I didn't get that.", "expected_responses": []})["bot"]
    return {"message": bot_message, "step": step}
