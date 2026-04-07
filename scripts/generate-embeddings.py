#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar embeddings para todas as aulas no banco de dados
"""

import sys
import os
from pathlib import Path

# Adicionar o diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils.embeddings import ensure_aula_embeddings, ensure_schema
from src.core.database import db_manager
from src.utils.logger import get_logger

logger = get_logger('generate_embeddings')

def main():
    """Gera embeddings para todas as aulas"""
    print("=" * 60)
    print("GERADOR DE EMBEDDINGS PARA AULAS")
    print("=" * 60)
    
    # Verificar se há API key configurada
    deepseek_key = os.getenv("DEEPSEEK_API_KEY", "").strip()
    openai_key = os.getenv("OPENAI_API_KEY", "").strip()
    
    if not deepseek_key and not openai_key:
        print("\nERRO: Nenhuma API key configurada!")
        print("Configure uma das seguintes variáveis de ambiente:")
        print("  - DEEPSEEK_API_KEY (recomendado - gratuito)")
        print("  - OPENAI_API_KEY")
        print("\nExemplo:")
        print("  export DEEPSEEK_API_KEY='sua-chave-aqui'")
        print("  python scripts/generate-embeddings.py")
        return 1
    
    print(f"\nAPI Key encontrada: {'DeepSeek' if deepseek_key else 'OpenAI'}")
    
    try:
        # Garantir que a coluna de embeddings existe
        print("\n1. Verificando estrutura do banco de dados...")
        ensure_schema()
        print("   ✓ Estrutura verificada")
        
        # Obter todas as aulas
        print("\n2. Obtendo lista de aulas...")
        aulas = db_manager.get_all_aulas()
        print(f"   ✓ Encontradas {len(aulas)} aulas")
        
        # Contar quantas precisam de embeddings
        aulas_sem_embedding = [a for a in aulas if not a.get('embedding_json')]
        print(f"   - Aulas sem embeddings: {len(aulas_sem_embedding)}")
        print(f"   - Aulas com embeddings: {len(aulas) - len(aulas_sem_embedding)}")
        
        if not aulas_sem_embedding:
            print("\n✓ Todas as aulas já possuem embeddings!")
            return 0
        
        # Gerar embeddings
        print(f"\n3. Gerando embeddings para {len(aulas_sem_embedding)} aulas...")
        print("   (Isso pode levar alguns minutos dependendo da quantidade de aulas)\n")
        
        ensure_aula_embeddings()
        
        # Verificar resultado
        aulas_atualizadas = db_manager.get_all_aulas()
        aulas_com_embedding = [a for a in aulas_atualizadas if a.get('embedding_json')]
        
        print(f"\n✓ Processo concluído!")
        print(f"   - Embeddings gerados: {len(aulas_com_embedding)}")
        print(f"   - Total de aulas: {len(aulas_atualizadas)}")
        
        if len(aulas_com_embedding) == len(aulas_atualizadas):
            print("\n🎉 Todas as aulas agora possuem embeddings!")
            print("   A busca semântica (RAG) está pronta para uso!")
        else:
            print(f"\n⚠ Aviso: {len(aulas_atualizadas) - len(aulas_com_embedding)} aulas ainda não possuem embeddings")
            print("   Verifique os logs para mais detalhes")
        
        return 0
        
    except Exception as e:
        logger.error(f"Erro ao gerar embeddings: {e}")
        print(f"\n✗ ERRO: {e}")
        print("\nPossíveis causas:")
        print("  - API key inválida ou sem créditos")
        print("  - Problema de conexão com a API")
        print("  - Erro no banco de dados")
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⚠ Processo interrompido pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ ERRO INESPERADO: {e}")
        sys.exit(1)
