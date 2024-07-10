## Velocímetro com OpenCV

Este projeto utiliza a biblioteca OpenCV para detectar objetos em movimento e calcular sua velocidade em km/h usando uma webcam. O código detecta o objeto mais próximo da câmera, calcula a distância percorrida em pixels e converte isso em uma estimativa de velocidade.

## Funcionalidades

Acesso à webcam do dispositivo para captura de vídeo em tempo real.
Detecção de objetos em movimento utilizando a diferença entre frames consecutivos.
Cálculo da velocidade do objeto detectado e exibição em tempo real.

## Estrutura do Código

O script é dividido em várias funções para modularidade e clareza:

calcular_velocidade(distancia, tempo_segundos): Calcula a velocidade média com base na distância percorrida e no tempo decorrido. Retorna a velocidade em cm/s.

main(): Orquestra a execução do programa, gerenciando a captura de vídeo, a detecção de movimento, o cálculo de velocidade, a exibição dos gráficos na janela e o encerramento do programa.

## IMPORTANTE

Certifique-se de que a webcam não está sendo usada por outro aplicativo.
O índice da câmera (captura_de_video = cv2.VideoCapture(0)) pode precisar ser ajustado dependendo do dispositivo e da configuração do sistema. O índice '0' geralmente se refere à webcam integrada em laptops.

## CURIOSIDADE

A diferença absoluta entre frames (cv2.absdiff) e a aplicação de um filtro Gaussiano (cv2.GaussianBlur) são técnicas comuns usadas para destacar mudanças significativas entre frames consecutivos, permitindo a detecção de movimento de forma robusta.