import cv2
import time

def calcular_velocidade(distancia, tempo_segundos):
    if tempo_segundos > 0:
        velocidade = distancia / tempo_segundos
        return velocidade
    else:
        return 0

def main():
    distancia_pixels = 0
    tempo_inicial = time.time()
    
    captura_de_video = cv2.VideoCapture(0)  
    
    if not captura_de_video.isOpened():
        print("Não foi possível abrir a webcam.")
        return
    
    referencia = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    referencia = cv2.GaussianBlur(referencia, (21, 21), 0)
    
    try:
        while True:
            ret, frame = captura_de_video.read()
    
            if not ret:
                print("Não foi possível receber frames da webcam.")
                break
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (9, 9), 0)
            delta_frame = cv2.absdiff(referencia, gray)
            _, thresh_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)
            thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
            contours, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if contours:
                maior_contorno = max(contours, key=cv2.contourArea)
                if cv2.contourArea(maior_contorno) >= 500:  
                    (x, y, w, h) = cv2.boundingRect(maior_contorno)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    distancia_pixels += w
    
            tempo_atual = time.time()
            tempo_decorrido = tempo_atual - tempo_inicial
            
            velocidade_cms = calcular_velocidade(distancia_pixels, tempo_decorrido)
            velocidade_kmh = velocidade_cms * 0.036  # Converter cm/s para km/h
            
            # Mostrar a velocidade no console
            print(f'Velocidade: {velocidade_kmh:.2f} km/h')
            
            # Atualizar o frame de referência periodicamente
            if tempo_decorrido > 1:  # Atualizar a cada segundo
                referencia = gray
                tempo_inicial = time.time()
                distancia_pixels = 0
    
            cv2.imshow('Detecção de Movimento e Velocidade', frame)
    
    finally:
        captura_de_video.release()
        cv2.destroyAllWindows()

# Função principal para executar o programa
if __name__ == "__main__":
    main()
