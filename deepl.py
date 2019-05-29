import requests
import time
import json
import sys

while(True):
    text = input("enter word or sentence to translate:")
    if text[0].lower() == "q":
        exit()
    url = 'https://www2.deepl.com/jsonrpc'

    data = {"jsonrpc": "2.0",
            "method": "LMT_handle_jobs",
            "params": {
                "jobs": [
                    {"kind": "default",
                     "raw_en_sentence": text,
                     "raw_en_context_before": [],
                     "raw_en_context_after":[],
                     "quality":"fast"
                     }
                ],
                "lang": {"user_preferred_langs": ["DE", "EN"],
                         "source_lang_user_selected": "auto",
                         "target_lang": "DE"
                         },
                "priority": -1,
                "timestamp": int(time.time()*1000)}
            }
    params = {}

    response = requests.post(url, params=params, json=data)

    j_content = json.loads(response.content)
    print(j_content)
    if "error" in j_content:
        print("error:", j_content["error"]["message"], file=sys.stderr)
        exit()

    translation = [j_content["result"]["translations"][i]["beams"][j]["postprocessed_sentence"]
                   for i in range(0, len(j_content["result"]["translations"]))
                   for j in range(0, len(j_content["result"]["translations"][i]["beams"]))]
    # translation = [ j_content["result"]["translations"][i]["beams"][0]["postprocessed_sentence"]for i in range(0,1)]

    print(f"Translation:{t for t in translation}")
