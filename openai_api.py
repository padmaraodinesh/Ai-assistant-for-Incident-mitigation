import openai

openai.api_key = "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"

def generate_mitigation(description):
    prompt = f'''
   
    Incident: Legit URL blocked
    Mitigation: check if url is legit or not -> delist the url -> perform RCA.

    Incident: Delist legit IP address
    Mitigation: check if Ip is legit or spammy -> check previous Ip traffic -> delist the IP from blocklist.

    Incident: FN mail got into user inbox
    Mitigation: Check if mail is FN or FP -> create a pattern rule to block that mail or campaign

    Incident: {description} 
    '''
    
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop='Incident',
        temperature=0.7,
        frequency_penalty=0.5,
        presence_penalty=0.5,
    )
    mitigation = response.choices[0].text.strip()
    return mitigation
