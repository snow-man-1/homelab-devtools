# ADR-002 Command Architecture

## Status
Accepted

## Context
In this cli we need a separation of business logic and typer/cli specific implementation in order to
- easier test code
- add more flexible new commands

## Decision
The Architecture will contain two and an optional third layer depending on data is needed.
The layers are:
- Command Layer: Here is the Typer implementation of each command. Each command group gets it's own class which will be registered to the app via a Registry
- Business Logic Layer: Here is no typer included only the code behind the typer command
- Data Layer: optional, if we need to handle data, like for a settings file, it can be later added if needed
