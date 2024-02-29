import requests as rq

class Wiktionary:
    __api = "https://%s.wiktionary.org/w/api.php"
    __fields = {
        'action': 'query',
        # 'titles': '',
        'format': 'json'
    }

    def __init__(self, language: str):
        self.__api = self.__api % language


    def is_exists(self, word: str) -> bool:
        if not word:
            return False
        fields = {'titles': word}
        fields.update(self.__fields)
        response = rq.get(self.__api, params=fields)
        if response.status_code != 200:
            print('Wiktionary service is not available')
            return True
        data = response.json()
        try:
            pages = data['query']['pages'].keys()
            for p in pages:
                if int(p) <= 0:
                    return False
            return True
        except ValueError:
            return False
        except KeyError:
            print('Wictionary response format mismatch')
            return False



if __name__ == '__main__':
    def test_Wiktionary():
        wikti = Wiktionary('ru')
        assert wikti.is_exists('лошадь') == True
        assert wikti.is_exists('лоладь') == False
        assert wikti.is_exists('') == False
        print('Test ok')

    test_Wiktionary()
