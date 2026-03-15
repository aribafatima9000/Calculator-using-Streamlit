import streamlit as st

st.title("Simple Calculator")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

operation = st.selectbox("Operation", ["Add","Subtract","Multiply","Divide"])

if st.button("Calculate"):
    
    if operation == "Add":
        result = a + b
        
    elif operation == "Subtract":
        result = a - b
        
    elif operation == "Multiply":
        result = a * b
        
    else:
        result = a / b

    st.write("Result:", result)