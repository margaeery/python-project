from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import warnings
warnings.filterwarnings("ignore")

model_name = "ai-forever/rugpt3small_based_on_gpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

ai = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1
)

prompt = "Что такое Python?"

result = ai(
    prompt,
    max_new_tokens=100,
    do_sample=True,
    temperature=0.5,
    top_p=0.9,
    repetition_penalty=1.2,
    pad_token_id=tokenizer.eos_token_id
)

print(f"\nВопрос: {prompt}")
print(f"Ответ: {result[0]['generated_text']}")
