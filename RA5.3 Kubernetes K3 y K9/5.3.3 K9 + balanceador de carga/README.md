# Actividad 5.3 - Despliegue de HAProxy + Nginx con Balanceo de Carga en K3s

## 🎯 Objetivo
Desplegar un balanceador HAProxy frente a múltiples instancias de Nginx en un clúster K3s y validar su funcionamiento mediante K9s.

---

##  Paso 1: Crear manifiestos de Kubernetes

### nginx-deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```

### nginx-service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 80
```

### haproxy-configmap.yaml
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: haproxy-config
data:
  haproxy.cfg: |
    global
        daemon
        maxconn 256

    defaults
        mode http
        timeout connect 5000ms
        timeout client 50000ms
        timeout server 50000ms

    frontend http-in
        bind *:80
        default_backend servers

    backend servers
        server web1 web.default.svc.cluster.local:80 check
        server web2 web.default.svc.cluster.local:80 check
```

### haproxy-deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: haproxy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: haproxy
  template:
    metadata:
      labels:
        app: haproxy
    spec:
      containers:
      - name: haproxy
        image: haproxy
        ports:
        - containerPort: 80
        volumeMounts:
        - name: haproxy-config
          mountPath: /usr/local/etc/haproxy
      volumes:
      - name: haproxy-config
        configMap:
          name: haproxy-config
```

---

##  Paso 2: Aplicar los recursos

```bash
kubectl apply -f nginx-deployment.yaml
kubectl apply -f nginx-service.yaml
kubectl apply -f haproxy-configmap.yaml
kubectl apply -f haproxy-deployment.yaml
```

---

##  Paso 3: Exponer HAProxy a puerto 8081

```bash
kubectl expose deployment haproxy \
  --type=LoadBalancer \
  --name=haproxy-lb \
  --port=8081 \
  --target-port=80
```

---

##  Paso 4: Verificar el puerto expuesto por K3d

```bash
kubectl get svc haproxy-lb
```

Ejemplo de salida:
```
haproxy-lb   LoadBalancer   ...   8081:31503/TCP   ...
```

Entonces accede desde tu navegador o curl:

```bash
curl http://localhost:31503
```

>  No uses directamente `localhost:8081` si K3d ha asignado un puerto aleatorio.

---

## 🧪 Paso 5: Validar con K9s

```bash
k9s
```

Verifica el estado de los pods y servicios desplegados.

---

##  Validación Final

- 2 pods de Nginx corriendo
- HAProxy desplegado correctamente
- Servicio expuesto con balanceo funcional

## Capturas

![](./Imagenes/Captura%20desde%202025-05-25%2023-45-17.png)

![](./Imagenes/Captura%20desde%202025-05-25%2023-45-28.png)

![](./Imagenes/Captura%20desde%202025-05-25%2023-45-47.png)

![](./Imagenes/Captura%20desde%202025-05-25%2023-47-18.png)
