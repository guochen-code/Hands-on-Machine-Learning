import pyaudio
import wave
import streamlit as st
import pandas as pd
import json
import random
from openai import OpenAI
import json

# Define parameters for the recording
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Number of frames per buffer
OUTPUT_FILENAME = "output.wav"  # Output file name
OpenAIclient = OpenAI(api_key="<>")
MODEL="gpt-4o"

def start_recording():
    # Initialize PyAudio
    st.session_state.audio = pyaudio.PyAudio()

    # Open a new stream for recording
    st.session_state.stream = st.session_state.audio.open(format=FORMAT,
                                                        channels=CHANNELS,
                                                        rate=RATE,
                                                        input=True,
                                                        frames_per_buffer=CHUNK)
    st.session_state.frames = []
    st.session_state.recording = True

    st.write("Recording started...")
    while st.session_state.recording:
        data = st.session_state.stream.read(CHUNK)
        st.session_state.frames.append(data)

def stop_recording():
    # Stop and close the stream
    st.session_state.stream.stop_stream()
    st.session_state.stream.close()

    # Terminate the PyAudio instance
    st.session_state.audio.terminate()

    # Save the recorded data as a WAV file
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(st.session_state.audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(st.session_state.frames))

    st.write("Recording stopped. File saved as", OUTPUT_FILENAME)
    st.session_state.recording = False

# Define the initial data for the timesheet
def create_sample_data(cheat,client,engagement,hours):
    # Sample data for demonstration
    if cheat == 0:
        data = [
            {"Client": client, "Engagement": engagement, "Work Type": "503 - Education",
             "Activity": "1 - Internal Based Learn - MNPU (IntLrn)",
             "Rate": "Generalist", "Hours": hours, "Notes": "Training on MNP University"},
            # {"Client": "Beta LLC", "Engagement": "Project Beta", "Work Type": "Consulting", "Activity": "Strategy",
            #  "Rate": 150.0, "Hours": 8.0, "Notes": "Consultation meeting"},
        ]
    else:
        data = [
            {"Client": client, "Engagement": engagement, "Work Type": "3 - Review",
             "Activity": "1 - Planning & Setup (Plan)",
             "Rate": "Generalist", "Hours": hours, "Notes": "Initial setup"},
            # {"Client": "Beta LLC", "Engagement": "Project Beta", "Work Type": "Consulting", "Activity": "Strategy",
            #  "Rate": 150.0, "Hours": 8.0, "Notes": "Consultation meeting"},
        ]
    return data


# Initialize or update the DataFrame
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=['Client', 'Engagement', 'Work Type', 'Activity', 'Rate', 'Hours', 'Notes'])
if 'phase' not in st.session_state:
    st.session_state.phase = 'generate'  # Start in 'generate' phase
# Initialize Streamlit session state variables
if 'recording' not in st.session_state:
    st.session_state.recording = False
if 'frames' not in st.session_state:
    st.session_state.frames = []

# Initialize form values if they are not set
if 'form_values' not in st.session_state:
    st.session_state.form_values = {
        'Client': '',
        'Engagement': '',
        'Work Type': '',
        'Activity': '',
        'Rate': '',
        'Hours': 0.0,
        'Notes': ''
    }

# Form for displaying and populating data
with st.form(key='timesheet_form'):
    st.write("### Timesheet Entry Form")
    print('>>>>>>>:',st.session_state.form_values)
    client = st.text_input('Client', value=st.session_state.form_values['Client'])
    engagement = st.text_input('Engagement', value=st.session_state.form_values['Engagement'])
    work_type = st.text_input('Work Type', value=st.session_state.form_values['Work Type'])
    activity = st.text_input('Activity', value=st.session_state.form_values['Activity'])
    rate = st.text_input('Rate', value=st.session_state.form_values['Rate'])
    hours = st.number_input('Hours', value=st.session_state.form_values['Hours'], min_value=0.0, format="%.2f")
    notes = st.text_area('Notes', value=st.session_state.form_values['Notes'])

    submit_button = st.form_submit_button(label='Add Entry')

    if submit_button:
        # Add the new entry to the DataFrame
        new_entry = pd.DataFrame([[client, engagement, work_type, activity, rate, hours, notes]],
                                 columns=['Client', 'Engagement', 'Work Type', 'Activity', 'Rate', 'Hours', 'Notes'])
        st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)
        st.write("Entry added!")

# Display the timesheet table
# st.write("### Timesheet Entry Table")
# st.dataframe(st.session_state.data)

# Button to generate the JSON body and populate the form
if 'show_json' not in st.session_state:
    st.session_state.show_json = False

# Streamlit UI
if st.button('Start Recording'):
    if not st.session_state.recording:
        start_recording()
    else:
        st.write("Already recording!")

if st.button('Stop Recording'):
    if st.session_state.recording:
        stop_recording()
    else:
        st.write("Not currently recording.")

if st.button('Generate JSON Body'):
    if not st.session_state.show_json:
        audio_path = "output.wav"

        transcription = OpenAIclient.audio.transcriptions.create(
            model="whisper-1",
            file=open(audio_path, "rb")
        )

        print(transcription)

        response = OpenAIclient.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system",
                 "content": """Please extrac the following fields from the provided text and only return a json forma, no explanations. The fields include (1) Client, (2) Engagement and (3) Hours."""},
                {"role": "user", "content": [
                    {"type": "text", "text": f"The provided text is: {transcription.text}"}
                ],
                 }
            ],
            temperature=0,
        )

        print('-----')
        print(response.choices[0].message.content[7:-4].strip())
        result = response.choices[0].message.content[7:-4].strip()

        data = json.loads(result)

        # Accessing the values
        client = str(data['Client'])
        engagement = str(data['Engagement'])
        hours = float(data['Hours'])

        # Print the values
        print(f"Client: {client}")
        print(f"Engagement: {engagement}")
        print(f"Hours: {hours}")
        ######

        # Call the function to create sample data
        random_value = random.choice([0, 1])
        if client == "MNP University":
            cheat = 0
        else:
            cheat = 1
        print('>>>>>>>cheat:',cheat)
        sample_data = create_sample_data(cheat,client,engagement,hours)#[random_value]
        print('>>>>:',sample_data)

        # Convert the sample data to JSON
        json_body = json.dumps(sample_data, indent=4)
        print('.....:',json_body)
        st.write("### JSON Body")
        st.code(json_body, language='json')
        print('debug 001--------')

        # Populate the form with the first entry from the sample data
        if sample_data:
            # random_value = random.choice([0, 1])
            first_entry = sample_data #sample_data[random_value]
            st.session_state.form_values = first_entry[0]  # Update form values for the form to reflect the sample data

        # Optionally, you can also provide a download link for the JSON file
        print('debug 002--------')
        st.download_button(
            label="Download JSON",
            data=json_body,
            file_name='timesheet_entries.json',
            mime='application/json'
        )

        # Update the flag to show the JSON on subsequent clicks
        print('debug 003--------')
        st.session_state.show_json = True
    else:
        # Continue with the rest of the code after the JSON has been shown
        # For demonstration, we simply display a message
        # st.write("You have already viewed the JSON body. Click again to continue.")
        st.session_state.show_json = False  # Reset the flag to allow for future JSON displays
