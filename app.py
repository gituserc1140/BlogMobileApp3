import json
import streamlit as st
import streamlit.components.v1 as components
import cohere

COMPATIBLE_COHERE_MODELS = [
    "command-a-03-2025",
    "command-r-plus-08-2024",
    "command-r-08-2024",
    "command-r7b-12-2024",
]


def generate_blog_content(api_key, topic, model, length=300):
    co = cohere.ClientV2(api_key)
    response = co.chat(
        model=model,
        messages=[{"role": "user", "content": f"Write a blog post about {topic}."}],
        max_tokens=length,
    )
    return response.message.content[0].text

def main():
    st.title('Blog Content Generator with Cohere API')
    api_key = st.text_input('Enter your Cohere API Key', type='password')
    topic = st.text_input('Enter the blog topic')
    model = st.selectbox(
        'Select Cohere model',
        COMPATIBLE_COHERE_MODELS,
        index=0,
    )
    length = st.number_input('Desired length of the blog (words)', min_value=100, max_value=1000, value=300)

    if st.button('Generate Blog'):
        if not api_key or not topic:
            st.error('Please provide both API Key and a topic.')
        else:
            try:
                st.session_state['blog_content'] = generate_blog_content(api_key, topic, model, length)
            except Exception as e:
                st.error(f'An error occurred: {e}')

    if 'blog_content' in st.session_state:
        st.subheader('Generated Blog Content')
        st.write(st.session_state['blog_content'])
        content_json = json.dumps(st.session_state['blog_content'])
        components.html(
            f"""
            <button id="copy-btn" onclick="
                var text = {content_json};
                var ta = document.createElement('textarea');
                ta.value = text;
                ta.style.position = 'fixed';
                ta.style.opacity = '0';
                document.body.appendChild(ta);
                ta.focus();
                ta.select();
                document.execCommand('copy');
                document.body.removeChild(ta);
                var btn = document.getElementById('copy-btn');
                btn.innerText = 'Copied!';
                setTimeout(function() {{ btn.innerText = 'Copy to Clipboard'; }}, 2000);
            " style="cursor:pointer;padding:8px 16px;background:#4CAF50;color:white;
                     border:none;border-radius:4px;font-size:14px;">
                Copy to Clipboard
            </button>
            """,
            height=50,
        )

if __name__ == '__main__':
    main()