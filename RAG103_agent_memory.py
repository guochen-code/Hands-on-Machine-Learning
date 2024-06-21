# it has memory
from openai import OpenAI
import streamlit as st
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.agents import initialize_agent
from langchain.agents import Tool


PINECONE_API = '<>'
OPENAI_API = '<>'

# initialize embedding model
model_name = 'text-embedding-ada-002'
embed = OpenAIEmbeddings(model=model_name,openai_api_key=OPENAI_API)

# initialize vectorstore
text_field = 'text'
index_name = 'test101'
vectorstore = PineconeVectorStore(index_name= index_name, embedding = embed, pinecone_api_key = PINECONE_API,text_key=text_field)

# initialize llm
llm = ChatOpenAI(openai_api_key=OPENAI_API,model_name="gpt-3.5-turbo", temperature=0.0) #,streaming=True,callbacks=[StreamingStdOutCallbackHandler()]

# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
conversational_memory = ConversationBufferWindowMemory(memory_key='chat_history',k=5,return_messages=True)

# conversational_memory.chat_memory.add_message('test-test-test')

# initialize QA chain
qa = RetrievalQA.from_chain_type(llm=llm,chain_type="stuff",retriever=vectorstore.as_retriever())

tools = [Tool(name='Knowledge Base',
              func=qa.invoke,
              description=('use this tool when answering general questions to get more information about the topic'))]


agent = initialize_agent(agent='chat-conversational-react-description',
                         tools=tools,
                         llm=llm,
                         verbose=False,
                         max_iterations=3,
                         early_stopping_method='generate',
                         memory = conversational_memory)

# print(agent("hi, how are you? my name is jack"))
# print(agent("what is my name?"))

# qa = ConversationalRetrievalChain.from_llm(
#     llm=llm,
#     retriever=vectorstore.as_retriever(),
#     chain_type="stuff",
#     memory=memory,
# )

# query = "my name is jack"
# # result = qa.invoke(query)['result']
# result = qa.invoke(query)
#
# print(result)
#
#
# query = "what is my name?"
# # result = qa.invoke(query)['result']
# result = qa.invoke(query)
#
# print(result)

#
# # Streamlit application setup
# st.title("ChatGPT-like clone")
#
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#
# # Chat interface
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.text(message["content"])
#
# # Input from the user
# user_input = st.text_input("You:", "")
#
# if st.button("Send"):
#     st.session_state.messages.append({"role": "user", "content": user_input})
#
#     # Get response from the model
#     response = qa.invoke(user_input)['result']
#
#     st.session_state.messages.append({"role": "assistant", "content": response})
#
#
#
#




st.title("Drilling Assistant")

client = OpenAI(api_key='<>')

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
#
# if prompt := st.chat_input("what is up?"):
#     print('debug001......')
#     st.session_state.messages.append({"role":"user","content":prompt})
#     print('debug002......')
#
#     with st.chat_message("user"):
#         print('debug003......')
#
#         st.markdown(prompt)
#
#     with st.chat_message("assistant"):
#         print('debug004......')
#
#         # stream = client.chat.completions.create(
#         #     model = st.session_state["openai_model"],
#         #     messages = [
#         #         {"role": m["role"], "content": m["content"]}
#         #         for m in st.session_state.messages
#         #     ],
#         #     stream = True,
#         # )
#         print('>>>',type(prompt), prompt)
#         result = qa.invoke(prompt)['result']
#         # print('response:',response)
#
#         # response = st.write_stream(stream)
#         response = st.write(result)
#
#
#     st.session_state.messages.append({"role":"assistant","content":response})
#     print('append...........')
#


if prompt := st.chat_input("You:"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner('Thinking...'):
        last_five = st.session_state.messages[-5:]
        print('last_five:',last_five)
        conversational_memory.chat_memory.add_message(str(last_five))
        result = agent(prompt)
        print('result:',result)
        response = result['output']

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.write(response)
