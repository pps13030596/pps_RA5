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