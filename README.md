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
