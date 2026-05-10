# ADR-007 Simplify command architecture

## Status
Status: Accepted
Date: 09.05.2026

## Context
The current command architecture based on the `BaseCommand` class creates too much complexity for the cli layer. Also typer already 
has these features already.

## Decision
The architecture is based on three layers:
- CLI Layer
  - Handles only the user interactions and responses
  - There is no business logic in this layer
  - Contains functions decorated with the typer command decorator
- Service Layer
  - Contains Business Logic
  - Should not use Typer this is the job of the CLI Layer
  - Returns only results or raises exceptions based on [ADR-004](004-error-handling-concept) 
- Data Layer
  - Optional, if needed it contains data access operations like file i/o

