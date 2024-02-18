# Bhub Challenge

## A proposta desse projeto é ser um esboço para a resolução do problema proposto no arquivo CHALLENGE.md

### Este será o projeto base onde serão cadastradas Regras e Ações que deverão ser executadas posteriormente à partir de uma fila, cada tipo de ação deverá ser executada por scripts especializados nesse determinado tipo de ação.

A ideia, conforme [fluxograma](https://drive.google.com/file/d/1UKDYw1ITCZAWV-NJ3L56_-pwWP3npvyk/view?usp=sharing) é que o sistema seja o mais simples possível, e responsável somente pelo cadastro das regras e ações, deixando o processamento e execução dessas ações para scripts externos, permitindo que desenvolvedores diferentes possam cuidar das diferentes partes da solução e reduzindo a necessidade de manutenção no sistema principal.

Uma versão bem simplificada e inicial da infraestrutura do projeto pode ser vista [aqui](https://drive.google.com/file/d/1qPRYob4pWSDpyqlX0a5UEpfIDBd4jM5i/view?usp=sharing).

## Como executar o projeto?

Para executar o projeto em seu ambiente local, tenha certeza de que possui:
- Docker
- Docker Compose
- Make
- Uma cópia do projeto ;-)


1. Crie o arquivo .env baseando-se no arquivo template sample.env

1. Execute o comando: `make initial-build` ou execute os comandos na ordem em que se encontram no arquivo `Makefile` (caso não possua o make instalado)

1. Será solicitado a criação do usuário administrador, depois o projeto estará rodando
