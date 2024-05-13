import streamlit as st

def main():
    # a simple title
    st.title("Hello World!")

    # a simple text
    st.text("This is a simple text.")

    # a simple markdown
    st.markdown("### This is a simple markdown.")

    # a simple button
    st.button("Simple Button")

if __name__ == "__main__":
    main()