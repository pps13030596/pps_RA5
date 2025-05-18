terraform {
  required_providers {
    vagrant = {
      source  = "bmatcuk/vagrant"
      version = ">= 0.1.0"
    }
  }
}

provider "vagrant" {}

resource "vagrant_vm" "ubuntu_vm" {
  name = "ubuntu2404"
  box  = "ubuntu/jammy64"  # Ubuntu 24.04 LTS, estable. (Puedes cambiar si encuentras box para 24.04)

  memory = 1024
  cpus   = 1

  provisioner "bin/bash" {
    inline = [
      "sudo apt update",
      "sudo apt install -y python3 python3-apt",
      "echo VM provisionada por Terraform"
    ]
  }
}
