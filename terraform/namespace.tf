provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace_v1" "dev" {
  metadata {
    name = "dev"
  }
}