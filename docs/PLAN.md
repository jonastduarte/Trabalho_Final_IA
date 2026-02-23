# 🎯 Plano de Implementação (PLAN.md)

🤖 **Applying knowledge of `@[project-planner]`...**

Este é o plano detalhado estruturado pelo `project-planner` para a execução da atividade, dividindo o desenvolvimento do App ToDoList, a documentação acadêmica e a garantia de qualidade conforme a Fase 1 da orquestração.

## Objetivo
Criar um aplicativo ToDoList em Python com interface gráfica (Tkinter) que implemente operações CRUD. Adicionalmente, redigir o relatório técnico exigido do "Trabalho Final IA" evidenciando a utilização do Antigravity Gemini 3.1 Pro como assistente generativo nas etapas de desenvolvimento, alinhando aos eixos solicitados no documento TrabalhoDisciplina.pdf.

## Agentes a Seren Envolvidos na Fase 2
Para que a orquestração fique completa e funcional, no mínimo 3 especialistas serão acionados em paralelo:

1. **`frontend-specialist` + `backend-specialist`**:
   - Criação da classe `ToDoList` utilizando Orientação a Objetos.
   - Aplicação de type hints e blocos `try/except`.
   - Adição da Interface Gráfica interativa (Tkinter).

2. **`documentation-writer`**:
   - Geração do relatório acadêmico de até 8 páginas formatado em Markdown detalhando a aplicação do Antigravity Gemini 3.1 Pro (AI4SE).
   - Análise crítica de produtividade, vulnerabilidades e implicações éticas/IPs na adoção dos LLMs no SDLC com base no material disponibilizado (Cap1 ao Cap6).

3. **`test-engineer`**:
   - Desenvolvimento de testes em `unittest` ou automatizando a validação de uso.
   - Validação da robustez das operações de Add/Remove/Complete nas listas de tarefas e exibição dos filtros de listagens.

## Estrutura de Arquivos Proposta
- `src/todolist.py` (O aplicativo completo com regras OOP, GUI limpa, docstrings e bloco de exemplo)
- `tests/test_todolist.py` (Testes da lógica das tarefas)
- `docs/Relatorio_Trabalho_Final.md` (O relatório final abordando as respostas das 4 perguntas essenciais do artigo)

## Plano de Verificação (Verification Plan)
- **Execução Automática**: Usar terminal para testar o código da classe diretamente integrando o exemplo principal `python src/todolist.py`.
- **Testes Manuais de GUI**: Iniciar o app via terminal e testar cada função listada - Adicionar novo card, Remover item, Concluir status, Listar todos os Pendentes e Concluídas com formatação limpa.
- **Validação de Código e Diretrizes**: Checklist final, onde aplicável.

## Pre-Requisitos e Contexto Atual
- Repositório do GitHub já clonado de forma limpa em `./Trabalho_Final_IA`.
- As entregas serão salvas, testadas, checadas no fluxo de checklist garantindo total compatibilidade para fazer os commits e ir ao origin em definitivo no GitHub.
