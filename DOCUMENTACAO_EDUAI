# EduAI - Plataforma de Ensino Inteligente
## Documentação Técnica Resumida

---

## 1. Visão Geral

**EduAI** -> É uma ferramenta que ajuda a desenvolver o gosto, das gerações mais recentes, ao uso dos SOs mais usados recente: Windows e Linux, afim de prepara-los para uma vida acadêmica e profissional mais autentica. Com explicações rápidas e consisas sobre o uso dos comandos, atalhos e usabilidade geral desses sistemas. Além de um bom uso da IA, permitindo o usuario perguntar o que deseja saber sobre tal questão ou dúvida que eventualmente venha a ter dentro da sua máquina.

---

## 2. Controle de Versão

> *"O controle de versão e o gerenciamento do histórico de desenvolvimento foram realizados com Git e GitHub, adotados para versionamento distribuído, gestão de branches e rastreabilidade de commits."*

O projeto utiliza **Git** como sistema de versionamento distribuído e **GitHub** como plataforma de hospedagem, garantindo rastreabilidade completa de mudanças, gestão de branches paralelos e colaboração entre membros da equipe.

---

## 3. Arquitetura

### Estrutura de Diretórios
```
SistemaAcademico/
├── assets/images/          # Logos e imagens
├── src/
│   ├── config/             # Configurações centralizadas
│   ├── core/               # Lógica de negócio e banco de dados
│   ├── ui/                 # Telas e componentes gráficos
│   ├── utils/              # Utilitários (cache, logger, IA)
│   └── main.py             # Inicialização da aplicação
├── requirements.txt        # Dependências Python
└── README.md
```

A arquitetura em **três camadas lógicas** permite separação clara entre interface (PySide6), lógica de negócio (Python) e persistência (MySQL), favorecendo manutenção, testabilidade e escalabilidade.

---

## 4. Stack Tecnológico

| Tecnologia | Versão | Função |
|-----------|--------|--------|
| **Python** | 3.8+ | Linguagem principal |
| **PySide6** | ≥6.8.0 | Interface gráfica (Qt for Python) |
| **MySQL** | - | Banco de dados com connection pooling |
| **PyMySQL** | ≥1.1.0 | Conector MySQL |
| **bcrypt** | ≥4.2.0 | Hash seguro de senhas |
| **OpenAI** | ≥1.58.0 | Embeddings para busca semântica |
| **Pillow** | ≥10.4.0 | Processamento de imagens |
| **NumPy** | ≥1.26.0 | Cálculos numéricos e estatísticas |
| **QtAwesome** | ≥1.4.0 | Iconografia Font Awesome |

---

## 5. Linguagens e Persistência

### Python como Linguagem Principal

> *"A linguagem principal adotada foi Python, em razão de sua legibilidade, velocidade de prototipação, ampla adoção acadêmica e integração madura com bibliotecas de IA e GUI."*

Python foi escolhido por sua sintaxe clara, prototipação rápida, ecossistema maduro e comunidade ativa — alinhado ao contexto acadêmico do projeto.

### SQL para Persistência

> *"Para persistência e consulta estruturada, a aplicação emprega SQL para modelagem das entidades essenciais: credenciais de login (armazenadas com hash seguro), papéis de usuário (aluno, educador, administrador), aulas e conteúdos preparados, registros de pesquisa dos alunos e sugestões de aulas submetidas pelos participantes."*

Entidades modeladas em SQL:
- **Usuários** — credenciais com hash bcrypt, papéis (aluno/educador/admin)
- **Aulas** — conteúdos preparados com metadados
- **Histórico de Pesquisa** — registros de consultas para análise
- **Sugestões** — recomendações geradas pela IA
- **Feedbacks** — avaliações de aulas pelos alunos

A estrutura SQL permite consultas analíticas, criação de índices, e geração de relatórios diagnósticos.

---

## 6. Framework de Interface

### PySide6 (Qt for Python)

> *"Optou-se por PySide6 (Qt for Python) como framework de interface devido à sua capacidade de construir aplicações desktop nativas com widgets ricos: QStackedWidget, QScrollArea, áreas roláveis, diálogos de seleção e barras de progresso que reproduzem o locus de interação do computador real e favorecem a transferência do aprendizado."*

**Componentes utilizados:**
- **QStackedWidget** — Pilha de telas para navegação
- **QScrollArea** — Áreas roláveis para listas longas
- **QDialog** — Diálogos modais
- **QProgressBar** — Indicadores de progresso
- **QTableWidget** — Tabelas de dados
- **QLineEdit** — Campos de entrada validados

### Customização Visual com QSS/CSS

> *"A possibilidade de customização via QSS/CSS foi utilizada para padronizar estilos, reduzir ruído cognitivo e tornar a experiência mais consistente entre diferentes ambientes."*

Estilos CSS customizados padronizam cores, tipografia e comportamentos visuais em toda a aplicação.

### QtAwesome

> *"Foram integrados componentes auxiliares conforme necessidade: QtAwesome para iconografia consistente."*

Font Awesome integrado oferece ícones consistentes e escaláveis em toda a interface.

---

## 7. Bibliotecas Especializadas

### Pillow — Processamento de Imagens

> *"Pillow (manipulação de imagens e geração de screenshots), empregada para criação e processamento dos passos ilustrados."*

