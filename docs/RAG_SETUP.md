# Configuração de RAG (Retrieval-Augmented Generation) e Busca Semântica

## O que é RAG?

RAG (Retrieval-Augmented Generation) é uma técnica que combina busca semântica com geração de respostas. No EduAI, isso significa:

1. **Embeddings**: Representações vetoriais das aulas que capturam o significado semântico
2. **Busca Semântica**: Comparação da pergunta do usuário com os embeddings das aulas
3. **Sugestões Inteligentes**: Retorno das aulas mais relevantes baseado no significado, não apenas palavras-chave

## Configuração

### 1. Obter uma API Key

Você precisa de uma API key para gerar embeddings. Duas opções:

#### Opção A: DeepSeek (Recomendado - Gratuito)
1. Acesse: https://platform.deepseek.com/
2. Crie uma conta
3. Obtenha sua API key
4. Configure a variável de ambiente:
   ```bash
   export DEEPSEEK_API_KEY='sua-chave-aqui'
   ```

#### Opção B: OpenAI (Pago)
1. Acesse: https://platform.openai.com/
2. Crie uma conta e adicione créditos
3. Obtenha sua API key
4. Configure a variável de ambiente:
   ```bash
   export OPENAI_API_KEY='sua-chave-aqui'
   ```

### 2. Gerar Embeddings para as Aulas

Execute o script de geração de embeddings:

```bash
python scripts/generate-embeddings.py
```

Este script irá:
- Verificar se a coluna `embedding_json` existe na tabela `aulas`
- Gerar embeddings para todas as aulas que ainda não possuem
- Salvar os embeddings no banco de dados

**Nota**: O processo pode levar alguns minutos dependendo da quantidade de aulas.

### 3. Verificar se Funcionou

Após executar o script, você pode verificar no banco de dados:

```sql
SELECT id_aula, titulo, 
       CASE WHEN embedding_json IS NULL THEN 'Sem embedding' ELSE 'Com embedding' END as status
FROM aulas;
```

Todas as aulas devem ter `embedding_json` preenchido.

## Como Funciona

### Busca Semântica vs Busca por Palavras-chave

**Antes (apenas palavras-chave)**:
- Usuário pergunta: "Como criar pastas?"
- Sistema busca por palavras: "criar", "pastas"
- Pode não encontrar se a aula usar termos diferentes

**Agora (RAG com embeddings)**:
- Usuário pergunta: "Como criar pastas?"
- Sistema converte a pergunta em um vetor (embedding)
- Compara com os vetores de todas as aulas usando similaridade de cosseno
- Retorna as aulas mais semanticamente similares, mesmo com palavras diferentes

### Fluxo de Busca

1. **Pergunta do Usuário** → "Quero aprender a criar pastas no Windows"
2. **Geração de Embedding** → Converte a pergunta em vetor numérico
3. **Busca Semântica** → Compara com embeddings das aulas
4. **Ranking** → Ordena por similaridade (score de 0 a 1)
5. **Resultado** → Retorna as 3 aulas mais relevantes

## Uso na Aplicação

O sistema agora usa RAG automaticamente quando:
- Uma API key está configurada
- Os embeddings foram gerados
- O usuário faz uma busca

Se os embeddings não estiverem disponíveis, o sistema faz fallback para busca por palavras-chave.

## Manutenção

### Adicionar Nova Aula

Quando uma nova aula é adicionada:
1. O sistema tentará gerar o embedding automaticamente na primeira busca
2. Ou você pode executar o script novamente para garantir

### Atualizar Embeddings

Se você modificar o conteúdo de uma aula (título, descrição, tags), execute:

```bash
python scripts/generate-embeddings.py
```

O script atualizará apenas as aulas que não possuem embeddings ou que foram modificadas.

## Troubleshooting

### Erro: "Cliente de embeddings não disponível"
- Verifique se a variável de ambiente está configurada
- No Windows PowerShell: `$env:DEEPSEEK_API_KEY='sua-chave'`
- No Windows CMD: `set DEEPSEEK_API_KEY=sua-chave`

### Embeddings não estão sendo gerados
- Verifique se a API key é válida
- Verifique se há créditos disponíveis (OpenAI)
- Verifique os logs para mais detalhes

### Busca ainda usa palavras-chave
- Verifique se os embeddings foram gerados: `SELECT COUNT(*) FROM aulas WHERE embedding_json IS NOT NULL`
- Execute o script de geração novamente
- Verifique se há erros nos logs

## Benefícios do RAG

✅ **Busca mais inteligente**: Entende o significado, não apenas palavras
✅ **Melhor relevância**: Retorna aulas realmente relacionadas à pergunta
✅ **Linguagem natural**: Funciona mesmo com perguntas mal formuladas
✅ **Sinônimos**: Encontra aulas mesmo usando palavras diferentes

## Exemplo

**Pergunta**: "Preciso aprender a organizar arquivos no computador"

**Sem RAG**: Pode não encontrar se a aula usar "pastas" ao invés de "arquivos"

**Com RAG**: Encontra a aula "Criar Pastas" porque entende que "organizar arquivos" e "criar pastas" são semanticamente similares
