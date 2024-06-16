from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Path to your saved model directory
model_directory = './results'

# Load the trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained(model_directory)
model = GPT2LMHeadModel.from_pretrained(model_directory)

def generate_text(prompt):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

# Example usage
prompt = "Extract information about a specific topic: "
generated_text = generate_text(prompt)
print(generated_text)
