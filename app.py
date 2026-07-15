import streamlit as st
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
        st.download_button(
            label='Download Blog as Markdown',
            data=st.session_state['blog_content'],
            file_name='blog.md',
            mime='text/markdown',
        )

if __name__ == '__main__':
    main()