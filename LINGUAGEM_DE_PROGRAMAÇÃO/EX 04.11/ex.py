notaAna1 = 8.5
notaAna2 = 7.0
notaAna3 = 9.0
statusAna = "Reprovado"

notaDaniel1 = 4.0
notaDaniel2 = 5.5
notaDaniel3 = 6.0
statusDaniel = "Reprovado"

notaJonatas1 = 3.0
notaJonatas2 = 2.5
notaJonatas3 = 4.0
statusJonatas = "Reprovado"

notaMaria1 = 9.0

notaMaria2 = 8.5
notaMaria3 = 10.0
statusMaria = "Reprovado"

mediaAna = (notaAna1 + notaAna2 + notaAna3*2)/4
mediaDani = (notaDaniel1 + notaDaniel2 + notaDaniel3*2) /4
mediaJonatas = (notaJonatas1 + notaJonatas2 + notaJonatas3*2)/4
mediaMaria = (notaMaria1+notaMaria2+notaMaria3*2) / 4

if mediaAna > 7:
    statusAna = "Aprovado, O diretor Raphael Amorim lhe deseja parabéns"
elif mediaAna<7 and mediaAna>5:
    statusAna = "Recuperação"
else:
    statusAna = "Reprovado"

if mediaDani > 7:
    statusDaniel = "Aprovado, O diretor Raphael Amorim lhe deseja parabéns"
elif mediaDani<7 and mediaDani>5:
    statusDaniel = "Recuperação"
else:
    statusDaniel = "Reprovado"

if mediaJonatas > 7:
    statusJonatas = "Aprovado, O diretor Raphael Amorim lhe deseja parabéns"
elif mediaJonatas<7 and mediaJonatas>5:
    statusJonatas = "Recuperação"
else:
    statusJonatas = "Reprovado" 


print(f''' 
      **********************************
        ESCOLA SOUFPHIA DEI SANTI TECH
            BOLETIM ESCOLAR ANA
      **********************************
      Nota 1: {notaAna1}
      Nota 2: {notaAna2}
      Nota 3: {notaAna3}
      Media: {mediaAna:.2f}
      Status: {statusAna}   
      **********************************''')

print(f''' 
      **********************************
        ESCOLA SOUFPHIA DEI SANTI TECH
            BOLETIM ESCOLAR DANIEL
      **********************************
      Nota 1: {notaDaniel1}
      Nota 2: {notaDaniel2}
      Nota 3: {notaDaniel3}
      Media: {mediaDani:.2f}
      Status: {statusDaniel}   
      **********************************''')

print(f''' 
      **********************************
        ESCOLA SOUFPHIA DEI SANTI TECH
            BOLETIM ESCOLAR JONATAS
      **********************************
      Nota 1: {notaJonatas1}
      Nota 2: {notaJonatas2}
      Nota 3: {notaJonatas3}
      Media: {mediaJonatas:.2f}
      Status: {statusJonatas}   
      **********************************''')

print(f''' 
      **********************************
        ESCOLA SOUFPHIA DEI SANTI TECH
            BOLETIM ESCOLAR MARIA
      **********************************
      Nota 1: {notaMaria1}
      Nota 2: {notaMaria2}
      Nota 3: {notaMaria3}
      Media: {mediaMaria:.2f}
      Status: {statusMaria}   
      **********************************''')






          

