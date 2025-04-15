import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



print("Il faut qu'il y ai deja au moins un cours pour que le script fonctionne.")

username = input("Ecrivez votre nom d'utilisateur : ")
password = input("Ecrivez votre mot de passe : ")
cours = input("Ecrivez la date de création du JT, exemple : 15.04.2025 : ")
date = input("Ecrivez le jour du cours, exemple : 20 : ")
periode = int(input("Ecrivez nombre de periode : "))
inputDo = input("Ecrivez en bref le ce que vous avez fait pendant le cours, exemple : html et css mais les bases : ")
graphic = input("Si vous voulez avoir l'interface ecrivez yes sinon mettez autres choses : ")



with open("question.txt", "w") as file:
    file.write(f"J'ai mon journal de travail a faire pour aujoudhui c'est un petit résumé sa doit faire entre 250 et 300 charactères. aujourd'hui c'est sur {inputDo}.")

subprocess.run(['bash', "script.sh"], check=True)

with open("reponse.txt", "r") as fichier:
    reponse = fichier.read()



chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

if graphic.lower() != "yes":
    chrome_options.add_argument("--headless")

chrome_service = Service(executable_path='/usr/bin/chromedriver')

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://jt.s2.rpn.ch")



time.sleep(2)

inputUsername = driver.find_element(By.CSS_SELECTOR, ".ant-input")
inputUsername.send_keys(username)

time.sleep(0.2)

inputPassword = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Mot de passe"]')
inputPassword.send_keys(password + Keys.ENTER)

time.sleep(0.2)

btnCours = driver.find_element(By.XPATH, f"//p[contains(@class, 'work-icon-date') and text()='{cours}']/ancestor::span[contains(@class, 'work-icon')]")
btnCours.click()

time.sleep(0.2)

btnAdd = driver.find_element(By.XPATH, "(//button[@class='ant-btn ant-btn-default ant-btn-circle ant-btn-lg ant-btn-background-ghost sidebar-btn'])[2]")
btnAdd.click()

time.sleep(0.2)

btnCalendar = driver.find_element(By.CSS_SELECTOR, ".ant-calendar-picker-input")
btnCalendar.click()

time.sleep(0.2)

btnDate = driver.find_element(By.XPATH, f"//div[contains(@class, 'ant-calendar-date') and normalize-space(text())='{date}']")
btnDate.click()

time.sleep(0.2)

btnPeriode = driver.find_element(By.CSS_SELECTOR, "input.ant-input-number-input")
btnPeriode.send_keys(Keys.CONTROL, "a" + Keys.DELETE)
btnPeriode.send_keys(periode)

time.sleep(0.2)

inputWrite = driver.find_element(By.CSS_SELECTOR, "textarea.ant-input[placeholder='Rentrez le contenu du détail ici']")
inputWrite.send_keys(reponse + Keys.ENTER)

time.sleep(0.2)

btnSave = driver.find_element(By.CSS_SELECTOR, "i.anticon-save")
btnSave.click()



if graphic.lower() != "yes":
    driver.quit()
else:
    input()