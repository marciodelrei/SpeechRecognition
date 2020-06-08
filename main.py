#https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio    <<- Biblioteca PyAudio conforme Python instalado
import os
from datetime import datetime
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import clipboard

diretorio_base = os.path.dirname(os.path.realpath(__file__))
now = datetime.now().strftime("%Y%m%d_%H%M%S")

OUVIR_OQ_FOI_DITO = False
OUVIR_OQ_FOI_ENTENDIDO = True

def cria_audio_captura(audio):
    caminho_audio = os.path.join(diretorio_base, f'audios\\{now}_audio_original.wav') 
    with open(caminho_audio, "wb") as f:
        f.write(audio.get_wav_data())
    return(caminho_audio)

#Funcao responsavel por falar 
def cria_audio(texto):
    tts = gTTS(texto,lang='pt-br')

    #Salva o arquivo de audio
    caminho_texto_convertido = os.path.join(diretorio_base, f'audios\\{now}_texto_convertido.mp3')
    tts.save(caminho_texto_convertido)
    return(caminho_texto_convertido)
    

def cria_arquivo_texto(texto):
    caminho_texto = os.path.join(diretorio_base, f'audios\\{now}_texto.txt')
    with open(caminho_texto, "w") as f:
        f.write(texto)
    print(f"Texto salvo em: {caminho_texto}")
    

def set_texto_para_clipboard(texto):
    clipboard.copy(texto)
    print("Texto copiado para o clipboard.")
    print("Use CTRL+V para colar.")


#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
    
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        #Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        #Avisa ao usuario que esta pronto para ouvir
        print("Diga alguma coisa: ")
        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source)
        print("Estou coletando o que você disse...")
        caminho_audio = cria_audio_captura(audio)
        if OUVIR_OQ_FOI_DITO:
            print("Você disse:")
            playsound(caminho_audio)

    try:
        #Passa o audio para o reconhecedor de padroes do speech_recognition
        frase = microfone.recognize_google(audio,language='pt-BR')

        caminho_texto_convertido = cria_audio(frase)
        if OUVIR_OQ_FOI_ENTENDIDO:
            print("Entendi isso:")
            playsound(caminho_texto_convertido)
        #Da play ao audio
        #Após alguns segundos, retorna a frase falada
        print("Transcrito: " + frase)
        cria_arquivo_texto(frase)
        set_texto_para_clipboard(frase)
        
    #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except sr.RequestError as errRequest:
        print(str(errRequest))
    except  sr.UnknownValueError as errUnkownValueError:
        print(str(errUnkownValueError))

    return frase

frase = ouvir_microfone()
