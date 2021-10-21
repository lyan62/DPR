# -*-coding:utf-8-*-
import codecs
import json
import argparse
import os.path
from tqdm import tqdm


def load_data(file_name):
    with codecs.open(file_name, 'r', 'utf-8') as data_file:
        data = json.loads(data_file.read())
    return data

def build_ctx_meta(k, evidence):
    # build context meta fields to match with nq data
    ctx_meta = {
        "title": "",
        "text": evidence,
        "score": 100,
        "title_score": 0,
        "passage_id": k
    }

    return ctx_meta

def reformat(item):
    positive_ctxs = []
    negative_ctxs = []
    answers = []
    for k, v in item['evidences'].items():
        if v['answer'] != ['no_answer']:
            answers.extend(v['answer'])
            positive_ctxs.append(
                build_ctx_meta(k, v['evidence'])
            )
        else:
            negative_ctxs.append(
                build_ctx_meta(k, v['evidence'])
            )
    return {
        "dataset": "webqa",
        "question": item["question"],
        "answers": list(set(answers)),
        "positive_ctxs": positive_ctxs,
        "negative_ctxs": negative_ctxs,
        "hard_negative_ctxs": []
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type=str, dest="file_name")
    args = parser.parse_args()

    data = load_data(args.file_name)
    reformated = []
    for item in tqdm(data.values()):
        reformated.append(reformat(item))

    if not os.path.exists("reformated/"):
        os.mkdir("reformated")

    output_path = os.path.join("reformated", args.file_name.replace(".json", "_reformated.json"))
    with open(output_path, "w") as output_json:
        json.dump(reformated, output_json, indent=4, ensure_ascii=False)
    print("output path: %s" % output_path)

