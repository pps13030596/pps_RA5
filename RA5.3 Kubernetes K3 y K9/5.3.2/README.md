# Actividad 5.2 - K3s en modo Alta Disponibilidad (HA) con K9s

## Paso 1: Instalación de Docker y k3d

### Instalar Docker sino lo tenemos instalado:
```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
newgrp docker
```

### Instalar k3d sino lo tenemos instalado:
```bash
curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash
```

---

## Paso 2: Crear un clúster HA con 3 servidores

```bash
k3d cluster create k3s-ha \
  --servers 3 \
  --agents 0 \
  --k3s-arg "--cluster-init@server:0" \
  --wait
```

Este comando crea un clúster K3s con 3 nodos de control (alta disponibilidad).

---

## Paso 3: Instalar kubectl (si no estaba disponible)

```bash
curl -LO "https://dl.k8s.io/release/$(curl -sL https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client
```

---

## Paso 4: Desplegar Nginx con 2 réplicas

Crear archivo de despliegue:
nginx-deployment.yaml
```bash

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```

Aplicar el despliegue:

```bash
kubectl apply -f nginx-deployment.yaml
```

Verificar estado:

```bash
kubectl get pods
```

---

## Paso 5: Verificar con K9s

Lanzar K9s:

```bash
k9s
```

Puedes navegar entre los recursos y verificar que el deployment está en estado `Running`.

---

## Validación final

- Verificamos los 3 nodos en el clúster con `kubectl get nodes`
- Verificamos los 2 pods de nginx corriendo
- Usamos K9s para monitorear el estado