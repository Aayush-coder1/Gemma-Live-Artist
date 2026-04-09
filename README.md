🎨 Live Artist: AI Makeup Mentor

Track: Digital Equity & Inclusivity
Powered by: Gemma 4 (31B-IT / 26B-A4B)

🌟 Vision

Traditional makeup tutorials are heavily visual and often inaccessible to beginners or individuals with visual impairments.

Live Artist leverages the multimodal capabilities of Gemma 4 to deliver real-time, spatial, and inclusive makeup guidance, making beauty education more accessible for everyone.

🚀 Features (Phase 1)
Multimodal Analysis
Processes live webcam input to detect and understand facial regions.
Smart Consultation
Provides beginner-friendly, personalized makeup suggestions based on facial features.
Privacy-First Design
Supports offline execution on edge devices (Gemma 4 E2B/E4B).
Inclusive UX
Designed with accessibility-first interactions for diverse users.

Further phases to be added soon!

🛠️ Tech Stack
AI Model: Gemma 4 (Google AI Studio API)
Frontend: Streamlit
Computer Vision: OpenCV, PIL
Deployment: GitHub, Streamlit Cloud
💻 Installation & Setup
1. Clone the Repository
git clone https://github.com/Aayush-coder1/Gemma-Live-Artist.git
cd Gemma-Live-Artist
2. Install Dependencies
pip install google-genai streamlit opencv-python-headless Pillow
3. Configure API Key

Create a secure configuration for your API key:

Create a .streamlit/ folder in the project root
Inside it, create a secrets.toml file
Add your API key:
GEMINI_API_KEY = "YOUR_API_KEY_HERE"

4. Run the Application
streamlit run app.py

🔒 Privacy & Accessibility
Designed to work locally on-device where possible
No unnecessary data storage
Focused on inclusive design, especially for users with visual challenges

📌 Future Enhancements
Voice-guided makeup assistance
Real-time step-by-step overlay instructions
Skin tone & product recommendation engine
AR-based visualization