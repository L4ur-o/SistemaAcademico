#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para testar conexão com o novo banco de dados
"""

import sys

# Testar primeiro com PostgreSQL
print("Testando conexão PostgreSQL...")
try:
    import psycopg2
    conn = psycopg2.connect(
        host="auth-db1524.hstgr.io",
        port=5432,  # Porta padrão PostgreSQL
        database="u359247811_biocalculadora",
        user="u359247811_admin2",
        password="cP$6nHI6Pmm",
        connect_timeout=10
    )
    print("OK: Conexao PostgreSQL bem-sucedida na porta 5432!")
    conn.close()
    sys.exit(0)
except Exception as e:
    print(f"ERRO: PostgreSQL porta 5432 falhou: {e}")

# Testar PostgreSQL na porta 3306 (improvável, mas vamos tentar)
print("\nTestando conexão PostgreSQL na porta 3306...")
try:
    import psycopg2
    conn = psycopg2.connect(
        host="auth-db1524.hstgr.io",
        port=3306,
        database="u359247811_biocalculadora",
        user="u359247811_admin2",
        password="cP$6nHI6Pmm",
        connect_timeout=10
    )
    print("OK: Conexao PostgreSQL bem-sucedida na porta 3306!")
    conn.close()
    sys.exit(0)
except Exception as e:
    print(f"ERRO: PostgreSQL porta 3306 falhou: {e}")

# Testar MySQL
print("\nTestando conexão MySQL...")
try:
    import pymysql
    conn = pymysql.connect(
        host="auth-db1524.hstgr.io",
        port=3306,
        database="u359247811_biocalculadora",
        user="u359247811_admin2",
        password="cP$6nHI6Pmm",
        connect_timeout=10
    )
    print("OK: Conexao MySQL bem-sucedida!")
    print("ATENCAO: O banco e MySQL, nao PostgreSQL!")
    print("   Sera necessario adaptar o codigo para usar PyMySQL ao inves de psycopg2")
    conn.close()
    sys.exit(0)
except ImportError:
    print("ERRO: PyMySQL nao esta instalado. Instale com: pip install pymysql")
except Exception as e:
    print(f"ERRO: MySQL falhou: {e}")

print("\nERRO: Nenhuma conexao funcionou. Verifique as credenciais e o tipo de banco de dados.")
