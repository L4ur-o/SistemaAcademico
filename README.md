# EduAI - Plataforma de Ensino Inteligente

Plataforma de ensino baseada em inteligência artificial, desenvolvida com **Python**, **PySide6** e **MySQL**.

## Tecnologias

- **Python 3.8+** — linguagem principal
- **PySide6** — interface gráfica (Qt)
- **MySQL (PyMySQL)** — banco de dados com connection pooling
- **bcrypt** — hash seguro de senhas
- **QtAwesome** — ícones Font Awesome

## Estrutura do Projeto

```
SistemaAcademico/
├── assets/images/          # Logos e imagens
├── src/                    # Código-fonte
│   ├── config/             # Configurações centralizadas
│   ├── core/               # Lógica de negócio (app, banco de dados)
│   ├── ui/                 # Telas da interface gráfica
│   ├── utils/              # Utilitários (cache, logger, validadores, IA)
│   └── main.py             # Inicialização da aplicação
├── main.py                 # Ponto de entrada (executa src/main.py)
├── requirements.txt        # Dependências Python
└── README.md
```

## Como Executar

```bash
# 1. Instale as dependências
pip install -r requirements.txt

# 2. Configure o .env com suas credenciais de banco
#    (copie o modelo e preencha)

# 3. Execute
python main.py
```

## Funcionalidades

- **Autenticação** — login e cadastro com validação robusta e hash de senhas
- **Busca inteligente** — busca semântica de aulas com IA (embeddings)
- **Dashboard do aluno** — pesquisa de aulas, histórico, perfil
- **Dashboard do educador/admin** — gestão de alunos, aulas, instituições, feedbacks
- **Sugestões de aulas** — recomendações personalizadas via IA
- **Sistema de feedback** — avaliação de aulas pelos alunos
- **Cache em memória** — performance otimizada com cache thread-safe
- **Logging** — logs no console (arquivo opcional via `ENABLE_FILE_LOGS=true`)

## Padrões de Projeto

- **Singleton** — DatabaseManager, CacheManager, Logger
- **Observer** — sinais Qt para eventos da interface
- **Strategy** — validadores centralizados

## Configuração

Variáveis de ambiente (definidas no `.env`):

| Variável | Descrição |
|----------|-----------|
| `DB_HOST` | Host do banco MySQL |
| `DB_PORT` | Porta (padrão: 3306) |
| `DB_NAME` | Nome do banco |
| `DB_USER` | Usuário |
| `DB_PASSWORD` | Senha |
| `DEBUG` | Modo debug (true/false) |
| `LOG_LEVEL` | Nível de log (INFO, DEBUG, etc.) |
| `ENABLE_FILE_LOGS` | Salvar logs em arquivo (true/false) |
| `OPENAI_API_KEY` | Chave da OpenAI (opcional) |
| `DEEPSEEK_API_KEY` | Chave da DeepSeek (opcional) |
