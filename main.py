import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")
st.title("Password Strength Meter 🔒")

st.markdown("""  
Enter a password to check its strength.

### **Strength Criteria:**  
- **Weak 🔴:** Short & easy to guess ❌  
- **Moderate 🟡:** Better but still predictable ⚠️  
- **Strong 🟢:** Long & complex ✅  

Try different passwords and see the result!
""")
password = st.text_input("Enter a password", type="password")

feedback = []
score = 0

if password:
    if len(password)>=8:
        feedback.append("✅ Long enough")
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")
    
    if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password):
        feedback.append("✅ Contains uppercase and lowercase letters")
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters")
    
    if re.search(r'\d',password):
        score += 1
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Password should contain numbers")
    
    if re.search(r'[^\w\s]', password):
        score += 1
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Password should contain special characters (!@#$%^&*)")
    
    if score == 4:
        feedback.append("🎉 Your Password is **Super Strong!** 💪 No one’s cracking this! 🟢")
    elif score == 3:
        feedback.append("😎 Your Password is **Moderate!** 🟡 Almost there, add more spice!")
    else:
        feedback.append("😬 Oops! Your Password is **Weak** 🔴 Add some muscles to it!")

    if feedback:
        st.markdown("### Password Analysis:")
        for item in feedback:
            st.markdown(item)
else:
    st.info("Please enter a password to check its strength.")

st.markdown(
    """
    <style>
        footer {visibility: hidden;}
        .viewerBadge_container__1QSob {display: none !important;}
    </style>
    """,
    unsafe_allow_html=True
)

        
        
        
        
        