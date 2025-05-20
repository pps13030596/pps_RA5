# RA5.2 – Configuración de Apache con Ansible

## Objetivo

Configurar una máquina virtual Ubuntu 24.04 en VirtualBox mediante Ansible para:

- Realizar `apt update` y `upgrade` del sistema.
- Instalar el servidor web Apache.

---

## Requisitos previos

- VM Ubuntu 24.04 corriendo (creada con Terraform + Vagrant).
- IP accesible desde el host, por ejemplo: `192.168.56.10`.
- Archivo de clave SSH generado por Vagrant (ubicado en `.vagrant/machines/.../private_key`).

---

## Estructura de Ansible

```
5.2.2 Ansible/
├── hosts.ini
└── setup_apache.yml
```

---

## hosts.ini

```ini
[web]
192.168.56.10 ansible_user=vagrant ansible_ssh_private_key_file=/home/<usuario>/.ssh/vagrant_key
```

> Asegúrate de haber copiado la clave privada a `~/.ssh/vagrant_key` y haberle aplicado `chmod 600`.

---

## setup_apache.yml

```yaml
---
- name: Configurar Ubuntu con Apache
  hosts: web
  become: yes
  tasks:
    - name: Actualizar caché de paquetes
      apt:
        update_cache: yes

    - name: Realizar upgrade (sin dist)
      apt:
        upgrade: yes
      ignore_errors: yes

    - name: Instalar Apache
      apt:
        name: apache2
        state: present
```

---

##  Comando para ejecutar

```bash
ansible-playbook -i hosts.ini setup_apache.yml --ssh-common-args='-o StrictHostKeyChecking=no'
```

---

## Resultado

- Apache fue instalado correctamente.
- La página por defecto de Apache está disponible en: `http://192.168.56.10`

---

## Nota sobre errores

Durante el proceso pueden aparecer errores relacionados con paquetes como `grub-efi-amd64-signed` o `shim-signed`. Estos errores son esperados en entornos BIOS como VirtualBox y **no afectan el funcionamiento de Apache**.
