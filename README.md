### PEC WATCHER
---

Um script em python para acompanhar as novas releases do PEC do ESUSAB

Configuração

1. Copie o arquivo config.py.example e insira seus parâmetros de configuração:

```
cp config.py.example config.py
```

2. Adicione a CRON para a execução do script

```
0 24 * * * python3 {repo_location}/main.py
```


Versões

- v1.0: Base do script para verificação da mudança de versão do PEC no site do ESUSAB
- v2.0: [PREVISTO] Geração do container docker para a nova versão do PEC identificada
