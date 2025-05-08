import pandas as pd
import datetime
import os

history_path = os.path.join("dataset", "transaction_history.csv")

def save_transaction(hindi, marwari, audio_path):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = pd.DataFrame([[now, hindi, marwari, audio_path]],
                             columns=["Timestamp", "Hindi", "Marwari", "AudioFile"])
    
    if os.path.exists(history_path):
        df = pd.read_csv(history_path)
        df = pd.concat([df, new_entry], ignore_index=True)
    else:
        df = new_entry

    df.to_csv(history_path, index=False)

