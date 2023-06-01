import json

body = {"name": "Hawkeye124",
        "universe": "Marvel Universe123",
        "education": "High school",
        "weight": 104,
        "height": 1.90,
        "identity": "Publicly known"}

headers = {'Content-type': 'application/json'}
test_data = json.dumps(body)

body_put = {"name": "Hawkeye124",
            "universe": "Hollywood Universe",
            "education": "High School (unfinished)",
            "weight": 110,
            "height": 1.90,
            "identity": "Publicly unknown"}

test_data_put = json.dumps(body_put)

body_expected_post = {'result':
                       {'education': 'High school',
                        'height': 1.9,
                        'identity': 'Publicly known',
                        'name': 'Hawkeye124',
                        'universe': 'Marvel Universe123',
                        'weight': 104.0}
               }