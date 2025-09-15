# ADR-006 CLI UX concept

## Status
Accepted

## Context
The typer cli project needs to be easy to use and extendable.
Also the cli can get complex when there are more commands added to it.
Therefore we define here some guidelines.

## Decision
1.  For consistent command naming we use lower case commands, where kebab-case is used if at least two words needs to stick together. Also subcommands needs to be logically grouped.

2. For help texts we use typer which brings already a consistent help text automatically.

    2.1 Typer will be configured that only the base command is a global help

    2.2 Also --help should be useable on every command

3. Output Formatting will be done by using `typer.echo` which provides a consistent formatting

4. If we need progress indicators we will use `rich` which is already included in the complete edition of `typer`

5. Settings can be addressed over a `--setting` syntax

   5.1 `--log-level` should be available to override the current log level.

   5.2. For command completions we can use typers integrated feature.
