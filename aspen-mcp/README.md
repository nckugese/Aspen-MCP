# Aspen Plus MCP Server

An MCP server for controlling Aspen Plus simulations via the Model Context Protocol.

## Workflow — Building a Simulation from Scratch

1. Open Aspen Plus and load a `.bkp` file
2. Add components (e.g. WATER, ETHANOL, METHANOL)
3. Set the property method (e.g. NRTL, PENG-ROB, UNIQUAC, IDEAL)
4. Place blocks and streams
5. Connect streams to block ports
6. Configure block and stream parameters
7. Run the simulation
8. Read results

> **Tip:** Use `search_properties` to find available property names, port names, or block types by keyword. It searches all YAML definition files and returns matching results with descriptions.
>
> Example: `search_properties("radfrac distillate")` lists RadFrac-related distillate ports and properties.

---

## Available Tools (18)

### Main (5)

| Tool | Description |
|------|-------------|
| `open_aspen_plus` | Open Aspen Plus and load a `.bkp` file |
| `close_aspen_plus` | Close an Aspen Plus session |
| `list_aspen_sessions` | List all active sessions |
| `run_simulation` | Run the simulation |
| `save_simulation` | Save the simulation to disk |

### Flowsheet (5)

| Tool | Description |
|------|-------------|
| `place_block` | Place a new block on the flowsheet |
| `remove_block` | Remove a block from the flowsheet |
| `place_stream` | Place a new stream on the flowsheet |
| `remove_stream` | Remove a stream from the flowsheet |
| `connect_stream` | Connect a stream to a block port |

### Properties (3)

| Tool | Description |
|------|-------------|
| `get_property_method` | Get the current global property method |
| `set_property_method` | Set the global property method |
| `add_component` | Add a component to the simulation |

### Block (2)

| Tool | Description |
|------|-------------|
| `get_block_value` | Get a property value from a block |
| `set_block_value` | Set a property value on a block |

### Stream (2)

| Tool | Description |
|------|-------------|
| `get_stream_value` | Get a property value from a stream |
| `set_stream_value` | Set a property value on a stream |

### Search (1)

| Tool | Description |
|------|-------------|
| `search_properties` | Search available properties by keyword |

---

## Block Reference

### RadFrac (Distillation Column)

Ports:

| Port | Description |
|------|-------------|
| F(IN) | Feed inlet |
| LD(OUT) | Liquid distillate outlet (top) |
| VD(OUT) | Vapor distillate outlet (top) |
| B(OUT) | Bottoms outlet |

Properties:

| Property | Type | Description |
|----------|------|-------------|
| number_of_stages | integer | Number of theoretical stages |
| condenser_type | string | Condenser type (TOTAL, PARTIAL-V, PARTIAL-V-L, NONE) |
| reboiler_type | string | Reboiler type (KETTLE, THERMOSIPHON, NONE) |
| reflux_ratio | float | Reflux ratio |
| distillate_to_feed_ratio | float | Distillate to feed ratio (D:F) |
| feed_stage | integer | Feed stage number (requires `stream_name` in extra_params) |
| condenser_pressure | float | Condenser pressure (stage 1 pressure) |

### Heater

| Property | Type | Description |
|----------|------|-------------|
| temperature | float | Outlet temperature |
| pressure | float | Outlet pressure |
| duty | float | Heat duty |
| vapor_fraction | float | Outlet vapor fraction |

### Pump

| Property | Type | Description |
|----------|------|-------------|
| discharge_pressure | float | Discharge pressure |
| pressure_increase | float | Pressure increase |
| efficiency | float | Pump efficiency |

---

## Stream Reference

### MATERIAL

Input properties:

| Property | Type | Description |
|----------|------|-------------|
| temperature | float | Stream temperature |
| pressure | float | Stream pressure |
| total_flow | float | Total flow rate |
| vapor_fraction | float | Vapor fraction |
| component_flow | float | Component flow rate (requires `component` in extra_params) |

Output properties (available after simulation):

| Property | Type | Description |
|----------|------|-------------|
| output_temperature | float | Output stream temperature |
| output_component_flow | float | Output component mole flow rate (requires `component` in extra_params) |

---

## Extending

You can add new block/stream definitions by creating YAML files in `definitions/`, or use the `create_tool` tool at runtime to generate them automatically. The searcher reloads immediately after a new definition is created.
