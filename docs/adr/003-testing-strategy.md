# ADR-003 Testing Strategy

## Status
Accepted

## Context
- The application is structured in different layers cli, services and optional data.
- The cli layer handles all typer related things, business logic is encapsulated in service layer and data provides optional data storage access.

## Decision
1. Service and Data Layer needs to be tested isolated and in integration with each other
2. CLI Tests should be minimal since they need more time
3. Service and Data Layer tests should be tested over the pre commit configuration and also in a pull request
4. Code Coverage should be at 80 - 90%
5. When building a release all tests will be executed
   - Those who test the cli minimal
   - Those who test integration between cli and service layer
   - Those who test service, data layer each and in integration with each other
6. As Framework we use pytest and if needed a tool for mocking
