# Gestión de Secretos en Jenkins con HashiCorp Vault

**Alumno:** José  
**Fecha:** 2025-06-01  
**Actividad:** RA5.4 – Secretos en Jenkins  

---

## Objetivos

- Configurar Jenkins para manejar secretos de forma segura usando:
  - Las **credenciales internas** de Jenkins.
  - **HashiCorp Vault** como gestor externo de secretos.
- Integrar Vault y Jenkins mediante el plugin oficial.
- Ejecutar un pipeline que recupere secretos almacenados en Vault.

---

## Entorno

- Jenkins ejecutándose en Docker: `myjenkins-blueocean:2.504.1-1`
- Vault ejecutándose **en el host** (modo desarrollo).
- IP del host: `192.168.0.245`
- Vault escuchando en: `http://192.168.0.245:8200`

---

## Parte 1 – Jenkins con Credenciales Propias

### 1. Añadir un secreto en Jenkins

1. Navegar a: `Manage Jenkins > Credentials > (global)`
2. Click en **Add Credentials**
3. Tipo: `Secret text`
4. Valor: `mi_token_seguro`
5. ID: `my_secret_token`

### 2. Pipeline de ejemplo

```groovy
pipeline {
    agent any

    environment {
        TOKEN = credentials('my_secret_token')
    }

    stages {
        stage('Usar el Token') {
            steps {
                sh 'echo "Usando el token de forma segura: $TOKEN"'
            }
        }
    }
}
```

---

## Parte 2 – Jenkins + Vault

### 1. Iniciar Vault en modo desarrollo

```bash
vault server -dev -dev-listen-address="0.0.0.0:8200"
```

📌 Esto permite conexiones externas, necesarias para Jenkins (en Docker).

### 2. Crear el secreto en Vault

```bash
vault kv put secret/dev API_TOKEN=mi_clave_secreta
```

Verificar:

```bash
vault kv get secret/dev
```

---

### 3. Configurar credencial del token de Vault en Jenkins

1. Ir a `Manage Jenkins > Credentials`
2. Añadir una nueva:
   - Tipo: `Secret text`
   - Valor: *root token mostrado al iniciar Vault*
   - ID: `vault_token`

### 4. Instalar y configurar el plugin de Vault

- `Manage Jenkins > Manage Plugins > Available`
- Instalar: `HashiCorp Vault Plugin`

Luego en `Configure System`, configurar Vault con:

- **Vault URL**: `http://192.168.0.245:8200`
- **Credential ID**: `vault_token`
- **Engine Version**: `2`

---

### 5. Jenkinsfile Final

```groovy
pipeline {
    agent any

    stages {
        stage('Acceder al secreto desde Vault') {
            steps {
                withVault(
                    configuration: [
                        vaultUrl: 'http://192.168.0.245:8200',
                        engineVersion: 2,
                        vaultCredentialId: 'vault_token'
                    ],
                    vaultSecrets: [
                        [
                            path: 'secret/data/dev',
                            secretValues: [
                                [vaultKey: 'API_TOKEN', envVar: 'API_TOKEN']
                            ]
                        ]
                    ]
                ) {
                    sh 'echo "Token desde Vault: $API_TOKEN"'
                }
            }
        }
    }
}
```

---

## Resultado

- Jenkins se conectó correctamente a Vault
- Recuperó el secreto `API_TOKEN`
- Ejecutó el pipeline mostrando:

```
Token desde Vault: ****
```

---

## Referencias

- https://www.jenkins.io/doc/book/using/using-credentials/
- https://www.jenkins.io/doc/developer/security/secrets/
- https://plugins.jenkins.io/hashicorp-vault-plugin/
- https://medium.com/@giovannyorjuel2/integrando-jenkins-con-vault-2f1d42e31f95

---

## Capturas

![]()
![]()
![]()
![]()
![]()