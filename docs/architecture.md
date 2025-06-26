# Arquitectura

```mermaid
flowchart LR
  subgraph Cliente
    U[Usuario]
  end

  subgraph Módulo Core
    DC[DBConnector]
    CFG[config.py<br/>validar()]
    FAC[Fábrica de conectores]
  end

  subgraph Conectores
    CBase[Connector (base)]
    CM[MySQLConnector]
    CP[PostgreSQLConnector]
    CMo[MongoDBConnector]
  end

  subgraph Bases de Datos
    DBM[(MySQL)]
    DBP[(PostgreSQL)]
    DBMo[(MongoDB)]
  end

  U -->|1. __init__(config)| DC
  DC --> CFG
  DC --> FAC
  FAC --> CBase
  CBase --> CM
  CBase --> CP
  CBase --> CMo
  CM -->|connect()| DBM
  CP -->|connect()| DBP
  CMo -->|connect()| DBMo

  U -->|2. read()/create()/…| DC
  DC --> CBase
  CBase -->|3. ejecutar operación| CM & CP & CMo
  CM & CP & CMo -->|4. resultados| DC
  DC -->|5. devuelve datos| U
```

# TODO: diagrama y explicación de la arquitectura
