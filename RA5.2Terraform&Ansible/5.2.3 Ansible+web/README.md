# RA5.2.3 – Configuración de página web con Ansible

## Objetivo

Configurar una máquina virtual Ubuntu 24.04 para:

- Crear un archivo `index.html` con el contenido `Ansible rocks`.
- Copiarlo al directorio web de Apache (`/var/www/html/`).
- Reiniciar Apache.
- Verificar que el contenido es servido correctamente mediante `curl`.

---

## Estructura del proyecto

```
5.2.2 Ansible/
├── hosts.ini
└── index_html.yml
```

---

## index_html.yml

```yaml
---
- name: Configurar index.html y verificar Apache
  hosts: web
  become: yes
  tasks:
    - name: Crear archivo index.html
      copy:
        dest: /var/www/html/index.html
        content: "Ansible rocks"

    - name: Reiniciar Apache
      service:
        name: apache2
        state: restarted

    - name: Verificar contenido de la web
      command: curl http://localhost
      register: web_output

    - name: Mostrar resultado
      debug:
        var: web_output.stdout
```

---

##  Comando para ejecutar

```bash
ansible-playbook -i hosts.ini index_html.yml --ssh-common-args='-o StrictHostKeyChecking=no'
```

---

## Resultado esperado

- El archivo `/var/www/html/index.html` contiene el texto `Ansible rocks`.
- La salida del playbook debe incluir:

```yaml
"web_output.stdout": "Ansible rocks"
```

- También puedes acceder desde el navegador: [http://192.168.56.10](http://192.168.56.10)

## Captura del resultado

Captura
![PaginamodificadadesdeAnsible](./Imagenes/2025-05-21%2000_41_35-Greenshot.png)