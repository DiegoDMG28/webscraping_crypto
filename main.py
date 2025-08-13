import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from time import sleep

driver = uc.Chrome()
driver.get('https://br.investing.com/crypto/currencies')

tabela = wait(driver, 15).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, '.datatable_table__DE_1_.border-separate.datatable_table--freeze-column__XKTDf')
))

colunas = tabela.find_elements(By.CSS_SELECTOR, '.datatable_row__Hk3IV')

for coluna in colunas:
  crpt_nome     = tabela.find_element(By.CSS_SELECTOR, '.crypto-coins-table_cellNameText__aaXmK')
  crpt_abrev    = tabela.find_elements(By.CSS_SELECTOR, '.pt-0.5.text-xs.text-inv-grey-650')
  crpt_abrev    = crpt_abrev[1]
  
  try:
    crpt_preco  = tabela.find_element(By.CSS_SELECTOR, '.datatable_cell__LJp3C datatable_cell--align-end__qgxDQ !text-sm text-link mdMax:!pl-8')
  except:
    crpt_preco  = 'Não foi possível coletar o preço'
  
  if not crpt_preco:
    crpt_preco  = 'Não foi possível coletar o preço'

driver.quit()