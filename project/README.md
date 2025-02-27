# API de Recomendação

Uma poderosa engine de recomendação escalável construída usando a fatoração de matriz Alternating Least Squares (ALS) implícita e disponibilizada através de uma interface FastAPI de alto desempenho.

## Visão Geral

Esta API de recomendação fornece recomendações personalizadas de itens para usuários com base em seu histórico de interações. Ela utiliza o algoritmo de filtragem colaborativa ALS implícito para identificar padrões nas interações usuário-item e gerar recomendações relevantes.

O sistema é containerizado usando Docker para facilitar a implantação e escalabilidade.

## Funcionalidades

- **Recomendações Personalizadas**: Gera recomendações sob medida para cada usuário
- **Recomendações para Novos Usuários**: Suporte para recomendações para usuários sem histórico prévio
- **Recomendações Baseadas em Sessão**: Incorpora atividade recente do usuário para sugestões mais relevantes
- **Abordagem Híbrida de Recomendação**: Combina diferentes técnicas de recomendação para desempenho ótimo
- **Arquitetura Escalável**: Projetada para servir recomendações com alta vazão
- **Tratamento Robusto de Erros**: Lida de forma elegante com casos de borda e requisições inválidas

## Stack Tecnológica

- **Algoritmo Principal**: Alternating Least Squares (ALS) implícito para filtragem colaborativa
- **Framework Web**: FastAPI para endpoints de API de alto desempenho
- **Containerização**: Docker para fácil implantação e escalabilidade
- **Operações Matriciais**: NumPy para computação eficiente
- **Processamento de Dados**: Pandas para manipulação de dados

## Endpoints da API

| Endpoint | Método | Descrição |
|----------|--------|-------------|
| `/health` | GET | Endpoint de verificação de saúde |
| `/model-info` | GET | Informações sobre o modelo carregado |
| `/recommend/{user_id}` | GET | Obter recomendações para um usuário existente |
| `/recommend/new-user` | POST | Obter recomendações para um novo usuário com base nas interações fornecidas |

## Instalação e Configuração

### Pré-requisitos

- Docker
- Python 3.9+ (para desenvolvimento local)