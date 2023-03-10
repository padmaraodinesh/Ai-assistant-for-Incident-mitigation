import openai

openai.api_key = "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"

def generate_mitigation(description):
    prompt = f"give action plan to mitigate this security incident : {description}, in 200 words."
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )
    mitigation = response.choices[0].text.strip()
    return mitigation