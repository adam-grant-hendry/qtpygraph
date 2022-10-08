<!-- markdownlint-configure-file
{
    "MD024": false
}
-->
## 0.2.0 (2022-10-08)

### Feat

- **ci**: change `release` workflow to publish to PyPI
- **ci**: make `release` a manual workflow
- **ci**: separate `test` and `release` workflows
- **ci**: add manual clear cache action
- **ci**: update `commitizen` settings and `pypi` uploading (#7)
- **ci**: modify cache configuration
- **ci**: add headless display action to `test.yml` (#3)
- **ci**: add tox to github actions

### Fix

- **ci**: update `tox` environments
- **changelog**: remove comment from `markdownlint` configuration
- **ci**: correct pypi password environment variable in release job (#6)
- **ci**: change concurrency group to use context variables (#4)

## 0.1.0 (2022-09-24)

### Feat

- **init**: initial commit
