# main.tf
resource "null_resource" "minikube_start" {
  provisioner "local-exec" {
    command = "minikube start --driver=docker"
  }
}