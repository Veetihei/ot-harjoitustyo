# Sekvenssikaavio
```mermaid
sequenceDiagram
  actor User
  participant Machine
  participant FuelTank
  participant Engine
  User->>Machine: Machine()
  Machine->>FuelTank: FuelTank()
  Machine->>FuelTank: fill(40)
  Machine->>Engine: Engine(FuelTank)
  User->>Machine: drive()
  Machine->>Engine: start()
  Engine->>FuelTank: consume(5)
  Machine->>Engine: is_running()
  Engine->>FuelTank: fuel_contents()
  FuelTank-->>Engine: 35
  Engine-->>Machine: True
  Machine->>Engine: use_energy()
  Engine->>FuelTank: consume(10)

```
