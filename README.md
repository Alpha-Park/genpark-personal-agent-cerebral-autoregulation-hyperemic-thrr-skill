# Cerebral Autoregulation & Transient Hyperemic Response Ratio (THRR) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Transcranial Doppler (TCD) Transient Hyperemic Response Ratio (THRR), carotid compression velocity drops, and cerebral dynamic autoregulatory reserve.

```mermaid
flowchart TD
    TCD_MCA["Baseline Transcranial Doppler MCA Mean Velocity (FV1)"] --> Compression["Transient Carotid Perfusion Dip (FV2, drop >= 25%)"]
    Compression --> Release["Compression Release -> Reactive Hyperemia (FV3)"]
    Release --> CalcTHRR["Transient Hyperemic Response Ratio (THRR = FV3 / FV1)"]
    CalcTHRR --> ReserveScore["Dynamic Autoregulation & Arteriolar Dilatory Reserve"]
    ReserveScore --> Agent["OpenClaw / Hermes Personal Agent Postural Guarding"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Neurovascular Standards**: Implements validated equations for TCD flow velocities, compression drop percentage, and Giller THRR ratios.
- **Dynamic Autoregulation Screening**: Detects early loss of myogenic and endothelial arteriolar vasodilatory capacity.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import CerebralAutoregulationTHRRClient

client = CerebralAutoregulationTHRRClient()
result = client.evaluate_thrr(
    baseline_flow_velocity_cm_s=62.0,
    compression_flow_velocity_cm_s=40.0,
    hyperemic_peak_flow_velocity_cm_s=78.5
)
print("THRR Ratio:", result["transient_hyperemic_response_ratio"])
print("Autoregulatory Score:", result["autoregulatory_reserve_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
