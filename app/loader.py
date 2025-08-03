import os

#load all .md files from data folder
def load_documents(data_dir: str = "data") -> list[tuple[str, str]]:
    documents = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".md"):
            path = os.path.join(data_dir, filename)
            with open(path, "r", encoding="utf-8") as f:
                documents.append((filename, f.read()))
    return documents
