# Roblox Event Types Generator

Automatically generates TypeScript-like type definitions for your Roblox EventManager by scanning your `Events.lua` files.

## Features

- 🔍 Automatically scans your Roblox project for `Events.lua` files
- 📝 Generates precise type definitions for each event (RemoteEvent, BindableEvent, etc.)
- ✨ Enables full IntelliSense in your IDE
- 🚀 Works with any Roblox project structure

## Installation

```bash
 python -m pip install git+https://github.com/SirBepy/roblox-event-generator.git
```

## Usage

Run in your Roblox project root directory:

```bash
roblox-event-generator
```

Or specify custom paths:

```bash
roblox-event-generator --src-dir ./game/src --output ./shared/EventManagerTypes.lua
```

Note: If your python PATH isnt properly setup, then use the following command

```bash
python -m roblox_event_generator.cli
```

## How It Works

1. Scans `src/ServerScriptService/*/Events.lua` for event definitions
2. Parses event definitions like:
   ```lua
   return EventManager.createServiceEvents("ObbySystem", {
       Skip = EventTypes.RemoteEvent,
       GiveItem = EventTypes.BindableEvent,
   })
   ```
3. Generates type-safe definitions in `EventManagerTypes.lua`:
   ```lua
   export type EventManagerType = {
       ObbySystem: {
           Skip: RemoteEvent,
           GiveItem: BindableEvent,
       },
   }
   ```

## Requirements

- Python 3.7+
- Your Events.lua files must use the EventTypes format

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

## License

MIT

---

Vibe Coded by [SirBepy](https://github.com/SirBepy) & Claude