Utilizada para redimensionamento de imagens, geração de thumbnails e screenshots para documentação.

### NumPy — Cálculos e Métricas

> *"NumPy (cálculos e métricas locais), usada para operações numéricas e estatísticas elementares que suportam métricas de desempenho e relatórios locais."*

Realiza cálculos estatísticos, processamento de embeddings vetoriais e matriz de similaridade para recomendações.

### PyMySQL — Conector MySQL

> *"PyMySQL (conector MySQL), utilizada para integração com bases MySQL/MariaDB quando requerido."*

Fornece conexão ao banco de dados com suporte a prepared statements (segurança contra SQL injection), connection pooling e transações ACID.

### bcrypt — Segurança de Senhas

Implementa algoritmo bcrypt com 12 rounds para hash criptográfico de senhas, com salt aleatório por usuário, resistindo a ataques de força bruta.

---

## 8. Busca Semântica e IA

> *"DeepSeek / OpenAI embeddings (camada de embeddings para busca semântica), adotada para viabilizar recuperação semântica dos conteúdos preparados pela equipe, combinando embeddings vetoriais com busca léxica para melhorar recall e precisão."*

### Estratégia Híbrida de Busca

> *"A estratégia híbrida de busca — embeddings semânticos combinados com busca léxica por termos — visa ampliar o recall em consultas com vocabulário distinto do acervo, mantendo precisão quando são usados termos exatos."*

**Componentes:**
1. **Embeddings Semânticos** — Entende contexto e conceitos relacionados
2. **Busca Léxica** — Busca por termos exatos
3. **Sugestões Personalizadas** — Recomendações baseadas no histórico do aluno

A abordagem híbrida garante:
- Recall aumentado (encontra documentos mesmo com vocabulário distinto)
- Precisão mantida (boost para termos exatos)
- Resiliência (funciona mesmo com falhas na API)

---

## 9. Padrões de Projeto

> *"Padrões de Projeto — Singleton, Observer, Strategy"*

### Singleton
**DatabaseManager, CacheManager, Logger** — Instância única thread-safe em toda a aplicação.

### Observer
**Sinais Qt para eventos da interface** — Componentes se registram como observadores e são notificados automaticamente de eventos.

### Strategy
**Validadores centralizados** — Diferentes estratégias de validação intercambiáveis (email, senha, nome).

---

## 10. Funcionalidades Principais

- **Autenticação Segura** — Login e cadastro com validação robusta e hash de senhas bcrypt
- **Busca Inteligente** — Busca semântica com embeddings combinada com busca léxica
- **Dashboard do Aluno** — Pesquisa de aulas, histórico, perfil, recomendações personalizadas
- **Dashboard do Educador/Admin** — Gestão de alunos, aulas, instituições, feedbacks
- **Sistema de Feedback** — Avaliação de aulas pelos alunos
- **Cache em Memória** — Performance otimizada com cache thread-safe
- **Logging Centralizado** — Rastreabilidade de operações (console e arquivo opcional)

---

## 11. Resiliência e Performance

> *"A arquitetura do projeto contempla logging e cache local para garantir rastreabilidade das operações e resiliência diante de conectividade instável em ambientes escolares."*

**Cache Thread-Safe** — Cache em memória com TTL (Time To Live) para dados frequentemente acessados.

**Logging Centralizado** — Logs em console com suporte opcional a arquivo para auditoria. Variável `ENABLE_FILE_LOGS=true` habilita persistência de logs.

**Connection Pooling** — Reutilização eficiente de conexões MySQL.

---

## 12. Configuração

### Variáveis de Ambiente (.env)

| Variável | Descrição |
|----------|-----------|
| `DB_HOST` | Host do banco MySQL |
| `DB_PORT` | Porta (padrão: 3306) |
| `DB_NAME` | Nome do banco |
| `DB_USER` | Usuário do banco |
| `DB_PASSWORD` | Senha do banco |
| `DEBUG` | Modo debug (true/false) |
| `LOG_LEVEL` | Nível de log (INFO, DEBUG, etc) |
| `ENABLE_FILE_LOGS` | Salvar logs em arquivo (true/false) |
| `OPENAI_API_KEY` | Chave da OpenAI (opcional) |
| `DEEPSEEK_API_KEY` | Chave da DeepSeek (opcional) |

---

## 13. Deployment

> *"A arquitetura do projeto contempla [...] além do uso de práticas de deploy em provedores comerciais por razões operacionais (Hostinger foi a opção do grupo por critérios de custo e facilidade de gestão)."*

**Infraestrutura:**
- **Hostinger** como provedor de hospedagem
- **Deploy contínuo** via Git push ou CI/CD
- **Acesso SSH** para manutenção
- **Backups automáticos** do banco de dados

---

## 14. Execução

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Configurar .env com credenciais do banco

# 3. Executar aplicação
python main.py
```

---

## Conclusão

EduAI integra tecnologias modernas (Python, PySide6, MySQL, APIs de IA), padrões de projeto consolidados (Singleton, Observer, Strategy), segurança robusta (bcrypt, prepared statements), performance otimizada (cache, connection pooling, embeddings) e resiliência arquitetural — permitindo manutenção colaborativa, escalabilidade e confiabilidade em ambientes acadêmicos com conectividade variável.
