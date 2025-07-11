# Dependabot Auto-Merge Setup

This document outlines the required GitHub repository settings to enable automatic merging of Dependabot dependency updates.

## Required Repository Settings

### 1. Enable Auto-Merge Feature
Navigate to: **Settings** → **General** → **Pull Requests**
- ✅ Check "Allow auto-merge"

### 2. Configure Branch Protection Rules
Navigate to: **Settings** → **Branches** → **Branch protection rules**

**For the `main` branch, configure:**
- ✅ Require a pull request before merging
  - ✅ Require approvals: 1
  - ✅ Dismiss stale PR reviews when new commits are pushed
  - ✅ Require review from code owners (optional)
- ✅ Require status checks to pass before merging
  - ✅ Require branches to be up to date before merging
  - ✅ Status checks that are required:
    - `Test Dependabot PR` (from dependabot-automerge.yml)
    - `Run Tests` (from release.yaml, if applicable)
- ✅ Require conversation resolution before merging
- ✅ Include administrators (recommended)

### 3. Repository Permissions
Ensure the following permissions are configured:
- Dependabot has write access to create PRs
- GitHub Actions has write permissions for auto-merge workflow

## Auto-Merge Behavior

### Automatically Merged:
- ✅ **Patch updates** (1.0.0 → 1.0.1)
- ✅ **Minor updates** (1.0.0 → 1.1.0) - excluding cookiecutter itself
- ✅ **Security updates** (any version) - with immediate approval

### Requires Manual Review:
- ❌ **Major updates** (1.0.0 → 2.0.0) - commented but not auto-merged
- ❌ **Cookiecutter minor updates** - too critical for auto-merge

### Safety Requirements:
All auto-merged PRs must:
1. ✅ Pass the fast test suite (26 tests, ~35 seconds)
2. ✅ Pass code quality checks (ruff)
3. ✅ Pass security audit (pip-audit)
4. ✅ Have valid commit messages and labels

## Workflow Files

### `.github/workflows/dependabot-automerge.yml`
- Runs tests on all Dependabot PRs
- Auto-approves and merges safe updates
- Comments on major updates requiring manual review

### `.github/dependabot.yml`
- Configured for daily Python dependency checks
- Weekly GitHub Actions updates
- Auto-merge labels applied to all PRs
- Limited PR count to prevent spam

## Monitoring

### PR Labels
All Dependabot PRs will include:
- `dependencies` - Indicates dependency update
- `python` or `github-actions` - Ecosystem type
- `automerge` - Marks PR for auto-merge consideration

### Notifications
- Major updates receive explanatory comments
- Security updates receive priority comments
- Auto-merged PRs include approval reasons

## Testing the Setup

1. After configuring repository settings, wait for next Dependabot run (daily at 8:00 AM CT)
2. Monitor the first few PRs to ensure workflow functions correctly
3. Check GitHub Actions logs for any workflow failures
4. Verify branch protection rules prevent unsafe merges

## Rollback Plan

If auto-merge causes issues:
1. Disable auto-merge in repository settings immediately
2. Manually review and revert problematic commits
3. Adjust workflow conditions in `dependabot-automerge.yml`
4. Re-enable with stricter conditions

## Security Considerations

- Only patch and minor updates are auto-merged
- All updates must pass comprehensive test suite
- Security audits are performed before merge
- Major updates always require human review
- Critical dependencies (like cookiecutter itself) have additional restrictions