O ecossistema do MESAFARTAI é composto por 4 grandes pilares tecnológicos desenvolvidos 100% em Python:
1.	Interface Conversacional (Front-End):
o	Chat interativo para cadastro de doações e consultas de ONGs.
o	Alternância de perfil na barra lateral ([Sou Doador | Sou ONG]).
2.	Motor de NLU & Trava de Segurança (Back-End - Scikit-Learn / Spacy):
o	Classificação de intenções (cadastrar_doacao, solicitar_alimentos, consultar_status, fora_de_escopo).
o	Mecanismo de Threshold (ex: < 0.60) com resposta de Fallback amigável quando a frase for ambígua.
3.	Extração de Entidades (Regex):
o	Captura automática de quantidades (kg, caixas, unidades), tipos de alimentos e prazos de validade (hoje, amanhã, 18h).
4.	Matchmaking Logístico & Banco de Dados (KNN + SQLite3):
o	Algoritmo KNN para calcular o match perfeito entre a oferta do doador e a ONG receptora mais próxima.
o	Banco de dados SQLite3 para persistência de doadores, receptores, doações e histórico de coletas.


Ongs vs Doadores

Passo 4: Script de Banco de Dados (src/database.py)
Criar o script Python responsável por inicializar o banco de dados relacional SQLite3 (mesafartai.db) com as tabelas fundamentais e popular com dados de teste.

