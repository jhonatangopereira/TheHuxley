TRAFICO = "tráfico"
ROUBO = "roubo"
HOMICIDIO = "homicídio"
DELACAO_CONCEDIDA = "Delação concedida."
DELACAO_REJEITADA = "Delação rejeitada."
CRIME_INVALIDO = "Crime inválido."
crime_delator = input()
if crime_delator == ROUBO or crime_delator == TRAFICO or crime_delator == HOMICIDIO:
  if crime_delator == ROUBO or crime_delator == TRAFICO:
    valor_crime_delator = int(input())
  
  crime_delatado = input()
  if crime_delatado == ROUBO or crime_delatado == TRAFICO or crime_delatado == HOMICIDIO:
    if crime_delatado == ROUBO or crime_delatado == TRAFICO:
      valor_crime_delatado = int(input())

    if (crime_delator == ROUBO or crime_delator == TRAFICO) and crime_delatado == HOMICIDIO:
      saida = DELACAO_CONCEDIDA
    elif crime_delator == crime_delatado:
      if ((crime_delator == ROUBO or crime_delator == TRAFICO) and valor_crime_delatado > 5 * valor_crime_delator) or crime_delator == HOMICIDIO:
        saida = DELACAO_CONCEDIDA
      else:
        saida = DELACAO_REJEITADA
    elif crime_delator == ROUBO and crime_delatado == TRAFICO:
      if valor_crime_delatado > 3 * valor_crime_delator:
        saida = DELACAO_CONCEDIDA
      else:
        saida = DELACAO_REJEITADA
    else:
      saida = DELACAO_REJEITADA
  else:
    saida = CRIME_INVALIDO
else:
  saida = CRIME_INVALIDO

print(saida)
