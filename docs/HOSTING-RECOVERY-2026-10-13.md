# Render recovery plan — 2026-10-13

## Verified observation

The connected `borza-api` service (`srv-d9k9hp3m8hqs73bvshb0`) tracks `flegardev/Borza` main. Its last three deployments failed during build. Readiness requests time out. Historical build logs were unavailable through the connector, so the exact build exception remains unverified.

The service root directory is `backend`, Docker context is `.`, and Dockerfile path is `./Dockerfile`. `backend/Dockerfile` copies `backend/requirements.txt`, `backend/`, and root-level `content/`. Those COPY paths require the repository-root Docker context. The committed Blueprint already expresses the correct paths, but also specifies a paid starter plan and an automatic Alembic migration. Applying it as-is is not authorized.

## Concrete change requiring operator approval

Keep the existing free service and environment values. Set root directory to the repository root, Docker context to `.`, and Dockerfile path to `./backend/Dockerfile`. Keep `/ready` as the readiness check. Do not add a migration pre-deploy command or select a paid plan. Review a backup and the Alembic state before separately approving any production migration.

After approval, deploy the reviewed main SHA, inspect full build logs, check `/live` and `/ready`, then verify an authenticated API request from the canonical frontend and confirm its configured origin is allowed by CORS. A healthy public landing page alone does not establish API health. Never copy production database credentials into a pull-request preview.

## Remaining access

The Render connector can inspect and trigger deployments but cannot update this service's Docker root/context settings. Use the authenticated Render dashboard or an authorized service-update API after approval. Supabase metadata reports Borza active, but database inspection failed authentication; schema/RLS verification requires restored connector access.
