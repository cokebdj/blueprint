# from mock import patch
from ml_api.app import  healthcheck
import json

def test_healthcheck_endpoint():
    _, status_code = healthcheck()
    assert status_code == 200

def test_correct_endpoint(client,input_dict):
    response = client.post('/transform',data=json.dumps(input_dict))
    assert response.status_code == 200

# patch("",class).start()
# patch.stopall()