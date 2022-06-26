# Desafio Backend

## Decisões Tomadas

### Decisões Iniciais

- Havia a possibilidade de usar qualquer linguagem e eu escolhi Python por já ter alguma familiaridade com FastAPI, que considereibum framework bastante adequado para esse desafio, por não ter muito boilerplate code.
- Caso o código em si fosse mais robusto, eu provavelmente iria fazer em Ruby on Rails.

### Decisões no decorrer do desenvolvimento

- Ao olhar as instruções do desafio eu pensei em criar duas classes: `Character`, para representar o personagem, e `Profession`, para representar as profissões.
- Tentei colocar o código principal (rotas e o desenvolvimento em si) em um arquivo `main.py`, mas eventualmente o arquivo começou a ficar muito grande e confuso e portanto eu decidi separar `api.py` com as rotas e `game.py` com o core do jogo.
- Eu achei importante criar outras validações (além de se o nome é válido ou não) na criação de personagens, e por isso as adicionei.
- Todos os métodos de ambas as classes criadas são estáticos, ou seja, não precisam de instâncias para serem chamados, porque fica mais fácil de eu conseguir utilizá-los em `game.py`.
- Em `game.py` eu mantive algumas funções referentes ao character, que na minha opinião devem ficar em `caracter.py`, mas por hora mantive lá considerando que fica mais fácil de utilizar o array `characters` em outros lugares.
- Eu criei um dicionário com as mensagens que serão mostradas no log do jogo, para evitar repetí-las no código.

### Possíveis melhorias

- Colocar os métodos create e retrieve character dentro da classe `Character`, o que faz mais sentido semânticamente.
- Modularizar mais o código da batalha e deixá-lo em um arquivo separado. Da forma como está agora fica ruim de entender e testar.
- Utilização de testes unitários para testar o código.

## Organização dos arquivos

- `app/api.py`: arquivo que contém as rotas.
- `app/game.py`: arquivo que contém o código 'core' do jogo.
- `app/character.py`: Classe Character.
- `app/profession.py`: Classe Profession.
- `README.md`: arquivo que contém o README do desafio.
- `requirements.txt`: arquivo que contém as dependências necessárias para rodar o jogo.

## Rodando o projeto

### Nativo

Para executar o projeto, basta seguir o seguinte passo a passo:

- Instalar as dependências com um `pip install -r requirements.txt`
- Executar o comando `uvicorn api:app --reload` dentro da pasta `app`
- Se dirigir ao endereço `127.0.0.1:8000/docs`

### Docker

Caso deseje, também é possível executar a aplicação através do Docker. Para isso, basta seguir os seguintes passos:

- Ter o docker instalado na sua máquina
- Criar a imagem com o seguinte comando, a partir da raiz do projeto: `docker build -t testloft .`
- Executar o container com `docker run -p 8080:80 -it testloft`
- Abrir o navegador no endereço `0.0.0.0:8080/docs`
- Explorar a API a partir desse endereço.

**Dica:**  Em `0.0.0.0:8080/docs`, você pode clicar em "Try it out" e testar a API.