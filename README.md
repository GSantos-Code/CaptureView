# CaptureView

<h1>Descrição<h1>

<p>- CaptureView é uma ferramenta de captura de imagens de forma automática no aplicativo OrthoAnalyzer.<p>

<h1>Pré-Requisitos:</h1>

- Monitor 1360x768
- OrthoAnalyzer
- Python 3.9 ou Superior instalado no PC.
- PIP do Python fazer um GET na Lib PyAutoGUI.

<h1>Instruções de uso:</h1>

- Passo 1: Abrir o Setup Virtual do Paciente.
- Passo 2: Executar a Ferramenta, melhor seria criar uma tecla de atalho para a mesma.
- Passo 3: O CaptureView irá tirar as fotos conforme o usuário irá ajustando o modelo.(Siga as instruções das caixas de diálogo)
- Passo 4: Nas fotos oclusais superiores e inferiores ajuste você poderá marcar a sobreposição e o IPR.

<h1>Avisos:</h1>

- Jamais sobreponha ou mexa no PC enquanto o script é executado, siga as instruções das caixas de diálogos.
- Caso OrthoAnalyzer trave, espere até o destravamento para não prejudicar os timers entre o Ortho e o Capture. Caso contrário, apresentará mal funcionamento.
- Caso ocorra um erro de nomeação de arquivos como inversão de Upper ou Lower Case(Raramente acontece), feche e execute o Capture até a ferramenta se estabilizar.
- Ao pressionar "OK" nas caixas de diálogos, o usuário terá 4 segundos para ajustar a posição do modelo.
- Você terá 5 segundos para marcar a sobreposição e 20 segundos para marcar o IPR.

<h1>Versão:<h1>
- Versão atual: 1.0
