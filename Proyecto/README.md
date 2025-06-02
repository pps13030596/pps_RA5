# ProxMox

## [Instalación y configuración de Proxmox VE en VirtualBox](#instalacion_y_configuracionparte-1-instalación-y-configuración-de-proxmox-ve-en-virtualbox)

## [Preparar VM y contenedor como plantillas para Terraform y Jenkins](#parte-2-preparar-vm-y-contenedor-como-plantillas-para-terraform-y-jenkins)



# Parte 1: Instalación y configuración de Proxmox VE en VirtualBox

## Requisitos previos
- Windows 11 Pro con VirtualBox instalado.
- ISO de Proxmox VE: [Descargar aquí](https://www.proxmox.com/en/downloads)
- Al menos 8 GB de RAM y 50 GB de espacio libre en disco.

---

## Paso 1: Crear la máquina virtual para Proxmox
1. Abrir VirtualBox y hacer clic en “Nueva”.
2. Configurar:
   - **Nombre**: `Proxmox-Server`
   - **Tipo**: `Linux`
   - **Versión**: `Debian (64-bit)`
3. Asignar:
   - **RAM**: mínimo 4096 MB (ideal 8192 MB)
   - **CPU**: 2 o más núcleos
   - **Disco duro virtual**: 64 GB (VDI, reservado dinámicamente)

---

## Paso 2: Montar la ISO e iniciar instalación
1. En la VM creada, ir a “Configuración” > “Almacenamiento”.
2. En el controlador IDE, añadir la ISO de Proxmox VE como unidad óptica.
3. Iniciar la VM.

---

## Paso 3: Instalar Proxmox VE
1. Seleccionar: **Install Proxmox VE**.
2. Aceptar el EULA.
3. Elegir el disco virtual para la instalación.
4. Configurar región, teclado y zona horaria.
5. Establecer:
   - Contraseña de root.
   - Email de administración.
6. Configurar red:
   - Asignar IP estática (opcional).
   - Nombre del host: `proxmox.local`
7. Finalizar instalación y **reiniciar**.

---

## Paso 4: Acceder a la interfaz web de Proxmox
1. Desde el navegador de Windows, acceder a:
   ```
   https://<IP-de-tu-Proxmox>:8006
   ```
   Ejemplo: `https://192.168.56.101:8006`

2. Iniciar sesión:
   - **Usuario**: `root`
   - **Contraseña**: la configurada
   - **Realm**: `Linux PAM`

 Ignorar el aviso de certificado inseguro.

## Capturas de la Instalacion de Proxmox

![](./Imagenes/2025-06-01%2022_59_16-Proyecto-ProxMox%20[Corriendo]%20-%20Oracle%20VirtualBox.png)
![](./Imagenes/2025-06-01%2023_00_52-Proyecto-ProxMox%20[Corriendo]%20-%20Oracle%20VirtualBox.png)
![](./Imagenes/2025-06-01%2023_16_20-Proyecto-ProxMox%20[Corriendo]%20-%20Oracle%20VirtualBox.png)
![](./Imagenes/2025-06-01%2023_23_59-pve%20-%20Proxmox%20Virtual%20Environment%20-%20Opera.png)

# Parte 2: Preparar VM y contenedor como plantillas para Terraform y Jenkins

## Objetivo
Crear una VM y un contenedor (LXC) que puedan usarse como plantillas para despliegues automatizados.

---

## 1. Preparar la VM base para Terraform y Jenkins

### Crear la VM en Proxmox
- Nombre: `ubuntu-template`
- ISO: Ubuntu Server 22.04
- Configuración mínima: 2 CPU, 2048 MB RAM, 10+ GB disco

### Dentro de la VM, ejecutar:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install openssh-server -y

sudo adduser devops
sudo usermod -aG sudo devops

sudo mkdir /home/devops/.ssh
sudo chmod 700 /home/devops/.ssh
sudo chown devops:devops /home/devops/.ssh
```

### Convertir VM en plantilla en Proxmox
1. Apagar la VM: `shutdown now`
2. En la interfaz de Proxmox: clic derecho > **Convert to Template**

---

## 2. Preparar contenedor LXC base

### Crear el contenedor:
- Nombre: `debian-template`
- Plantilla: `debian-11-standard`
- Configuración mínima: 1 CPU, 512 MB RAM, 4+ GB disco

### Dentro del contenedor, ejecutar:
```bash
apt update && apt upgrade -y
apt install openssh-server sudo curl vim net-tools -y

adduser devops
usermod -aG sudo devops

mkdir /home/devops/.ssh
chmod 700 /home/devops/.ssh
chown devops:devops /home/devops/.ssh
```

### Convertir CT en plantilla (si tu almacenamiento lo permite)
1. Apagar el contenedor.
2. En Proxmox: clic derecho > **Convert to Template**

---

## Ventajas para Terraform y Jenkins
- Terraform puede clonar estas plantillas automáticamente.
- Jenkins puede usar estas VMs/CTs como nodos de prueba.
- Evitas repetir configuración básica en cada despliegue.

## Capturas

![](./Imagenes/2025-06-02%2019_23_13-pve%20-%20Proxmox%20Virtual%20Environment%20-%20Opera.png)
![](./Imagenes/2025-06-02%2019_28_55-pve%20-%20Proxmox%20Virtual%20Environment%20-%20Opera.png)
![](./Imagenes/2025-06-02%2019_28_55-pve%20-%20Proxmox%20Virtual%20Environment%20-%20Opera.png)
![](./Imagenes/2025-06-02%2020_18_09-pve%20-%20Proxmox%20Virtual%20Environment%20-%20Opera.png)
![](./Imagenes/2025-06-02%2020_18_21-pve%20-%20Proxmox%20Virtual%20Environment%20-%20Opera.png)
![](./Imagenes/2025-06-02%2020_19_23-pve%20-%20Proxmox%20Virtual%20Environment%20-%20Opera.png)
![](./Imagenes/2025-06-02%2020_19_44-pve%20-%20Proxmox%20Virtual%20Environment%20-%20Opera.png)
![](./Imagenes/2025-06-02%2020_21_40-pve%20-%20Proxmox%20Virtual%20Environment%20-%20Opera.png)
![](./Imagenes/2025-06-02%2020_22_19-pve%20-%20Proxmox%20Virtual%20Environment%20-%20Opera.png)
![](./Imagenes/2025-06-02%2021_41_35-pve%20-%20Proxmox%20Virtual%20Environment%20-%20Opera.png)
![](./Imagenes/2025-06-02%2021_51_13-pve%20-%20Proxmox%20Virtual%20Environment%20-%20Opera.png)
![](./Imagenes/2025-06-02%2021_51_38-pve%20-%20Proxmox%20Virtual%20Environment%20-%20Opera.png)
![](./Imagenes/2025-06-02%2021_54_07-pve%20-%20Proxmox%20Virtual%20Environment%20-%20Opera.png)