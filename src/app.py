import re

mensagem = "Atenção: estamos doando 35 lt de leite fresco que vence em 2 dias!"

# Número (inteiro ou decimal com . ou ,) + unidade
padrao_qtd = r'(\d+(?:[.,]\d+)?)\s*(kg|quilos?|g|lt|l|litros?|caixas?|unidades?)\b'

# "vence/vencem/validade em N dia(s)"
padrao_dias = r'(?:venc\w*|validade)\s+(?:em\s+)?(\d+)\s*dias?'

# Alimento: a palavra que vem logo depois de "<qtd> <unidade> de"
padrao_alimento = padrao_qtd + r'\s+de\s+(\w+)'

# --- Extração ---
m_qtd = re.search(padrao_qtd, mensagem, re.IGNORECASE)
m_dias = re.search(padrao_dias, mensagem, re.IGNORECASE)
m_ali = re.search(padrao_alimento, mensagem, re.IGNORECASE)

quantidade = float(m_qtd.group(1).replace(',', '.')) if m_qtd else 1.0
unidade = m_qtd.group(2).lower() if m_qtd else "un"
alimento = m_ali.group(3).capitalize() if m_ali else "Não identificado"
dias = int(m_dias.group(1)) if m_dias else None

# --- Urgência (perecibilidade) ---
if dias is None:
    urgencia = "NÃO INFORMADA"
elif dias <= 3:
    urgencia = f"ALTA (Vence em {dias} dias)"
elif dias <= 7:
    urgencia = f"MÉDIA (Vence em {dias} dias)"
else:
    urgencia = f"BAIXA (Vence em {dias} dias)"

print(f"Alimento: {alimento} | Quantidade: {quantidade} {unidade} | Urgência: {urgencia}")
