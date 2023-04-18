import json

def parse_response(query_response, model = None):
    # Depending on the LLM, we may have to write a different parsing script
    model_predictions = json.loads(query_response["Body"].read())
    generated_text = model_predictions["generated_text"]
    return generated_text


def parse_response_multiple_texts(query_response):
    model_predictions = json.loads(query_response["Body"].read())
    generated_text = model_predictions["generated_texts"]
    return generated_text