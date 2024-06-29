#pyautogui help us to tell at what position our cursor is that means it tell as in our screen what is the coordinates of our cursor
#pyperclip is used to take texts from clipboard
import pyautogui
import pyperclip
import time
import openAI

client = OpenAI(
  api_key="<Your Key Here>",
)

def is_last_message_from_sender(chat_log,sender_name="Ritwik"):
    #Split the chat log into individual messages
    message=chat.log.strip().split("/2024] ")[-1]
    if sender_name in message:
        return True
    return False

            
#Step 1: Click on the whatsapp icon at coordinates (1243,1502)
pyautogui.click(1243,1502)
time.sleep(1)

while True:
    

    #Step 2: Drag the mouse from (552,143) to (1888,949) to select the text
    pyautogui.moveTo(620,220)
    pyautogui.dragTo(1888,949, duration=1.0,button='left')
    #Drag for 1 second

    #Step 3 : Copy the selected text to clipboard
    pyautogui.hotkey('ctrl','c')
    pyautogui.doubleClick(1790,870)
    time.sleep(2)
    #Wait for 1 second to ensure the copy command is completed

    #Step 4: Retrieve the text from the clipboard and store it in a 
    chat_history=pyperclip.paste()

    #Print the copied text to verify
    print(chat_history)

    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named lavkesh who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Lavkesh. Output should be the next chat response (text message only)"},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        pyautogui.click(944,962)
        time.sleep(1) #wait for 1 second to ensure the click is registered

        #Paste the text
        pyautogui.hotkey('ctrl','v')

        pyautogui.press('Enter')