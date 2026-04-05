### The What

A Python CLI tool that scans a Roblox project for `Events.lua` files and generates a single `EventManagerTypes.lua` with strongly-typed definitions for every service's events. Install it via pip, run it from the project root, and get full IntelliSense for all your events.

### The Why

Manually maintaining event type definitions across multiple services is tedious and error-prone. Every time you add or rename an event, you have to update the types file by hand. This tool eliminates that by reading event definitions directly from the source files and generating the types automatically.

### The How

The generator walks `ServerScriptService/*/Events.lua`, uses regex to parse `EventTypes.RemoteEvent` and similar patterns, then builds a Luau type export with nested service-to-event mappings. It's packaged as a standard Python CLI tool with setuptools, so it installs cleanly via pip and works from any terminal.
