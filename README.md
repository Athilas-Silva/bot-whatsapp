# Bot do Whatsapp

Bot para enviar mensagem de forma automática para seus contatos no whatsapp.

<p align="center">
  <img src="https://img.shields.io/twitter/url?color=%23007ACC&label=Vs%20Code&logo=Visual%20Studio%20Code&logoColor=%23007ACC&style=for-the-badge&url=https%3A%2F%2Fsimpleicons.org%2Ficons%2Fvisualstudiocode.svg">    <img src="https://img.shields.io/twitter/url?color=%233776AB&label=Python&logo=Python&logoColor=%233776AB&style=for-the-badge&url=https%3A%2F%2Fsimpleicons.org%2Ficons%2Fpython.svg" />
</p>

##

### Ferramentas necessarias:

- [Vs Code](https://code.visualstudio.com/download)
- [Python](https://www.python.org/)

Dependências da aplicação:
- `` pip install selenium ``
- `` pip install webdriver_manager ``
##

### O que é Selenium e Webdriver

O Selenium é um biblioteca utilizada para testes automatizados de navegadores. Trata-se de uma ferramenta bastante poderosa, porém leve, para criar scripts de casos de testes automatizados. Com uma simples configuração (descrita abaixo), você pode começar a executar o script usando os métodos do Selenium para lidar com a UI do aplicativo. O Selenium WebDriver é gratuito e oferece suporte a diversos tipos de navegadores e sistemas operacionais. Saiba mais [aqui](https://developer.ibm.com/br/devpractices/software-development/articles/maximo-selenium-autom-tests/) ou [aqui](https://imasters.com.br/back-end/google-search-usando-selenium-e-python-o-basico-sobre-selenium-python#:~:text=O%20Selenium%20%C3%A9%20um%20biblioteca,fazer%20uma%20pesquisa%20no%20Google.).

##

### Print do código

![parte 1](https://user-images.githubusercontent.com/71888055/116464636-93729500-a842-11eb-993c-28bb8841eb50.PNG)

![parte 2](https://user-images.githubusercontent.com/71888055/116464177-08919a80-a842-11eb-9f46-a1619b2ffe4d.PNG)

- 1 e 2: Importação das biblioteas instaladas e escolhendo navegador para abrir o whatsapp web
- 3: Definindo as configurações do driver, escolhendo o Microsoft Edge como navegador de uso, pegando o link do whatsapp web e deixando um tempo de 30 segundos de espera para poder escanear o QR Code do site.
- 4: Definindo para quem enviar as mensagens e qual a mensagem a ser enviada
- 5: Função para buscar o contato na sua lista, através da busca de elementos no html que no nosso caso é `` '//div[contains(@class, "copyable-text selectable-text")]' ``
- 6: Função que envia a mensagem através do elemento ``'//div[contains(@class, "copyable-text selectable-text")]' `` porém selecionando o segundo elemento com o mesmo nome, passando o indice 1 para selecionar a segunda caixa de texto.

##

### Tutorial e perfil de referência

- Perfil no Github [Jhonatan de Souza](https://github.com/Jhonatan-de-Souza)
- Perfil do canal no Github [Dev Aprender](https://github.com/devaprender)
- Video [tutorial](https://www.youtube.com/watch?v=_ZDBVeqyK6g)
