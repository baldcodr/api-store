terraform {
  backend "gcs" {}
}

resource "google_service_account" "default" {
  account_id   = var.app_name
  display_name = var.app_name
}
resource "google_container_cluster" "primary" {
  name     = "${var.project_id}-gke"
  location = var.zone
  project  = var.project_id

  workload_identity_config {
    workload_pool = "${var.project_id}.svc.id.goog"
  }

  initial_node_count = var.gke_num_nodes
  node_config {
    service_account = google_service_account.default.email
    disk_size_gb    = 10
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
    labels = {
      env = "production"
    }
  }
}

resource "google_project_iam_member" "workload_identity_binding" {
  project = var.project_id
  role    = "roles/iam.workloadIdentityUser"
  member  = "serviceAccount:${var.project_id}.svc.id.goog[default/${var.app_name}-service-account]"
}

resource "google_artifact_registry_repository" "api-store-repo" {
  provider      = google
  location      = var.region
  project       = var.project_id
  repository_id = "${var.app_name}-repo"
  format        = "DOCKER"
  description   = "Docker repository"
}
