import streamlit as st
import app as pp

# Entorno basico: fondo y título.
st.set_page_config(page_title = 'Asistente emocional', page_icon = '🤖')
st.title('ChatBot emocional')
st.write('Habla con el ChatBot sobre como te sientes')

# Inicializa el historial
if 'messages' not in st.session_state :
    st.session_state.messages = [{'role': 'chatbot', 'content': '¡Hola! soy un chat emocional. ¿Cómo te encuentras hoy?'}]

# Imprime el mensaje predeterminado del bot al iniciar el chat.
for message in st.session_state.messages :
    with st.chat_message(message['role']) :
        st.markdown(message['content'])

# Barra de input.
user_input = st.chat_input('¡Bienvenido al asistente emocional! Escribe "chao" para terminar.')

# Se ejecuta después de cada input del usuario, que almacena en el historial y lo muestra
# junto a una llamada a la IA, de cuya respuesta almacena.

if user_input :
    st.session_state.messages.append({'role': 'user', 'content': user_input})
    with st.chat_message('user') :
        st.markdown(user_input)

    with st.chat_message("ChatBot"):
        response = pp.conver(user_input)

        bot_reply = response
        st.markdown(bot_reply)

#Guarda la respuesta de la IA en el historial.
st.session_state.messages.append({"role": "ChatBot", "content": bot_reply})