newline, bold, unbold = "\n", "\033[1m", "\033[0m"

def parse_response(query_response, model = None)
# Depending on the LLM, we may have to write a different parsing script
    model_predictions = json.loads(query_response["Body"].read())
    generated_text = model_predictions["generated_text"]
    return generated_text