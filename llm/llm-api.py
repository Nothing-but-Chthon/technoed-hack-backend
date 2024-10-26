from fastapi import FastAPI
import uvicorn
from transformers import AutoTokenizer, AutoModelForCausalLM


model_name = "ai-forever/mGPT"
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir='tokenizer', local_files_only=False)
model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir='model', local_files_only=False)

app = FastAPI()

@app.post("/predict")
def predict(request: dict):
    setup = ("Получив список отзывов студентов об академическом курсе, напишите краткое, "
              "деперсонализированное резюме, в котором объективно выделите основные темы и моменты отзывов. "
              "Сосредоточьтесь на повторяющихся сильных сторонах, областях, требующих улучшения, и общих "
              "тенденциях в мнениях студентов, не приписывая высказывания отдельным рецензентам и не используя "
              "личные местоимения. Убедитесь, что резюме нейтрально, информативно и избегает субъективных "
              "формулировок. Ключевые аспекты, которые следует осветить, включают эффективность преподавания, "
              "качество содержания курса, рабочую нагрузку, практическое применение, а также любые общие отзывы "
              "об организации курса или ресурсах. Список отзывов:"
    )

    for i, review in enumerate(request["reviews"], start=1):
        setup += f"\n{i}. {review['text']}"

    input_ids = tokenizer.encode(setup, return_tensors="pt")

    generated_ids = model.generate(input_ids, max_length=len(setup)+500, num_return_sequences=1, no_repeat_ngram_size=2)
    res = tokenizer.decode(generated_ids[0], skip_special_tokens=True)[len(setup)+3:]
    return {"result": res}


if __name__ == "__main__":
    uvicorn.run("llm-api:app", port=8000, host='0.0.0.0')