from typing import Dict, List
import time


WINDOW_SECONDS = 600
AGGREGATOR: Dict[int, List[Dict]] = {}


def record_aggregator(cell_id: int, confidence: float):
    t = time.time()
    AGGREGATOR.setdefault(cell_id, []).append({"ts": t, "confidence": confidence})
    AGGREGATOR[cell_id] = [r for r in AGGREGATOR[cell_id] if r["ts"] >= t - WINDOW_SECONDS]

def aggregator_count(cell_id: int) -> int:
    return len(AGGREGATOR.get(cell_id, []))
