# Release evidence checklist

Historical code-under-test: `d320eee` on `test/full-platform-hardening`. The passed items below preserve local/isolated evidence from that exact historical review; they are not automatically valid for later commits and do not constitute hosted-production approval.

## Historical isolated evidence at `d320eee`

- [x] Clean baseline inspected; no unrelated source changes overwritten.
- [x] Content validator and seven validator tests pass.
- [x] Backend format, lint, mypy and coverage suite pass (38 passed, 2 PostgreSQL skips, 87%).
- [x] Premium safety suite passes (59 passed, 3 expected platform/integration skips).
- [x] Frontend format, lint, typecheck, 37 unit tests and strict 37-route build pass.
- [x] Strict production frontend Docker image builds; isolated frontend/API/PostgreSQL stack is healthy.
- [x] Desktop and mobile production browser journeys pass, including console/page-error and overflow checks.
- [x] Axe WCAG/best-practice scans pass with color contrast enabled.
- [x] Keyboard focus/activation and frontend API-failure fallback pass on desktop/mobile.
- [x] Performance budgets pass; 10/30/100 learner classroom runs have zero errors.
- [x] Host, CORS, method, malformed JSON, extra field, oversized body, rate-limit spoof, ownership, classroom token/replay, prompt injection/PII and public answer-key cases exercised.
- [x] Clean SQLite head/check/downgrade/upgrade and real PostgreSQL 16/RLS integration pass.
- [x] Database outage readiness and recovery behavior pass.
- [x] npm production/full audits report zero vulnerabilities; no direct Git dependency.
- [x] Worktree secret token patterns report zero matching files.
- [x] Pinned Gitleaks scan reports no leaks across the complete Git history.
- [x] Retention CLI is dry-run first and deletion/cascade is regression-tested.
- [x] CI builds the real production frontend image.

## Current portfolio-upgrade evidence (2026-08-09)

- [x] Academy content validator passes with 12 paths, 4 active paths, 32 lessons and 6 classroom activities.
- [x] All 8 content-validator regression tests pass, including canonical classroom activity-type validation.
- [x] Targeted classroom API tests pass: 8 tests, including activity type/ID mismatch rejection.
- [x] Complete SQLite backend suite passes: 38 tests, 2 expected PostgreSQL-profile skips, 87% coverage; Ruff formatting/lint and mypy pass on Python 3.12.13.
- [x] Frontend lint and typecheck pass.
- [x] Frontend coverage passes: 38 tests, 91.45% statements and 93.4% lines.
- [x] Strict 37-route frontend build passes.
- [x] Full and production-only npm audits report zero vulnerabilities.
- [x] Focused catalogue regression passes in desktop and mobile Chromium: four active links, eight non-interactive roadmap cards, correct numbering and zero browser-console errors.
- [x] Disposable PostgreSQL 16/RLS profile rebuilt from the Alpine test target and passes: 2 integration tests, with its containers and network removed afterward.
- [x] Production frontend and backend Docker images build and answer HTTP health smokes as UID/GID `10001:10001`.
- [x] Docker Scout reports 0 critical, high, medium or low findings for the final frontend (`9353c17a978a`) and backend (`c7caaacb733b`) images. The backend moved from Debian slim to the supported Python Alpine variant after the Debian image exposed four unfixed Perl findings in an unused runtime package.
- [ ] The complete Windows dev-server E2E run is partial evidence only: 26 passed, 13 failed on cold-loading/localized-copy timing, and 1 skipped. Require the Linux pull-request gate, which runs one worker with retries, before preview approval.
- [ ] Run hosted authentication, persistence, accessibility and performance flows on the exact pull-request head before changing release status. Local performance automation could not be completed because the existing Windows wrapper depends on the removed `wmic.exe` command.

## Preview evidence

- GitHub Actions security, backend and frontend checks completed successfully on the draft PR.
- The first automatic Vercel Preview stopped because Preview lacked `NEXT_PUBLIC_API_URL`.
- A Preview-only `https://api.example.invalid` value was added to avoid production traffic; the isolated demo/fallback redeploy completed Ready at `https://borza-om71blia8-flegar-tech.vercel.app`.
- The preview is intentionally not evidence of hosted API, authentication or persistence behavior.

## Required before controlled pilot

- [ ] Apply migration 0015 to the pilot database and verify grants/security advisors.
- [ ] Configure real Supabase Auth and assign teacher roles only through protected app metadata.
- [ ] Schedule/monitor the retention command; approve school privacy/safeguarding notices and lawful basis.
- [ ] Configure distributed/edge rate limits and verify the 100-student NAT scenario.
- [ ] Run hosted smoke/ownership/accessibility/performance checks on the exact preview commit.
- [ ] Confirm backup restore, error monitoring, alerting, log redaction/retention and incident ownership.
- [ ] Decide whether the optional AI provider stays disabled; if enabled, run live provider privacy, timeout, cost and prompt-safety tests.

## Required before broad production

- [ ] Remove CSP `unsafe-inline` through a reviewed nonce/hash design.
- [ ] Separate browser demo scoring metadata if demo evidence could be mistaken for authoritative assessment.
- [ ] Complete NVDA/VoiceOver/TalkBack, zoom/reflow and forced-colors testing.
- [ ] Add canonical URL, robots, sitemap and approved social-preview metadata.
- [ ] Obtain a successful Python advisory scan; current `pip-audit` attempts timed out externally.
- [ ] Complete a staging soak/load test with query/pool/CPU/memory telemetry and hosted Core Web Vitals.
- [ ] Perform production-like restore and rollback rehearsal.

## Decision

**NOT PRODUCTION-READY.** The portfolio-upgrade working tree fixes the confirmed catalogue and classroom-integrity defects, passes local backend/frontend/build/database gates, and has clean npm and final-image advisory results. The full browser suite remains partial on this Windows host, and hosted authentication, persistence, accessibility, performance and data-operations evidence has not been repeated on the pull-request head. Preview eligibility must be established by that commit's CI and preview checks. A controlled pilot remains conditional on completing every unchecked pilot item above.
