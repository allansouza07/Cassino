
# 🎰 Cassino Virtual

Um sistema desenvolvido em **Python** que simula o funcionamento básico de um cassino virtual por meio de uma roleta de símbolos.

O projeto permite que o usuário realize **cadastro e login**, informe o valor da aposta e participe de uma rodada da roleta. O resultado é definido a partir da combinação dos símbolos sorteados, podendo gerar diferentes retornos para a aposta.

> **Projeto desenvolvido com foco na prática de lógica de programação, estruturas condicionais, funções, manipulação de arquivos e geração de valores aleatórios em Python.**

---

## 📌 Sobre o projeto

O **Cassino Virtual** foi desenvolvido como um projeto de estudo para aplicar conceitos fundamentais da linguagem Python em uma aplicação interativa executada pelo terminal.

O sistema possui um fluxo simples:

1. O usuário informa se já possui cadastro.
2. Caso não possua, realiza seu cadastro.
3. O usuário realiza login utilizando nome e senha.
4. O sistema apresenta as regras da aposta.
5. O usuário informa o valor que deseja apostar.
6. A roleta realiza o sorteio de três símbolos.
7. O sistema verifica a combinação obtida.
8. O usuário recebe o resultado da rodada.
9. É possível realizar uma nova aposta.

Os dados de cadastro são armazenados em um arquivo de texto, permitindo que as informações permaneçam disponíveis entre diferentes execuções do programa.

---

## 🎯 Objetivos

O principal objetivo do projeto é colocar em prática conceitos essenciais de programação através de uma aplicação que possui entrada de dados, processamento, armazenamento e interação com o usuário.

### Conceitos trabalhados

- Lógica de programação
- Estruturas condicionais
- Estruturas de repetição
- Funções
- Tratamento de exceções
- Manipulação de arquivos
- Geração de números aleatórios
- Entrada e saída de dados
- Organização de código em diferentes módulos
- Validação de informações
- Simulação de regras de negócio

---

## 🎰 Funcionamento da roleta

A roleta utiliza diferentes símbolos de frutas:

| Símbolo | Classificação |
|---|---|
| 🍇 | Comum |
| 🍑 | Comum |
| 🍉 | Comum |
| 🍍 | Especial |
| 🍒 | Coringa |

A cada rodada, três elementos são sorteados aleatoriamente utilizando a biblioteca `random`.

O programa também utiliza a biblioteca `time` para criar uma pequena animação durante o sorteio, simulando o giro da roleta.

### 🏆 Resultados

Existem diferentes possibilidades de resultado:

#### 🍍 Combinação especial

Quando os três símbolos sorteados são `🍍`, o usuário recebe um retorno equivalente a **3x o valor apostado**.

#### 🎰 Três símbolos iguais

Quando os três símbolos são iguais, o usuário recebe um retorno equivalente a **2x o valor apostado**.

#### 🍒 Combinações com o símbolo coringa

O `🍒` possui regras especiais dentro da lógica da roleta e pode contribuir para uma aposta vencedora.

#### ⚠️ Dois símbolos iguais

Quando apenas dois símbolos coincidem, o sistema informa que a rodada chegou perto de uma combinação vencedora.

#### ❌ Nenhuma combinação

Quando não ocorre nenhuma das condições anteriores, a aposta é considerada perdida.

---

## 👤 Sistema de cadastro e login

O projeto possui um sistema simples de autenticação desenvolvido utilizando arquivos de texto.

Durante o cadastro, o sistema solicita:

- Nome
- Idade
- Senha

O programa também possui uma validação que impede o cadastro de usuários menores de 18 anos.

As informações de usuário e senha são armazenadas no arquivo:

```text
banco_dados.txt
````

Os dados são separados pelo caractere `|`, seguindo o formato:

```text
nome|senha
```

A autenticação é realizada posteriormente comparando os dados informados pelo usuário com os registros existentes no arquivo.

---

## 💰 Sistema de apostas

Antes de iniciar uma rodada, o usuário informa o valor que deseja apostar.

O sistema apresenta previamente os possíveis retornos:

```text
Retorno normal: 2x o valor da aposta
Retorno especial: 3x o valor da aposta
```

O usuário pode confirmar ou cancelar a aposta antes que a roleta seja executada.

---

## 🗂️ Estrutura do projeto

```text
Cassino/
│
├── cassino.py
├── funcoes_banco.py
├── banco_dados.txt
├── LICENSE
├── README.md
└── .gitattributes
```

### `cassino.py`

Arquivo principal da aplicação.

É responsável pelo fluxo do cassino, incluindo:

* Cadastro
* Login
* Apostas
* Sorteio da roleta
* Validação dos resultados
* Interação com o usuário

### `funcoes_banco.py`

Módulo responsável pelas operações relacionadas ao arquivo de usuários.

Possui funções para:

* Verificar a existência do arquivo;
* Cadastrar usuários;
* Analisar as credenciais de login.

### `banco_dados.txt`

Arquivo utilizado para armazenar os dados básicos dos usuários cadastrados.

### `LICENSE`

O projeto utiliza a **MIT License**.

---

## 🛠️ Tecnologias utilizadas

### Python

Linguagem principal utilizada no desenvolvimento da aplicação.

### Bibliotecas

O projeto utiliza bibliotecas nativas do Python:

* `random` — geração dos resultados aleatórios da roleta;
* `time` — controle do tempo entre os resultados exibidos;
* `open()` — leitura e escrita do arquivo de usuários.

Exemplo:

```python
import random
import time
```

O projeto também utiliza um módulo próprio para separar parte da lógica relacionada ao armazenamento dos usuários.

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/allansouza07/Cassino.git
```

### 2. Entre na pasta

```bash
cd Cassino
```

### 3. Execute o programa

```bash
python cassino.py
```

Em algumas instalações do Windows, pode ser necessário utilizar:

```bash
py cassino.py
```

---

## 🖥️ Exemplo de utilização

Ao iniciar o programa, o usuário encontra a opção de acessar uma conta existente ou realizar um novo cadastro:

```text
Você já possui cadastro em nosso sistema?

[1] Sim
[2] Não
```

Após realizar o login, o sistema apresenta as regras da aposta:

```text
🎰 GIRANDO A ROLETA...

🍇 | 🍒 | 🍍
```

O resultado é então analisado pelo programa e uma mensagem correspondente à combinação sorteada é apresentada.

---


## ⚠️ Observação

Este projeto possui **finalidade exclusivamente educacional** e foi desenvolvido como uma simulação de um cassino virtual para prática de programação.

Não se trata de uma plataforma real de apostas e não realiza transações financeiras.

---

## 📄 Licença

Este projeto está disponível sob a licença **MIT**.

Consulte o arquivo [`LICENSE`](LICENSE) para mais informações.

---

## 👨‍💻 Desenvolvedor

**Allan Souza**

Estudante de **Análise e Desenvolvimento de Sistemas** e desenvolvedor em formação, com interesse em desenvolvimento de software, banco de dados e análise de dados.

### 🔗 Links

* **GitHub:** [allansouza07](https://github.com/allansouza07)
* **Repositório:** [Cassino](https://github.com/allansouza07/Cassino)

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório!

```
```
