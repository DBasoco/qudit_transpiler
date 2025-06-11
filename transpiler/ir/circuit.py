from typing import List, Optional
from .gates import QuditGate

class QuditCircuit:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.gates: List[QuditGate] = []

    def add_gate(self, gate: QuditGate):
        if gate.dimension != self.dimension:
            raise ValueError(f"Gate {gate.name} dimension {gate.dimension} does not match circuit dimension {self.dimension}")
        self.gates.append(gate)

    def __repr__(self):
        return f"<QuditCircuit d={self.dimension} gates={len(self.gates)}>"

    def print_circuit(self):
        for idx, gate in enumerate(self.gates):
            print(f"{idx}: {gate}")
