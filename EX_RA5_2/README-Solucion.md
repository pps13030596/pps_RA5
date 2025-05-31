Proceso de Puesta en Marcha del Entorno de Monitorización Jenkins + Prometheus + Grafana

-------------------------------------------------------
Estructura Base del Proyecto
-------------------------------------------------------

- Jenkins ejecuta pipelines y expone métricas vía plugin Prometheus.
- Prometheus recoge las métricas desde Jenkins.
- Grafana visualiza las métricas y muestra alertas.
- El proyecto se despliega con `docker-compose`.

-------------------------------------------------------
Cambios Realizados
-------------------------------------------------------

1. Unificación del nombre del job: `demo-pps`
   - Se corrigió:
     - alerts.rules.yml → cambiado a demo-pps
     - jenkins_pipeline_dashboard.json → cambiado a demo-pps

2. Confirmación del plugin Prometheus
   - Verificado que el Dockerfile de Jenkins instala el plugin `prometheus`.

3. Configuración del pipeline en Jenkins
   - Se creó un job llamado demo-pps con este Jenkinsfile:

     pipeline {
         agent any
         stages {
             stage('Build') { steps { echo 'Compilando...' } }
             stage('Test') { steps { echo 'Testeando...' } }
             stage('Deploy') { steps { echo 'Desplegando...' } }
         }
     }

-------------------------------------------------------
Integración con GitHub
-------------------------------------------------------

4. Configuración del webhook
   - Webhook creado en GitHub:
     - URL: https://<ngrok>.ngrok-free.app/github-webhook/
     - Evento: Push
     - Tipo de contenido: application/json

5. Configuración del job demo-pps
   - Pipeline script from SCM
   - Git repo: https://github.com/pps13030596/pps_RA5
   - Rama: */main
   - Script Path: Jenkinsfile
   - Activado: GitHub hook trigger for GITScm polling

-------------------------------------------------------
Verificaciones realizadas
-------------------------------------------------------

Prometheus:
- Scrapea métricas en /prometheus desde Jenkins.
- Métricas visibles tras ejecutar el build al menos una vez.

Grafana:
- Dashboard “Jenkins Pipelines Overview” importado manualmente.
- Conectado a datasource Prometheus.
- Paneles muestran datos del job demo-pps.
