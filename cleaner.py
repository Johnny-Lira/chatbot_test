import re

def remove_chat_metadata(chat_export_file):
    initial_message = r"(\d+\/\d+\/\d+\s\d+:\d+\s-\s(As mensagens e as ligações são protegidas com a criptografia de ponta a ponta e ficam somente entre você e os participantes desta conversa. Nem mesmo o WhatsApp pode lê-las ou ouvi-las. Toque para saber mais.))"
    date_time = r"(\d+\/\d+\/\d+\s\d+:\d+)"  # e.g. "9/16/22, 06:34"
    dash_whitespace = r"\s-\s"  # " - "
    username = r"([\w\s]+)"  # e.g. "Martin"
    metadata_end = r":\s"  # ": "
    pattern = date_time + dash_whitespace + username + metadata_end

    with open(chat_export_file, "r") as corpus_file:
        content = corpus_file.read()
    
    cleaned_initial = re.sub(initial_message, "", content) 
    cleaned_corpus = re.sub(pattern, "", cleaned_initial)

    return tuple(cleaned_corpus.split("\n"))

def remove_non_message_text(export_text_lines):
    messages = export_text_lines[1:-1]

    filter_out_msgs = ("<Media omitted>",)
    return tuple((msg for msg in messages if msg not in filter_out_msgs))

def clean_corpus(chat_export_file):
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus
