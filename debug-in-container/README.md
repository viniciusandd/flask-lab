# Debugando uma aplicação Flask dentro de um container Docker

## Preparando o ambiente

1. Clone o repositório: `git clone https://github.com/viniciusandd/flask-lab.git`

1. Entre na pasta do projeto atual: `cd debug-in-container`

## Preparando o ambiente de desenvolvimento

1. Builde um container com o ambiente de desenvolvimento: `docker build -t debug-in-container:development .`

2. Certifique-se de que o arquivo [launch.json](.vscode/launch.json) (arquivo que possui as configurações de depuração do vscode) possui a seguinte configuração:

```
    "configurations": [
        {
            "name": "Python: Attach",
            "type": "python",
            "request": "attach",
            "port": 5678,
            "host": "localhost",
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}",
                    "remoteRoot": "/var/www/app"
                }
            ]
        }
    ]
```

3. Execute o container. No comando será passado um volume (`-v`) com o código fonte que está na máquina local, dessa forma é possível sincronizar o código em tempo real com o container. Outro parâmetro é o que mapeia a porta (`-p`) do container com a porta do host. O comando para iniciar o container é: `docker run -v $PWD:/var/www/app -p 8000:5000 debug-in-container:development`

4. O servidor do Flask não será iniciado, pois dentro do Dockerfile no comando `CMD` foi passado o parâmetro `--wait`, ou seja, ele ficará aguardando até que ocorra um attach.

5. Adicione um breakpoint no código fonte.

6. Inicie o debug do vscode.

7. (**Opcional**) Se o vscode mostrar uma mensagem avisando que ocorreu um erro ao dar attach (geralmente em uma porta diferente da informada nas configurações), substitua no arquivo [launch.json](.vscode/launch.json) a linha `host": "localhost"` por `host": "{ip-do-container}"`

8. (**Opcional**) Para buscar o ip do container, execute `docker ps` e copie o ID do container. Com o ID, execute o comando `docker inspect {id-do-container} | grep -i IPAddress`.

9. (**Opcional**) Inicie novamente o debug do vscode.

10. Para testar, inicie um browser e passe a seguinte url: `http://localhost:8000`. Ou através da linha de comando com `curl http://localhost:8000`.

## Criando o ambiente de produção

O ambiente de produção será criado em cima do ambiente de desenvolvimento.

1. Execute o comando para buildar o container. No comando será passado o parametro que aponta para o Dockerfile de produção (`--file Release`): `docker build -t debug-in-container:production . --file Release`

2. Execute o container mapeando ele para a porta do host com o parâmetro `-p`: `docker run -p 5000:5000 debug-in-container:production`

3. Para testar, inicie um browser e passe a seguinte url: `http://localhost:5000`. Ou através da linha de comando com `curl http://localhost:5000`.