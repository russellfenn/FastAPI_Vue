# Sub Applications

The goal of this experiment is to explore [Sub Applications](https://fastapi.tiangolo.com/advanced/sub-applications/)

## Questions

The Technical Details section of the docs say this uses [root_path](https://fastapi.tiangolo.com/advanced/sub-applications/), which is also useful in a deployment where our app sits behind a [Traefik](https://traefik.io/) proxy. Will this work, or will the `root_path` be confused?

## Testing root_path Confusion

1. Build two independant apps
1. Mount these apps under the parent app
1. Test under `uvicorn` in a VirtualEnv
1. Verify both apps are independant
1. Verify OpenAPI docs
1. Build as a Docker image
1. Deploy behind Traefik
