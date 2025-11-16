# 🛰️ GeoSearch Automation

Automação de pesquisas no **Google Maps** e **Google Search** utilizando **Python + Selenium**.  
O usuário informa coordenadas e um termo de pesquisa, e o sistema executa automaticamente:

- Busca no Google Maps  
- Busca no Google Search  
- Captura de screenshots  
- Exibição do link final  
- Execução em modo *headless* (sem abrir janela)

---

## ✨ Funcionalidades

- 🔎 Pesquisa automática de latitude/longitude no Google Maps  
- 🌍 Obtenção do link final da pesquisa  
- 🖥️ Pesquisa textual no Google Search  
- 📸 Captura automática de screenshots  
- ⚙️ Execução em *headless mode*  
- 🔁 Menu interativo para repetir buscas

---

## 📁 Estrutura do Projeto
├── main.py # Arquivo principal
├── class_navegador.py # Classe base (automação com Selenium)
├── class_pesquisa_usuario.py # Classe de pesquisa no Google (herda Navegador)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x  
- Selenium WebDriver  
- webdriver-manager  
- Google Chrome Driver  
- Chrome Options (headless)

---

## 🚀 Como Executar

### 1. Instale as dependências:

```bash
pip install selenium webdriver-manager
```
### 2. Execute o programa:
```bash
python __main__.py
```
### 3. Preencha as informações solicitadas:

- Latitude

- Longitude

- Termo da pesquisa
