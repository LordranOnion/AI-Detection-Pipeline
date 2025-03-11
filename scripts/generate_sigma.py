import openai
import json

# OpenAI API configuration
# openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate Sigma rule
def generate_sigma_rule(logs):
    prompt = (
        "Based on the following logs, generate a Sigma rule to detect similar events:\n\n"
        f"{json.dumps(logs, indent=4)}"
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    sigma_rule = response.choices[0].text.strip()
    return sigma_rule

# Load logs and generate Sigma rule
with open("logs/latest_alerts.json", "r") as file:
    logs = json.load(file)
sigma_rule = generate_sigma_rule(logs)

# Save the generated Sigma rule
with open("rules/generated_rule.yml", "w") as file:
    file.write(sigma_rule)
print("Generated Sigma rule saved to rules/generated_rule.yml")
