from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def load_dataset_from_text(file_path):
    # Load dataset with a specific encoding, handling potential decoding errors
    dataset = load_dataset('text', data_files={'train': file_path}, split='train')
    return dataset

def main():
    # Load pre-trained model and tokenizer
    model_name = 'gpt2'
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Set pad token to eos token
    tokenizer.pad_token = tokenizer.eos_token

    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Extract text from PDF
    pdf_path = 'Internship Guide.pdf'
    pdf_text = extract_text_from_pdf(pdf_path)

    # Save the extracted text to 'extracted_text.txt'
    with open('extracted_text.txt', 'w', encoding='utf-8') as file:
        file.write(pdf_text)

    # Load your dataset from 'extracted_text.txt'
    train_file_path = 'extracted_text.txt'
    train_dataset = load_dataset_from_text(train_file_path)

    # Tokenize the dataset
    def tokenize_function(examples):
        return tokenizer(examples['text'], truncation=True, padding='max_length', max_length=128)

    tokenized_train_dataset = train_dataset.map(tokenize_function, batched=True, num_proc=4,
                                                remove_columns=["text"])  # Use multiple processors if available

    # Data collator for language modeling
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,
    )

    # Training arguments
    training_args = TrainingArguments(
        output_dir='./results',
        overwrite_output_dir=True,
        num_train_epochs=1,
        per_device_train_batch_size=2,  # Smaller batch size for CPU training
        save_steps=10_000,
        save_total_limit=2,
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=tokenized_train_dataset,
    )

    # Train the model
    trainer.train()

if __name__ == "__main__":
    main()
