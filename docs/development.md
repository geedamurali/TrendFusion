# Development Guide

## Branch strategy

TrendFusion uses one shared `main` branch.

Before starting work:
```bash
git pull origin main
```

After a coherent change:
```bash
git add .
git commit -m "feat: describe the change"
git push origin main
```

## Commit convention

- `feat:` new capability
- `fix:` bug correction
- `refactor:` internal restructuring
- `test:` tests
- `docs:` documentation
- `chore:` tooling/configuration

## Quality gate

Before pushing:
```bash
pytest
```

For API changes:
```bash
uvicorn backend.app.main:app --reload
```

Then verify `/api/health`.

## Collaboration rule

Do not make unrelated changes in the same commit. Keep commits small enough that their purpose is obvious.
