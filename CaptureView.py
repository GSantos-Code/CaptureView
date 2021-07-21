import time, pyautogui

ortho= pyautogui.getWindowsWithTitle("OrthoAnalyzer")

ortho[0].activate()
ortho[0].maximize()

def capture(value):
    pyautogui.click(1340,636)
    pyautogui.write(value)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

def questao():
    x= pyautogui.confirm(title="Tem IPR?",text="",buttons=["SIM","NAO"])
    return x

def ajuste():
    pyautogui.alert(title="Atenção",text="Ajuste a posição")
    time.sleep(4)

pyautogui.click(1301,89)
pyautogui.click(1298,120)
time.sleep(1)
pyautogui.click(1340,169)
ajuste()
capture("Vista Oclusal Anterior")
pyautogui.click(1340,196)
ajuste()
capture("Vista Oclusal Posterior")
pyautogui.click(1340,238)
ajuste()
capture("Vista Lateral Direita 90°")
pyautogui.moveTo(450,300)
pyautogui.dragTo(366,300, button="right")
capture("Vista Lateral Direita 45°")
pyautogui.click(1340,275)
ajuste()
capture("Vista Lateral Esquerda 90°")
pyautogui.moveTo(366,300)
pyautogui.dragTo(450,300, button="right")
capture("Vista Lateral Esquerda 45°")
pyautogui.click(1340,344)
pyautogui.click(1225,120)
ajuste()
capture("Vista Oclusal Superior")
pyautogui.click(1300,225)
pyautogui.alert(title="Atenção",text="Marque os dentes da sobreposicao")
time.sleep(7)
capture("Vista Oclusal Superior com Sobreposicao")
pyautogui.click(1227,224)
pyautogui.alert(title="Atenção",text="Você tem 20 segundos a partir do Ok para marcar o IPR")
time.sleep(20)
pyautogui.click(1340,636)
q1= questao()
if q1 == "SIM":
    pyautogui.write("Vista Oclusal Superior com indicacao de IPR")
else:
    pyautogui.write("Vista Oclusal Superior sem indicacao de IPR")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.click(252,609)
pyautogui.click(34,301)
pyautogui.click(234,406)
pyautogui.click(31,338)
pyautogui.click(76,433)
pyautogui.click(1230,89)
pyautogui.click(1298,120)
pyautogui.click(1340,309)
ajuste()
capture("Vista Oclusal Inferior")
pyautogui.click(1300,225)
pyautogui.alert(title="Atenção",text="Marque os dentes da sobreposicao")
time.sleep(7)
capture("Vista Oclusal Inferior com Sobreposicao")
pyautogui.click(1227,224)
time.sleep(20)
pyautogui.click(1340,636)
q2= questao()
if q2 == "SIM":
    pyautogui.write("Vista Oclusal Inferior com indicacao de IPR")
else:
    pyautogui.write("Vista Oclusal Inferior sem indicacao de IPR")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")














