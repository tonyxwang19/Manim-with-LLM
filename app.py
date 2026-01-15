import streamlit as st
from llm_service import generate_manim_code
from renderer import render_manim_code


st.set_page_config(page_title="Math to Manim Generator", page_icon="📐")

st.title("📐 Math to Manim Animation Generator")
st.write("Enter a math topic, and I'll generate a Manim animation for you using DeepSeek!")

api_key = 'YOUR_KEY'

# Main input
topic = st.text_area("What do you want to visualize?", height=100, placeholder="e.g., The Pythagorean Theorem, A rotating 3D cube, The area of a circle...")

if st.button("Generate Animation", type="primary"):
    if not api_key:
        st.error("DeepSeek API Key is required!")
    elif not topic:
        st.error("Please enter a topic.")
    else:
        # 1. Generate Code
        with st.status("Processing...", expanded=True) as status:
            st.write("Querying DeepSeek...")
            code = generate_manim_code(topic, api_key)
            
            if code.startswith("# Error"):
                status.update(label="Generation Failed", state="error")
                st.error(code)
            else:
                st.write("Code generated successfully!")
                st.code(code, language="python")
                
                # 2. Render Video
                st.write("Rendering video... (This may take a while)")
                try:
                    video_path = render_manim_code(code)
                    status.update(label="Animation Ready!", state="complete")
                    
                    st.success("Rendering Complete!")
                    st.video(video_path)
                    
                    # Provide download button
                    with open(video_path, "rb") as file:
                        btn = st.download_button(
                            label="Download Video",
                            data=file,
                            file_name="manim_animation.mp4",
                            mime="video/mp4"
                        )
                except Exception as e:
                    status.update(label="Rendering Failed", state="error")
                    st.error(f"Error during rendering: {e}")
