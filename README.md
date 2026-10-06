# MEDUSA CTFd Plugins

This repository contains the MEDUSA CTFd plugin layer for the custom cyber-operations platform built on top of CTFd 3.8.8.

## Architecture

The plugin layer is intentionally kept separate from CTFd core. Plugins are loaded by CTFd as Python modules and can extend routes, templates, and admin behavior without forking the upstream project.

## Current plugin

- `plugins/medusa_core` — bootstrap plugin for the MEDUSA control plane

## Local installation pattern

When used inside a CTFd instance, place the plugin as a module under:

```bash
CTFd/plugins/medusa_core/
```

The plugin exposes a `load(app)` entry point and a basic admin dashboard route.

## Planned plugin suite

- `medusa_core`
- `medusa_university`
- `medusa_sandbox`
- `medusa_audit`
- `medusa_anticheat`

## Validation

This repo is intentionally lightweight and validates through Python syntax checks before integration into the upstream CTFd runtime.
