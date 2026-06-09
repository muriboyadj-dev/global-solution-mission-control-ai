# Mission Control AI - EnviroSat

## Global Solution FIAP

### Integrantes

Murillo Boyadjian - 570774
Lucas Barros - 571528
Renan Eskildssen - 571097

---

# Descrição do Projeto

O Mission Control AI - EnviroSat é um sistema de monitoramento de telemetria espacial desenvolvido para auxiliar equipes de controle de missão na análise de dados operacionais de satélites voltados ao monitoramento ambiental.

A solução recebe informações de telemetria, identifica anomalias, classifica níveis de severidade e apresenta recomendações operacionais juntamente com a avaliação do impacto terrestre causado por possíveis falhas.

O sistema foi projetado para apoiar missões de observação ambiental responsáveis pelo monitoramento de queimadas, incêndios florestais e áreas de desmatamento.

---

# Objetivo

Desenvolver uma solução capaz de:

* Receber dados de telemetria espacial.
* Detectar anomalias operacionais.
* Classificar o nível de severidade da missão.
* Gerar alertas automáticos.
* Explicar impactos terrestres decorrentes de falhas.
* Auxiliar operadores na tomada de decisão.

---

# Problema Abordado

Satélites ambientais são responsáveis pela coleta de dados utilizados para identificar incêndios florestais, queimadas e alterações ambientais.

Falhas operacionais podem comprometer a qualidade dessas informações, causando atrasos na identificação de eventos críticos e dificultando ações de resposta.

O Mission Control AI auxilia no monitoramento contínuo desses sistemas, permitindo a rápida identificação de problemas e reduzindo riscos operacionais.

---

# Funcionalidades

## Monitoramento de Telemetria

O sistema recebe:

* Energia (%)
* Temperatura do sensor térmico (°C)
* Ocupação do buffer de imagens (%)
* Precisão de geolocalização (m)

## Sistema de Alertas

O sistema identifica automaticamente:

* Energia baixa
* Energia crítica
* Temperatura elevada
* Temperatura crítica
* Buffer próximo do limite
* Buffer lotado
* Imprecisão de geolocalização
* Erro crítico de geolocalização

## Classificação de Severidade

A missão é classificada como:

* NORMAL
* MODERADO
* CRÍTICO

## Histórico Operacional

O sistema mantém os últimos ciclos analisados para acompanhamento operacional.

## Análise Inteligente

O Mission Control AI gera:

* Diagnóstico da missão
* Impacto terrestre
* Ação recomendada
* Resumo executivo

---

# Estrutura do Projeto

```text
mission-control-ai-envirosat/

├── main.py
├── README.md
├── requirements.txt

├── src/
│   ├── telemetria.py
│   ├── alertas.py
│   ├── engine.py
│   └── ui.py

└── prompts/
    └── system_prompt.md
```

---

# Tecnologias Utilizadas

* Python 3
* Estruturas de Dados
* Programação Modular
* Engenharia de Prompt
* GitHub

---

# Como Executar

Execute o arquivo principal:

```bash
python main.py
```

---

# Exemplo de Entrada

```text
Energia (%): 25
Sensor térmico (°C): 91
Buffer (%): 97
Precisão GPS (m): 8
```

---

# Exemplo de Saída

```text
SEVERIDADE:
CRÍTICO

ALERTAS:
 ENERGIA CRÍTICA
 TEMPERATURA CRÍTICA
 BUFFER LOTADO
 ERRO CRÍTICO DE GEOLOCALIZAÇÃO
```

---

# Impacto Social

A solução contribui para a continuidade do monitoramento ambiental realizado por satélites responsáveis pela observação da Terra.

A rápida identificação de falhas operacionais reduz riscos de perda de dados utilizados no combate a incêndios florestais, monitoramento de queimadas e preservação ambiental.

---

# Modelo de Negócio

## Cliente

* Agências espaciais
* Instituições ambientais
* Empresas de sensoriamento remoto
* Centros de monitoramento orbital

## Fonte de Receita

Licenciamento da plataforma de monitoramento.

## Métrica de Impacto

* Tempo médio de detecção de falhas.
* Disponibilidade operacional do satélite.
* Redução do tempo de resposta a incidentes ambientais.

---

# Limitações

* Utiliza dados simulados.
* Não realiza comunicação direta com satélites reais.
* Não utiliza APIs externas nesta versão.

---

# Conclusão

O Mission Control AI - EnviroSat demonstra como sistemas inteligentes podem auxiliar no monitoramento de missões espaciais voltadas à preservação ambiental, fornecendo diagnósticos rápidos, alertas automáticos e suporte à tomada de decisão.
