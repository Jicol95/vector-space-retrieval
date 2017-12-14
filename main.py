from vector_Space_Model import vector_space_model
from document import document

if __name__ == '__main__':
    vector_space_model = vector_space_model()
    while (True):
        option = input("\nWhat would you like to do?\n\n1:Build a search query\n2:Quit\n\n")
        if option == 1:
            search_terms = input("Enter your search query")
            query_document = document("query", search_terms)
            vector_space_model.documents.append(query_document)
            vector_space_model.build_documents()
            vector_space_model.document_length()
            vector_space_model.cosine_similarity()
            print(vector_space_model.document_return.text)
        elif option == 2:
            break
        else:
            continue
