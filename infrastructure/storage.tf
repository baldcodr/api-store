
resource "google_firebase_project" "default" {
  provider = google-beta
  project  = var.project_id
}

resource "google_firestore_database" "database" {
  project     = var.project_id
  name        = "api-store"
  location_id = "nam5"
  type        = "FIRESTORE_NATIVE"
}

resource "google_firestore_document" "apidoc" {
  project     = var.project_id
  database    = google_firestore_database.database.name
  collection  = "persons"
  document_id = "4b7f376c-2376-4185-ba64-d539bdf40dcf-dw"
  fields      = "{\"id\":{\"mapValue\":{\"fields\":{\"id\":{\"stringValue\":\"4b7f376c-2376-4185-ba64-d539bdf40dcf-dw\"}}}}}"
}

resource "google_firebaserules_ruleset" "primary" {
  source {
    files {
      content = "service cloud.firestore {match /databases/{database}/documents { match /{document=**} { allow read, write: if request.auth != null; } } }"
      name    = "firestore.rules"
    }
  }
  project = var.project_id
}