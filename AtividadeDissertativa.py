# Atividade:
# Exercício 01: O programa escutar a voz do usuário e exibir a mensagem na forma textual no console. 
# Exercício 02: O programa deve aceitar as operações de Adição de números. Por exemplo, se o usuário falar: 
# a) “Um Mais Dois”, o programa vai exibir no console: “1 + 2 = 3”.
# b) “Três Menos Dois”, o programa vai exibir no console: “3 - 2 = 1”.
# c) “Três Vezes Dois”, o programa vai exibir no console: “O algoritmo trata apenas as operações de Adição e Subtração”.
# d) “Isso é um teste”, o programa vai exibir no console: “A entrada dos dados não é válida para o algoritmo”.


import speech_recognition as sr
import os

def fExercicio01():
    os.system('cls')
    print('Exercício 01 - Captura e processamento de áudio')
    input('Ligue seu microfone, aguarde o início da captura e fale pausadamente < pressione qualquer tecla para continuar >')
    texto = fEscutar()
    print('')
    print('Transcrição do audio capturado: ' + texto)
    
def fExercicio02():
    me = ('dummy', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
    os.system('cls')
    print('Exercício 02 - Captura e processamento de áudio - Cálculo matemático simples (valores entre 1 e 999)')
    input('Exercício 02 - Ligue seu microfone, aguarde o início da captura e fale pausadamente < pressione qualquer tecla para continuar >')
    t1 = str(fEscutar()).lower()
    texto = t1.split()
    print('')
    print('Transcrição do audio capturado: ' + t1)
    print('')
    if texto[1] in ('*','vezes','/','dividido','multiplicado','x'):
        print('O algoritmo trata apenas as operações de Adição e Subtração')
    elif texto[1] not in ('+', 'mais', '-', 'menos'):
        print('A entrada dos dados não é válida para o algoritmo')
    else:    
        try:
            n1 = int(texto[0])
        except :
            n1 = me.index(texto[0])
        try:
            n2 = int(texto[2])
        except :
            n2 = me.index(texto[2])   
        if texto[1] in ('+','mais'):
            print(str(n1) + ' + ' + str(n2) + ' = ' + str(n1 + n2))
        elif texto[1] in ('-','menos'):
            print(str(n1) + ' - ' + str(n2) + ' = ' + str(n1 - n2))
        
        
    
    
def fEscutar():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Início da captura: ")
        audio = mic.listen(source)
        print("Fim da captura: ")
        try:
            frase = mic.recognize_google(audio, language='pt-BR') 
            return frase
        except sr.UnknownValueError:
            print("Não entendi")

if __name__ == '__main__':
    os.system('cls')
    while True:
        print('')
        exercicio = input('Pressione: < 1 > para Exercicio 01 - < 2 > para Exercício 02 - < 3 > para Encerrar: ')  
        if exercicio == '1':
            fExercicio01()
        elif exercicio == '2':
            fExercicio02()
        elif exercicio == '3':
            os.system('cls')
            break
    
        