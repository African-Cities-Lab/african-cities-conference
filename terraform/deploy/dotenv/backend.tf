terraform {
  cloud {
    organization = "exaf-epfl"
    workspaces {
      name = "african-cities-conference-dotenv"
    }
  }
}
