variable "region" {
  type        = string
  default     = "europe-central2"
  description = "GCP region for deployment"
}
variable "zone" {
  type        = string
  default     = "europe-central2-b"
  description = "GCP zone for deployment"
}
variable "project_id" {
  type        = string
  description = "GCP project id"
}

variable "gke_num_nodes" {
  default     = 1
  description = "number of gke nodes"
}

variable "app_name" {
  type        = string
  default     = "api-store"
  description = "GCP project id"
}