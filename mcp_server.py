"""
MCP Server for Cerebral Autoregulation & Transient Hyperemic Response Ratio (THRR) Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating TCD hyperemic response ratios, compression drops, and autoregulatory scores.
"""

import sys
import json
from typing import Dict, Any
from client import CerebralAutoregulationTHRRClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_thrr",
                "description": "Calculates Transcranial Doppler (TCD) Transient Hyperemic Response Ratio (THRR = FV3/FV1), compression drop %, and cerebral dynamic autoregulatory score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "baseline_flow_velocity_cm_s": {
                            "type": "number",
                            "description": "Baseline Middle Cerebral Artery (MCA) mean flow velocity FV1 in cm/s (e.g. 62.0 cm/s, normative 45-75 cm/s)."
                        },
                        "compression_flow_velocity_cm_s": {
                            "type": "number",
                            "description": "MCA mean flow velocity during transient ipsilateral carotid compression FV2 in cm/s (e.g. 40.0 cm/s)."
                        },
                        "hyperemic_peak_flow_velocity_cm_s": {
                            "type": "number",
                            "description": "Peak MCA flow velocity upon release of compression FV3 in cm/s (e.g. 76.0 cm/s)."
                        },
                        "mean_arterial_pressure_mmhg": {
                            "type": "number",
                            "description": "Systemic mean arterial pressure in mmHg (default: 90.0 mmHg).",
                            "default": 90.0
                        }
                    },
                    "required": ["baseline_flow_velocity_cm_s", "compression_flow_velocity_cm_s", "hyperemic_peak_flow_velocity_cm_s"]
                }
            }
        ]
    }


def handle_request(client: CerebralAutoregulationTHRRClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_thrr":
            res = client.evaluate_thrr(
                baseline_flow_velocity_cm_s=float(args.get("baseline_flow_velocity_cm_s", 60.0)),
                compression_flow_velocity_cm_s=float(args.get("compression_flow_velocity_cm_s", 40.0)),
                hyperemic_peak_flow_velocity_cm_s=float(args.get("hyperemic_peak_flow_velocity_cm_s", 72.0)),
                mean_arterial_pressure_mmhg=float(args.get("mean_arterial_pressure_mmhg", 90.0))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = CerebralAutoregulationTHRRClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
