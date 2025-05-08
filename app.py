import streamlit as st
import pandas as pd
import os
import datetime
from gtts import gTTS
import pickle
from PIL import Image


# --- Page Configuration ---
st.set_page_config(
    page_title="SwasthyaBot",
    page_icon="🩺",
    layout="wide"

)

# Title and Description
st.markdown("<h1 class='swasthya-title'>🤖 SwasthyaBot: A Rural Women’s Health Chatbot</h1>", unsafe_allow_html=True)
st.markdown("""
   <p class='swasthya-desc' style='font-weight: bold; background-color: #f0f8ff; padding: 0px ; border-radius: 0px; color: black; text-align: center;'>Empowering women through AI-driven healthcare conversations in Marwari.</p>
""", unsafe_allow_html=True)


with open("styles.css.html") as f:
    st.markdown("<hr style='border: 1px solid #e0e0e0;'>", unsafe_allow_html=True)


# Features
st.markdown("<div class='features'>", unsafe_allow_html=True)
st.markdown("<h2>🌟 मुख्य विशेषताएँ </h2>", unsafe_allow_html=True)
st.markdown("""
<ul>
    <li>🎤 हिंदी से मारवाड़ी आवाज अनुवाद
      <dl>यह सुविधा हिंदी पाठ को मारवाड़ी बोली में बदलती है। </dl>
    </li>
    <li>🗣️ महिलाओं के स्वास्थ्य के लिए एआई-संचालित चैटबॉट
       <dl>कृत्रिम बुद्धिमत्ता से लैस चैटबॉट जो महिलाओं के स्वास्थ्य संबंधी जानकारी और सहायता प्रदान करता है।</dl>
    </li>
    <li>📱 फ़ोन पर आसान पहुँच
        <dl>इस चैटबॉट को फ़ोन पर आसानी से इस्तेमाल किया जा सकता है।</dl>
    </li>
    <li>🔊 पहुँच के लिए ऑडियो प्रतिक्रियाएँ
       <dl> यह चैटबॉट ऑडियो के माध्यम से प्रतिक्रियाएँ देता है, जिससे पहुँच और आसान हो जाती है।</dl>
    </li>
</ul>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)





# Characteristics
st.markdown("<h3>👩‍⚕️ स्वस्थबॉट की विशेषताएँ </h3>", unsafe_allow_html=True)
st.markdown("""
- ग्रामीण भारतीय महिलाओं के लिए सांस्कृतिक रूप से प्रासंगिक 🧕
- आवाज समर्थन के साथ उपयोग में आसान 📢
- स्वास्थ्य सुझाव प्रदान करता है, सवालों के जवाब देता है और मार्गदर्शन देता है  🏥
""", unsafe_allow_html=True)

# Steps
st.markdown("<h3>🛠️ कैसे इस्तेमाल करें ? </h3>", unsafe_allow_html=True)
st.markdown("""
1. अपना स्वास्थ्य प्रश्न हिंदी में लिखिए 🗨️
2. बॉट इसे मारवाड़ी में अनुवाद करता है 🔄
3. एआई संसाधित करता है और स्वास्थ्य सलाह के साथ उत्तर देता है 👩‍⚕️
4. आप ऑडियो प्रारूप में प्रतिक्रिया सुनते हैं  🔊
""", unsafe_allow_html=True)



# --- Custom CSS ---
st.markdown("""
   <style>
       .main-title {
           display: flex;
           align-items: center;
           justify-content: center;
           gap: 15px;
           font-family: 'Trebuchet MS', sans-serif;
           color: #FF5733;
       }
       .description {
           text-align: center;
           font-family: 'Calibri', sans-serif;
           font-size: 16px;
           margin-bottom: 20px;
       }
       .features-heading {
           text-align: center;
           font-family: 'Trebuchet MS', sans-serif;
           font-size: 26px;
           color: #2E8B57;
           margin-top: 20px;
       }
       .feature-item {
           text-align: center;
           font-family: 'Calibri', sans-serif;
           font-size: 16px;
           margin-bottom: 10px;
       }
       .chatbot-button {
           display: block;
           margin: 30px auto;
           padding: 12px 30px;
           background-color: #FF5733;
           color: white;
           border: none;
           border-radius: 8px;
           font-size: 18px;
           cursor: pointer;
           transition: background-color 0.3s ease;
           text-align: center; /* Center the button text */
       }
       .dialog-box {
           border: 2px solid #FF5733;
           border-radius: 12px;
           padding: 20px;
           background-color: #fff0e6;
           text-align: center;
           font-family: 'Calibri', sans-serif;
       }
       .image-container {
           display: flex;
           flex-direction: column;
           align-items: center;
       }
       .image-caption-box {
           background-color: #f0f8ff; /* Light Alice Blue - You can change this */
           border: 1px solid #e0e0e0;
           padding: 10px;
           margin-top: 5px;
           border-radius: 5px;
           text-align: center;
           font-size: 14px;
           color: #333; /* Darker text for readability */
       }
       
       .detailed-features-container {
           background-color: #E0FFFF
           padding: 20px;
           margin-top: 30px; /* Space from the above section */
           border-radius: 5px;
           color: #333; /* Dark text color */
       }
       .detailed-feature-heading {
           text-align: center;
           font-size: 24px;
           font-weight: bold;
           color: #2E8B57; /* Green heading color */
           margin-bottom: 15px;
       }
       .detailed-feature-item-container {
           background-color:#ffe4e1; /* Light Pink background for each point */
           padding: 15px;
           margin-bottom: 10px;
           border-radius: 5px;
           border: 1px solid #e0e0e0; /* Light grey border for each point */
           color: #333; /* Dark text color */
       }
       
       
    
       
       .point-heading {
           text-align: center;
           font-weight: bold;
           display: block;
       }
       
       
       
       
       
       
       
       </style>
""", unsafe_allow_html=True)


# --- Main Title ---



st.markdown(f"""
   <div class="main-title">
       <h1>🌸 SwasthyaBot 🌸</h1>
   </div>
""", unsafe_allow_html=True)


# --- Description ---
st.markdown("""
   <div class="description">
       <p>हमारा SwasthyaBot एक AI-पावर्ड हेल्थ ट्रांसलेटर चैटबॉट है, जो ग्रामीण महिलाओं के लिए स्वास्थ्य शिक्षा
       को सरल और प्रभावी तरीके से प्रस्तुत करता है। यहाँ आप हिंदी में पूछकर मारवाड़ी में स्वास्थ्य संबंधी सलाह और जानकारी प्राप्त कर सकते हैं।</p>
   </div>
""", unsafe_allow_html=True)


# --- Representative Images ---
image_info = [
   {"url": "C:/hindi_marwari_chatbot/image1.jpg", "caption": "📱 मोबाइल से आसानी से उपयोग"},
   {"url": "C:/hindi_marwari_chatbot/image2.jpg", "caption": "🤖 AI आधारित स्मार्ट सहायक"},
   {"url": "C:/hindi_marwari_chatbot/image3.jpg", "caption": "👩‍🌾 महिलाओं के लिए विशेष रूप से"}
]
cols = st.columns(3)
for idx, col in enumerate(cols):
   with col:
       st.markdown("<div class='image-container'>", unsafe_allow_html=True)
       st.image(image_info[idx]["url"], use_container_width=True) # Changed parameter here
       st.markdown(f"<div class='image-caption-box'>{image_info[idx]['caption']}</div>", unsafe_allow_html=True)
       st.markdown("</div>", unsafe_allow_html=True)





# --- विस्तृत विशेषताएँ ---
# Features
st.markdown("<div class='features'>", unsafe_allow_html=True)
st.markdown("<h2><b>🌟 मुख्य विशेषताएँ </b> </h2>", unsafe_allow_html=True)
st.markdown("""
   <div class="detailed-features-container">
       <div class="detailed-feature-item-container">
           <b>1. सामान्य और विशिष्ट स्वास्थ्य प्रश्नों का मारवाड़ी में ऑडियो उत्तर</b><br>
           आपका चैटबॉट उपयोगकर्ताओं द्वारा पूछे गए सामान्य स्वास्थ्य संबंधी प्रश्नों और मासिक धर्म स्वच्छता व बीमारियों की रोकथाम जैसे विशिष्ट क्षेत्रों से संबंधित हिंदी पाठ को मारवाड़ी ऑडियो में उत्तर देगा। इससे उपयोगकर्ताओं को अपनी भाषा में जानकारी आसानी से समझने में मदद मिलेगी।
       </div>
       <div class="detailed-feature-item-container">
           <b>2. सुलभ और श्रव्य स्वास्थ्य मार्गदर्शन</b><br>
           यह चैटबॉट स्वास्थ्य संबंधी जानकारी को सुनने योग्य प्रारूप में उपलब्ध कराएगा, जिससे उन लोगों के लिए भी यह सुलभ होगा जो पढ़ना पसंद नहीं करते या जिन्हें पढ़ने में कठिनाई होती है। मारवाड़ी ऑडियो प्रारूप जानकारी को अधिक व्यक्तिगत और समझने में आसान बना सकता है।
       </div>
       <div class="detailed-feature-item-container">
           <b>3. विशिष्ट स्वास्थ्य विषयों पर स्थानीय भाषा में जागरूकता</b><br>
           आपका मॉडल मासिक धर्म स्वच्छता और बीमारियों की रोकथाम जैसे महत्वपूर्ण स्वास्थ्य विषयों पर मारवाड़ी भाषा में जानकारी प्रदान करके स्थानीय समुदाय में जागरूकता बढ़ाने में महत्वपूर्ण भूमिका निभाएगा। यह उन लोगों तक पहुंचने में मदद करेगा जो हिंदी में सहज नहीं हैं, जिससे स्वास्थ्य संबंधी महत्वपूर्ण संदेश प्रभावी ढंग से संप्रेषित किए जा सकेंगे।
       </div>
   </div>
""", unsafe_allow_html=True)



# --- Chatbot Button ---
st.markdown("""
   <div style="text-align: center;">
       <button class="chatbot-button">💬 Chat with SwasthyaBot</button>
   </div>
""", unsafe_allow_html=True)


# --- Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "Hindi_Marwari.csv")
MODEL_PATH = os.path.join(BASE_DIR, "translation_model", "translation_model.pkl")
HISTORY_PATH = os.path.join(BASE_DIR, "translation_history.csv")
AUDIO_FOLDER = os.path.join(BASE_DIR, "Audio")


# --- Load Model ---
if not os.path.exists(MODEL_PATH):
   st.error(f"🚨 Model file not found at: {MODEL_PATH}")
   st.stop()
try:
   with open(MODEL_PATH, 'rb') as f:
       translation_model = pickle.load(f)
except Exception as e:
   st.error(f"🚨 Model load error: {e}")
   st.stop()


# --- Load Dataset ---
if not os.path.exists(DATASET_PATH):
   st.error(f"🚨 Dataset file not found at: {DATASET_PATH}")
   st.stop()
try:
   df = pd.read_csv(DATASET_PATH)
   if 'hindi question' not in df.columns or 'marwari answer' not in df.columns:
       st.error("🚨 Dataset में 'hindi question' और 'marwari answer' columns होने चाहिए।")
       st.stop()
   hindi_marwari_dict = pd.Series(df['marwari answer'].values, index=df['hindi question']).to_dict()
except Exception as e:
   st.error(f"🚨 Dataset load error: {e}")
   st.stop()


# --- Input ---
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("🖊️ हिंदी में सामान्य वाक्य लिखें:")
input_text = st.text_input("")


# --- Translate + Audio ---
if st.button("🔊 मारवाड़ी ऑडियो चलाएँ"):
   if input_text.strip() == "":
       st.warning("⚠️ कृपया वाक्य दर्ज करें।")
   else:
       translated = hindi_marwari_dict.get(input_text.strip())
       if translated:
           try:
               tts = gTTS(translated, lang='hi')
               os.makedirs(AUDIO_FOLDER, exist_ok=True)
               timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
               filename = "".join(e for e in translated if e.isalnum() or e.isspace()).replace(" ", "_")
               audio_file = os.path.join(AUDIO_FOLDER, f"{filename}_{timestamp}.mp3")
               tts.save(audio_file)
               with open(audio_file, 'rb') as f:
                   st.audio(f.read(), format='audio/mp3')
               st.success(f"✅ अनुवाद: {translated}")
               history_row = pd.DataFrame([[datetime.datetime.now(), input_text.strip(), translated, audio_file]],
                                          columns=["Timestamp", "Hindi Input", "Marwari Output", "Audio Path"])
               if os.path.exists(HISTORY_PATH):
                   old_history = pd.read_csv(HISTORY_PATH)
                   pd.concat([old_history, history_row], ignore_index=True).to_csv(HISTORY_PATH, index=False)
               else:
                   history_row.to_csv(HISTORY_PATH, index=False)
           except Exception as e:
               st.error(f"🚨 Audio error: {e}")
       else:
           st.warning("⚠️ अनुवाद नहीं मिला।")


# --- Show History ---
st.markdown("<hr>", unsafe_allow_html=True)
with st.expander("🔎 अनुवाद इतिहास देखें"):
   if os.path.exists(HISTORY_PATH):
       try:
           history_df = pd.read_csv(HISTORY_PATH)
           st.dataframe(history_df)
       except Exception as e:
           st.error(f"🚨 History load error: {e}")
   else:
       st.info("ℹ️ कोई अनुवाद इतिहास उपलब्ध नहीं है।")
       pass  # Load CSV logic here

       # --- Footer ---
       st.markdown("""
              <footer>
                  📞 123-456-7890 | ✉️ support@swasthyabot.in | 🌐 www.swasthyabot.in
              </footer>
          """, unsafe_allow_html=True)





