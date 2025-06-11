from typing import List, Union

class QuditGate:
    def __init__(self, name: str, targets: List[int], controls: List[int] = None, params: Union[None, List[float], List[complex]] = None, dimension: int = 3):
        self.name = name                  
        self.targets = targets            
        self.controls = controls or []   
        self.params = params or []        
        self.dimension = dimension       

    def __repr__(self):
        ctrl = f"ctrl={self.controls}" if self.controls else ""
        params = f"params={self.params}" if self.params else ""
        return f"{self.name}(t={self.targets} {ctrl} {params})"


# Predefined convenience constructors

def X_d(j: int, x: complex, y: complex, dimension: int):
    return QuditGate(
        name=f"X_d^{j}",
        targets=[j],
        params=[x, y],
        dimension=dimension
    )

def Z_d(theta: float, dimension: int):
    return QuditGate(
        name="Z_d",
        targets=list(range(dimension)),  # Applies to all |l⟩⟨l| basis states
        params=[theta],
        dimension=dimension
    )

def H_d(target: int, dimension: int):
    return QuditGate(
        name="H_d",
        targets=[target],
        dimension=dimension
    )

def Lambda2_Rd(control: int, target: int, rd_name: str, rd_params: List = None, dimension: int = 3):
    return QuditGate(
        name=f"Lambda2_{rd_name}",
        targets=[target],
        controls=[control],
        params=rd_params or [],
        dimension=dimension
    )

def SWAP(q1: int, q2: int, dimension: int):
    return QuditGate(
        name="SWAP",
        targets=[q1, q2],
        dimension=dimension
    )

def GXOR(control: int, target: int, dimension: int):
    return QuditGate(
        name="GXOR",
        targets=[target],
        controls=[control],
        dimension=dimension
    )
