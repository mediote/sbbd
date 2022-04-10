[![PyPI - Python](https://img.shields.io/badge/python-v3.6+-blue.svg)](https://pypi.org/project/bertopic/)
[![BERTopic](https://img.shields.io/badge/BERtopic-v0.9%20-brightgreen)](https://github.com/MaartenGr/BERTopic)
[![PyPI - License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/mediote/twAnalytics/blob/main/LICENSE)
[![Lattes](https://img.shields.io/badge/Lattes-CNPq-blueviolet)](http://lattes.cnpq.br/2455024624300452)
[![SBBD](https://img.shields.io/badge/SBBD-2022-green)](https://sbbd.org.br/2022/)

## Colab 

| Code, Tools and Apps  | Link  |
|---|---|
| Crawling on Twitter API, text pre-processing and Topic modeling with BERTopic  | [![Open on Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mediote/sbbd/blob/main/sbbd.ipynb)  |
| Utils  | [![Open on Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mediote/sbbd/blob/main/utils.ipynb)  |
| Streamlit App for data Crawling on Twitter API  | [![Open on Colab](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/mediote/sbbd/main/app.py)  |



## Entendimento do negócio e dados

### RQ1: Como os posicionamentos sobre a campanha de vacinação nos EUA evoluem com o tempo?
### RQ2: Quais os principais argumentos usados para defender cada posicionamento?
### RQ3: Como os argumentos evoluem com o decorrer da vacinação?

## Coleta e pré-processamento

### 1: Pesquisei por TERMOS vacina e vacinação no periodo usando geolocalização ( OMS definiu status de pandemia até ontem - 11/03/2020 até 06/04/2022).
### 2: Extrai as hashtags que claramente indicam o alvo.
### 3: Coleta individual para cada hashtag.


# Pré=processamento

#Pro-vaxxers
    #getvaccinated - 1075
    #vaccineswork - 874
    #vaccinessavelives - 757
#Anti-vaxxers
    #novaccine - 37
    #novaccineforme - 32
    #novaccinepassports - 26
