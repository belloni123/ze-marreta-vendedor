# ZE MARRETA - VENDEDOR

**Uma base de conhecimento e uma skill para transformar sua IA em um parceiro de vendas high ticket.**

O ZE MARRETA ajuda a diagnosticar o comercial, preparar reuniões, escrever scripts, investigar objeções, negociar e organizar ofertas. Reúne os **11 documentos de conhecimento do WOLF** e uma adaptação do **Framework Comercial de 7 Etapas**, indicado por Felipe Belloni.

Você recebe arquivos de instruções e consulta. Adicioná-los à sua IA configura seu comportamento e oferece contexto; isso não retreina o modelo nem garante resultados de vendas. Não há servidor, assinatura deste projeto ou chave de API para instalar o pacote. O serviço de IA escolhido pode ter seus próprios custos e limites.

## Comece aqui — sem programação

1. **Baixe o projeto:** clique em **Code → Download ZIP** neste GitHub, ou use [este link para baixar](https://github.com/belloni123/ze-marreta-vendedor/archive/refs/heads/main.zip). Extraia o ZIP.
2. **Abra sua IA:** escolha um chat, projeto ou assistente que aceite instruções e arquivos de conhecimento. Isso pode ser feito em serviços como ChatGPT, Claude ou Gemini, conforme os recursos disponíveis na sua conta.
3. **Defina o nome:** use `ZE MARRETA - VENDEDOR` se a ferramenta permitir nomear o assistente ou projeto.
4. **Cole as instruções:** abra [prompts/INSTRUCOES.md](prompts/INSTRUCOES.md), copie o texto e cole no campo de instruções da ferramenta. Se houver apenas um chat, envie o texto como primeira mensagem.
5. **Adicione o conhecimento:** anexe os arquivos `.md` da pasta [skills/ze-marreta-vendedor/references](skills/ze-marreta-vendedor/references). Inclua o framework e o índice, além dos 11 documentos WOLF. Se sua ferramenta aceitar apenas um arquivo, use [dist/ZE-MARRETA-COMPLETO.md](dist/ZE-MARRETA-COMPLETO.md), que reúne instruções e toda a base.
6. **Informe seu negócio:** envie o exemplo abaixo, preenchido com seus dados.
7. **Confira a instalação:** peça que a IA identifique as sete etapas e os documentos que consegue consultar. Depois solicite uma resposta para um caso real e confira se ela usa seu contexto.

```text
ZE MARRETA, vendo [produto/serviço] para [público B2B ou B2C].
Meu ticket médio é [valor], meu canal principal é [canal] e meu time tem [estrutura].
O problema atual é [dificuldade]. Os dados disponíveis são [dados e período].
Use o framework de sete etapas para localizar o gargalo e propor a primeira ação.
Separe fatos, hipóteses e informações que ainda preciso levantar.
```

**Se a IA não conseguir ler os arquivos:** envie somente o framework e os documentos relacionados ao pedido atual. A base completa é extensa e pode exceder a janela de contexto. Um ZIP anexado não garante que a IA leia o conteúdo; prefira os arquivos Markdown extraídos. Um link para o GitHub também não equivale a instalar a base.

Os nomes dos campos e os limites variam entre ferramentas. Use o recurso de instruções e conhecimento disponível na sua conta. As instruções do serviço continuam tendo precedência.

## Usar no Claude

Configure um Projeto para reutilizar as instruções e o conhecimento nas conversas dele. O procedimento segue a [documentação oficial de Projetos do Claude](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

1. Baixe e extraia o ZIP deste repositório, conforme o início deste README.
2. Acesse [Projetos do Claude](https://claude.ai/projects), clique em **Novo projeto / New Project** e dê o nome `ZE MARRETA - VENDEDOR`.
3. Abra **Definir instruções do projeto / Set project instructions**. Copie o texto de [prompts/INSTRUCOES.md](prompts/INSTRUCOES.md), cole nesse campo e salve.
4. Na área de conhecimento ou arquivos do projeto, clique em **+** e envie o arquivo extraído [dist/ZE-MARRETA-COMPLETO.md](dist/ZE-MARRETA-COMPLETO.md). Ele já reúne toda a base e o framework. Você também pode enviar os documentos separados da pasta `references`, em vez do arquivo completo.
5. Abra uma conversa **dentro do projeto** e envie a frase abaixo, substituindo os campos entre colchetes.
6. Peça que o Claude consulte o framework e identifique os documentos utilizados na resposta.

**Frase para copiar e usar no Claude:**

```text
ZE MARRETA, consulte os arquivos deste projeto.
Vendo [produto ou serviço] para [público B2B ou B2C],
com ticket médio de R$ [valor], pelo canal [canal].
Minha maior dificuldade é [problema].
Use o framework comercial de sete etapas para diagnosticar o gargalo
e me dar uma ação prioritária com um exemplo prático.
Separe fatos, hipóteses e dados que ainda preciso fornecer.
```

## Usar na OpenAI — ChatGPT

No ChatGPT, configure um Projeto com as instruções e os arquivos do ZE MARRETA. O procedimento segue a [documentação oficial de Projetos do ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt). Para instalar no **Codex**, use a seção de skills logo abaixo.

1. Baixe e extraia o ZIP deste repositório.
2. Acesse [ChatGPT](https://chatgpt.com), selecione **Novo projeto / New project** na barra lateral e dê o nome `ZE MARRETA - VENDEDOR`.
3. No menu **•••** do projeto, abra **Configurações do projeto / Project settings** e adicione as instruções de [prompts/INSTRUCOES.md](prompts/INSTRUCOES.md).
4. Na área de fontes ou arquivos do projeto, envie o arquivo extraído [dist/ZE-MARRETA-COMPLETO.md](dist/ZE-MARRETA-COMPLETO.md). Como alternativa, envie os documentos separados de `references`, respeitando o limite de arquivos da sua conta.
5. Abra um chat **dentro desse projeto** e envie a frase abaixo com seus dados.
6. Confira se a resposta consulta o material enviado e adapta a recomendação ao seu negócio.

**Frase para copiar e usar no ChatGPT:**

```text
ZE MARRETA, siga as instruções deste projeto e consulte a base anexada.
Meu negócio vende [produto ou serviço] para [público],
com ticket médio de R$ [valor]. Nosso canal principal é [canal].
Estamos travando em [problema], e temos estes dados: [dados e período].
Aplique o framework de sete etapas, indique a etapa prioritária
e entregue um plano de ação com indicador e um script que eu possa usar.
Não invente números, cases ou promessas de resultado.
```

## Usar no Gemini — criar um Gem

Um Gem permite salvar as instruções e os arquivos de referência do ZE MARRETA. O procedimento segue a [documentação oficial de Gems do Google](https://support.google.com/gemini/answer/15146780?hl=pt-BR).

1. Baixe e extraia o ZIP deste repositório.
2. No computador, acesse [Gemini](https://gemini.google.com), abra a barra lateral e selecione **Gems → Novo Gem**.
3. Dê o nome `ZE MARRETA - VENDEDOR` e cole o conteúdo de [prompts/INSTRUCOES.md](prompts/INSTRUCOES.md) no campo de instruções.
4. Em **Conhecimento → Adicionar arquivos**, envie o arquivo extraído [dist/ZE-MARRETA-COMPLETO.md](dist/ZE-MARRETA-COMPLETO.md). Ele contém instruções, os 11 documentos WOLF e o framework integrado.
5. Clique em **Salvar**. Depois, abra o ZE MARRETA em **Meus Gems**.
6. Envie a frase abaixo, preenchida com as informações do seu negócio.

**Frase para copiar e usar no Gemini:**

```text
ZE MARRETA, use suas instruções e os arquivos de conhecimento deste Gem.
Vendo [produto ou serviço] para [público], com ticket de R$ [valor].
Meu canal de aquisição é [canal] e o principal problema é [problema].
Diagnostique meu comercial com o framework de sete etapas.
Explique qual etapa devo trabalhar primeiro, o que fazer agora
e como medir o avanço. Inclua um exemplo prático adaptado ao meu negócio
e indique quais informações ainda estão faltando.
```

## Usar em um chat comum ou resolver dificuldades de envio

Se você não tiver acesso ao recurso de Projeto ou Gem, abra um chat comum, cole [as instruções](prompts/INSTRUCOES.md), anexe [o pacote completo](dist/ZE-MARRETA-COMPLETO.md) e envie uma das frases acima, trocando “projeto” ou “Gem” por “conversa”. Repita a configuração ao iniciar outra conversa.

Se a plataforma recusar a extensão `.md`, salve uma cópia do arquivo como `.txt`, mantendo o texto, e tente enviá-la. Se o conteúdo exceder o limite, envie primeiro o framework e os documentos pertinentes ao pedido. Aguarde o processamento dos arquivos antes de começar.

**Para ensinar o pessoal:** “Primeiro adicione as instruções e o conhecimento do ZE MARRETA à sua IA. Depois conte o que vende, para quem, por quanto e onde está travando. Peça que ele aplique o framework de sete etapas e entregue a primeira ação.”

## Instalar como skill em agentes compatíveis

A pasta [skills/ze-marreta-vendedor](skills/ze-marreta-vendedor) contém o ponto de entrada `SKILL.md` e suas referências. Copie **a pasta inteira**, preservando a estrutura, para o diretório de skills aceito pelo seu agente.

Para Codex, uma instalação no diretório pessoal de skills pode ser feita assim, no terminal:

O caminho pessoal segue a [documentação de skills do Codex](https://learn.chatgpt.com/guides/best-practices#turn-repeatable-work-into-skills).

```bash
git clone https://github.com/belloni123/ze-marreta-vendedor.git
cd ze-marreta-vendedor
python3 scripts/instalar_skill.py --destino ~/.agents/skills
```

Abra uma nova sessão e use `$ze-marreta-vendedor` ou solicite a skill pelo nome. A descoberta depende do suporte do seu agente. Para outro agente, informe seu diretório de skills em `--destino`; copiar arquivos não acrescenta suporte a skills a uma ferramenta que não o possui.

O instalador exige Python 3, copia apenas a skill e **recusa sobrescrever uma instalação existente**. Para atualizar, faça uma cópia da versão antiga, remova ou renomeie a pasta antiga e execute novamente. Se preferir instalar manualmente, baixe [o ZIP da skill](dist/ze-marreta-vendedor-skill.zip), extraia e copie a pasta para o local apropriado.

## Como o framework entra nas respostas

As sete etapas organizam a construção do comercial. As metodologias dos livros ajudam a executar as ações dentro de cada etapa.

| Etapa | Entrega principal | Conhecimento conectado |
|---|---|---|
| 1. ICP | Perfil e critérios de qualificação | Challenger, SPIN, Expert Secrets |
| 2. Benefícios | Relação entre necessidade e entrega | SPIN, Gatilhos Mentais |
| 3. Etapas e Estatística | Jornada, conversão e gargalos | Síntese integrada e guia de implementação |
| 4. Processo Comercial | Roteiros e critérios de avanço | Scripts, objeções, Voss, Três Tens |
| 5. Máquina de Vendas | Papéis, transferências e treinamento | Gestão comercial e playbooks |
| 6. Canais de Aquisição | Experimentos e desempenho por canal | Expert Secrets, Challenger |
| 7. Arquitetura de Receita | Aquisição, retenção e expansão | Money Models e negociação |

Leia [a integração completa](skills/ze-marreta-vendedor/references/framework-comercial-7-etapas.md). A estrutura em sete etapas é creditada a **Gabriel Magioli / Consultoria UP**, conforme o [painel indicado](https://frameworkcomercial.netlify.app/painel-7-etapas-fluxo.html). A adaptação oferece critérios e modelos operacionais; os percentuais de previsibilidade do painel não são garantias.

Para pedidos pontuais, como uma objeção de preço, o ZE MARRETA consulta o material pertinente sem exigir que você preencha um diagnóstico completo.

## O que foi transferido do WOLF

Os 11 documentos originais foram preservados integralmente, com os mesmos nomes e conteúdo:

| Documento | Uso |
|---|---|
| Expert Secrets — Russell Brunson | Funis, audiência, narrativa e apresentações |
| Gatilhos Mentais — Gustavo Ferreira | Comunicação e persuasão |
| SPIN Selling — Neil Rackham | Investigação consultiva |
| Negocie — Chris Voss | Empatia tática e negociação |
| Way of the Wolf — Jordan Belfort | Confiança, condução e gestão |
| The Challenger Sale — Matthew Dixon | Insights e adaptação por decisor |
| $100M Money Models — Alex Hormozi | Sequência e arquitetura de ofertas |
| Inteligência de Vendas — Síntese Integrada | Conexão entre metodologias |
| Playbook de Scripts | Roteiros por etapa |
| Playbook de Objeções | Diagnóstico de resistências |
| Guia de Implementação | Organização e acompanhamento |

As instruções originais também estão preservadas em [origem/instrucoes-wolf.md](origem/instrucoes-wolf.md). A nova skill adapta o nome, os caminhos e o uso do framework. O inventário com hashes permite conferir a integridade dos documentos. O nome histórico WOLF pode aparecer nas fontes e no título do livro *Way of the Wolf*.

## Arquivos para cada finalidade

| Arquivo ou pasta | Para que serve |
|---|---|
| [prompts/INSTRUCOES.md](prompts/INSTRUCOES.md) | Texto para configurar sua IA |
| [skills/ze-marreta-vendedor/SKILL.md](skills/ze-marreta-vendedor/SKILL.md) | Instruções para agentes com suporte a skills |
| [references/indice.md](skills/ze-marreta-vendedor/references/indice.md) | Escolher o documento certo |
| [dist/ZE-MARRETA-COMPLETO.md](dist/ZE-MARRETA-COMPLETO.md) | Instruções e conhecimento em um único arquivo |
| [docs/EXEMPLOS.md](docs/EXEMPLOS.md) | Pedidos prontos para adaptar |
| [NOTICE.md](NOTICE.md) | Origem, autoria e direitos das fontes |

## Para quem mantém ou adapta o projeto

Após alterar instruções ou referências, reconstrua os arquivos de distribuição e valide:

```bash
python3 scripts/empacotar.py
python3 scripts/verificar.py
```

A verificação confere a integridade dos 11 documentos WOLF, links locais, conteúdo do pacote unificado e do ZIP da skill. Ela não certifica a qualidade de respostas de todos os modelos. Confira sempre o material antes de usá-lo em uma conversa com clientes.

## Créditos

A base veio do WOLF, cujo manifesto identifica **FRANCISCO E B SILVA** como autor. O novo nome e a organização não alteram os créditos dos autores dos livros ou do framework. Consulte [NOTICE.md](NOTICE.md). O repositório não concede uma licença ampla sobre materiais de terceiros.
