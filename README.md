<!-- TODO: one day consider stylized SVG title headers instead of plain markdown headings -->

# Roblox Event Types Generator

> Automatically generates type definitions for your Roblox EventManager by scanning Events.lua files.

![Last Commit](https://img.shields.io/github/last-commit/SirBepy/roblox-event-generator) ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Roblox](https://img.shields.io/badge/Roblox-000000?logo=roblox&logoColor=white)

---

## About

A Python CLI tool that scans your Roblox project for `Events.lua` files and generates TypeScript-like type definitions for your EventManager. This gives you full IntelliSense in your IDE for all event names and types across services.

Built because manually maintaining event type definitions is tedious and error-prone, especially as the number of services and events grows. This tool automates it by reading event definitions directly from source.

The generator parses `EventTypes.RemoteEvent`, `EventTypes.BindableEvent`, and similar patterns from each service's `Events.lua`, then outputs a single `EventManagerTypes.lua` with strongly-typed definitions for every service.

---

## How to run

Install from GitHub:

```bash
python -m pip install git+https://github.com/SirBepy/roblox-event-generator.git
```

Run in your Roblox project root:

```bash
roblox-event-generator
```

Or specify custom paths:

```bash
roblox-event-generator --src-dir ./game/src --output ./shared/EventManagerTypes.lua
```

If your Python PATH isn't properly set up:

```bash
python -m roblox_event_generator.cli
```

---

## Project Structure Expected

```
your-roblox-project/
├── src/
│   ├── ServerScriptService/
│   │   ├── InventoryService/
│   │   │   └── Events.lua
│   │   ├── ObbySystem/
│   │   │   └── Events.lua
│   │   └── ...
│   └── ReplicatedStorage/
│       └── _Libs/
│           └── EventManagerTypes.lua (generated)
```

---

## License

MIT

---

Vibe Coded by [SirBepy](https://github.com/SirBepy) & Claude
