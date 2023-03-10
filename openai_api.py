import openai

openai.api_key = "key"

def generate_mitigation(description):
    prompt = f'''
   
    Incident: Legit URL blocked
    Mitigation: check if url is legit or not -> delist the url -> perform RCA.

    Incident: Network latency
    Mitigation: Increased the bandwidth between the data centers and optimized the routing tables.

    Incident: Database corruption
    Mitigation: Restored the latest database backup and ran the database repair scripts to recover the data.

    Incident: {description} 
    '''
    
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop='incident',
        temperature=1,
        frequency_penalty=0.5,
        presence_penalty=0,
    )
    mitigation = response.choices[0].text.strip()
    return mitigation
