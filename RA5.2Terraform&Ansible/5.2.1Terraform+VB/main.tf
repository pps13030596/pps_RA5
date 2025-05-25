resource "null_resource" "vagrant_vm" {
  provisioner "local-exec" {
    command = "vagrant up"
  }

  triggers = {
    always_run = "${timestamp()}"
  }
}
