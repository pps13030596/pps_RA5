# Jenkins + Prometheus + Grafana: Monitorización de Pipelines

Este entorno proporciona un sistema completo de monitorización para **pipelines de Jenkins**, utilizando:

- **Jenkins** como orquestador de CI/CD
- **Prometheus** para recolectar métricas
- **Grafana** para visualizarlas

---

## 🚀 ¿Qué hace este stack?

- Levanta Jenkins con el plugin Prometheus instalado
- Exponer métricas de los jobs y pipelines
- Visualiza en Grafana:
  - Estado de las últimas ejecuciones
  - Duración de builds
  - Número de ejecuciones
  - Alertas en caso de fallo

---

## 📁 Estructura

```
jenkins-monitoring-stack/
├── docker-compose.yml
├── jenkins/
│   └── Dockerfile
├── prometheus/
│   ├── prometheus.yml
│   └── alerts.rules.yml
├── grafana/
│   └── dashboards/
│       └── jenkins_pipeline_dashboard.json
├── Jenkinsfile
└── README.md
```

---

## ⚙️ Requisitos

- Docker
- Docker Compose

---

## ▶️ Levantar el entorno

```bash
docker-compose up --build
```

---

## ✍️ Antes de monitorear...

**Crea una o más pipelines en Jenkins**, por ejemplo usando este `Jenkinsfile` incluido:

```groovy
pipeline {
    agent any
    stages {
        stage('Build') { steps { echo 'Compilando...' } }
        stage('Test') { steps { echo 'Testeando...' } }
        stage('Deploy') { steps { echo 'Desplegando...' } }
    }
}
```

**Importante**: Nombrar el job como `demo-pps` y editar el dashboard/datos en Prometheus para matchear el nombre.

---

## 📈 Métricas y visualización

- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000
  - Usuario: `admin`
  - Contraseña: `admin`

Dashboard incluido: `Jenkins Pipelines Overview`

---

## 📡 Alertas

Una alerta está preconfigurada para notificar si una pipeline falla (estado 1) durante más de 1 minuto.

---
