import http.client, urllib.request, urllib.parse, urllib.error

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '05fab847904c416d8a4f62c412c0024c',
}


def get_tournaments():
    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/golf/v2/json/Tournaments?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def get_leaderboard(format):
    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/golf/v2/"+format+"/Leaderboard/304?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data);
        conn.close()
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))