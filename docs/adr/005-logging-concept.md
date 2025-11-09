# ADR-005 Logging concept

## Status
Accepted

## Context
Beside User output a internal logging will be needed.

## Decision
We use the python logging module to do internal logging.

- There will be a Factory which gets a logger for each class module, ...
- The centralized Error handling will log unexpected errors
- The output of the logger will go primarly in a file
- For debugging purposes the option will be given to set the logging output to stdout
- There will be a settings class which defines the default log level, which can be overriden over an environment variable or maybe a config file.
