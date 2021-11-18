import requests


thingin_api_url = "https://coreapi.di.thinginthefuture.com/"
value_property = "valeur"


def post_initial_data(data, access_token):
    return requests.post(thingin_api_url+"batch/avatars", json=data,
      headers={'Content-Type':'application/json',
               'Authorization': '{}'.format(access_token)})


def put_motion_event_thingin(uuid, iri, motion_data, access_token):
    put_motion_event_payload = {
        #saref_value_iri:motion_data, todo : complete be extracting relevant motion value
        "_iri": iri
    }
    print("## Trying to update node : "+uuid)
    return requests.put(thingin_api_url+"avatars/update/set/"+uuid, json=put_motion_event_payload,
      headers={'Content-Type':'application/json',
               'Authorization': '{}'.format(access_token)})


def put_luminance_thingin(uuid, iri, luminance_data, access_token):
    put_luminance_payload = {
        value_property: luminance_data['data'][0][1][0],
        "_iri": iri
    }
    print("## Trying to update node : " + uuid+ " with value : "+str(luminance_data['data'][0][1][0]))
    return requests.put(thingin_api_url+"avatars/update/set/"+uuid, json=put_luminance_payload,
      headers={'Content-Type':'application/json',
               'Authorization': '{}'.format(access_token)})



