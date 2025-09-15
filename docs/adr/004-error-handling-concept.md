# ADR-004 Error handling concept

## Status
Accepted

## Context
Since the business logic and the cli itself are encapsulated in different layers we need to handle different types of errors.

## Decision
- Error Types
  - Business Logic Errors
  - System Errors like access to a file faile
  - User Errros like bad inputs
- These Errors will be handled through own error classes which will be handled in a central spot for each command
- The CLI will than depending on the error type respond to the caller with a specified error code
  - 0: everything ok
  - 1: User Errors
  - 2: Business Logic Errors
  - 3: System Errors
  - 100: Unexpected Errors
- If there are more cases which needs a separate error class new codes will be added.
