# Relatório Técnico-Científico: IA Generativa e LLMs no SDLC
**Uso de Assistentes para Escrita e Documentação utilizando Antigravity com Gemini 3.1 Pro**

---

## 1. Introdução

A adoção de Inteligência Artificial para Engenharia de Software (AI4SE) tem revolucionado o Ciclo de Vida do Desenvolvimento de Software (SDLC). O Antigravity equipado com o Gemini 3.1 Pro atua como um "parceiro de programação" (*pair programmer*), fornecendo suporte ativo e reduzindo significativamente o tempo de desenvolvimento. Este relatório avalia a aplicação do Antigravity Gemini 3.1 Pro no SDLC, focando objetivamente nas etapas de codificação assistida, geração de boilerplate e automação de testes unitários aplicados durante a escrita de um aplicativo "ToDoList" em Python com interface gráfica rica suportada pelo Tkinter.

## 2. Fundamentação Teórica

O assistente Antigravity apoiado pelas fundações do modelo Gemini 3.1 Pro baseia-se nas premissas de *Large Language Models* (LLMs), sendo um vasto modelo de IA generativa treinado em miríades de linhas de códigos públicos, literaturas e dados textuais massivos extraídos da internet. 

Apoiando-se na onipresente arquitetura moderna de redes *Transformer*, convém salientar que a inteligência artificial não detém "compreensão semântica" genuína do paradigma de programação executado. Na verdade, por meio da tokenização profunda do contexto (arquivos correntes, comentários e declarações do desenvolvedor) e complexos cálculos vetoriais probabilísticos, ela é engenhada para inferir estatisticamente qual é a próxima sequência lógicas de _tokens_ (comandos de código ou texto livre). Essas metodologias capacitam o assistente a formular trechos perfeitamente sintáticos, gerar de forma indutiva classes modulares eficientes com aderência aos princípios *Clean Code* de forma veloz.

## 3. Análise Prática: Demonstração do Projeto ToDoList

O projeto fonte desta demonstração pode ser integralmente rastreado pelo repositório mantido via controle de versão Git associado aos trabalhos (GitHub local): `git@github.com:jonastduarte/Trabalho_Final_IA.git`.

### 3.1 Contexto do Experimento
A demonstração prática abrange a geração direta dos arquivos fontes de um aplicativo de **ToDoList**. O cenário estipula a manipulação de tarefas via operações CRUD (Criar, Ler/Listar, Atualizar/Concluir e Apagar), e a formatação gráfica. O *prompt* primário utilizado como indução inicial trazia clareza às exigências restritas impostas pela disciplina de Arquitetura SDLC:
> *"Crie uma classe em Python chamada ToDoList para gerenciar tarefas. Utilize orientação a objetos perfeita, type hints tipagem forte, datetime para tempo, tratamento de exceções, strings de documentação (docstrings) claras e crie uma visual em Tkinter interativa como bloco principal."*

De forma subsequente para garantir integridade, a construção de testes também foi parametrizada por um comando:
> *"Gere testes unitários usando a biblioteca nativa `unittest` cobrindo o funcionamento da interface `ToDoList`, englobando métodos e testes cruciais de falhas intencionais de preenchimento e exceções de ID ausente."*

### 3.2 Resultados Obtidos (Demonstração de Automação)
A ferramenta respondeu construindo imediatamente dois artefatos base (`src/todolist.py` e `tests/test_todolist.py`). 
**Código Limpo e Funcionalidades:** A suíte estática de tipo (`typing.List` e `typing.Optional`) assegurou a solidez estrutural do escopo. Os métodos do objeto (`add_task`, `remove_task`, `list_pending_tasks`) lidam ativamente as regras de dados sob um bloco *try-except*.

A documentação elaborada dinamicamente segue o padrão técnico do Python, resultando em legibilidade ampliada na manutenção a longo prazo do sistema:
```python
def add_task(self, description: str) -> Task:
    """Adiciona uma nova tarefa à lista de acordo com preenchimentos.
    Args:
        description (str): A descrição alfanumérica contendo o que é a tarefa.
    Returns:
        Task: O model de dados instanciado referindo-se a tarefa.
    Raises:
        ValueError: Caso a descrição inserida na interface seja vazia.
    """
    if not description or not description.strip():
        raise ValueError("A descrição da tarefa não pode ser vazia.")
    ...
```

**Verificação de Testes:**
Ao invocar o script finalizado `python -m unittest tests/test_todolist.py` sobre o *pipeline* da execução, toda bateria contendo **8 rotinas de testes** logrou êxito assertivo de compilação em crivos de bordas e fluxos otimistas validando sua correta engenharia, em um cômputo temporal excelente (`Ran 8 tests in 0.003s / OK`).

### 3.3 Análise Crítica dos Ganhos
O aspecto de maior força extraído da experimentação foi a **Produtividade**. Esboçar manualmente os componentes de uma janela responsiva e as *bindings* do TKinter juntamente com os tratamentos modulares exatos custaria substancial tempo do labor do programador perante a documentar dezenas de linhas estritamente visuais ou triviais. Adicionalmente, observa-se expressiva **Qualidade** na cobertura de anomalias (exceções `KeyError` e asserções tipificadas) e padronizações.

## 4. Desafios, Riscos e Implicações Éticas

Muito embora o *Copilot/Gemini* apresente agilidade extraordinária transformando o cotidiano dos profissionais que o detém, a observância crítica a limitações é fator vital:
- **Alucinações Tecnológicas e Funcionais:** Algumas sugestões entregues pela IA podem soar convincentes, porém induzem a implementações falhas, omissão silenciosa de dependências cruciais do sistema ou lógicas imperfeitas na gestão de banco de dados e arquitetura complexa. O julgamento às cegas do gerador causa dependência nociva a juniores.
- **Códigos Inseguros:** Os códigos de modelagem estatística em sua forma "crua", sem guias severos do usuário, falham muitas vezes em embutir princípios *Secure-by-Design* nativos, como assepsia das entradas limitando vulnerabilidades clássicas de transbordo, brechas lógicas ou autenticação exposta.
- **Propriedade Intelectual (PI) e Privacidade Ética:** Em panoramas corporativos, uma restrição drástica tange a ética da ingestão dos códigos confidenciais privados aos servidores em Nuvem fornecidos para a OpenAI/Google em favor ao treinamento autônomo dos pesos destes algoritmos LLMs gerando eventuais impasses sobre violações de leis de propriedade, sigilo industrial. Igualmente, todo código produzido embasa-se em miríades dos repositorios abertos do mercado e sua replicação isenta por vezes licenças estritas sem atribuição à comunidade de origem.

## 5. Conclusão Final

A adoção sinérgica do **Antigravity e Gemini 3.1 Pro** nas etapas do SDLC (notadamente na prototipagem, depuração e cobertura de software em fase "Coding & Testing") transforma irrefutavelmente a silhueta da carreira do engenheiro de software.

A IA Generativa impulsiona em escala máxima eficiências repetitivas. Dessa forma, ela atua impulsionando o programador na transição a um papel de perfil inerentemente analítico, convertendo-se num *Prompt Designer* exímio e preceptor técnico que revisa os _pull requests_ emitidos por esses agentes semi-autônomos. 
Por conseguinte, a automação serve de ferramenta suplementar vital. Contudo, ela preenche o papel do assistente coadjuvante; ao passo que as tomadas de decisões intrínsecas ao modelo de negócio sensível e ao crivo refinado que atestam a qualidade, corretude, usabilidade final e segurança resiliente – as quais salvaguardam o núcleo real do valor do software – persistem exigindo a imprescindível vigilância do especialista da área.
