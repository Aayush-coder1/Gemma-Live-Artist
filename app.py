import streamlit as st
from google import genai
from google.genai import types
from PIL import Image

# --- 1. SETUP & THEME ---
st.set_page_config(page_title="Gemma Live Artist", page_icon="💄")
st.title("🎨 Gemma 4: Live Artist Consultant")
st.markdown("### Track: Digital Equity & Inclusivity")

# --- 2. CONNECT TO GEMMA 4 ---
API_KEY = st.secrets["GEMINI_API_KEY"]
client = genai.Client(
    api_key=API_KEY, 
    http_options=types.HttpOptions(api_version="v1beta")
)

# --- 3. THE "AGENT" LOGIC ---
# This prompt defines the "Agentic" behavior required by the hackathon
SYSTEM_PROMPT = """
You are a professional makeup consultant powered by Gemma 4. 
Your goal is to assist people, including those with visual impairments, in applying makeup.
1. Analyze the uploaded image.
2. Identify specific facial zones (Eyes, Lips, Cheeks).
3. Provide clear, spatial instructions (e.g., 'Apply slightly higher on the cheekbone').
4. Be encouraging and concise.
"""

# --- 4. UI SHELL ---
st.subheader("Step 1: Capture or Upload Face")
img_file = st.camera_input("Take a photo to start your consultation")

if img_file:
    image = Image.open(img_file)
    st.image(image, caption="Current State", use_container_width=True)

    if st.button("Get Professional Advice"):
        with st.spinner("Gemma 4 is analyzing your features..."):
            try:
                # OFFICIAL MODEL NAME FOR APRIL 2026 HACKATHON
                response = client.models.generate_content(
                    model="gemma-4-26b-a4b-it", # This MoE model is the hackathon favorite
                    contents=[SYSTEM_PROMPT, image]
                )
                st.success("Consultation Ready!")
                st.write(response.text)
                
                # Accessibility Feature: Text-to-Speech hint
                st.info("💡 Tip: You can use a screen reader to hear these instructions.")
                
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()
st.caption("Phase 1 & 2 Hybrid | Built for Gemma 4 Good Hackathon")