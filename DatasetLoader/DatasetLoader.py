import json
import os

def load_dataset(dataset_base_path, filename):

    article_links = []
    article_headlines = []
    article_ground_truths = []

    with open(os.path.join(dataset_base_path, filename), "r") as file:
        # Each line contains a unique JSON object
        lines = file.readlines()
        for line in lines:
            parsed_obj = json.loads(line)
            article_links.append(parsed_obj["article_link"])
            article_headlines.append(parsed_obj["headline"])
            article_ground_truths.append(parsed_obj["is_sarcastic"])

    return (article_links, article_headlines, article_ground_truths)


