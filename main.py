import twitter
import random
from credentials import *
from friendly_train.main import LanguageGenerator3000


def execute():
  api = twitter.Api(consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET,
                    access_token_key=ACCESS_TOKEN_KEY,
                    access_token_secret=ACCESS_TOKEN_SECRET)

  trend = random.choice(api.GetTrendsWoeid(23424829))

  status = ''
  while len(status) > 140 or status == '':
    status = LanguageGenerator3000(sample_size=1).generate_sentence_list(10, True, random_sentence_structure=True)[0]['sentence']
    status = status.replace(random.choice(status.split(" ")), '#' + trend.name, 1)

  status = api.PostUpdate(status)
  print(status.text)


if __name__ == '__main__':
  execute()
