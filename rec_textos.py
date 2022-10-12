#Enzo Bloss Stival
"""Sua  tarefa  será  transformar  um  conjunto  de  5  sites,  sobre  o  tema  de  processamento  de 
linguagem natural em um conjunto de cinco listas distintas de sentenças. Ou seja, você fará uma função 
que, usando a biblioteca Beautifull Soap, faça a requisição de uma url, e extrai todas as sentenças desta 
url. Duas condições são importantes:  
a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que 
1000 palavras.  
b) O texto desta página deverá ser transformado em um array de senteças.  
 
Para separar as sentenças você pode usar os sinais de pontuação ou as funções da biblioteca 
Spacy. 
"""
from bs4 import BeautifulSoup
import requests
import re

sentencas = []
urls = ["https://www.ibm.com/cloud/learn/natural-language-processing", "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP", "https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/", "https://hbr.org/2022/04/the-power-of-natural-language-processing", "https://machinelearningmastery.com/natural-language-processing/"]
for link in urls:
    url = requests.get(link).content
    html = BeautifulSoup(url, "html.parser")
    for data in html(['style', 'script']):
        data.decompose()
    html = ' '.join(html.stripped_strings)
    html = re.sub("[\n\t]", "", html)
    html = re.split("[.!:?;]", html)
    sentencas.append(html)
print(sentencas)
