# Sewa Setu — Old Age Pension Portal

Handover copy. Vendor maintenance contract ended 31/01/2026.

## Running

```
docker compose up --build
```

- Portal: http://localhost:8000
- SMS gateway console (simulated telecom): http://localhost:8000/__gateway/ —
  "sent" OTPs appear here once delivered. The gateway runs on the internal
  network and is served through the portal, so only one port is exposed.
- Database: Postgres, loaded from `seed/seed.sql` on first boot

## Maintenance fixes

The portal preserves Unicode applicant names, validates the CAPTCHA and uploads, separates
admin authorization from citizen sessions, parameterizes password reset queries, prevents
cross-citizen application access, supports pending application editing/cancellation, repairs
the RTPS deemed-approval scheduler, and adds database indexes.

Assessor admin login: `admin` / `sewasetu@123`. Production deployments should set
`ADMIN_USERNAME`, `ADMIN_PASSWORD`, `FLASK_SECRET_KEY`, and database environment variables.

## Tests

```bash
python -m unittest discover -s app -p "test*.py" -v
```

Production server logs (Jan–Jun 2026) are provided in `logs/`.

Listen to `dc-briefing.mp3` first (the DC's briefing), then read `BRIEF.md`.
