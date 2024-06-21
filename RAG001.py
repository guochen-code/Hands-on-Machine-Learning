######### single PDF file
def process_pdf(file_path):
    # create a loader
    loader = PyPDFLoader(file_path)
    # load your data
    data = loader.load()
    # Split your data up into smaller documents with Chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    documents = text_splitter.split_documents(data)
    return documents

type(documents) -> list

documents[0] ->
Document(page_content='1 \n A Case Study on the Classification of Lost Circulation Events During Drilling using \nMachine Learning Techniques on an Imbalanced Large Dataset  
\nToluwalase A. Olukoga1, Yin Feng2 \n University of Louisiana at Lafayette  \nAbstract  \nIn this study, we present machine learning classification models that  
forecast and categorize lost \ncirculation severity preemptively using a large class imbalanced drilling dataset with good', 
metadata={'source': './pinecone101/Loss of circulation_classifier.pdf', 'page': 0})

############## directory loader
from langchain.document_loaders import DirectoryLoader

directory = './pinecone101'

def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents

documents = load_docs(directory)
len(documents)

from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_docs(documents,chunk_size=500,chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

docs = split_docs(documents)
print(len(docs))

docs[0] ->
Document(page_content='A Case Study on the Classification of Lost Circulation Events During Drilling using Machine Learning Techniques on an Imbalanced Large Dataset\n\nToluwalase A. 
Olukoga1, Yin Feng2\n\nUniversity of Louisiana at Lafayette\n\nAbstract', metadata={'source': 'pinecone101\\Loss of circulation_classifier.pdf'})



##############

from langchain.embeddings.openai import OpenAIEmbeddings

# get openai api key from platform.openai.com
OPENAI_API_KEY = '<>'
model_name = 'text-embedding-ada-002'

embed = OpenAIEmbeddings(
    model=model_name,
    openai_api_key=OPENAI_API_KEY
)

emb_vectors = embed.embed_documents(docs) # docs has to be a list
ids=[str(i) for i in range(0,111)]
meta_data = [{"text": i} for i in docs]
to_upsert = zip(ids, emb_vectors, meta_data)  
index.upsert(vectors=to_upsert)


################
pinecone = Pinecone(api_key=PINECONE_API_KEY)

# Define the index name
index_name = "pdf101"

# Create the index if it doesn't exist
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=1536,spec=ServerlessSpec(cloud='aws', region='us-east-1') )

# Instantiate the index
index = pinecone.Index(index_name)


################# utility
# Define a function to preprocess text
def preprocess_text(text):
    # Replace consecutive spaces, newlines and tabs
    text = re.sub(r'\s+', ' ', text)
    return text
