# ADR-001 Choose a CLI Framework for the homelab devtools

## Status
Accepted

## Context
For the homelab devtools as it will be a cli tool with python and poetry we need a modern cli framework which supports:
- Modern python features
- Class based command architecture
- Type safety for ensuring code quality

## Decision
We use Typer since it is build around type safety.
