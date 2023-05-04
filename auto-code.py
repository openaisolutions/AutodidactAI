import requests
import subprocess
import tempfile

# Define the OpenAI API key (replace with actual value)
API_KEY = 'your_key_here'

#Function to get the list of available models
def get_models():
    try:
        # Call the OpenAI API to get the list of models
        response = openai.Model.list()
        
        # Print the list of models
        for model in response['data']:
            print(model['id'])
    
    except Exception as e:
        print(f"Error: {e}")

# Call the function to get the list of models
get_models()
def generate_code(prompt):
    # Define the OpenAI API endpoint
    api_endpoint = 'https://api.openai.com/v1/engines/davinci-codex/completions'

    # Define the headers for the API request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    # Define the data for the API request (customize the prompt and other parameters)
    data = {
        'prompt': prompt,
        'max_tokens': 100
    }

    # Make the API request and get the response
    response = requests.post(api_endpoint, json=data, headers=headers)
    response_json = response.json()

    # Check if the response contains an error message
    if 'error' in response_json:
        raise Exception(response_json['error'])

    # Check if the response contains the expected 'choices' key
    if 'choices' not in response_json:
        raise Exception('Unexpected response format from the OpenAI API.')

    # Extract the generated code from the response
    code = response_json['choices'][0]['text']
    return code.strip()

def run_code(code):
    # Create a temporary Python script file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
        # Write the generated code to the temporary file
        temp_file.write(code)
        temp_file.flush()

        # Run the temporary Python script and capture the output and errors
        try:
            output = subprocess.check_output(['python', temp_file.name], stderr=subprocess.STDOUT)
            return output.decode('utf-8'), None
        except subprocess.CalledProcessError as e:
            return None, e.output.decode('utf-8')

def main():
    # Define the initial prompt for code generation
    prompt = 'Generate Python code to do the following task: ...'

    while True:
        # Generate code using the OpenAI API
        code = generate_code(prompt)
        print('Generated code:')
        print(code)

        # Run the generated code
        output, error = run_code(code)

        # Check if there are errors
        if error:
            print('Error:', error)
            # Update the prompt to include the error message for the next code generation
            prompt = f'The previous code generated an error: {error}\nPlease generate a corrected Python code for the task: ...'
        else:
            print('Output:', output)
            break

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print('Error:', err)
