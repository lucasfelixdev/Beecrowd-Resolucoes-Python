positivo = 0                                # Armazena qntd de positivos
for y in range(6):                          # Para cada item até 6
    a = float(input())                      # Lê valor flutuante
    if a > 0:                               # a sendo maior que 0
        positivo += 1                       # Positivo recebe maior
print(f"{positivo} valores positivos")      # Exibe mensagem apos for ser concluído
