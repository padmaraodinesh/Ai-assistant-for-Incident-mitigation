import openai

openai.api_key = "api_key"

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
