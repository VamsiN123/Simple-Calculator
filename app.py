import streamlit as st

st.title("Calculator Application")

number1=st.number_input("Insert a Number: ", placeholder="Enter your first number")
number2=st.number_input("Insert a Number: ", placeholder="Enter your second number")

st.write(number1,number2)

option=st.selectbox(
    "Choose the Operation",
    ("Addition","Subtraction"),
    placeholder="Select the operation"
)

if st.button("Calculate"):
    if option=="Addition":
        st.write("Sum of ",number1,number2,"is",number1+number2)
    elif option=="Subtraction":
            st.write("Difference of ",number1,number2,"is",number1-number2)
    #st.balloons()