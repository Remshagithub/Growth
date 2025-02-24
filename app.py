import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="🧠")

st.title("🌟 Growth Mindset Challenge: Day 1")
st.header("👋 Welcome to the Growth Mindset Challenge! Today is Day 1. Let's get started!")

st.write("Today's challenge is to write down *3 things* you are grateful for. This can be anything—from the people in your life, to the food you eat, to the air you breathe. 🌸\n\nTake a moment to reflect on the things that bring you joy and write them down below. ✨")

# Quote section
st.header("💡 Today's Growth Mindset Quote:")
st.write("Success is not final, failure is not fatal: It is the courage to continue that counts. – *Winston Churchill*")

# User Challenge
st.header("🚀 What is your challenge for today?")
user_input = st.text_area("💭 Describe the challenge you're facing today:")

if user_input:
    st.success(f"💪 You're facing: *{user_input}*. Keep pushing toward your goal! 🌟")
else:
    st.warning("⚠ Tell us about your challenge to get started!")

# Reflection
st.header("📝 Reflect on Your Learning")
reflection = st.text_area("📖 Write your reflection here:")

if reflection:
    st.success(f"⭐⭐⭐ Great insight! Your reflection: *{reflection}*")
else:
    st.info("💡 Reflection on past experiences helps you grow! Share your thoughts with us.")

# Achievement
st.header("🥳 Celebrate Your Wins!")
achievement = st.text_input("🏆 Share something you've recently accomplished:")

if achievement:
    st.success(f"🎉 Congratulations on your achievement: *{achievement}*")
else:
    st.info("🌟 Big or small, every achievement counts! Share one with us.")

# Footer
st.write("---")
st.write("🌱 Keep believing in yourself. Growth is a journey, not a destination.")
st.write("Created with ❤ by Rimsha")